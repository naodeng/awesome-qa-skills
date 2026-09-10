#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

echo "[1/8] Organize and validate project directories"
python3 scripts/organize_project_dirs.py >/tmp/skills-organize-check.out
cat /tmp/skills-organize-check.out

echo "[2/8] Validate agents metadata"
python3 scripts/validate_agents_metadata.py --report /tmp/skills-metadata-check.md >/tmp/skills-metadata-check.out
cat /tmp/skills-metadata-check.out

echo "[3/8] Check generated governance inventory"
python3 scripts/generate_skill_governance_inventory.py --check

echo "[4/8] Validate skills independence"
python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings --report-md /tmp/skills-independence-check.md >/tmp/skills-independence-check.out
cat /tmp/skills-independence-check.out

echo "[5/8] Validate all skills integrity"
python3 scripts/validate_skills_integrity.py --fail-on-findings --report-md /tmp/skills-integrity-check.md >/tmp/skills-integrity-check.out
cat /tmp/skills-integrity-check.out

echo "[6/8] Check external snapshot hygiene"
python3 scripts/check_external_snapshots.py --skills-root skills --max-per-skill 5 >/tmp/skills-external-check.out
cat /tmp/skills-external-check.out

echo "[7/8] Validate skill-up eval YAML (if skill-up installed)"
bash scripts/validate_skill_evals.sh >/tmp/skills-eval-validate.out
cat /tmp/skills-eval-validate.out

echo "[8/8] Validate bilingual documentation and Skill catalog"
python3 scripts/check_docs_bilingual.py --repo-root .

echo "Skills quality checks passed."
