#!/usr/bin/env bash
set -euo pipefail

target="all"
force=false
dry_run=false
home_dir="${HOME:-}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target) target="$2"; shift 2 ;;
    --force) force=true; shift ;;
    --dry-run) dry_run=true; shift ;;
    --home) home_dir="$2"; shift 2 ;;
    *) echo "Uso: $0 [--target codex|claude|opencode|all] [--force] [--dry-run] [--home caminho]" >&2; exit 2 ;;
  esac
done

[[ -n "$home_dir" && "$home_dir" != "/" ]] || { echo "Diretório de usuário inválido. Defina HOME ou use --home caminho." >&2; exit 1; }

repository_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Descobre as skills pela presença de SKILL.md: adicionar uma pasta nova
# no repositório já a torna instalável, sem editar este script.
skills=()
for dir in "$repository_root"/*/; do
  [[ -f "${dir}SKILL.md" ]] || continue
  skills+=("$(basename "$dir")")
done

[[ ${#skills[@]} -gt 0 ]] || { echo "Nenhuma skill encontrada em $repository_root (procure por pastas com SKILL.md)." >&2; exit 1; }

echo "Skills encontradas: ${skills[*]}"

check_target() {
  local platform="$1"
  local destination_root="$2"
  local skill source destination

  for skill in "${skills[@]}"; do
    source="$repository_root/$skill"
    destination="$destination_root/$skill"
    [[ -f "$source/SKILL.md" ]] || { echo "Skill de origem não encontrada: $source" >&2; exit 1; }
    if [[ -e "$destination" && "$force" != true ]]; then
      echo "A skill já existe em $destination. Revise-a e execute novamente com --force para atualizar seus arquivos." >&2
      exit 1
    fi
  done
}

install_target() {
  local platform="$1"
  local destination_root="$2"
  local skill source destination

  for skill in "${skills[@]}"; do
    source="$repository_root/$skill"
    destination="$destination_root/$skill"
    if [[ "$dry_run" == true ]]; then
      echo "Instalaria: $platform -> $destination"
    else
      mkdir -p "$destination_root"
      cp -R "$source" "$destination_root/"
      echo "Instalada: $platform -> $destination"
    fi
  done
}

case "$target" in
  codex)
    check_target "Codex" "$home_dir/.codex/skills"
    install_target "Codex" "$home_dir/.codex/skills"
    ;;
  claude)
    check_target "Claude Code" "$home_dir/.claude/skills"
    install_target "Claude Code" "$home_dir/.claude/skills"
    ;;
  opencode)
    check_target "OpenCode" "$home_dir/.config/opencode/skills"
    install_target "OpenCode" "$home_dir/.config/opencode/skills"
    ;;
  all)
    check_target "Codex" "$home_dir/.codex/skills"
    check_target "Claude Code" "$home_dir/.claude/skills"
    check_target "OpenCode" "$home_dir/.config/opencode/skills"
    install_target "Codex" "$home_dir/.codex/skills"
    install_target "Claude Code" "$home_dir/.claude/skills"
    install_target "OpenCode" "$home_dir/.config/opencode/skills"
    ;;
  *) echo "Destino inválido: $target" >&2; exit 2 ;;
esac
