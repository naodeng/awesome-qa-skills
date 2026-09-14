<div align="right"><a href="./2026-09-13-phase-0-skill-governance-design.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# Phase 0 Skill Governance Data Design

## Goal

Turn the existing 79 bilingual Skill pairs from a physical-directory inventory plus governance prose into reproducible, validated, per-Skill governance data: a complete Matrix, traceable candidate capability-match decisions, and evidence-bounded Quality Score / Eval states.

## Scope and non-goals

This iteration covers the 79 logical Skill pairs under `skills/{zh,en}/` and every candidate already recorded in `SKILL_MATCHING_REGISTER.md`. Each record must include virtual Domain, SDLC stage, role, governance status, relationships, evidence location, and next action. Candidates must complete the six-step Capability Match and conclude only `EXISTING`, `MATCH`, `ENHANCE`, `MERGE`, or `NEW`.

It does not add or remove Skill directories, execute Prompts, models, or external test targets, infer semantic equivalence or runtime effectiveness from directory structure, or describe unrun Evals as passing. Phase 1 Shift-Left enhancements are scheduled separately after these match decisions.

## Design

### Single source of truth and generated views

Add `docs/governance/skill-governance-registry.yaml` as the per-Skill source of truth. Every logical Skill uses its directory name as its unique key and declares Domain, SDLC stage, role, status, priority, input/output summary, related Skills, Workflow, Match / Merge / Enhance / Deprecation fields, Quality Score state, and the Chinese and English paths. A separate `candidates` section records six-step matching evidence, conclusion, target, and next action.

Add a deterministic `scripts/generate_skill_governance_matrix.py`. It cross-checks the registry with the physical `skills/` inventory and generates bilingual `docs/SKILL_MATRIX*.md` and `docs/SKILL_MATCHING_REGISTER*.md`. It must reject missing or extra Skills, unpaired language directories, unknown enums, `NEW` entries without Scope / Non-goals, and claimed completed scores without inspectable evidence.

The Matrix and Register are generated views and must not be hand-edited; the registry is the auditable governance decision source. `generate_skill_inventory.py` remains limited to a physical snapshot and makes no semantic or quality claim.

### Evidence boundaries

Every `quality_score` is exactly `NOT_SCORED`, `PARTIALLY_SCORED`, or `SCORED`. `SCORED` requires all nine dimension values, review-evidence paths, and a total; other states must name missing evidence and cannot yield Stable or Beta claims. Eval file structure and execution result remain separate: this repository can collect structure evidence now, while execution defaults to `NOT_RUN` unless this iteration actually executes and records the command and result.

Capability Match records evidence for name, purpose, input, output, decision logic, and Workflow role. A match conclusion is not effectiveness proof, and `EXISTING` / `MATCH` never bypass later review.

### Quality gate and compatibility

`check_skills_quality.sh` gains registry-to-output freshness verification while retaining the physical inventory and v1.0 governance inventory checks. Existing directories, installers, and document entry points remain compatible; README and Catalog/Graph are updated only if navigation or commands change.

Generator tests cover the full 79-pair input, missing/extra directories, invalid enums, `NEW` required boundaries, unscored states, score-evidence completeness, candidate six-step evidence, and `--check` drift detection. Focused tests, complete `check_skills_quality.sh`, and `git diff --check` are final checks; none substitutes for model Eval or runtime-quality evidence.

## Data flow

```text
skills/{zh,en}/ + registry.yaml
        │ cross-check
        ▼
generate_skill_governance_matrix.py
        ├── docs/SKILL_MATRIX.md / _EN.md
        ├── docs/SKILL_MATCHING_REGISTER.md / _EN.md
        └── --check (quality gate)
```

## Acceptance criteria

1. The registry covers exactly 79 logical bilingual Skill pairs with no drift from physical directories.
2. Matrix and Matching Register are generator-owned, structurally equivalent in Chinese and English, and cross-linked.
3. Every registered candidate has six-step evidence and one valid conclusion; only `NEW` enters later new-Skill planning.
4. Quality Score and Eval execution state never overstate evidence; unscored and unrun items remain explicit.
5. Focused generator tests, full `check_skills_quality.sh`, and `git diff --check` pass.

## Risks and trade-offs

Per-Skill governance for 79 entries requires human-reviewable evidence; name or directory similarity cannot safely make those decisions in bulk. This iteration therefore retains `NOT_SCORED` or `UNASSESSED` for semantic and score claims without evidence instead of inventing coverage or maturity. A `NEW` conclusion changes whether a directory is created later, so it has stricter boundary requirements than the other conclusions.
