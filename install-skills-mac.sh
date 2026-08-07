#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ -x "$SCRIPT_DIR/scripts/install-skills-mac.sh" ]]; then
  exec bash "$SCRIPT_DIR/scripts/install-skills-mac.sh" "$@"
fi

echo "Installer implementation not found: $SCRIPT_DIR/scripts/install-skills-mac.sh" >&2
exit 1
