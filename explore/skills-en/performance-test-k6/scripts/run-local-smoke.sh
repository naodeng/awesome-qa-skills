#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TOOLS_DIR="$SCRIPT_DIR/tools"
MOCK_PORT="${MOCK_PORT:-18080}"
BASE_URL="${BASE_URL:-http://127.0.0.1:${MOCK_PORT}}"

python3 "$TOOLS_DIR/local_mock_server.py" --port "$MOCK_PORT" >/tmp/perf-mock-${MOCK_PORT}.log 2>&1 &
MOCK_PID=$!

cleanup() {
  kill "$MOCK_PID" >/dev/null 2>&1 || true
}
trap cleanup EXIT

ready=0
for _ in $(seq 1 30); do
  if command -v curl >/dev/null 2>&1 && curl -sf "$BASE_URL/" >/dev/null; then
    ready=1
    break
  fi
  sleep 0.1
done

if [ "$ready" -ne 1 ]; then
  echo "Local mock server is not reachable at $BASE_URL."
  echo "This environment may block localhost networking."
  echo "Try running this command on a local machine with loopback enabled."
  exit 2
fi

export BASE_URL
export ENV="${ENV:-local}"
export K6_WEB_DASHBOARD="${K6_WEB_DASHBOARD:-false}"

"$SCRIPT_DIR/run-tests.sh" smoke
