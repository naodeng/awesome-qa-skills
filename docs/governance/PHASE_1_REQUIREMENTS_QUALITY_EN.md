<div align="right"><a href="./PHASE_1_REQUIREMENTS_QUALITY.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# v1.1 Phase 1: Requirement Quality Skill Development

## Current status

`IN_PROGRESS_WITH_LIMITATIONS` (2026-09-14). Remote `main` has been fast-forwarded into local `develop`. The first five v1.1 P0 requirement-quality Skills now have independent bilingual packages, package-level static checks, and Eval dry-runs. Real model Evals have not run because no usable Claude login is available in the current environment; `eval_execution` therefore remains `NOT_RUN`.

This phase covers only the first batch of requirement-quality capabilities. It is not evidence of a v1.1 release, runtime effectiveness, a closed business requirement, or a Go/No-Go decision.

## Scope

| Order | Skill | Primary responsibility | Project card |
| --- | --- | --- | --- |
| 1 | `requirement-quality-review` | Review completeness, clarity, verifiability, feasibility, scope, and evidence quality, then route specialist analysis | `PVTI_lAHOAHP1as4BjBhVzg6Sbo4` · `v1.1 P0｜候选 Skill｜requirement-quality-review` |
| 2 | `requirement-ambiguity-analysis` | Detect ambiguity in actors, objects, conditions, quantities, timing, states, and acceptance language | `PVTI_lAHOAHP1as4BjBhVzg6Sbp0` · `v1.1 P0｜候选 Skill｜requirement-ambiguity-analysis` |
| 3 | `requirement-consistency-analysis` | Compare terminology, identifiers, formats, states, rules, behavior, and version scope across sources | `PVTI_lAHOAHP1as4BjBhVzg6Sbsc` · `v1.1 P0｜候选 Skill｜requirement-consistency-analysis` |
| 4 | `requirement-conflict-detection` | Detect mutually exclusive rules and constraints in one scope, preserve both, and leave the decision to a Human | `PVTI_lAHOAHP1as4BjBhVzg6Sbuk` · `v1.1 P0｜候选 Skill｜requirement-conflict-detection` |
| 5 | `requirement-traceability-analysis` | Build bidirectional traceability across requirements, acceptance, design, code, tests, defects, and evidence | `PVTI_lAHOAHP1as4BjBhVzg6Sbxw` · `v1.1 P0｜候选 Skill｜requirement-traceability-analysis` |

All five cards are `In Progress`. This phase does not move other Project cards, create Issues, push, or publish a version.

## Shared boundaries

- Every Skill has an independent Chinese and English `SKILL.md`, primary Prompt, `agents/openai.yaml`, Eval configuration, and three boundary cases.
- Input audits consistently preserve `known`, `missing`, `conflicting`, `stale`, `out_of_scope`, and `assumptions`, while finding IDs and specialist outputs remain Skill-specific.
- Static presence, name matching, report wording, and dry-runs prove structure or declarations only; they are not model behavior, test execution, defect closure, approval, or release evidence.
- The five packages do not change existing `requirements-analysis` or `requirements-analysis-plus` behavior and do not use relative links to another Skill's internal files.
- `requirement-quality-review` provides overview and routing; it does not produce a numeric quality score or Go/No-Go. The four specialists report bounded findings and do not decide for a Human.

## Delivery and acceptance

1. Each language has 84 logical Skill packages, for 168 physical directories total; each new package has aligned directory, frontmatter `name`, and Agent metadata key.
2. All five Eval YAML files load with `skill-up validate`, their three case types can dry-run, and structural, metadata, independence, and integrity checks pass.
3. The registry records each new Skill as `Planned-P0`, `P0`, `Engineering QA`, and `requirements`, with roles, evidence paths, and `NOT_SCORED`/`NOT_RUN` states. It also records six-field match evidence for all five candidates.
4. Bilingual READMEs, Catalog, Graph, governance Matrix, matching Register, and inventories reproduce from current repository content without drift.
5. Real model Evals, external targets, business semantic equivalence, quality scoring, and release are separate follow-ups; without evidence they remain `NOT_RUN`, `UNASSESSED`, or `IN_PROGRESS_WITH_LIMITATIONS`.

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
