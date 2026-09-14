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

`IN_PROGRESS_WITH_LIMITATIONS`: the first five v1.1 P0 requirement-quality Skills now have bilingual packages and package-level structural checks, while their Project #4 cards remain `In Progress`. See the [Phase 1 requirement-quality record](./PHASE_1_REQUIREMENTS_QUALITY_EN.md) for scope, card IDs, input-audit boundaries, evidence limits, and acceptance commands. Real model Evals have not run, so semantic effectiveness and release completion must not be claimed.

## Phase reviews

Each phase runs Coverage, Duplicate, Match, Merge, Enhancement, Eval, Usage, and Maintenance reviews. Findings distinguish verified, failed, not run, blocked, and not applicable; static checks are not runtime proof.
