#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
INPUT_PATH="${1:-$ROOT_DIR/examples}"
TMP_JSON="$ROOT_DIR/.tmp.normalized.json"
OUT_TEST="$SCRIPT_DIR/templates/supertest/tests/test_generated_api.test.js"

python3 "$SCRIPT_DIR/parse_api_sources.py" --input "$INPUT_PATH" --output "$TMP_JSON"
python3 "$SCRIPT_DIR/generate_supertest_tests.py" --input "$TMP_JSON" --output-dir "$SCRIPT_DIR/templates/supertest/tests"

if ! command -v npm >/dev/null 2>&1; then
  echo "npm not found. Tests were generated at: $OUT_TEST"
  exit 0
fi

cd "$SCRIPT_DIR/templates/supertest"
if [ ! -d node_modules ]; then
  npm install
fi
npm test
