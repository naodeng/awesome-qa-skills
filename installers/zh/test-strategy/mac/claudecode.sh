#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCAL_REPO_ROOT="$(cd "$SCRIPT_DIR/../../../../" && pwd)"
SOURCE_REPO="/Users/nao.deng/awsomeCode/awesome-qa-skills"

if [[ -x "$LOCAL_REPO_ROOT/install-skills-mac.sh" ]]; then
  exec bash "$LOCAL_REPO_ROOT/install-skills-mac.sh" --tool "claudecode" --lang "zh" --skill "test-strategy" "$@"
fi

exec bash "$SOURCE_REPO/install-skills-mac.sh" --tool "claudecode" --lang "zh" --skill "test-strategy" "$@"
