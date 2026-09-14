<div align="right"><a href="./2026-09-14-v1-1-test-design-discovery-five.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# v1.1 Test-Design Discovery Five-Skill Implementation Plan

> **For agentic workers:** Execute tasks in order and track them with checkboxes. Each Skill must independently complete RED → GREEN → REFACTOR. Work only in the current `develop` workspace; do not commit or push.

**Goal:** In the current workspace, deliver bilingual standalone Skill packages, Evals, local trigger rules, governance records, generated views, and verification for `test-gap-analysis`, `risk-based-testing`, `edge-case-discovery`, `negative-scenario-discovery`, and `test-data-requirement-analysis`.

**Architecture:** The design classifies all five as `NEW`. Each has an independent bilingual directory and stable finding IDs. They share evidence boundaries and the local validation contract, but do not link internal files to one another; neighboring Skills are referenced only in prose for boundaries.

**Tech stack:** Markdown, YAML, CSV, JSON, Python 3 standard library, `skill-up validate/run`, the repository trace runner, GitHub Project CLI, and existing quality gates.

**Design basis:** `docs/superpowers/specs/2026-09-14-v1-1-test-design-discovery-five-design_EN.md` and its Chinese mirror.

## Global constraints after review

- Only the five candidates may add physical bilingual directories; no alias or duplicate target directory is allowed.
- Every package includes `SKILL.md`, `prompts/<slug>.md`, `agents/openai.yaml`, `evals/eval.yaml`, `basic-success.yaml`, `edge-incomplete-input.yaml`, `edge-scope-boundary.yaml`, `trigger-prompts.csv`, and `local-rules.json`.
- `SKILL.md` frontmatter `description` follows the repository convention `Use this skill when ...; triggers include ...`; names, metadata keys, and Prompt structure remain bilingual-aligned.
- Prompts audit `known`, `missing`, `conflicting`, `stale`, `out_of_scope`, and `assumptions` first, separating facts, evidence-backed inference, recommendations, and Human decisions.
- Stable artifacts are `TG-##`, `RBT-##`, `EC-##`, `NS-##`, and `TDR-##`; without execution evidence, never write `passed`, `complete coverage`, verified, or approved.
- Trigger CSV covers `explicit`, `implicit`, `contextual`, and `negative` with both positive and negative samples; `local-rules.json` `skill` equals the physical slug.
- Move only the five exact Project #4 item IDs to `In Progress`; do not change other cards. Do not create Issues, push, or publish; preserve existing uncommitted changes.
- Real model Evals remain `NOT_RUN`, governance quality remains `NOT_SCORED`, and the local runner reports `BLOCKED` when real `skill.selection` evidence is absent.

---

### Task 1: Write the batch contract test and observe RED

**Files**

- Create: `scripts/tests/test_v11_test_design_discovery_contracts.py`
- Read-only: `scripts/tests/test_v11_ten_quality_skill_contracts.py`
- Read-only: `scripts/run_skill_trace_eval.py`, `scripts/skill_eval_rules.py`

**Contract:** `NEW_SLUGS = ("test-gap-analysis", "risk-based-testing", "edge-case-discovery", "negative-scenario-discovery", "test-data-requirement-analysis")`. For both languages, check entry point, Prompt, metadata, eval, three case types, all four trigger modes, positive/negative triggers, and the physical-slug rule. Check the per-Skill unique artifact/boundary markers: `TG-` + “not a coverage claim”; `RBT-` + “not a full test strategy”; `EC-` + “do not invent thresholds”; `NS-` + “do not run fault injection”; `TDR-` + “do not generate data”. Generic `risk`, `test`, or `coverage` words do not satisfy the contract.

- [x] Write the contract test before creating any package content.
- [x] Run `python3 -m unittest scripts.tests.test_v11_test_design_discovery_contracts -v`; it must fail because the five bilingual directories are absent.
- [x] Run `git diff --check` and `git status --short`; confirm the RED test did not overwrite or revert existing work.
- [x] After confirming RED, move the five exact Project #4 items to `In Progress` and immediately verify their status:

  ```bash
  project_id=PVT_kwHOAHP1as4BjBhV
  status_field_id=PVTSSF_lAHOAHP1as4BjBhVzhh3bSA
  in_progress_option_id=47fc9ee4
  for item_id in \
    PVTI_lAHOAHP1as4BjBhVzg6ScBw \
    PVTI_lAHOAHP1as4BjBhVzg6ScEE \
    PVTI_lAHOAHP1as4BjBhVzg6ScGA \
    PVTI_lAHOAHP1as4BjBhVzg6ScIs \
    PVTI_lAHOAHP1as4BjBhVzg6ScKk; do
    gh project item-edit --id "$item_id" --project-id "$project_id" \
      --field-id "$status_field_id" --single-select-option-id "$in_progress_option_id"
  done
  gh project item-list 4 --owner @me --format json --limit 200
  ```

  Only these five cards may move from `Todo` to `In Progress`; if any ID, project, or field does not match, stop implementation and repair the state operation first.

### Task 2: Add `test-gap-analysis`

**Files:** Create the matching files under `skills/zh/testing-types/test-gap-analysis/` and `skills/en/testing-types/test-gap-analysis/`: `SKILL.md`, the main Prompt, metadata, `evals/eval.yaml`, three case files, `trigger-prompts.csv`, and `local-rules.json`.

**Contract:** Consume requirement/risk/change/defect/test-asset evidence and output `TG-##` gaps. Distinguish missing mapping, orphan, unverified, stale, uncovered risk, and low-value duplicate; do not replace the RT/TC matrix or execution evidence.

- [x] Write three Evals and local triggers for evidence-backed success, bounded incomplete-input output, and refusal to call static presence coverage.
- [x] Run `skill-up validate skills/<lang>/testing-types/test-gap-analysis/evals/eval.yaml` and its `--dry-run` for each language.
- [x] Write minimal bilingual entry points, Prompts, and metadata and compare their output contracts.
- [x] Run the batch contract test and `git diff --check` before the next Skill.

### Task 3: Add `risk-based-testing`

**Files:** Create the matching files under `skills/zh/testing-types/risk-based-testing/` and `skills/en/testing-types/risk-based-testing/`.

**Contract:** Convert risk evidence into `RBT-##` test priority, level/method, depth, and scope tradeoffs; do not replace risk identification, a complete strategy, regression selection, or execution.

- [x] Write three Evals for an explainable risk-to-test mapping, a bounded result when key risk material is missing, and resource/time-box tradeoffs with expansion triggers.
- [x] Run validate/dry-run for both languages, the contract test, and diff check.
- [x] Ensure risk numbers have evidence or are labeled assumptions; do not output pseudo-precise scores or Human release decisions.

### Task 4: Add `edge-case-discovery`

**Files:** Create the matching files under `skills/zh/testing-types/edge-case-discovery/` and `skills/en/testing-types/edge-case-discovery/`.

**Contract:** Output `EC-##` boundary candidates across value/length, null/type, time/timezone, state, capacity/resource, concurrency/order, platform/localization, and combination dimensions; do not write full cases or invent thresholds.

- [x] Write three Evals for multi-dimensional boundary discovery, explicit gaps/assumptions for incomplete input, and unknown-threshold scope boundaries.
- [x] Run validate/dry-run for both languages, the contract test, and diff check.
- [x] Preserve source, trigger, concern, priority, validation suggestion, and open question for every candidate.

### Task 5: Add `negative-scenario-discovery`

**Files:** Create the matching files under `skills/zh/testing-types/negative-scenario-discovery/` and `skills/en/testing-types/negative-scenario-discovery/`.

**Contract:** Output `NS-##` failure/denial/degradation/recovery candidates, distinguishing invalid input, unauthorized access, dependency failure, timeout, retry exhaustion, duplicate request, partial failure, and unsafe recovery; do not run fault injection or invent error codes.

- [x] Write three Evals for valid failure-path discovery, missing failure contracts, and refusal to turn scope boundaries into execution or release conclusions.
- [x] Run validate/dry-run for both languages, the contract test, and diff check.
- [x] Ensure expected behavior includes trigger, preconditions, visible result, consistency impact, and evidence needs.

### Task 6: Add `test-data-requirement-analysis`

**Files:** Create the matching files under `skills/zh/testing-types/test-data-requirement-analysis/` and `skills/en/testing-types/test-data-requirement-analysis/`.

**Contract:** Output `TDR-##` data-preparation requirements covering entities/fields, relationships, states, roles, valid/invalid/boundary/combination conditions, sources, masking, setup, cleanup, and blockers; do not create records or read production data.

- [x] Write three Evals for complete prerequisites, missing schema/privacy/cleanup evidence, and real data-source/production-mirror boundaries.
- [x] Run validate/dry-run for both languages, the contract test, and diff check.
- [x] Confirm the analysis can be consumed by `test-data-generation` without copying its generation rules or dataset output.

### Task 7: Synchronize governance, indexes, and generated views

**Files:** Update `docs/governance/skill-governance-registry.yaml`, bilingual `docs/SKILL_MATCHING_REGISTER*`, `docs/SKILL_MATRIX*`, `docs/catalog/*`, `docs/generated/*`, bilingual READMEs, and required Phase 1 documents using existing generators.

- [x] Each Skill registry record has bilingual paths, `Planned-P0` status, Engineering QA / Test Design and Preparation stage, roles, inputs, outputs, workflow, and evidence paths; quality is `NOT_SCORED` and execution is `NOT_RUN`. The corresponding five candidate records are `NEW` and separately record scope/non-goals.
- [x] Each candidate's six-field match evidence agrees with this design; neighboring Skill names must not be treated as proof of duplication or coverage.
- [x] Run `python3 scripts/generate_skill_inventory.py`, `python3 scripts/generate_skill_governance_inventory.py`, and `python3 scripts/generate_skill_governance_matrix.py`, then their `--check` forms; preserve existing uncommitted differences.
- [x] `python3 scripts/check_docs_bilingual.py --repo-root .` and the independence check must pass.

### Task 8: Run unified verification and verify Project cards

- [x] Run `skill-up validate` and `skill-up run ... --dry-run` for zh/en evals of all five slugs.
- [x] Run the batch contract test, the two previous contract tests, and `python3 -m unittest discover -s scripts/tests -v`.
- [x] Run `bash scripts/check_skills_quality.sh`, `bash scripts/validate_skill_evals.sh`, metadata/independence/integrity/external-snapshot checks, and `git diff --check`.
- [x] Run the default dry-run of `scripts/run_skill_trace_eval.py` for the fifteen physical targets (the ten previous targets plus these five); record `BLOCKED` when no `skill.selection` exists and never manufacture a trigger pass.
- [x] Use `gh project item-list 4 --owner @me --format json --limit 200` to verify the five exact cards are `In Progress`, while `decision-table-testing`, `state-transition-testing`, and `boundary-value-testing` remain `Todo`.
- [x] Run scoped trailing-whitespace checks over new packages and governance docs, then report the final file list, commands, and unexecuted boundaries; do not commit or push.

## Plan self-review

- [x] Every candidate has a capability match, six-field evidence, explicit inputs/outputs/decision logic, and neighboring-Skill boundary.
- [x] Every candidate has an independent Task, bilingual file list, three Evals, four trigger modes, and per-package verification.
- [x] RED precedes package content; Project cards move only after RED and before package implementation; governance generation follows package verification.
- [x] Static structure, local dry-runs, and Project status are not presented as model effectiveness, runtime results, Human decisions, or Release completion.
