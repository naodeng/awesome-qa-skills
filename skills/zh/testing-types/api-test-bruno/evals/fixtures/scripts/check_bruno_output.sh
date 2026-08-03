#!/usr/bin/env bash
# Script judge for Bruno-oriented skill outputs.
# skill-up provides: EVAL_FINAL_MESSAGE, EVAL_EXIT_CODE, EVAL_TRANSCRIPT_PATH
set -euo pipefail

text="${EVAL_FINAL_MESSAGE:-}"
if [[ -z "$text" && -n "${EVAL_TRANSCRIPT_PATH:-}" && -f "$EVAL_TRANSCRIPT_PATH" ]]; then
  text="$(cat "$EVAL_TRANSCRIPT_PATH")"
fi
if [[ -z "$text" && -f "outputs/response.md" ]]; then
  text="$(cat outputs/response.md)"
fi
if [[ -z "$text" ]]; then
  # last resort: search workspace
  f="$(find . -name response.md 2>/dev/null | head -1 || true)"
  if [[ -n "$f" ]]; then
    text="$(cat "$f")"
  fi
fi

if [[ -z "$text" ]]; then
  echo "FAIL: empty final message / no response.md"
  exit 1
fi

fail=0
need_any() {
  local label="$1"
  shift
  local ok=0
  local k
  for k in "$@"; do
    if grep -Fqi -- "$k" <<<"$text"; then
      ok=1
      break
    fi
  done
  if [[ "$ok" -eq 0 ]]; then
    echo "FAIL missing any of: $*"
    fail=1
  else
    echo "OK: $label"
  fi
}

need_any "Bruno marker" "Bruno" "bruno"
need_any "collection marker" "collection" "Collection" "集合" ".bru"

if grep -Eiq 'Bearer [A-Za-z0-9_\-]{20,}' <<<"$text"; then
  echo "FAIL: looks like a hardcoded bearer token"
  fail=1
else
  echo "OK: no long bearer literal"
fi

if [[ "$fail" -ne 0 ]]; then
  exit 1
fi
exit 0
