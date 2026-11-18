#!/usr/bin/env python3
"""Valida as skills deste repositorio sem dependencias externas.

Confere, para cada pasta da raiz que tenha SKILL.md:

  - frontmatter YAML presente e legivel
  - `name` igual ao nome da pasta, em minusculas com hifens
  - `description` preenchida e dentro do limite de 1024 caracteres
  - caminhos citados (`scripts/...`, `references/...`) existem de fato
  - scripts Python compilam (sem gravar .pyc)

Uso:
    python scripts/validar_skills.py

Saida: relatorio por skill. Codigo 0 quando tudo passa, 1 quando ha erro.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
PATH_RE = re.compile(r"(?<![\w/])((?:scripts|references|assets)/[A-Za-z0-9._/-]+)")
SKIP_DIRS = {"scripts", ".git", ".github", "node_modules", "__pycache__"}


def reconfigure_stdout() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, "SKILL.md nao comeca com --- (frontmatter ausente)"

    data: dict[str, str] = {}
    key: str | None = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return data, None
        if not line.strip():
            continue
        if line[:1].isspace() and key:
            data[key] = (data[key] + " " + line.strip()).strip()
            continue
        if ":" not in line:
            return {}, f"linha {index + 1} do frontmatter sem ':'"
        key, _, value = line.partition(":")
        key = key.strip()
        data[key] = value.strip().strip("'\"")
    return {}, "frontmatter sem fechamento ---"


def check_paths(skill_dir: Path, text: str) -> list[str]:
    problems: list[str] = []
    seen: set[str] = set()
    for match in PATH_RE.finditer(text):
        raw = match.group(1).rstrip(".,;:)")
        if raw in seen or "*" in raw or "<" in raw:
            continue
        # Referência a pasta (termina em / ou não tem extensão) é exemplo de
        # organização, não arquivo obrigatório.
        if raw.endswith("/") or "." not in raw.rsplit("/", 1)[-1]:
            continue
        seen.add(raw)
        if not (skill_dir / raw).exists():
            problems.append(f"caminho citado nao existe: {raw}")
    return problems


def check_python(skill_dir: Path) -> tuple[list[str], int]:
    problems: list[str] = []
    count = 0
    for path in sorted(skill_dir.rglob("*.py")):
        if "__pycache__" in path.parts:
            continue
        count += 1
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except SyntaxError as exc:
            problems.append(f"{path.relative_to(skill_dir)}: erro de sintaxe na linha {exc.lineno}")
        except UnicodeDecodeError:
            problems.append(f"{path.relative_to(skill_dir)}: nao esta em UTF-8")
    return problems, count


def validate(skill_dir: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    notes: list[str] = []
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")

    meta, fm_error = parse_frontmatter(text)
    if fm_error:
        errors.append(fm_error)
        return errors, notes

    name = meta.get("name", "")
    if not name:
        errors.append("frontmatter sem 'name'")
    elif name != skill_dir.name:
        errors.append(f"name '{name}' difere da pasta '{skill_dir.name}'")
    elif not NAME_RE.match(name):
        errors.append(f"name '{name}' fora do padrao minusculas-com-hifens")
    else:
        notes.append("name")

    description = meta.get("description", "")
    if not description:
        errors.append("frontmatter sem 'description'")
    elif len(description) > 1024:
        errors.append(f"description com {len(description)} caracteres (limite 1024)")
    elif len(description) < 40:
        errors.append(f"description curta demais ({len(description)} caracteres)")
    else:
        notes.append(f"description ({len(description)} caracteres)")

    path_problems = check_paths(skill_dir, text)
    errors.extend(path_problems)
    if not path_problems:
        notes.append("caminhos citados")

    python_problems, py_count = check_python(skill_dir)
    errors.extend(python_problems)
    if not python_problems and py_count:
        notes.append(f"python ({py_count} arquivo(s))")

    if not (skill_dir / "SKILL.md").read_text(encoding="utf-8").strip():
        errors.append("SKILL.md vazio")

    return errors, notes


def main() -> int:
    reconfigure_stdout()
    root = Path(__file__).resolve().parent.parent
    skills = sorted(
        path
        for path in root.iterdir()
        if path.is_dir()
        and path.name not in SKIP_DIRS
        and (path / "SKILL.md").is_file()
    )

    if not skills:
        print(f"[ERRO] nenhuma skill encontrada em {root}")
        return 1

    total_errors = 0
    for skill_dir in skills:
        errors, notes = validate(skill_dir)
        status = "OK   " if not errors else "FALHA"
        print(f"{status} {skill_dir.name}")
        for note in notes:
            print(f"        ok  {note}")
        for error in errors:
            print(f"        erro {error}")
        total_errors += len(errors)

    print()
    print(f"{len(skills)} skill(s) verificada(s), {total_errors} erro(s)")
    return 0 if total_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
