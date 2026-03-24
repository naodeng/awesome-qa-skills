#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_ROOT="$REPO_ROOT/skills"

TOOL="${TOOL:-all}"           # claude|cursor|codex|kiro|opencode|all
LANGUAGE="${LANGUAGE:-all}"   # zh|en|all
DEST="${DEST:-}"              # optional custom destination
DRY_RUN="${DRY_RUN:-0}"       # 1 for preview only
SKILL="${SKILL:-all}"         # all or exact skill directory name

usage() {
  cat <<'EOF'
Usage:
  scripts/install-skills-mac.sh [--tool TOOL] [--lang LANG] [--skill NAME] [--dest PATH] [--dry-run]

Options:
  --tool       Target AI tool: claude | cursor | codex | kiro | opencode | all
  --lang       Skills language: zh | en | all
  --skill      Install only one skill directory name (e.g. functional-testing, functional-testing-en)
  --dest       Custom install destination (overrides tool default path)
  --dry-run    Preview operations without writing files
  -h, --help   Show help

Examples:
  scripts/install-skills-mac.sh --tool codex --lang zh
  scripts/install-skills-mac.sh --tool codex --lang all --skill functional-testing-en
  scripts/install-skills-mac.sh --tool all --lang all
  scripts/install-skills-mac.sh --tool cursor --lang en --dry-run
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --tool) TOOL="${2:-}"; shift 2 ;;
    --lang) LANGUAGE="${2:-}"; shift 2 ;;
    --skill) SKILL="${2:-}"; shift 2 ;;
    --dest) DEST="${2:-}"; shift 2 ;;
    --dry-run) DRY_RUN=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; usage; exit 1 ;;
  esac
done

default_dest_for_tool() {
  case "$1" in
    claude) echo "$HOME/.claude/skills" ;;
    cursor) echo "$HOME/.cursor/skills" ;;
    codex) echo "$HOME/.codex/skills" ;;
    kiro) echo "$HOME/.kiro/skills" ;;
    opencode) echo "$HOME/.opencode/skills" ;;
    *) return 1 ;;
  esac
}

collect_skill_dirs() {
  local section="$1"
  local dir="$SKILLS_ROOT/$section"
  [[ -d "$dir" ]] || return 0
  for s in "$dir"/*; do
    [[ -d "$s" ]] || continue
    local name
    name="$(basename "$s")"
    if [[ "$LANGUAGE" == "zh" ]]; then
      if [[ "$name" != *-en ]]; then
        if [[ "$SKILL" == "all" || "$SKILL" == "$name" ]]; then
          echo "$s"
        fi
      fi
    elif [[ "$LANGUAGE" == "en" ]]; then
      if [[ "$name" == *-en ]]; then
        if [[ "$SKILL" == "all" || "$SKILL" == "$name" ]]; then
          echo "$s"
        fi
      fi
    else
      if [[ "$SKILL" == "all" || "$SKILL" == "$name" ]]; then
        echo "$s"
      fi
    fi
  done
}

sync_dir() {
  local src="$1"
  local dst="$2"
  if [[ "$DRY_RUN" == "1" ]]; then
    echo "[DRY-RUN] copy $src -> $dst"
    return 0
  fi

  mkdir -p "$(dirname "$dst")"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a --delete "$src/" "$dst/"
  else
    rm -rf "$dst"
    mkdir -p "$dst"
    cp -R "$src/." "$dst/"
  fi
}

install_for_tool() {
  local tool="$1"
  local target="$DEST"
  if [[ -z "$target" ]]; then
    target="$(default_dest_for_tool "$tool")"
  fi
  if [[ -z "$target" ]]; then
    echo "Unable to determine target path for tool: $tool" >&2
    return 1
  fi

  echo "==> Installing skills for tool: $tool"
  echo "    Target: $target"
  echo "    Language: $LANGUAGE"

  local src
  while IFS= read -r src; do
    [[ -n "$src" ]] || continue
    local section name dst
    section="$(basename "$(dirname "$src")")"
    name="$(basename "$src")"
    dst="$target/$section/$name"
    sync_dir "$src" "$dst"
  done < <(
    collect_skill_dirs "testing-types"
    collect_skill_dirs "testing-workflows"
  )
}

if [[ ! -d "$SKILLS_ROOT/testing-types" || ! -d "$SKILLS_ROOT/testing-workflows" ]]; then
  echo "skills source not found under: $SKILLS_ROOT" >&2
  exit 1
fi

TOOLS=()
if [[ "$TOOL" == "all" ]]; then
  TOOLS=(claude cursor codex kiro opencode)
else
  TOOLS=("$TOOL")
fi

for t in "${TOOLS[@]}"; do
  install_for_tool "$t"
done

if [[ "$DRY_RUN" == "1" ]]; then
  echo "Dry-run completed. No files were written."
else
  echo "Installation completed."
fi
