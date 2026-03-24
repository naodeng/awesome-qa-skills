# skills-en Deep Audit Report

- Audit Date: 2026-03-24
- Scope: `skills/skills-en` (mapped from English skills under `skills/testing-types` and `skills/testing-workflows`)
- Method: structure audit + link integrity audit + metadata validation

## Summary

- Overall status: PASS (usable)
- Critical blockers: 0
- Fixed issue categories: 3 (broken links, missing language partition, missing example placeholders)

## Fixes Applied

1. Added English partition directory  
- Added `skills/skills-en/` as a language-based skill view (symlink mapping).

2. Fixed English-related broken links  
- Repaired cross-folder references in EN prompts and workflow prompts.
- Corrected invalid relative paths for shared docs (FAQ/contributing references).

3. Added minimal missing resources  
- Added missing `examples/` placeholders and `README.md` files referenced by quick-start docs.
- Added missing reference docs (`references/troubleshooting.md`, `output-formats.md` where required).

## Verification

- Link integrity check (excluding `node_modules`): `broken = 0`
- Metadata validation (`agents/openai.yaml`): `findings = 0`
- Language partition structure: active (`skills-en/testing-types/*`, `skills-en/testing-workflows/*`)
- Independence validation: `external = 0` (no cross-skill external dependency references)

## Remaining Recommendations

1. Remove vendored `node_modules` from example projects and enforce ignore rules.
2. Add a recurring CI check for markdown link validation to prevent regressions.

## This Round Remediation (Fix + Hardening)

1. Cross-folder document dependencies were localized into each skill (`references/_external/`).
2. Vendored `node_modules` under examples were removed to avoid external package carry-in.
3. Added automated guard script:
- `scripts/validate_skills_independence.py`
- Verifies both broken links and cross-skill dependency references.
