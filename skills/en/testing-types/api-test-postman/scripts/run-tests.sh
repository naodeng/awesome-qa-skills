#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPORT_DIR="$SCRIPT_DIR/../reports"
mkdir -p "$REPORT_DIR"
TS="$(date +%Y%m%d-%H%M%S)"
REPORT_JSON="$REPORT_DIR/api-test-postman-$TS.json"

echo "Running api-test-postman lightweight entry point"
echo "Report path: $REPORT_JSON"

newman run "${COLLECTION:-collection.json}" -e "${ENVIRONMENT:-environment.json}" --reporters cli,json --reporter-json-export "$REPORT_JSON"
