#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_REPO="/Users/nao.deng/awsomeCode/awesome-qa-skills"

if [[ -x "$SCRIPT_DIR/scripts/install-skills-mac.sh" ]]; then
  exec bash "$SCRIPT_DIR/scripts/install-skills-mac.sh" "$@"
fi

exec bash "$SOURCE_REPO/scripts/install-skills-mac.sh" "$@"
