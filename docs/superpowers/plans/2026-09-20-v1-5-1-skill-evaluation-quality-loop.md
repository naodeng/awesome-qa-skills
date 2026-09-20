# v1.5.1 Skill Evaluation Quality Loop Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the supplied Skill Evaluation Design into a small, bilingual, evidence-bounded operating loop on top of the existing `skill-up` and local trace-rule infrastructure.

**Architecture:** Add two independently installable Skill Engineering packages (`skill-quality-review` and `skill-evaluation`), a bilingual evaluation contract/design/pilot record, and a metadata layer around the existing local trace runner. Reuse `skill-up`, the current twenty deterministic trace rules, and the existing Quality Score contract; do not add a competing evaluator, judge, benchmark runner, or score.

**Tech Stack:** Markdown, YAML, Python 3 standard library, `skill-up` 0.12.0, existing shell quality gates, GitHub Projects CLI.

**Spec:** `docs/governance/SKILL_EVALUATION_DESIGN.md` (the repository copy of the user-supplied, read-only source for this iteration).

## Global Constraints

- `skill-up` remains the primary generic Skill Eval Engine.
- Trace checks remain complementary evidence and never become a second generic Eval Engine.
- Runtime evidence never creates a second repository Quality Score.
- Both Meta Skills are bilingual, independently installable, and each has success, incomplete-input, and boundary cases.
- Static, structural, evaluation, runtime, and human-review claims remain separate; unknown evidence stays `NOT_RUN`, `UNASSESSED`, `BLOCKED`, or `INSUFFICIENT_EVIDENCE`.
- No model-backed eval run is claimed unless a real model run produces fresh evidence.
- Do not modify, revert, commit, or publish unrelated work; no push is required by this task.
- Project #4 card state is an execution record and is not release approval or runtime-effectiveness proof.

## Review Focus

- Missing or invalid run metadata must be explicit rather than silently guessed; test the default `unknown` path and the reproducible hash path in `scripts/skill_eval_evidence.py`.
- A failing trace must remain distinguishable from an infrastructure error or an unclassified failure; test each evidence state in the runner report.
- Trigger output without an observable `skill.selection` event must remain `BLOCKED`, not become a negative trigger result; preserve the existing local rule and document it.
- The bilingual Meta Skills must not claim runtime behavior from static package review; pin this in both boundary eval cases and the contract.
- Generated inventories, catalog counts, and registry records must stay synchronized after adding two logical Skill pairs; run the existing generators and quality gate.

### Task 1: Add the v1.5.1 plan, evidence contract, and pilot record

**Files:**
- Create: `docs/governance/SKILL_EVALUATION_DESIGN.md`
- Create: `docs/governance/SKILL_EVALUATION_DESIGN_EN.md`
- Create: `docs/governance/SKILL_EVALUATION_CONTRACT.md`
- Create: `docs/governance/SKILL_EVALUATION_CONTRACT_EN.md`
- Create: `docs/governance/SKILL_EVALUATION_PILOTS.md`
- Create: `docs/governance/SKILL_EVALUATION_PILOTS_EN.md`
- Modify: `scripts/check_docs_bilingual.py`
- Test: `scripts/tests/test_skill_evaluation_contract.py`

- [x] Write failing contract tests for the required bilingual documents, status vocabulary, judge order, pilot identifiers, and explicit no-second-engine/no-second-score boundaries.
- [x] Run `python3 -m unittest scripts.tests.test_skill_evaluation_contract -v` and observe the missing-document failure.
- [x] Add concise Chinese and English architecture documents that preserve the supplied design's purpose, non-goals, source-of-truth map, responsibilities, case types, judge strategy, trigger/neighbor/benchmark/regression boundaries, CI levels, roadmap, invariants, and Definition of Done.
- [x] Add the bilingual Evaluation Contract defining evidence layers, `PASS`/`FAIL`/`BLOCKED`/`NOT_RUN`/`NOT_SCORED`/`UNASSESSED`/`INSUFFICIENT_EVIDENCE`, run metadata, failure classification, comparability, and the standard report outline.
- [x] Add the bilingual pilot record for `requirements-analysis` (analysis pilot) and `ui-test-playwright` (executable artifact pilot), explicitly recording runtime/model execution as `NOT_RUN` until fresh evidence exists.
- [x] Register all three new document pairs in `check_docs_bilingual.py` and make the tests pass.

### Task 2: Add evidence metadata and regression-case conversion around the existing runner

**Files:**
- Create: `scripts/skill_eval_evidence.py`
- Create: `scripts/add_skill_eval_regression_case.py`
- Create: `scripts/compare_skill_eval_runs.py`
- Modify: `scripts/run_skill_trace_eval.py`
- Modify: `scripts/tests/test_run_skill_trace_eval.py`
- Create: `scripts/tests/test_skill_eval_evidence.py`
- Create: `scripts/tests/test_add_skill_eval_regression_case.py`
- Create: `scripts/tests/test_compare_skill_eval_runs.py`
- Modify: `docs/SKILL_EVAL_RULES.md`
- Modify: `docs/SKILL_EVAL_RULES_EN.md`

- [x] Write failing tests for metadata defaults, commit/eval hashes, unique `run_id`, evidence-state mapping, explicit failure classification, safe regression-case IDs, and refusal to overwrite an existing case.
- [x] Run the focused tests and observe the missing-module/API failures.
- [x] Implement standard-library-only metadata helpers that record timestamp, run ID, skill/eval hashes, `skill-up` version when available, engine/model/provider values, judge type, environment, and unknown values without guessing.
- [x] Extend the existing runner's JSON report with `run_metadata`, `evidence_state`, and `failure_classification` while preserving existing exit codes and dry-run behavior.
- [x] Add a small regression-case writer that creates a case under an explicitly supplied Skill's `evals/cases/` directory, marks it `REGRESSION`, and never edits `SKILL.md` or silently overwrites an existing case.
- [x] Add a deterministic previous/current report comparator that checks the comparability contract before reporting regression observations.
- [x] Document how metadata, trace evidence, failure classifications, and regression candidates are interpreted; keep local twenty-rule semantics unchanged.
- [x] Run focused tests and confirm the new helpers pass without network access.

### Task 3: Create bilingual `skill-quality-review` and `skill-evaluation` Meta Skills

**Files:**
- Create: `skills/zh/skill-engineering/skill-quality-review/SKILL.md`
- Create: `skills/zh/skill-engineering/skill-quality-review/prompts/skill-quality-review.md`
- Create: `skills/zh/skill-engineering/skill-quality-review/agents/openai.yaml`
- Create: `skills/zh/skill-engineering/skill-quality-review/evals/eval.yaml`
- Create: `skills/zh/skill-engineering/skill-quality-review/evals/cases/{basic-success,edge-incomplete-input,edge-runtime-claim}.yaml`
- Create: `skills/en/skill-engineering/skill-quality-review/SKILL.md`
- Create: `skills/en/skill-engineering/skill-quality-review/prompts/skill-quality-review.md`
- Create: `skills/en/skill-engineering/skill-quality-review/agents/openai.yaml`
- Create: `skills/en/skill-engineering/skill-quality-review/evals/eval.yaml`
- Create: `skills/en/skill-engineering/skill-quality-review/evals/cases/{basic-success,edge-incomplete-input,edge-runtime-claim}.yaml`
- Create: `skills/zh/skill-engineering/skill-evaluation/SKILL.md`
- Create: `skills/zh/skill-engineering/skill-evaluation/prompts/skill-evaluation.md`
- Create: `skills/zh/skill-engineering/skill-evaluation/agents/openai.yaml`
- Create: `skills/zh/skill-engineering/skill-evaluation/evals/eval.yaml`
- Create: `skills/zh/skill-engineering/skill-evaluation/evals/cases/{basic-success,edge-incomplete-input,edge-no-second-engine}.yaml`
- Create: `skills/en/skill-engineering/skill-evaluation/SKILL.md`
- Create: `skills/en/skill-engineering/skill-evaluation/prompts/skill-evaluation.md`
- Create: `skills/en/skill-engineering/skill-evaluation/agents/openai.yaml`
- Create: `skills/en/skill-engineering/skill-evaluation/evals/eval.yaml`
- Create: `skills/en/skill-engineering/skill-evaluation/evals/cases/{basic-success,edge-incomplete-input,edge-no-second-engine}.yaml`

- [x] Write the 24 package-file fixtures and use `skill-up validate` as the configuration test; the initial validation must fail because the directories do not exist.
- [x] Implement `skill-quality-review` as a package-level static review: scope, architecture, triggers, completeness, progressive disclosure, independent installation, bilingual consistency, eval readiness, and evidence boundaries; it must not claim runtime behavior.
- [x] Implement `skill-evaluation` as a design/run/interpret/report/recommend workflow using `skill-up`, existing trace checks, deterministic/script/semantic judge ordering, trigger/neighbor/benchmark/regression distinctions, and explicit failure classification.
- [x] Keep Chinese natural-language artifacts Chinese and English artifacts English, while preserving technical identifiers; in particular, do not use a Chinese phrase in the English case files.
- [x] Add three meaningful cases per Meta Skill: happy path, incomplete information, and a boundary case that rejects runtime overclaiming or a competing engine/score.
- [x] Run `skill-up validate` for all four `eval.yaml` files and `python3 -m unittest` for the package/contract tests.

### Task 4: Synchronize repository governance, catalogs, generated views, and CI

**Files:**
- Modify: `docs/governance/skill-governance-registry.yaml`
- Modify: `docs/catalog/skills-index.md`
- Modify: `docs/catalog/skills-index_EN.md`
- Modify: `skills/zh/README.md`
- Modify: `skills/en/README.md`
- Modify: `README.md`
- Modify: `README_EN.md`
- Modify: `docs/governance/QA_SKILLS_EVOLUTION_ROADMAP.md`
- Modify: `docs/governance/QA_SKILLS_EVOLUTION_ROADMAP_EN.md`
- Modify: `.github/workflows/project-quality.yml`
- Modify: `scripts/check_skills_quality.sh`
- Generated: `docs/generated/skill-inventory.md`
- Generated: `docs/generated/skill-governance-inventory.md`
- Generated: `docs/generated/skill-governance-inventory_EN.md`
- Generated: `docs/SKILL_MATRIX.md`
- Generated: `docs/SKILL_MATRIX_EN.md`
- Generated: `docs/SKILL_MATCHING_REGISTER.md`
- Generated: `docs/SKILL_MATCHING_REGISTER_EN.md`

- [x] Add registry records for both new logical Skills with D14, P1/Experimental, `NOT_SCORED`, `NOT_RUN`, bilingual paths, and evidence paths; do not create a new Quality Score dimension.
- [x] Update bilingual catalog/readme counts from 162/3 to 164/5 and add both packages to the Skill Engineering navigation.
- [x] Add a short v1.5.1 entry to both governance roadmaps that points to the design, contract, pilots, and evidence rules, while keeping v1.5's historical CLI closeout separate.
- [x] Add the contract validator to the quality gate/CI after its tests exist; install pinned `skill-up` and make the Level 1 validation fail closed in CI; retain the CLI compatibility job.
- [x] Run the generators in their documented order and use their `--check` modes to prove generated files are synchronized.

### Task 5: Verify implementation and update Project #4

**Project:** `https://github.com/users/naodeng/projects/4`

- [x] Run focused unit tests, `skill-up validate` for all new eval suites, `python3 scripts/check_docs_bilingual.py --repo-root .`, `bash scripts/check_skills_quality.sh`, `bash scripts/check_skills_cli_compatibility.sh`, and `git diff --check`.
- [x] Inspect the final worktree and confirm only v1.5.1-owned files changed; do not commit or push unless separately requested.
- [x] Add `v1.5.1` to Project #4's `Target Version` single-select field, preserving all existing options.
- [x] Create one detailed Draft Issue card `v1.5.1｜迭代｜Skill Evaluation Quality Loop` covering the supplied design, the two Meta Skills, evidence contract/metadata, pilots, regression conversion, CI, limitations, and DoD; set `Status=Done`, `Priority=P1`, and `Target Version=v1.5.1` after repository verification.
- [x] Set every live Project #4 item whose `Target Version` is `v1.5` to `Status=Done`, preserving title, priority, and target version; verify the count before and after mutation.
- [x] Re-read the Project item list and record the new card ID, target version, status, priority, and the set of v1.5 cards now Done. Treat model/runtime evidence as `NOT_RUN` if no authorized real-model run exists.
