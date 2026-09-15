<div align="right"><a href="./SKILL_GOVERNANCE_ROADMAP.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# Skill Governance and Long-Term Roadmap

This is the context entry for future governance. `QA_SKILLS_EVOLUTION_ROADMAP.md` remains the historical record of completed earlier iterations; neither document replaces the other.

## Principles

Match before enhancement; merge before adding. Stable physical directories preserve compatibility, while virtual Domains, the Matrix, metadata, Workflows, and documentation provide governance and discovery.

## Delivery sequence

Phase 0 establishes inventory, 16 virtual Domains, matching, lifecycle, quality score, minimum Evals, and the Matrix. Phase 1 covers Shift-Left Quality; Phase 2 separates test methodology from framework/tool adapters; Phase 3 addresses reliability, security, QE productivity, AI Native Quality, and reviews existing Performance and AI capabilities.

## Project and documentation synchronization

`Awesome QA Skills — Governance & Roadmap` is the execution board. Every card includes objective, scope, non-goals, dependencies, deliverables, acceptance criteria, and related documents. Board status is not release approval or risk acceptance.

For every lifecycle change, check the Matrix, bilingual entry READMEs, Catalog/Graph, Workflows, Evals, `agents/openai.yaml`, and installation/contribution documents. Mark non-applicable work explicitly as `N/A`.

## Phase 0 current status (2026-09-14)

`COMPLETED_WITH_LIMITATIONS`: the registry covers all 79 logical bilingual Skill pairs individually; every record preserves evidence paths for both `SKILL.md` files, the primary prompts, Eval structure, and `agents/openai.yaml`, while the Matrix/Register are generated and freshness-gated. All 13 candidates have six recorded comparison fields backed by the pinned `awesome-qa-prompt` Prompt Baseline commit `554178fe9b93d851ec01388597ceb7996d22bd1c` (see the [Phase 0 source register](./PHASE_0_PROMPT_BASELINE_SOURCES_EN.md)). Candidate conclusions remain the proposed `MATCH` / `MERGE` / `ENHANCE` values, with `decision_state` set to `REVIEWED_WITH_LIMITATION`; project-specific semantic equivalence still needs requirements, Issue/PR, or test-asset review, so these records must not directly create or change a Skill. Phase 0 ran no model, external test target, or real quality evaluation, so Quality Score / Eval execution remain `NOT_SCORED` / `NOT_RUN`; Prompt semantic equivalence, runtime behavior, and effectiveness remain `UNASSESSED`.

## Phase 1 current work item (2026-09-14)

`ACCEPTED_WITH_DEFERRED_EVAL`: the first five v1.1 requirement-quality Skills, the following ten quality-skill cards, and the current five test-design discovery Skills have passed unified implementation-scope acceptance; the corresponding 20 Project #4 cards move to `Done`. See the [Phase 1 requirement-quality record](./PHASE_1_REQUIREMENTS_QUALITY_EN.md) for scope, card IDs, input-audit boundaries, evidence limits, and acceptance commands. Real-model Evals are deferred by the user and remain `NOT_RUN`, so semantic effectiveness, quality scoring, and release completion must not be claimed.

## Phase 3 current work item (2026-09-15)

`ACCEPTED_WITH_DEFERRED_EVAL`: the Match, RED-contract, Skill-implementation, governance-sync, and quality-gate deliverables for v3-v4 Phase 3 Batch 1 (Reliability + Security, 17 cards) and Batch 2 (Quality Engineering + AI Native, 25 cards) are complete; the current Project snapshot shows all 42 cards as `Done`. The available Project query cannot prove that the historical `In Progress → Done` transition occurred, so the transition audit remains `UNASSESSED`. Batch 2 delivers 24 bilingual physical Skill packages and records `prompt-regression-testing` as an enhancement mode inside `prompt-testing`, with no alias directory. Real-model Eval, external-target execution, quality scores, and business acceptance remain `NOT_RUN` / `NOT_SCORED` / `INCOMPLETE`. See the [v3-v4 Phase 3 record](./PHASE_3_V3_V4_EN.md).

## Phase reviews

Each phase runs Coverage, Duplicate, Match, Merge, Enhancement, Eval, Usage, and Maintenance reviews. Findings distinguish verified, failed, not run, blocked, and not applicable; static checks are not runtime proof.
