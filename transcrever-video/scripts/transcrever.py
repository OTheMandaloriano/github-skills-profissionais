#!/usr/bin/env python3
r"""
transcrever.py — transcreve a fala de um video e devolve o texto.

Regra: nada fica no disco. Todo trabalho acontece em uma pasta temporaria
que e apagada no fim. Exportacao (txt/srt/json/md/pdf) so acontece quando
--out e --format sao passados de proposito.

Uso:
    python transcrever.py <url-ou-arquivo> [--model small] [--lang pt]
                          [--prompt "termos, nomes"] [--duration 96.7]
                          [--format md,txt,srt,json,pdf] [--out PASTA]
                          [--name NOME] [--cleanup-input]

Saida padrao: transcricao no stdout (para o chat) e nada em disco.

Codigos de saida:
    0  sucesso
    2  uso incorreto
    3  YouTube bloqueou o download -> usar captura pelo navegador
    4  falha na transcricao
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import time
from pathlib import Path

EXIT_OK = 0
EXIT_USAGE = 2
EXIT_FALLBACK = 3
EXIT_FAIL = 4


# --------------------------------------------------------------------------- #
# utilidades
# --------------------------------------------------------------------------- #

def _installer_hint() -> str:
    here = Path(__file__).resolve().parent
    return (
        f'powershell -ExecutionPolicy Bypass -File "{here / "instalar_dependencias.ps1"}"'
    )


def check_dependencies() -> list[tuple[str, bool, str]]:
    import importlib.util

    results: list[tuple[str, bool, str]] = []
    for module, package in (
        ("faster_whisper", "faster-whisper"),
        ("yt_dlp", "yt-dlp"),
    ):
        found = importlib.util.find_spec(module) is not None
        results.append((package, found, "import ok" if found else "nao instalado"))

    try:
        exe = ffmpeg_exe()
        results.append(("ffmpeg", True, exe))
    except Exception as exc:  # noqa: BLE001
        results.append(("ffmpeg", False, str(exc)[:120]))
    return results


def require_dependencies() -> None:
    missing = [name for name, ok, _ in check_dependencies() if not ok]
    if not missing:
        return
    print(
        "[DEPENDENCIAS] faltando: " + ", ".join(missing) + "\n"
        "Instale com:\n  " + _installer_hint(),
        file=sys.stderr,
    )
    raise SystemExit(EXIT_FAIL)


def ffmpeg_exe() -> str:
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg

        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(
            "ffmpeg nao encontrado. Instale o ffmpeg ou rode: pip install imageio-ffmpeg"
        ) from exc


def run_ffmpeg(args: list[str]) -> None:
    cmd = [ffmpeg_exe(), "-hide_banner", "-loglevel", "error", "-y", *args]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg falhou: {proc.stderr.strip()[:400]}")


def fmt_ts(seconds: float, sep: str = ",") -> str:
    ms = int(round(seconds * 1000))
    h, rem = divmod(ms, 3_600_000)
    m, rem = divmod(rem, 60_000)
    s, ms = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"


def short_ts(seconds: float) -> str:
    total = int(seconds)
    return f"{total // 60:02d}:{total % 60:02d}"


def safe_name(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE).strip()
    text = re.sub(r"\s+", "_", text)
    return text[:80] or "transcricao"


# --------------------------------------------------------------------------- #
# download
# --------------------------------------------------------------------------- #

def download_audio(url: str, dest: Path) -> tuple[Path, dict]:
    """Baixa o audio tentando clientes do YouTube que ainda funcionam."""
    try:
        from yt_dlp import YoutubeDL
    except ImportError as exc:  # noqa: BLE001
        print("[DEPENDENCIAS] yt-dlp ausente. Instale com:\n  " + _installer_hint(), file=sys.stderr)
        raise SystemExit(EXIT_FAIL) from exc

    attempts = [["android_music"], ["android_vr"], ["web_safari", "tv_embedded"], ["mweb"]]
    last_error = ""

    for clients in attempts:
        opts = {
            "format": "bestaudio/best",
            "outtmpl": str(dest / "audio.%(ext)s"),
            "quiet": True,
            "no_warnings": True,
            "noplaylist": True,
            "extractor_args": {"youtube": {"player_client": clients}},
        }
        try:
            with YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
            files = sorted(dest.glob("audio.*"), key=lambda p: p.stat().st_mtime)
            if not files:
                raise RuntimeError("download nao gerou arquivo")
            meta = {
                "title": info.get("title") or "video",
                "duration": float(info.get("duration") or 0),
                "uploader": info.get("uploader") or "",
                "url": url,
            }
            return files[-1], meta
        except Exception as exc:  # noqa: BLE001
            last_error = str(exc)
            for leftover in dest.glob("audio.*"):
                leftover.unlink(missing_ok=True)

    print(
        "[FALLBACK] o YouTube recusou o download direto "
        f"({last_error[:200]}).\n"
        "Use a captura pelo navegador descrita em references/captura-navegador.md "
        "e rode este script apontando para o arquivo capturado.",
        file=sys.stderr,
    )
    raise SystemExit(EXIT_FALLBACK)


def probe_duration(media: Path) -> float:
    """Duracao via ffmpeg (sem ffprobe)."""
    proc = subprocess.run(
        [ffmpeg_exe(), "-hide_banner", "-i", str(media)],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    match = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.?\d*)", proc.stderr)
    if not match:
        return 0.0
    h, m, s = match.groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


# --------------------------------------------------------------------------- #
# transcricao
# --------------------------------------------------------------------------- #

def transcribe(wav: Path, model_size: str, lang: str | None, prompt: str | None):
    try:
        from faster_whisper import WhisperModel
    except ImportError as exc:  # noqa: BLE001
        print("[DEPENDENCIAS] faster-whisper ausente. Instale com:\n  " + _installer_hint(), file=sys.stderr)
        raise SystemExit(EXIT_FAIL) from exc

    model = WhisperModel(
        model_size,
        device="cpu",
        compute_type="int8",
        cpu_threads=max(4, (os.cpu_count() or 4) // 2),
    )
    segments, info = model.transcribe(
        str(wav),
        language=lang,
        beam_size=5,
        vad_filter=True,
        vad_parameters={"min_silence_duration_ms": 400},
        initial_prompt=prompt,
    )
    result = [
        {"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()}
        for s in segments
    ]
    return result, info


# --------------------------------------------------------------------------- #
# PDF minimo (sem dependencia externa, WinAnsi cobre portugues)
# --------------------------------------------------------------------------- #

class _Pdf:
    PAGE_W, PAGE_H = 595.0, 842.0
    MARGIN = 56.0
    BODY = 10.5
    LEAD = 15.0

    def __init__(self, title: str):
        self.title = title
        self.pages: list[list[str]] = [[]]
        self.max_chars = 92

    def _wrap(self, text: str, width: int | None = None) -> list[str]:
        return textwrap.wrap(
            text,
            width=width or self.max_chars,
            break_long_words=False,
            break_on_hyphens=False,
        ) or [""]

    def add_heading(self, text: str) -> None:
        for line in self._wrap(text, 78):
            self.pages[-1].append(("bold", line))

    def add_paragraph(self, text: str) -> None:
        for line in self._wrap(text):
            self.pages[-1].append(("body", line))

    def new_page(self) -> None:
        self.pages.append([])

    def _escape(self, text: str) -> bytes:
        data = text.encode("cp1252", errors="replace")
        return data.replace(b"\\", b"\\\\").replace(b"(", b"\\(").replace(b")", b"\\)")

    def _content(self, lines: list[tuple[str, str]], page_no: int) -> bytes:
        out = [b"BT"]
        y = self.PAGE_H - self.MARGIN - 18
        out.append(f"1 0 0 1 {self.MARGIN:.1f} {y:.1f} Tm".encode())
        out.append(b"/F2 9 Tf")
        out.append(b"(" + self._escape(self.title) + b") Tj")
        y -= 22
        for style, line in lines:
            font = b"/F2" if style == "bold" else b"/F1"
            size = b"11" if style == "bold" else b"10.5"
            out.append(f"1 0 0 1 {self.MARGIN:.1f} {y:.1f} Tm".encode())
            out.append(font + b" " + size + b" Tf")
            out.append(b"(" + self._escape(line) + b") Tj")
            y -= self.LEAD
        out.append(f"1 0 0 1 {self.PAGE_W / 2:.1f} 30 Tm".encode())
        out.append(b"/F1 8 Tf")
        out.append(f"({page_no}) Tj".encode())
        out.append(b"ET")
        return b"\n".join(out)

    def build(self) -> bytes:
        objects: list[bytes] = []
        page_ids = []
        content_ids = []
        base = 3  # 1=catalog, 2=pages
        for _ in self.pages:
            page_ids.append(base)
            content_ids.append(base + 1)
            base += 2
        font_regular = base
        font_bold = base + 1

        objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
        kids = " ".join(f"{pid} 0 R" for pid in page_ids)
        objects.append(f"<< /Type /Pages /Kids [{kids}] /Count {len(page_ids)} >>".encode())

        for page_id, content_id, lines in zip(page_ids, content_ids, self.pages):
            objects.append(
                f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.PAGE_W} {self.PAGE_H}] "
                f"/Resources << /Font << /F1 {font_regular} 0 R /F2 {font_bold} 0 R >> >> "
                f"/Contents {content_id} 0 R >>".encode()
            )
            content = self._content(lines, page_ids.index(page_id) + 1)
            objects.append(b"<< /Length " + str(len(content)).encode() + b" >>\nstream\n" + content + b"\nendstream")

        objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
        objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>")

        pdf = bytearray(b"%PDF-1.4\n")
        offsets = []
        for idx, obj in enumerate(objects, 1):
            offsets.append(len(pdf))
            pdf += f"{idx} 0 obj\n".encode() + obj + b"\nendobj\n"
        xref_pos = len(pdf)
        pdf += f"xref\n0 {len(objects) + 1}\n".encode()
        pdf += b"0000000000 65535 f \n"
        for off in offsets:
            pdf += f"{off:010d} 00000 n \n".encode()
        pdf += (
            f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
            f"startxref\n{xref_pos}\n%%EOF\n"
        ).encode()
        return bytes(pdf)


def export_pdf(path: Path, meta: dict, segments: list[dict]) -> None:
    pdf = _Pdf(meta.get("title") or path.stem)
    info_lines = [
        f"Idioma: {meta.get('language', '?')}  |  Duracao: {meta.get('duration', 0):.1f}s",
    ]
    if meta.get("uploader"):
        info_lines.append(f"Canal: {meta['uploader']}")
    if meta.get("url"):
        info_lines.append(f"Fonte: {meta['url']}")
    for line in info_lines:
        pdf.add_paragraph(line)
    pdf.add_paragraph("")
    for seg in segments:
        pdf.add_paragraph(f"[{fmt_ts(seg['start'], '.')[3:8]}] {seg['text']}")
        if len(pdf.pages[-1]) > 45:
            pdf.new_page()
    path.write_bytes(pdf.build())


def export_outputs(out_dir: Path, base: Path, formats: list[str], meta: dict, segments: list[dict]) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    if "txt" in formats:
        path = base.with_suffix(".txt")
        path.write_text(
            "\n".join(f"[{fmt_ts(s['start'], '.')} -> {fmt_ts(s['end'], '.')}] {s['text']}" for s in segments) + "\n",
            encoding="utf-8",
        )
        written.append(path)

    if "md" in formats:
        path = base.with_suffix(".md")
        lines = [f"# {meta.get('title', 'Transcricao')}", ""]
        if meta.get("url"):
            lines.append(f"- Fonte: {meta['url']}")
        if meta.get("uploader"):
            lines.append(f"- Canal: {meta['uploader']}")
        lines.append(f"- Duracao: {meta.get('duration', 0):.1f}s")
        lines.append("")
        lines.extend(f"**[{short_ts(s['start'])}]** {s['text']}" for s in segments)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        written.append(path)

    if "srt" in formats:
        path = base.with_suffix(".srt")
        blocks = [
            f"{i}\n{fmt_ts(s['start'])} --> {fmt_ts(s['end'])}\n{s['text']}\n"
            for i, s in enumerate(segments, 1)
        ]
        path.write_text("\n".join(blocks), encoding="utf-8")
        written.append(path)

    if "json" in formats:
        path = base.with_suffix(".json")
        payload = {
            "title": meta.get("title"),
            "url": meta.get("url"),
            "uploader": meta.get("uploader"),
            "language": meta.get("language"),
            "duration": round(meta.get("duration", 0), 2),
            "segments": segments,
        }
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        written.append(path)

    if "pdf" in formats:
        path = base.with_suffix(".pdf")
        export_pdf(path, meta, segments)
        written.append(path)

    return written


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #

def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    ap = argparse.ArgumentParser(description="Transcreve a fala de um video sem deixar residuo.")
    ap.add_argument("source", nargs="?", help="URL do video ou arquivo local")
    ap.add_argument("--model", default="small", help="small (padrao), medium, large-v3")
    ap.add_argument("--lang", default="pt", help="idioma; 'auto' detecta")
    ap.add_argument("--prompt", default=None, help="contexto para nomes proprios")
    ap.add_argument("--duration", type=float, default=0, help="corta o audio nesse segundo")
    ap.add_argument("--format", default="", help="md,txt,srt,json,pdf (separados por virgula)")
    ap.add_argument("--out", default="", help="pasta escolhida para exportar")
    ap.add_argument("--name", default="", help="nome base dos arquivos exportados")
    ap.add_argument("--cleanup-input", action="store_true", help="apaga o arquivo de entrada ao terminar")
    ap.add_argument("--check", action="store_true", help="verifica dependencias e sai")
    args = ap.parse_args()

    if args.check:
        results = check_dependencies()
        for name, ok, detail in results:
            print(f"{'OK   ' if ok else 'FALTA'} {name}: {detail}")
        return EXIT_OK if all(ok for _, ok, _ in results) else EXIT_FAIL

    require_dependencies()

    if not args.source:
        print("[ERRO] informe a fonte (URL ou arquivo) ou use --check.", file=sys.stderr)
        return EXIT_USAGE

    formats = [f.strip().lower() for f in args.format.split(",") if f.strip()]
    if formats and not args.out:
        print("[ERRO] escolha a pasta de destino com --out antes de exportar.", file=sys.stderr)
        return EXIT_USAGE
    if args.out and not formats:
        formats = ["md"]

    started = time.time()
    lang = None if args.lang.lower() == "auto" else args.lang

    with tempfile.TemporaryDirectory(prefix="transcrever-video-") as tmp:
        tmp_dir = Path(tmp)
        src = Path(args.source)
        meta: dict = {}

        if src.exists():
            media = src
            meta["title"] = args.name or src.stem
            meta["duration"] = args.duration or probe_duration(media)
        else:
            if not re.match(r"^https?://", args.source):
                print(f"[ERRO] arquivo nao encontrado: {args.source}", file=sys.stderr)
                return EXIT_USAGE
            media, meta = download_audio(args.source, tmp_dir)
            if args.duration:
                meta["duration"] = args.duration

        wav = tmp_dir / "audio_16k.wav"
        cut = ["-t", f"{args.duration:.2f}"] if args.duration else []
        run_ffmpeg(["-i", str(media), *cut, "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", str(wav)])

        try:
            segments, info = transcribe(wav, args.model, lang, args.prompt)
        except Exception as exc:  # noqa: BLE001
            print(f"[ERRO] transcricao falhou: {exc}", file=sys.stderr)
            return EXIT_FAIL

        meta["language"] = info.language
        meta["duration"] = meta.get("duration") or info.duration

        base_name = safe_name(args.name or meta.get("title") or "transcricao")
        base = Path(args.out).expanduser().resolve() / base_name if formats else None

    # a pasta temporaria ja foi apagada aqui

    print(f"# {meta.get('title', 'Transcricao')}")
    if meta.get("uploader"):
        print(f"# canal: {meta['uploader']}")
    print(f"# idioma: {info.language} ({info.language_probability:.0%}) | duracao: {meta['duration']:.1f}s")
    print()
    for seg in segments:
        print(f"[{short_ts(seg['start'])}] {seg['text']}")

    if formats and base:
        written = export_outputs(base.parent, base, formats, meta, segments)
        print("\n# exportado:")
        for path in written:
            print(f"#   {path}")

    print(f"\n# tempo: {time.time() - started:.1f}s | residuo em disco: 0 arquivo temporario")
    if args.cleanup_input and src.exists() and src.resolve().is_file():
        src.unlink()
        print(f"# entrada removida: {src}")
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
