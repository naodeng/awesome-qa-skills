<div align="right"><a href="./PHASE_1_REQUIREMENTS_QUALITY.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# v1.1 Phase 1: Requirement Quality Skill Development

## Current status

`ACCEPTED_WITH_DEFERRED_EVAL` (2026-09-14). Remote `main` has been fast-forwarded into local `develop`. The first five v1.1 P0 requirement-quality Skills, the following ten quality-skill cards, and the current five test-design discovery Skills now have bilingual packages, enhancement modes, package-level static checks, local-runner dry-runs, and semantic boundary-judge configuration. The user explicitly agreed to defer real-model Evals, so registry `eval_execution` remains `NOT_RUN`.

This status means the v1.1 **implementation scope has been accepted as a whole**. It is not evidence of real-model behavior, business semantic equivalence, quality scoring, Go/No-Go approval, or a version release. Real-model Evals remain a later unified follow-up.

## Unified acceptance result

| Acceptance item | Current evidence | State |
| --- | --- | --- |
| Bilingual packages, metadata, independence, integrity, docs, and governance views | `bash scripts/check_skills_quality.sh`: 192 Skills, `skill-up validate` 192/192, 20 local rules; all passed | `verified` |
| Contract tests and full repository unit tests | `python3 -m unittest discover -s scripts/tests -v`: 40/40 passed | `verified` |
| Local trigger-data dry-run | 18 targets × two languages = 36 datasets, 36/36 exited 0 | `verified` |
| Real-model Eval | Explicitly deferred by the user; registry remains `eval_execution: NOT_RUN` | `deferred` |
| External targets, business semantic equivalence, quality scoring, and release | Outside this implementation acceptance | `UNASSESSED` |

Decision: this acceptance closes only the v1.1 implementation scope. The 20 corresponding Project cards move to `Done`; all other cards retain their existing state.

## Scope

| Order | Skill | Primary responsibility | Project card |
| --- | --- | --- | --- |
| 1 | `requirement-quality-review` | Review completeness, clarity, verifiability, feasibility, scope, and evidence quality, then route specialist analysis | `PVTI_lAHOAHP1as4BjBhVzg6Sbo4` · `v1.1 P0｜候选 Skill｜requirement-quality-review` |
| 2 | `requirement-ambiguity-analysis` | Detect ambiguity in actors, objects, conditions, quantities, timing, states, and acceptance language | `PVTI_lAHOAHP1as4BjBhVzg6Sbp0` · `v1.1 P0｜候选 Skill｜requirement-ambiguity-analysis` |
| 3 | `requirement-consistency-analysis` | Compare terminology, identifiers, formats, states, rules, behavior, and version scope across sources | `PVTI_lAHOAHP1as4BjBhVzg6Sbsc` · `v1.1 P0｜候选 Skill｜requirement-consistency-analysis` |
| 4 | `requirement-conflict-detection` | Detect mutually exclusive rules and constraints in one scope, preserve both, and leave the decision to a Human | `PVTI_lAHOAHP1as4BjBhVzg6Sbuk` · `v1.1 P0｜候选 Skill｜requirement-conflict-detection` |
| 5 | `requirement-traceability-analysis` | Build bidirectional traceability across requirements, acceptance, design, code, tests, defects, and evidence | `PVTI_lAHOAHP1as4BjBhVzg6Sbxw` · `v1.1 P0｜候选 Skill｜requirement-traceability-analysis` |

All five cards were `In Progress` during implementation and move to `Done` after unified acceptance. No other Project cards move; no Issues are created, no push occurs, and no version is published.

## Following ten P0 cards

| Order | Card | Delivery shape | Project card |
| --- | --- | --- | --- |
| 1 | `business-rule-extraction` | New bilingual physical Skill | `PVTI_lAHOAHP1as4BjBhVzg6Sb0o` |
| 2 | `business-rule-consistency-review` | Enhance `requirement-consistency-analysis` with business-rule mode | `PVTI_lAHOAHP1as4BjBhVzg6Sb2Q` |
| 3 | `technical-design-quality-review` | New bilingual physical Skill | `PVTI_lAHOAHP1as4BjBhVzg6Sb3A` |
| 4 | `architecture-testability-review` | Enhance `testability-analysis` with architecture mode | `PVTI_lAHOAHP1as4BjBhVzg6Sb4I` |
| 5 | `api-design-quality-review` | New bilingual physical Skill | `PVTI_lAHOAHP1as4BjBhVzg6Sb5U` |
| 6 | `database-design-quality-review` | New bilingual physical Skill | `PVTI_lAHOAHP1as4BjBhVzg6Sb6o` |
| 7 | `observability-design-review` | New bilingual physical Skill | `PVTI_lAHOAHP1as4BjBhVzg6Sb7Y` |
| 8 | `error-handling-design-review` | New bilingual physical Skill | `PVTI_lAHOAHP1as4BjBhVzg6Sb8Y` |
| 9 | `test-scope-analysis` | New bilingual physical Skill | `PVTI_lAHOAHP1as4BjBhVzg6Sb_M` |
| 10 | `test-coverage-analysis` | Enhance `requirement-traceability-analysis` with coverage_analysis mode | `PVTI_lAHOAHP1as4BjBhVzg6ScAY` |

All ten cards were `In Progress` during implementation and move to `Done` after unified acceptance. Enhancement cards do not create duplicate directories; no other Project cards move, no Issues are created, no push occurs, and no version is published.

## Current five test-design discovery cards

| Order | Card | Delivery shape | Project card |
| --- | --- | --- | --- |
| 1 | `test-gap-analysis` | New bilingual physical Skill | `PVTI_lAHOAHP1as4BjBhVzg6ScBw` |
| 2 | `risk-based-testing` | New bilingual physical Skill | `PVTI_lAHOAHP1as4BjBhVzg6ScEE` |
| 3 | `edge-case-discovery` | New bilingual physical Skill | `PVTI_lAHOAHP1as4BjBhVzg6ScGA` |
| 4 | `negative-scenario-discovery` | New bilingual physical Skill | `PVTI_lAHOAHP1as4BjBhVzg6ScIs` |
| 5 | `test-data-requirement-analysis` | New bilingual physical Skill | `PVTI_lAHOAHP1as4BjBhVzg6ScKk` |

All five cards were `In Progress` during implementation and move to `Done` after unified acceptance. This batch does not move other Project cards, create Issues, push, or publish a version.

## Shared boundaries

- Every Skill has an independent Chinese and English `SKILL.md`, primary Prompt, `agents/openai.yaml`, Eval configuration, three boundary cases, `trigger-prompts.csv`, and `local-rules.json`; trigger data covers explicit, implicit, contextual, and negative controls.
- Input audits consistently preserve `known`, `missing`, `conflicting`, `stale`, `out_of_scope`, and `assumptions`, while finding IDs and specialist outputs remain Skill-specific.
- Static presence, name matching, report wording, and dry-runs prove structure or declarations only; they are not model behavior, test execution, defect closure, approval, or release evidence.
- The five packages do not change existing `requirements-analysis` or `requirements-analysis-plus` behavior and do not use relative links to another Skill's internal files.
- The following ten cards deliver seven new physical Skills and three enhancement modes on existing Skills; candidate card names and physical directories are registered separately, without alias directories.
- `requirement-quality-review` provides overview and routing; it does not produce a numeric quality score or Go/No-Go. The four specialists report bounded findings and do not decide for a Human.

## Delivery and acceptance

1. Each language has 96 logical Skill packages, for 192 physical directories total; each new package has an aligned directory, frontmatter `name`, and Agent metadata key, while enhancement candidates have no alias directory.
2. The seven previous new packages, five current new packages, and three enhancement targets load with `skill-up validate`, their new or enhancement case types can dry-run, the local trigger runner loads all 36 Chinese/English target datasets (18 targets × two languages), and structural, metadata, independence, and integrity checks pass.
3. The registry records twelve new Skills as `Planned-P0`, `P0`, `Engineering QA`, and their reviewed stages, with roles, evidence paths, and `NOT_SCORED`/`NOT_RUN` states. It also records six-field match evidence for the three enhancement candidates.
4. Bilingual READMEs, Catalog, Graph, governance Matrix, matching Register, and inventories reproduce from current repository content without drift.
5. Real model Evals, external targets, business semantic equivalence, quality scoring, and release are separate follow-ups; this acceptance explicitly does not block on real-model Eval, and unsupported evidence remains `NOT_RUN` or `UNASSESSED`.

## Reproduce

```bash
python3 scripts/validate_agents_metadata.py --report /tmp/v11-final-metadata.md
python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings --report-md /tmp/v11-final-independence.md
python3 scripts/validate_skills_integrity.py --fail-on-findings --report-md /tmp/v11-final-integrity.md
bash scripts/validate_skill_evals.sh
bash scripts/check_skills_quality.sh
```

Generated views:

```bash
python3 scripts/generate_skill_inventory.py
python3 scripts/generate_skill_governance_inventory.py
python3 scripts/generate_skill_governance_matrix.py
python3 scripts/generate_skill_governance_inventory.py --check
python3 scripts/generate_skill_governance_matrix.py --check
```

Preview local trigger datasets (run once for each of eighteen target Skills in each language; without `--run`, this is only a structural dry-run):

```bash
python3 scripts/run_skill_trace_eval.py \
  --prompts skills/en/testing-types/requirement-quality-review/evals/trigger-prompts.csv \
  --config skills/en/testing-types/requirement-quality-review/evals/local-rules.json \
  --project-root /tmp/v11-requirement-quality-projects \
  --output-dir /tmp/v11-requirement-quality-reports
```
