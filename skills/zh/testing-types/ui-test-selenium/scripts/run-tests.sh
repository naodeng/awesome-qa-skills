#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPORT_DIR="$SCRIPT_DIR/../reports"
mkdir -p "$REPORT_DIR"
TS="$(date +%Y%m%d-%H%M%S)"
REPORT_JSON="$REPORT_DIR/ui-test-selenium-$TS.json"

echo "Running ui-test-selenium lightweight entry point"
echo "Report path: $REPORT_JSON"

echo "Run your Selenium suite with the project command, for example: mvn test, pytest, gradle test, or npm test"
