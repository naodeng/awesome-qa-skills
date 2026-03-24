#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

echo "[1/6] Organize and validate project directories"
python3 scripts/organize_project_dirs.py >/tmp/skills-organize-check.out
cat /tmp/skills-organize-check.out

echo "[2/6] Validate agents metadata"
python3 scripts/validate_agents_metadata.py --report /tmp/skills-metadata-check.md >/tmp/skills-metadata-check.out
cat /tmp/skills-metadata-check.out

echo "[3/6] Validate skills independence"
python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings --report-md /tmp/skills-independence-check.md >/tmp/skills-independence-check.out
cat /tmp/skills-independence-check.out

echo "[4/6] Validate all skills integrity"
python3 scripts/validate_skills_integrity.py --fail-on-findings --report-md /tmp/skills-integrity-check.md >/tmp/skills-integrity-check.out
cat /tmp/skills-integrity-check.out

echo "[5/6] Check external snapshot hygiene"
python3 scripts/check_external_snapshots.py --skills-root skills --max-per-skill 5 >/tmp/skills-external-check.out
cat /tmp/skills-external-check.out

echo "[6/6] Build release skill directories"
python3 scripts/build_release_skill_dirs.py >/tmp/skills-release-build.out
cat /tmp/skills-release-build.out

echo "Skills quality checks passed."
