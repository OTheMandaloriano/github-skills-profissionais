#!/usr/bin/env bash
set -euo pipefail

check=false
upgrade=false

for arg in "$@"; do
  case "$arg" in
    --check) check=true ;;
    --upgrade) upgrade=true ;;
    *) echo "Uso: $0 [--check] [--upgrade]" >&2; exit 2 ;;
  esac
done

skill_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
requirements="$skill_root/requirements.txt"

python_bin="${PYTHON:-python3}"
command -v "$python_bin" >/dev/null 2>&1 || python_bin="python"
command -v "$python_bin" >/dev/null 2>&1 || {
  echo "Python 3 nao encontrado. Instale python3 e tente novamente." >&2
  exit 1
}

version="$("$python_bin" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
echo "Python: $version ($python_bin)"

"$python_bin" - <<'PY' || {
import sys
if sys.version_info < (3, 9):
    raise SystemExit("Python 3.9 ou superior e necessario.")
PY
  exit 1
}

modules_ok=false
if "$python_bin" -c 'import importlib.util as u, sys; sys.exit(0 if all(u.find_spec(m) for m in ("faster_whisper", "yt_dlp")) else 1)'; then
  modules_ok=true
fi

ffmpeg_path="$(command -v ffmpeg || true)"
if [[ -z "$ffmpeg_path" ]]; then
  ffmpeg_path="$("$python_bin" -c 'import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())' 2>/dev/null || true)"
fi

if [[ "$check" == true ]]; then
  [[ "$modules_ok" == true ]] && echo "OK    faster-whisper + yt-dlp" || echo "FALTA faster-whisper + yt-dlp"
  [[ -n "$ffmpeg_path" ]] && echo "OK    ffmpeg: $ffmpeg_path" || echo "FALTA ffmpeg"
  [[ "$modules_ok" == true && -n "$ffmpeg_path" ]] && exit 0 || exit 1
fi

if [[ "$modules_ok" != true ]]; then
  args=(-m pip install --user --disable-pip-version-check -r "$requirements")
  [[ "$upgrade" == true ]] && args+=(--upgrade)
  "$python_bin" "${args[@]}"
  "$python_bin" -c 'import importlib.util as u, sys; sys.exit(0 if all(u.find_spec(m) for m in ("faster_whisper", "yt_dlp")) else 1)' || {
    echo "pip instalou, mas os modulos ainda nao aparecem. Verifique o ambiente virtual." >&2
    exit 1
  }
fi

if [[ -z "$ffmpeg_path" ]]; then
  ffmpeg_path="$("$python_bin" -c 'import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())' 2>/dev/null || true)"
fi

if [[ -n "$ffmpeg_path" ]]; then
  echo "Dependencias prontas. ffmpeg: $ffmpeg_path"
  exit 0
fi

echo "Ainda falta ffmpeg. Instale o pacote do sistema ou rode: $python_bin -m pip install --user imageio-ffmpeg" >&2
exit 1
