#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TEST_DIR="$SCRIPT_DIR/tests"
REPORT_DIR="$SCRIPT_DIR/../reports"

mkdir -p "$REPORT_DIR"

TEST_TYPE="${1:-load}"

case "$TEST_TYPE" in
  load)
    ENTRY="$TEST_DIR/load.js"
    ;;
  stress)
    ENTRY="$TEST_DIR/stress.js"
    ;;
  spike)
    ENTRY="$TEST_DIR/spike.js"
    ;;
  soak)
    ENTRY="$TEST_DIR/soak.js"
    ;;
  smoke|api)
    ENTRY="$TEST_DIR/api-smoke.js"
    ;;
  *)
    echo "Unknown test type: $TEST_TYPE"
    echo "Usage: $0 [load|stress|spike|soak|smoke]"
    exit 1
    ;;
esac

TS="$(date +%Y%m%d-%H%M%S)"
SUMMARY_JSON="$REPORT_DIR/${TEST_TYPE}-${TS}-summary.json"

echo "Running $TEST_TYPE test with entry: $ENTRY"
K6_SUMMARY_EXPORT="$SUMMARY_JSON" k6 run "$ENTRY"

echo "Summary exported: $SUMMARY_JSON"
