#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
INPUT_PATH="${1:-$ROOT_DIR/examples}"
TMP_JSON="$ROOT_DIR/.tmp.normalized.json"
OUT_JAVA="$SCRIPT_DIR/templates/restassured/src/test/java/com/example/api/GeneratedApiTest.java"

python3 "$SCRIPT_DIR/parse_api_sources.py" --input "$INPUT_PATH" --output "$TMP_JSON"
python3 "$SCRIPT_DIR/generate_restassured_tests.py" --input "$TMP_JSON" --output "$OUT_JAVA"

if ! command -v mvn >/dev/null 2>&1; then
  echo "mvn not found. Test class generated at: $OUT_JAVA"
  exit 0
fi

cd "$SCRIPT_DIR/templates/restassured"
mvn -q test
