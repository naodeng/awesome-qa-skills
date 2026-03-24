#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
INPUT_PATH="${1:-$ROOT_DIR/examples}"
TMP_JSON="$ROOT_DIR/.tmp.normalized.json"
OUT_TEST="$SCRIPT_DIR/templates/pytest/tests/test_generated_api.py"

python3 "$SCRIPT_DIR/parse_api_sources.py" --input "$INPUT_PATH" --output "$TMP_JSON"
python3 "$SCRIPT_DIR/generate_pytest_tests.py" --input "$TMP_JSON" --output "$OUT_TEST"

cd "$SCRIPT_DIR/templates/pytest"
python3 -m pytest -q || {
  echo "pytest run failed (likely missing dependencies). Install with:"
  echo "pip install -r requirements.txt"
  exit 1
}
