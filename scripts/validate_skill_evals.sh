#!/usr/bin/env bash
# Validate all skill-up eval.yaml files (no API key required).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

if ! command -v skill-up >/dev/null 2>&1; then
  echo "skill-up not found in PATH; skip eval YAML validation."
  echo "Install: curl -fsSL https://raw.githubusercontent.com/alibaba/skill-up/main/install.sh | bash"
  exit 0
fi

fail=0
ok=0
while IFS= read -r f; do
  if skill-up validate "$f" >/dev/null 2>&1; then
    ok=$((ok + 1))
  else
    echo "FAIL: $f"
    skill-up validate "$f" 2>&1 || true
    fail=$((fail + 1))
  fi
done < <(find skills -name eval.yaml | sort)

echo "skill-up validate: ok=$ok fail=$fail"
if [[ "$fail" -gt 0 ]]; then
  exit 1
fi
