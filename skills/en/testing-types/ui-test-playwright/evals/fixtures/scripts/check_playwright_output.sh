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

export EVAL_FINAL_MESSAGE="$text"
tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT
artifact="$tmp_dir/playwright-artifact.js"

if ! python3 - "$artifact" <<'PY'
from pathlib import Path
import os
import re
import sys

text = os.environ.get("EVAL_FINAL_MESSAGE", "")
blocks = re.findall(r"```(?:javascript|js)\s*\r?\n(.*?)```", text, flags=re.IGNORECASE | re.DOTALL)
if not blocks:
    print("FAIL: no JavaScript code block was provided", file=sys.stderr)
    raise SystemExit(1)

artifact = max(blocks, key=len).strip()
if not artifact:
    print("FAIL: JavaScript code block is empty", file=sys.stderr)
    raise SystemExit(1)

required = {
    "test declaration": r"\btest\s*\(",
    "navigation": r"\bpage\.goto\s*\(",
    "assertion": r"\bexpect\s*\(",
}
for label, pattern in required.items():
    if not re.search(pattern, artifact):
        print(f"FAIL: missing {label} in extracted artifact", file=sys.stderr)
        raise SystemExit(1)

Path(sys.argv[1]).write_text(artifact + "\n", encoding="utf-8")
PY
then
  exit 1
fi

if ! command -v node >/dev/null 2>&1; then
  echo "FAIL: node is required for JavaScript syntax validation" >&2
  exit 1
fi
if ! node --check "$artifact" >/dev/null 2>&1; then
  echo "FAIL: extracted Playwright artifact has invalid JavaScript syntax" >&2
  exit 1
fi

echo "PASS: Playwright artifact has a JavaScript block, test declaration, navigation, assertion, and valid syntax"
