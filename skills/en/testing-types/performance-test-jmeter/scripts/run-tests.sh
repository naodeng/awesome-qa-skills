#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPORT_DIR="$SCRIPT_DIR/../reports"
mkdir -p "$REPORT_DIR"
TS="$(date +%Y%m%d-%H%M%S)"
REPORT_JSON="$REPORT_DIR/performance-test-jmeter-$TS.json"

echo "Running performance-test-jmeter lightweight entry point"
echo "Report path: $REPORT_JSON"

jmeter -n -t "${TEST_PLAN:-test-plan.jmx}" -l "$REPORT_DIR/results.jtl" -e -o "$REPORT_DIR/html"
