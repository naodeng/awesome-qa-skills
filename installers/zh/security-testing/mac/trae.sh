#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCAL_REPO_ROOT="$(cd "$SCRIPT_DIR/../../../../" && pwd)"

if [[ -x "$LOCAL_REPO_ROOT/install-skills-mac.sh" ]]; then
  exec bash "$LOCAL_REPO_ROOT/install-skills-mac.sh" --tool "trae" --lang "zh" --skill "security-testing" "$@"
fi

echo "Installer wrapper not found: $LOCAL_REPO_ROOT/install-skills-mac.sh" >&2
exit 1
