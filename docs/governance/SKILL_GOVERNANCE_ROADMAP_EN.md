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

## v1.5 current work item (2026-09-19)

`In Progress`: add one Project card, `v1.5｜迭代｜Skills CLI / Agent Skills Ecosystem Integration`, covering all 15 documents in the supplied `awesome-qa-skills-skills-cli-integration-pack (1)`: architecture and ADR, portable compatibility contract, repository changes, CLI distribution, CI quality gates, authoring/DX, migration, tests, rollback and risk, DoD, implementation Epics A–H, final structure, and README changes. The attachment's Iteration 0–7, PR slicing, Later, and Optional sections are source recommendations only; per the user request they are consolidated into one v1.5 iteration, with no separate follow-up integration cards.

After inserting v1.5, the existing Project target versions shift exactly once: former `v1.5` → `v1.6`, former `v1.6` → `v1.7`, former `v1.7` → `v1.8`, and former `v1.8` → `v1.9`. Existing card themes, priorities, and current statuses are preserved; the new card was initially created as `Todo` / `P1` / `v1.5`. This schedule change does not alter the historical v1.4 closeout evidence or treat Project status as release approval or runtime proof.

Development started (2026-09-19): the v1.5 card is now `In Progress` / `P1` / `v1.5`; the shifted existing cards retain their individual statuses.

## Phase 0 current status (2026-09-16)

`COMPLETED_WITH_LIMITATIONS`: the registry currently covers all 162 logical bilingual Skill pairs individually; every record preserves evidence paths for both `SKILL.md` files, the primary prompts, Eval structure, and `agents/openai.yaml`. The D01–D16 taxonomy source and the Matrix/Register are generated and freshness-gated. The registry contains 100 candidate records, each with six evidence fields; the Phase 0 Prompt Baseline remains pinned to `awesome-qa-prompt` commit `554178fe9b93d851ec01388597ceb7996d22bd1c` (see the [Phase 0 source register](./PHASE_0_PROMPT_BASELINE_SOURCES_EN.md)). Candidate conclusions retain `MATCH` / `MERGE` / `ENHANCE` / `NEW`, while `decision_state` remains stage-specific as `REVIEWED_WITH_LIMITATION` / `REVIEWED` / `PROPOSED`. Project-specific semantic equivalence still needs requirements, Issue/PR, or test-asset review, so these records must not directly create or change a Skill. Phase 0 ran no model, external test target, or real quality evaluation, so Quality Score / Eval execution remain `NOT_SCORED` / `NOT_RUN`; Prompt semantic equivalence, runtime behavior, and effectiveness remain `UNASSESSED`.

The typical mapping review (2026-09-16) records 20 roadmap relationships in the Registry `match_reviews`: 13 candidate mappings and 7 Existing self-reviews. The [bilingual review views](./PHASE_0_MATCH_MERGE_REVIEW_EN.md) and the Matrix/Matching Register are generated. This review records relationships, target Skills, evidence paths, and follow-up actions only; it does not authorize duplicate directories or upgrade static relationship records into semantic-equivalence, runtime-effectiveness, model-evaluation, or release-approval evidence.

The [Phase 0 closeout view](./PHASE_0_V1_4_CLOSEOUT_EN.md) registers all 35 v1.4 Project cards. The [Deprecation contract](./DEPRECATION_DECISION_CONTRACT_EN.md), [bilingual consistency contract](./BILINGUAL_CONSISTENCY_CONTRACT_EN.md), [Quality Score/Eval contract](./QUALITY_SCORE_EVAL_CONTRACT_EN.md), [Workflow/Eval/installation checklist](./WORKFLOW_EVAL_INSTALL_SYNC_EN.md), [Enhancement Sprint](./ENHANCEMENT_SPRINT_EN.md), [15-step template](./CANDIDATE_SKILL_15_STEP_TEMPLATE_EN.md), and [Shift Left milestone](./SHIFT_LEFT_MILESTONE_EN.md) keep executable rules separate. The current v1.5–v1.9 schedule is recorded above; this historical closeout does not start later versions.

## Phase 1 current work item (2026-09-14)

`ACCEPTED_WITH_DEFERRED_EVAL`: the first five v1.1 requirement-quality Skills, the following ten quality-skill cards, and the current five test-design discovery Skills have passed unified implementation-scope acceptance; the corresponding 20 Project #4 cards move to `Done`. See the [Phase 1 requirement-quality record](./PHASE_1_REQUIREMENTS_QUALITY_EN.md) for scope, card IDs, input-audit boundaries, evidence limits, and acceptance commands. Real-model Evals are deferred by the user and remain `NOT_RUN`, so semantic effectiveness, quality scoring, and release completion must not be claimed.

## Phase 3 current work item (2026-09-15)

`ACCEPTED_WITH_DEFERRED_EVAL`: the Match, RED-contract, Skill-implementation, governance-sync, and quality-gate deliverables for v3-v4 Phase 3 Batch 1 (Reliability + Security, 17 cards) and Batch 2 (Quality Engineering + AI Native, 25 cards) are complete; the current Project snapshot shows all 42 cards as `Done`. The available Project query cannot prove that the historical `In Progress → Done` transition occurred, so the transition audit remains `UNASSESSED`. Batch 2 delivers 24 bilingual physical Skill packages and records `prompt-regression-testing` as an enhancement mode inside `prompt-testing`, with no alias directory. Real-model Eval, external-target execution, quality scores, and business acceptance remain `NOT_RUN` / `NOT_SCORED` / `INCOMPLETE`. See the [v3-v4 Phase 3 record](./PHASE_3_V3_V4_EN.md).

## Phase reviews

Each phase runs Coverage, Duplicate, Match, Merge, Enhancement, Eval, Usage, and Maintenance reviews. Findings distinguish verified, failed, not run, blocked, and not applicable; static checks are not runtime proof.
