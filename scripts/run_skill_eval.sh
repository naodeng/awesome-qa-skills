#!/usr/bin/env bash
# Run skill-up with an isolated output directory and start-time evidence.
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

eval_absolute="$(cd "$(dirname "$EVAL_YAML")" && pwd)/${EVAL_YAML##*/}"
skill_dir="$(dirname "$eval_absolute")"
while [[ ! -f "$skill_dir/SKILL.md" ]]; do
  parent_dir="$(dirname "$skill_dir")"
  if [[ "$parent_dir" == "$skill_dir" ]]; then
    echo "Could not find Skill package root for Eval: $EVAL_YAML" >&2
    exit 2
  fi
  skill_dir="$parent_dir"
done
eval_relative="${eval_absolute#"$skill_dir"/}"
skill_name="$(basename "$skill_dir")"
workspace_root="${SKILL_UP_WORKSPACE_ROOT:-${REPO_ROOT}/.skill-up-workspaces}"
run_id="$(date -u +%Y%m%dT%H%M%SZ)-$$-${RANDOM}"
out_dir="${workspace_root}/${skill_name}/runs/${run_id}"

echo "eval:    $EVAL_YAML"
if [[ -n "${SKILL_UP_ENGINE:-}" ]]; then
  echo "engine:  ${SKILL_UP_ENGINE} (explicit override)"
else
  echo "engine:  configured by $eval_relative"
fi
echo "output:  $out_dir"

runner_args=(
  python3 "${REPO_ROOT}/scripts/run_skill_eval_with_evidence.py"
  --skill-dir "$skill_dir"
  --eval-file "$eval_relative"
  --output-dir "$out_dir"
  --skill-up-bin "$(command -v skill-up)"
)
if [[ -n "${SKILL_UP_ENGINE:-}" ]]; then
  runner_args+=(--engine "$SKILL_UP_ENGINE")
fi
exec "${runner_args[@]}" -- "$@"
