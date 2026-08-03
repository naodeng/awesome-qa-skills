#!/usr/bin/env bash
# Run skill-up with a repo-local output dir (never pollute skills/).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

if ! command -v skill-up >/dev/null 2>&1; then
  echo "skill-up not found. Install:"
  echo "  curl -fsSL https://raw.githubusercontent.com/alibaba/skill-up/main/install.sh | bash"
  exit 1
fi

EVAL_YAML="${1:?Usage: $0 <path-to-evals/eval.yaml> [extra skill-up run args...]}"
shift || true

# Derive a stable output folder name from the skill directory
skill_dir="$(cd "$(dirname "$EVAL_YAML")/.." && pwd)"
skill_name="$(basename "$skill_dir")"
out_dir="${REPO_ROOT}/.skill-up-workspaces/${skill_name}"
mkdir -p "$out_dir"

engine="${SKILL_UP_ENGINE:-codex}"

echo "eval:    $EVAL_YAML"
echo "engine:  $engine"
echo "output:  $out_dir"

exec skill-up run "$EVAL_YAML" \
  --engine "$engine" \
  --output-dir "$out_dir" \
  "$@"
