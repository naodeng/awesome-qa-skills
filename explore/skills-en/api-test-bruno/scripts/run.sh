#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
INPUT_PATH="${1:-$ROOT_DIR/examples}"
TMP_JSON="$ROOT_DIR/.tmp.normalized.json"
OUT_DIR="$ROOT_DIR/generated-bruno"

python3 "$SCRIPT_DIR/parse_api_sources.py" --input "$INPUT_PATH" --output "$TMP_JSON"
python3 "$SCRIPT_DIR/generate_bruno_requests.py" --input "$TMP_JSON" --output-dir "$OUT_DIR"

if ! command -v bru >/dev/null 2>&1; then
  echo "bru not found. Collection generated at: $OUT_DIR"
  exit 0
fi

"$SCRIPT_DIR/run-tests.sh" "$OUT_DIR" "staging"
