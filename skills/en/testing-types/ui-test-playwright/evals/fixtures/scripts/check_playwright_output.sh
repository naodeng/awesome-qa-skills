#!/usr/bin/env bash
# Script judge for the minimal Playwright artifact pilot.
set -euo pipefail

text="${EVAL_FINAL_MESSAGE:-}"
if [[ -z "$text" && -n "${EVAL_TRANSCRIPT_PATH:-}" && -f "$EVAL_TRANSCRIPT_PATH" ]]; then
  text="$(cat "$EVAL_TRANSCRIPT_PATH")"
fi
if [[ -z "$text" && -f "outputs/response.md" ]]; then
  text="$(cat outputs/response.md)"
fi

if [[ -z "$text" ]]; then
  echo "FAIL: no final response was provided"
  exit 1
fi

if [[ "${EVAL_EXIT_CODE:-0}" != "0" ]]; then
  echo "FAIL: the Skill run exited with ${EVAL_EXIT_CODE}"
  exit 1
fi

for marker in "Playwright" "test(" "page.goto(" "expect("; do
  if ! grep -Fqi -- "$marker" <<<"$text"; then
    echo "FAIL: missing artifact marker: $marker"
    exit 1
  fi
done

echo "PASS: minimal Playwright artifact markers are present"
