#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"
CLI_VERSION="1.7.0"
CLI_PACKAGE="${SKILLS_CLI_PACKAGE:-naodeng/awesome-qa-skills}"
REPRESENTATIVE_SKILLS=(
  requirements-analysis
  functional-testing
  api-testing
  performance-testing
  ai-agent-testing
  release-testing-workflow
  skill-change-verification
)

python3 "${SCRIPT_DIR}/check_skills_cli_compatibility.py" \
  --skills-root "${REPO_ROOT}/skills" \
  --fail-on-findings \
  "$@"

CLI_OUTPUT="$(mktemp "${TMPDIR:-/tmp}/awesome-qa-skills-cli-discovery.XXXXXX")"
SMOKE_HOME="$(mktemp -d "${TMPDIR:-/tmp}/awesome-qa-skills-cli-home.XXXXXX")"
cleanup() {
  rm -f "${CLI_OUTPUT}"
  rm -rf "${SMOKE_HOME}"
}
trap cleanup EXIT

run_cli() {
  npx --yes "skills@${CLI_VERSION}" "$@"
}

echo "[skills-cli] Discovering representative Skills with skills@${CLI_VERSION} from ${CLI_PACKAGE}"
(
  export HOME="${SMOKE_HOME}"
  export XDG_CONFIG_HOME="${SMOKE_HOME}/.config"
  run_cli add "${CLI_PACKAGE}" --list
) >"${CLI_OUTPUT}" 2>&1
cat "${CLI_OUTPUT}"
for skill in "${REPRESENTATIVE_SKILLS[@]}"; do
  if ! grep -Fq "${skill}" "${CLI_OUTPUT}"; then
    echo "[skills-cli] missing representative Skill in CLI discovery: ${skill}" >&2
    exit 1
  fi
done

echo "[skills-cli] Installing English functional-testing into an isolated global Codex target"
(
  export HOME="${SMOKE_HOME}"
  export XDG_CONFIG_HOME="${SMOKE_HOME}/.config"
  run_cli add "${CLI_PACKAGE}" --skill functional-testing -g -a codex -y
)

INSTALLED_SKILL="${SMOKE_HOME}/.agents/skills/functional-testing/SKILL.md"
test -f "${INSTALLED_SKILL}"
grep -Fxq "name: functional-testing" "${INSTALLED_SKILL}"
grep -Fxq "# Functional Testing (English)" "${INSTALLED_SKILL}"
echo "[skills-cli] English functional-testing smoke passed"
