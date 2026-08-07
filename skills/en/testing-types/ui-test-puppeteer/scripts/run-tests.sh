#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPORT_DIR="$SCRIPT_DIR/../reports"
mkdir -p "$REPORT_DIR"
TS="$(date +%Y%m%d-%H%M%S)"
REPORT_JSON="$REPORT_DIR/ui-test-puppeteer-$TS.json"

echo "Running ui-test-puppeteer lightweight entry point"
echo "Report path: $REPORT_JSON"

node "${TEST_FILE:-scripts/puppeteer-check.js}"
