# v1.5 Skills CLI Integration Project Resequencing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Register the supplied Skills CLI / Agent Skills ecosystem integration pack as one complete v1.5 iteration and move the existing Project schedule one version later without creating multiple integration iterations.

**Architecture:** Keep the repository's bilingual Skill taxonomy and existing installers as the source and fallback layer. Treat the `skills` CLI as a compatible distribution layer, `skill-up` as the evaluation layer, and the supplied pack as the complete scope of one Project card. Preserve existing card themes and statuses while changing only their scheduled target versions, with a new v1.9 option for the former v1.8 queue.

**Tech Stack:** Markdown governance docs, GitHub Projects CLI/API, existing repository quality scripts.

**Spec:** The task-supplied `awesome-qa-skills-skills-cli-integration-pack (1)` documents, from `00_README.md` through `14_ADR_AGENT_SKILLS_DISTRIBUTION.md`.

## Global Constraints

- The complete contents of the supplied 15-document pack are one v1.5 Project task; do not create separate v1.6–v1.9 integration tasks.
- Keep `awesome-qa-skills` as the QA source/governance layer, `skill-up` as the evaluation layer, and `skills` CLI as the distribution layer.
- Do not add the CLI as a runtime dependency, flatten bilingual/category directories, remove legacy installers, or claim untested agents as tested.
- Preserve existing card status and priority while moving target versions; the new integration card starts as `Todo`, `P1`, `v1.5`.
- Keep evidence labels separate: static compatibility, runtime/discovery/install smoke, behavioral Eval, and release approval are independent.

## Review Focus

- Every attachment section is represented in the single card body, including the original phased migration plan, all backlog epics, optional developer experience work, rollback, and the full DoD.
- Existing cards with target versions `v1.5`, `v1.6`, `v1.7`, and `v1.8` are shifted exactly once to `v1.6`, `v1.7`, `v1.8`, and `v1.9`; their status remains observable and unchanged.
- Direct version prefixes in existing `v1.5｜Match Review` titles are updated to `v1.6`, while domain/theme labels such as `v4.1` and `v2.4` are retained.
- The Project target-version field gains `v1.9` without changing existing option IDs or invalidating current assignments.
- Local bilingual governance context and the Project README describe the same v1.5 insertion and version shift.

### Task 1: Record the local roadmap change

**Files:**
- Modify: `docs/governance/SKILL_GOVERNANCE_ROADMAP.md`
- Modify: `docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md`

- [x] Add the single v1.5 Skills CLI integration scope and state that the attached Iteration 0–7 suggestions are consolidated into this one task.
- [x] Record the resulting v1.6–v1.9 schedule shift and preserve the historical v1.4 closeout boundary.
- [x] Keep Chinese and English structure and meaning aligned.

### Task 2: Update the GitHub Project version model

**Project:** `https://github.com/users/naodeng/projects/4`

- [x] Add `v1.9` to the existing `Target Version` single-select field while preserving current options.
- [x] Update the Project README with the new v1.5 scope, the one-iteration rule, the v1.6–v1.9 shift, and explicit status/version handling.

### Task 3: Create the single v1.5 card

- [x] Create one detailed Draft Issue titled `v1.5｜迭代｜Skills CLI / Agent Skills Ecosystem Integration`.
- [x] Include architecture/ADR, compatibility contract, repository change plan, CLI lifecycle, CI gate, authoring/DX, migration, test plan, rollback/risk, DoD, implementation epics A–H, final structure, README specification, and the one-iteration override.
- [x] Set `Status=Todo`, `Priority=P1`, and `Target Version=v1.5`.

### Task 4: Shift the existing scheduled cards

- [x] Enumerate all cards by the live `Target Version` field before mutation.
- [x] Move 19 `v1.5` cards to `v1.6`, 15 `v1.6` cards to `v1.7`, 3 `v1.7` cards to `v1.8`, and 2 `v1.8` cards to `v1.9`.
- [x] Preserve each card's current status and priority; rename only the four direct `v1.5｜Match Review` titles to `v1.6｜Match Review`.

### Task 5: Verify the result

- [x] Confirm the new card has the requested title, body coverage, `Todo`, `P1`, and `v1.5` values.
- [x] Confirm the moved-card counts and target versions are exact, no old scheduled cards remain under `v1.5`–`v1.8`, and all moved cards retain `Todo`.
- [x] Confirm the Project README and local bilingual roadmap contain the same schedule.
- [x] Run the repository documentation/bilingual checks relevant to the local edits and inspect `git diff --check` and `git status`.

## Execution record

- Project #4 card: `PVTI_lAHOAHP1as4BjBhVzg7ufKI`.
- Initial scheduled-card snapshot: `v1.5=1`, `v1.6=19`, `v1.7=15`, `v1.8=3`, `v1.9=2`; all were `Todo` at insertion.
- Development-start verification (2026-09-19): card `PVTI_lAHOAHP1as4BjBhVzg7ufKI` is `In Progress` with Target Version `v1.5`; the shifted `v1.6`–`v1.9` cards retain their prior statuses.
- Repository gates: `python3 scripts/check_docs_bilingual.py --repo-root .` reported `bilingual_docs_findings=0`; `bash scripts/check_skills_quality.sh` passed with 324 Skills, 324 valid Eval files, and 135 tests passing; `git diff --check` passed.
