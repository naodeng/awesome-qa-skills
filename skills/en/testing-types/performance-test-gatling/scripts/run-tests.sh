#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SIM_DIR="$SCRIPT_DIR/simulations"
REPORT_DIR="$SCRIPT_DIR/../reports"
mkdir -p "$REPORT_DIR"

TEST_TYPE="${1:-load}"

case "$TEST_TYPE" in
  load)
    SIM_CLASS="simulations.LoadSimulation"
    ;;
  stress)
    SIM_CLASS="simulations.StressSimulation"
    ;;
  spike)
    SIM_CLASS="simulations.SpikeSimulation"
    ;;
  soak)
    SIM_CLASS="simulations.SoakSimulation"
    ;;
  smoke|api)
    SIM_CLASS="simulations.ApiSmokeSimulation"
    ;;
  *)
    echo "Unknown test type: $TEST_TYPE"
    echo "Usage: $0 [load|stress|spike|soak|smoke]"
    exit 1
    ;;
esac

GATLING_BIN="${GATLING_BIN:-gatling}"
if ! command -v "$GATLING_BIN" >/dev/null 2>&1; then
  echo "Gatling CLI not found."
  echo "Install Gatling and ensure 'gatling' is in PATH, or set GATLING_BIN=/path/to/gatling."
  echo "Reference: ../references/setup-and-ci.md"
  exit 1
fi

echo "Running $TEST_TYPE using $SIM_CLASS"
echo "Simulation sources directory: $SIM_DIR"

TS="$(date +%Y%m%d-%H%M%S)"
RUN_DESC="perf-${TEST_TYPE}-${TS}"

# Note: CLI flags vary by Gatling distribution.
# This command assumes modern Gatling CLI with --simulation and --sources-folder options.
"$GATLING_BIN" --simulation "$SIM_CLASS" --sources-folder "$SIM_DIR" --run-description "$RUN_DESC"

echo "Completed: $RUN_DESC"
echo "Check generated reports in your Gatling results directory."
