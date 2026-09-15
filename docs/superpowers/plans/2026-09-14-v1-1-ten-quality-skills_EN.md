<div align="right"><a href="./2026-09-14-v1-1-ten-quality-skills.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# v1.1 Ten Quality Skills Unified Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Complete the previous five and current five v1.1 P0 quality Skills in one `develop` worktree: bilingual packages, enhancements, Evals, local trigger rules, governance records, and verification.

**Architecture:** This plan covers seven standalone new Skills and three enhancements to existing Skills. Each new Skill owns its `SKILL.md`, primary Prompt, metadata, and Evals; enhancements preserve their directories and stable contracts while adding business-rule, architecture-testability, and coverage-analysis modes. All packages share evidence boundaries but do not link to other Skills' internal files or share runtime code.

**Tech Stack:** Markdown, YAML, CSV, JSON, Python 3 standard library, `skill-up validate/run`, the repository-local trace runner, GitHub Project CLI, and existing quality gates.

**Spec:**

- `docs/superpowers/specs/2026-09-14-v1-1-next-five-quality-skills-design.md`
- `docs/superpowers/specs/2026-09-14-v1-1-following-five-quality-skills-design.md`

## Global Constraints

- This plan covers these ten logical candidates: `business-rule-extraction`, `business-rule-consistency-review`, `technical-design-quality-review`, `architecture-testability-review`, `api-design-quality-review`, `database-design-quality-review`, `observability-design-review`, `error-handling-design-review`, `test-scope-analysis`, and `test-coverage-analysis`.
- Create bilingual directories only for the seven `NEW` logical Skills. `business-rule-consistency-review` enhances `requirement-consistency-analysis`, `architecture-testability-review` enhances `testability-analysis`, and `test-coverage-analysis` enhances `requirement-traceability-analysis`; create no duplicate directories for those three.
- Every new package contains `SKILL.md`, `prompts/<slug>.md`, `agents/openai.yaml`, `evals/eval.yaml`, `basic-success.yaml`, `edge-incomplete-input.yaml`, `edge-scope-boundary.yaml`, `trigger-prompts.csv`, and `local-rules.json`; each enhancement reuses its directory and adds the matching three Evals and local trigger data.
- Enhanced candidates do not get alias directories: their local `trigger-prompts.csv` and `local-rules.json` live under the physical target Skill's `evals/`; JSON `skill` remains the physical target slug, and CSV data includes the candidate name or mode phrase to verify candidate-mode routing.
- Chinese and English `name`, directory name, `agents/openai.yaml` `metadata.key`, Prompt structure, and Eval semantics remain paired; descriptions start with `Use when...` and describe triggers only.
- Every Prompt starts with an audit of `known`, `missing`, `conflicting`, `stale`, `out_of_scope`, and `assumptions`; facts, evidence-backed inferences, recommendations, and Human decisions remain separate.
- Do not upgrade file presence, name matching, design claims, report wording, or static gates into execution results, compatibility passes, quality scores, risk acceptance, Human approval, or Release completion.
- Each Skill gets its own RED → minimal GREEN → REFACTOR and target Eval checks; a unified plan does not skip per-Skill evidence.
- The ten Project #4 cards remain `In Progress`; do not change other cards, create Issues, push, or publish. Preserve existing uncommitted `requirement-*` changes.
- Registry real-model execution remains `NOT_RUN` and quality remains `NOT_SCORED` unless independent evidence exists; the local trace runner reports only `BLOCKED` when `skill.selection` evidence is absent.
- Do not commit or push; keep changes in the current worktree unless Git delivery is separately authorized.

---

### Task 1: Establish the ten-Skill contract test and observe RED

**Files:**

- Create: `scripts/tests/test_v11_ten_quality_skill_contracts.py`
- Read-only reference: `scripts/tests/test_v11_requirement_quality_contracts.py`
- Read-only reference: `scripts/run_skill_trace_eval.py`
- Read-only reference: `scripts/skill_eval_rules.py`

**Interfaces:**

- Consumes: fixed paths and mode markers for seven new Skills and three enhancement targets.
- Produces: repeatable checks for physical packages, bilingual parity, local trigger data, and enhancement modes.
- Boundary: checks repository structure and text contracts only; it does not run a real model or prove Skill effectiveness.

- [x] **Step 1: Write the failing contract test first.**

  Fix these sets and check the same contract for both languages:

  ```python
  NEW_SLUGS = (
      "business-rule-extraction",
      "technical-design-quality-review",
      "api-design-quality-review",
      "database-design-quality-review",
      "observability-design-review",
      "error-handling-design-review",
      "test-scope-analysis",
  )
  ENHANCEMENTS = {
      "business-rule-consistency-review": {
          "target": "requirement-consistency-analysis",
          "mode_markers": ("business-rule", "business_rule"),
          "artifact_markers": ("BR-",),
          "case_prefix": "business-rule-",
      },
      "architecture-testability-review": {
          "target": "testability-analysis",
          "mode_markers": ("architecture",),
          "artifact_markers": ("seam", "substitute", "fault injection"),
          "case_prefix": "architecture-",
      },
      "test-coverage-analysis": {
          "target": "requirement-traceability-analysis",
          "mode_markers": ("coverage_analysis",),
          "artifact_markers": ("TC-", "RT-"),
          "case_prefix": "coverage-",
      },
  }
  ```

  New-package tests assert the presence of `SKILL.md`, the Prompt, metadata, `eval.yaml`, three cases, CSV, and JSON. Each CSV contains `explicit`, `implicit`, `contextual`, and `negative` plus both positive and negative controls; JSON `skill` equals the physical directory slug. Enhancement tests must check exact mode and domain-artifact markers in the target SKILL/Prompt, the corresponding case prefix, a target-slug JSON value, and at least one CSV prompt containing the candidate name or mode alias; the coverage enhancement must also preserve the `RT-##` and coverage-state contract. This prevents a generic “business rule”/“architecture”/“coverage” word from producing a false pass.

- [x] **Step 2: Run only this contract test and confirm RED.**

  ```bash
  python3 -m unittest scripts.tests.test_v11_ten_quality_skill_contracts -v
  ```

  Expected: FAIL because the seven new bilingual package directories and three enhancement-mode contracts do not exist yet. If it passes, tighten the assertion until failure is caused by missing target behavior rather than a test typo.

- [x] **Step 3: Inspect the RED diff and preserve existing work.**

  ```bash
  git diff --check
  git status --short
  ```

  Do not delete, reset, or overwrite existing `requirement-*` changes; keep the contract test as a new file for this batch.

---

### Task 2: Add `business-rule-extraction`

**Files:**

- Create: `skills/zh/testing-types/business-rule-extraction/SKILL.md`
- Create: `skills/zh/testing-types/business-rule-extraction/prompts/business-rule-extraction.md`
- Create: `skills/zh/testing-types/business-rule-extraction/agents/openai.yaml`
- Create: `skills/zh/testing-types/business-rule-extraction/evals/eval.yaml`
- Create: `skills/zh/testing-types/business-rule-extraction/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: `skills/zh/testing-types/business-rule-extraction/evals/{trigger-prompts.csv,local-rules.json}`
- Create: matching files under `skills/en/testing-types/business-rule-extraction/`

**Interfaces:**

- Consumes: PRDs, policies, contracts, workflows, acceptance criteria, and supplied examples.
- Produces: atomic `BR-##` rules containing rule, source, actor/object, trigger, preconditions, action/outcome, constraints/invariants, exceptions, evidence, unknowns, impact, and validation hints.
- Boundary: does not invent thresholds, precedence, state transitions, or exceptions; turn recommendations into facts; or approve rules for Business or Compliance.

- [x] **Step 1:** Write three Evals and trigger data covering a traceable rule, incomplete material, and a rule-scope boundary.
- [x] **Step 2:** Run zh/en `skill-up validate`; after the minimal package files exist it must pass, while behavioral effectiveness remains unexecuted.

  ```bash
  skill-up validate skills/zh/testing-types/business-rule-extraction/evals/eval.yaml
  skill-up validate skills/en/testing-types/business-rule-extraction/evals/eval.yaml
  ```

- [x] **Step 3:** Write the minimal bilingual entry, Prompt, and metadata. The Prompt follows input audit, atomization, source retention, exception/unknown handling, and output contract order; the description contains triggers only.
- [x] **Step 4:** Run both-language dry-runs, local trigger data checks, and the contract test; confirm examples and recommendations cannot become business facts.

  ```bash
  skill-up run skills/zh/testing-types/business-rule-extraction/evals/eval.yaml --dry-run
  skill-up run skills/en/testing-types/business-rule-extraction/evals/eval.yaml --dry-run
  python3 -m unittest scripts.tests.test_v11_ten_quality_skill_contracts -v
  ```

- [x] **Step 5:** Run `git diff --check`, record the package structure evidence, and then move to the next package.

---

### Task 3: Enhance `business-rule-consistency-review` → `requirement-consistency-analysis`

**Files:**

- Modify: `skills/zh/testing-types/requirement-consistency-analysis/SKILL.md`
- Modify: `skills/zh/testing-types/requirement-consistency-analysis/prompts/requirement-consistency-analysis.md`
- Add: `skills/zh/testing-types/requirement-consistency-analysis/evals/cases/{business-rule-success,business-rule-incomplete-input,business-rule-scope-boundary}.yaml`
- Modify: `skills/zh/testing-types/requirement-consistency-analysis/evals/{eval.yaml,trigger-prompts.csv,local-rules.json}`
- Modify: matching English files under `skills/en/testing-types/requirement-consistency-analysis/`

**Interfaces:**

- Consumes: two or more business-rule statements with applicability scope, version, or region where available.
- Produces: a business-rule mode with stable rule keys, subject/object, trigger, applicability, precedence/override relation, action, outcome, and exception comparison; preserve `RC-##` and separate relations from statuses.
- Boundary: never treat “stricter” as higher precedence; preserve generic consistency analysis; create no `business-rule-consistency-review` directory.

- [x] **Step 1:** Add the three business-rule Evals and trigger data without overwriting current uncommitted content. Success must preserve both statements and rule-level evidence; incomplete input must expose gaps; cross-version/region input must preserve scope differences.
- [x] **Step 2:** Run the enhancement contract test to record RED.
- [x] **Step 3:** Make the minimal bilingual SKILL/Prompt edits for mode selection, stable comparison keys, unresolved precedence, and rule-level evidence; preserve existing generic cases and the `RC-##` contract.
- [x] **Step 4:** Run target validation/dry-runs, existing contract tests, and independence checks; confirm no duplicate directory exists.

  ```bash
  skill-up validate skills/zh/testing-types/requirement-consistency-analysis/evals/eval.yaml
  skill-up validate skills/en/testing-types/requirement-consistency-analysis/evals/eval.yaml
  skill-up run skills/zh/testing-types/requirement-consistency-analysis/evals/eval.yaml --dry-run
  skill-up run skills/en/testing-types/requirement-consistency-analysis/evals/eval.yaml --dry-run
  python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings
  ```

- [x] **Step 5:** Run the contract test and `git diff --check`; confirm the existing generic capability was not rewritten.

---

### Task 4: Add `technical-design-quality-review`

**Files:**

- Create: `skills/zh/testing-types/technical-design-quality-review/{SKILL.md,agents/openai.yaml}`
- Create: `skills/zh/testing-types/technical-design-quality-review/prompts/technical-design-quality-review.md`
- Create: `skills/zh/testing-types/technical-design-quality-review/evals/eval.yaml`
- Create: `skills/zh/testing-types/technical-design-quality-review/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: `skills/zh/testing-types/technical-design-quality-review/evals/{trigger-prompts.csv,local-rules.json}`
- Create: matching files under `skills/en/testing-types/technical-design-quality-review/`

**Interfaces:**

- Consumes: architecture notes, ADRs, component/data-flow designs, technical proposals, and non-functional constraints.
- Produces: `TD-##` findings covering boundaries, dependencies/failure modes, data consistency, security, performance, observability, compatibility, maintainability, and verification readiness.
- Boundary: does not review code that was not supplied, run builds/tests, turn design presence into implementation correctness, or approve architecture for a Human.

- [x] **Step 1:** Write success, incomplete, and design/implementation-boundary Evals plus four trigger modes.
- [x] **Step 2:** Run zh/en validation and dry-runs to confirm the case schema.
- [x] **Step 3:** Write the minimal bilingual package with the fixed output order: input audit, design coverage matrix, `TD-##` findings, gap actions, owner roles, validation methods, and Human questions.
- [x] **Step 4:** Run the contract test, metadata/independence checks, and `git diff --check`; real model execution remains `NOT_RUN`.

---

### Task 5: Enhance `architecture-testability-review` → `testability-analysis`

**Files:**

- Modify: `skills/zh/testing-types/testability-analysis/SKILL.md`
- Modify: `skills/zh/testing-types/testability-analysis/prompts/testability-analysis.md`
- Add: `skills/zh/testing-types/testability-analysis/evals/cases/{architecture-success,architecture-incomplete-input,architecture-unsafe-seam-boundary}.yaml`
- Modify: `skills/zh/testing-types/testability-analysis/evals/{eval.yaml,trigger-prompts.csv,local-rules.json}`
- Modify: matching English files under `skills/en/testing-types/testability-analysis/`

**Interfaces:**

- Consumes: architecture diagrams, component boundaries, dependency topology, asynchronous flows, data stores, external services, configuration, and deployment environments.
- Produces: architecture-mode test seams, substitute strategy, isolation boundaries, fault-injection entry points, environment reproducibility, and evidence gaps while preserving generic testability dimensions.
- Boundary: does not treat a test framework name as testability, recommend unsafe backdoors, or create an `architecture-testability-review` directory.

- [x] **Step 1:** Add three architecture Evals and trigger data. Success requires architecture-level evidence; incomplete input retains gaps; unsafe-seam cases reject backdoors.
- [x] **Step 2:** Run the enhancement contract test to record RED, then make minimal bilingual entry/Prompt edits while retaining observability, controllability, isolation, determinism, and data dimensions.
- [x] **Step 3:** Run target validation/dry-runs, contract tests, independence checks, and diff check.

---

### Task 6: Add `api-design-quality-review`

**Files:**

- Create: `skills/zh/testing-types/api-design-quality-review/{SKILL.md,agents/openai.yaml}`
- Create: `skills/zh/testing-types/api-design-quality-review/prompts/api-design-quality-review.md`
- Create: `skills/zh/testing-types/api-design-quality-review/evals/eval.yaml`
- Create: `skills/zh/testing-types/api-design-quality-review/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: `skills/zh/testing-types/api-design-quality-review/evals/{trigger-prompts.csv,local-rules.json}`
- Create: matching files under `skills/en/testing-types/api-design-quality-review/`

**Interfaces:**

- Consumes: API designs, OpenAPI/contracts, request/response examples, error models, authentication/authorization, idempotency, pagination, status codes, version evolution, and consumer impact.
- Produces: `API-##` findings retaining operation, source, evidence, impact, compatibility risk, migration questions, owner role, and validation method.
- Boundary: does not execute an API, treat examples as a complete contract, claim compatibility/security tests passed, or choose the final versioning policy.

- [x] **Step 1:** Write three Evals and four trigger modes; boundary cases must reject unsupported “complete example,” “security passed,” and “compatibility passed” claims.
- [x] **Step 2:** Run validation/dry-runs, then write the bilingual entry, Prompt, and metadata while keeping the boundary separate from `api-contract-testing` verification.
- [x] **Step 3:** Run contract, metadata/independence, and diff checks.

---

### Task 7: Add `database-design-quality-review`

**Files:**

- Create: `skills/zh/testing-types/database-design-quality-review/{SKILL.md,agents/openai.yaml}`
- Create: `skills/zh/testing-types/database-design-quality-review/prompts/database-design-quality-review.md`
- Create: `skills/zh/testing-types/database-design-quality-review/evals/eval.yaml`
- Create: `skills/zh/testing-types/database-design-quality-review/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: `skills/zh/testing-types/database-design-quality-review/evals/{trigger-prompts.csv,local-rules.json}`
- Create: matching files under `skills/en/testing-types/database-design-quality-review/`

**Interfaces:**

- Consumes: ERDs, DDL, ORM schemas, migration plans, data ownership, lifecycle, query constraints, transaction/concurrency, and recovery design.
- Produces: `DB-##` findings containing object, evidence, constraints/indexes, transaction/concurrency, migration rollback, impact, owner role, and closure evidence.
- Boundary: does not connect to or migrate a real database, run queries/benchmarks, invent business rules or thresholds from table names, or approve launch for a Human.

- [x] **Step 1:** Write success, incomplete, and database-execution-boundary Evals plus local trigger data.
- [x] **Step 2:** Run validation/dry-runs, then write the bilingual package covering model integrity, constraints, indexes, lifecycle/privacy, transaction isolation, migration compatibility, performance risk, backup/recovery, and test readiness.
- [x] **Step 3:** Run contract, metadata/independence, and diff checks; confirm all examples use redacted sample data.

---

### Task 8: Add `observability-design-review`

**Files:**

- Create: `skills/zh/testing-types/observability-design-review/{SKILL.md,agents/openai.yaml}`
- Create: `skills/zh/testing-types/observability-design-review/prompts/observability-design-review.md`
- Create: `skills/zh/testing-types/observability-design-review/evals/eval.yaml`
- Create: `skills/zh/testing-types/observability-design-review/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: `skills/zh/testing-types/observability-design-review/evals/{trigger-prompts.csv,local-rules.json}`
- Create: matching files under `skills/en/testing-types/observability-design-review/`

**Interfaces:**

- Consumes: log, metric, trace, context propagation, SLO/SLI, alert, dashboard, sampling, retention, privacy, and cost designs.
- Produces: `OBS-##` findings containing signal, object, fields/dimensions, semantics, gap, impact, detection action, owner role, and validation method.
- Boundary: does not read real runtime signals to declare health, treat a dashboard as alert effectiveness, execute production probes, or choose SLO/incident severity for a team.

- [x] **Step 1:** Write three Evals and four trigger modes, including sensitive-data, cardinality, sampling, and alert-actionability boundaries.
- [x] **Step 2:** Run validation/dry-runs, then write the bilingual package with explicit runtime-evidence boundaries from `log-analysis`, `distributed-trace-analysis`, and `metrics-anomaly-analysis`.
- [x] **Step 3:** Run contract, metadata/independence, and diff checks.

---

### Task 9: Add `error-handling-design-review`

**Files:**

- Create: `skills/zh/testing-types/error-handling-design-review/{SKILL.md,agents/openai.yaml}`
- Create: `skills/zh/testing-types/error-handling-design-review/prompts/error-handling-design-review.md`
- Create: `skills/zh/testing-types/error-handling-design-review/evals/eval.yaml`
- Create: `skills/zh/testing-types/error-handling-design-review/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: `skills/zh/testing-types/error-handling-design-review/evals/{trigger-prompts.csv,local-rules.json}`
- Create: matching files under `skills/en/testing-types/error-handling-design-review/`

**Interfaces:**

- Consumes: error taxonomy, exception boundaries, timeouts, retry/backoff, circuit breaking, degradation, idempotency, transaction consistency, error propagation, consumer contracts, telemetry, and recovery design.
- Produces: `EH-##` failure-mode findings that distinguish retryable, non-retryable, human-intervention, and safe-rejection paths with evidence, impact, owner, and validation method.
- Boundary: does not run fault injection, review a real incident, treat error-handling code presence as correctness, or choose SLA, copy, or risk acceptance for a Human.

- [x] **Step 1:** Write three Evals and four trigger modes; boundary cases prevent one generic error response from being treated as a complete design.
- [x] **Step 2:** Run validation/dry-runs, then write the bilingual package with explicit boundaries from `production-incident-analysis` and `root-cause-analysis`.
- [x] **Step 3:** Run contract, metadata/independence, and diff checks.

---

### Task 10: Add `test-scope-analysis`

**Files:**

- Create: `skills/zh/testing-types/test-scope-analysis/{SKILL.md,agents/openai.yaml}`
- Create: `skills/zh/testing-types/test-scope-analysis/prompts/test-scope-analysis.md`
- Create: `skills/zh/testing-types/test-scope-analysis/evals/eval.yaml`
- Create: `skills/zh/testing-types/test-scope-analysis/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: `skills/zh/testing-types/test-scope-analysis/evals/{trigger-prompts.csv,local-rules.json}`
- Create: matching files under `skills/en/testing-types/test-scope-analysis/`

**Interfaces:**

- Consumes: test goals, product surface, changes/risks, constraints, existing assets, platforms/roles, data, and environments.
- Produces: `TS-##` inclusion/exclusion, depth, dependencies, stop conditions, expansion triggers, residual risk, evidence, and owner role.
- Boundary: does not generate a full test strategy, choose a concrete executable set, execute tests, or turn a scope statement into coverage proof.

- [x] **Step 1:** Write three Evals; success covers core/transitive impact and scope tradeoffs, incomplete input gives a constrained draft, and boundary input rejects unauthorized all-or-nothing coverage conclusions.
- [x] **Step 2:** Run validation/dry-runs, then write the bilingual package with explicit boundaries from `regression-scope-analysis`, `regression-test-selection`, and `test-strategy`.
- [x] **Step 3:** Run contract, metadata/independence, and diff checks.

---

### Task 11: Enhance `test-coverage-analysis` → `requirement-traceability-analysis`

**Files:**

- Modify: `skills/zh/testing-types/requirement-traceability-analysis/SKILL.md`
- Modify: `skills/zh/testing-types/requirement-traceability-analysis/prompts/requirement-traceability-analysis.md`
- Add: `skills/zh/testing-types/requirement-traceability-analysis/evals/cases/{coverage-success,coverage-incomplete-input,coverage-scope-boundary}.yaml`
- Modify: `skills/zh/testing-types/requirement-traceability-analysis/evals/{eval.yaml,trigger-prompts.csv,local-rules.json}`
- Modify: matching English files under `skills/en/testing-types/requirement-traceability-analysis/`

**Interfaces:**

- Consumes: requirements, risks, behaviors/scenarios, test assets, and real execution evidence when supplied.
- Produces: existing `RT-##` bidirectional relationships plus `TC-##` coverage views with object, source, test asset, relation type, coverage state, execution identity/time/environment, evidence quality, orphan signal, gap action, and validation method.
- Boundary: creates no `test-coverage-analysis` directory, treats no test file/name/report summary as executed coverage, and calculates no code-line coverage without tool evidence.

- [x] **Step 1:** Write valid-mapping, incomplete-input, and scope/execution-evidence boundary Evals plus four trigger modes; keep existing generic traceability cases.
- [x] **Step 2:** Run the enhancement contract test to record RED, then make minimal bilingual SKILL/Prompt edits for the optional `coverage_analysis` mode, `TC-##` contract, and coverage-state boundaries.
- [x] **Step 3:** Run validation/dry-runs, contract tests, independence checks, and diff check; confirm `RT-##` relation enums remain separate from coverage-state enums.

---

### Task 12: Synchronize governance registry, matching register, and generated views

**Files:**

- Modify: `docs/governance/skill-governance-registry.yaml`
- Modify: `docs/governance/PHASE_1_REQUIREMENTS_QUALITY.md`
- Modify: `docs/governance/PHASE_1_REQUIREMENTS_QUALITY_EN.md`
- Modify: `docs/SKILL_MATRIX.md`
- Modify: `docs/SKILL_MATRIX_EN.md`
- Modify: `docs/SKILL_MATCHING_REGISTER.md`
- Modify: `docs/SKILL_MATCHING_REGISTER_EN.md`
- Modify: `docs/generated/skill-governance-inventory.md`
- Modify: `docs/generated/skill-governance-inventory_EN.md`
- Modify: `docs/generated/skill-inventory.md`
- Modify: `skills/zh/README.md`
- Modify: `skills/en/README.md`
- Modify: `docs/catalog/skills-index.md`
- Modify: `docs/catalog/skills-index_EN.md`
- Modify: `docs/catalog/skills-graph.md`
- Modify: `docs/catalog/skills-graph_EN.md`
- Modify: `README.md`
- Modify: `README_EN.md`
- Read-only generator sources: `scripts/generate_skill_governance_matrix.py`, `scripts/generate_skill_governance_inventory.py`, `scripts/generate_skill_inventory.py`

**Interfaces:**

- Consumes: seven new packages, three enhanced targets, and Capability Match evidence from both design specs after package gates pass.
- Produces: seven physical Skill registry records, three `ENHANCE` candidate records, and bilingual Matrix/Matching Register/Inventory/Catalog/Graph/index views.
- Boundary: registry records structure and governance state only; `quality_score.state=NOT_SCORED` and `eval_execution.state=NOT_RUN`; no semantic effectiveness is fabricated.

- [x] **Step 1:** Add seven `skills` records and three candidate records to the registry. `NEW` records require scope/non-goals; enhancement records point to existing targets and six-field evidence.
- [x] **Step 2:** Run registry/matrix validation and repair slug, zh/en path, metadata, evidence-path, and physical-directory cross-check errors.

  ```bash
  python3 scripts/generate_skill_inventory.py
  python3 scripts/generate_skill_governance_inventory.py
  python3 scripts/generate_skill_governance_matrix.py
  python3 scripts/generate_skill_governance_inventory.py --check
  python3 scripts/generate_skill_governance_matrix.py --check
  ```

- [x] **Step 3:** Refresh bilingual generated views with existing generators; retain only related generated differences and do not overwrite unrelated documentation changes.
- [x] **Step 4:** Update Phase 1, Catalog, Graph, root README, and `skills/zh/README.md` / `skills/en/README.md` bilingual entries and capability boundaries; update language/total Skill counts from generator output (baseline 84/168; expected 91/182 if the seven new logical packages are the only physical additions), and do not present candidate aliases as physical Skill directories.
- [x] **Step 5:** Run bilingual documentation and independence checks, proving that all ten candidates resolve to a physical package or enhancement target.

---

### Task 13: Run unified quality gates and verify Project cards

**Files:**

- Test: `scripts/tests/test_v11_requirement_quality_contracts.py`
- Test: `scripts/tests/test_v11_ten_quality_skill_contracts.py`
- Verify: all seven new bilingual packages and three enhanced bilingual target packages
- Verify: Project #4 item IDs for the ten cards

**Interfaces:**

- Consumes: all ten Skills' packages, Evals, local rules, governance records, and generated views.
- Produces: reviewable static quality, Eval schema/dry-run, local-trigger, and Project-state evidence; real model execution remains `NOT_RUN`.
- Boundary: no push, publish, or execution against real API, database, production observability, incident, or test targets.

- [x] **Step 1:** Run `skill-up validate` and `--dry-run` for every target package; all seven new packages and three enhanced targets must pass structure checks.
- [x] **Step 2:** Run both local contract tests and the full test suite.

  ```bash
  python3 -m unittest discover -s scripts/tests -p 'test_*.py'
  ```

- [x] **Step 3:** Run repository quality gates.

  ```bash
  bash scripts/check_skills_quality.sh
  bash scripts/validate_skill_evals.sh
  python3 scripts/check_docs_bilingual.py --repo-root .
  git diff --check
  ```

- [x] **Step 4:** Run the default dry-run of `scripts/run_skill_trace_eval.py` for every target package with explicit `--prompts`, `--config`, `--project-root`, and `--output-dir` arguments and no `--run` flag:

  ```bash
  trace_targets=(
    business-rule-extraction
    requirement-consistency-analysis
    technical-design-quality-review
    testability-analysis
    api-design-quality-review
    database-design-quality-review
    observability-design-review
    error-handling-design-review
    test-scope-analysis
    requirement-traceability-analysis
  )
  for language in zh en; do
    for skill_slug in "${trace_targets[@]}"; do
      python3 scripts/run_skill_trace_eval.py \
        --prompts "skills/$language/testing-types/$skill_slug/evals/trigger-prompts.csv" \
        --config "skills/$language/testing-types/$skill_slug/evals/local-rules.json" \
        --project-root "/private/tmp/v11-trace-projects/$language-$skill_slug" \
        --output-dir "/private/tmp/v11-trace-reports/$language-$skill_slug"
    done
  done
  ```

  Without real `skill.selection` evidence, report `BLOCKED`, never PASS; dry-run proves only that the command and inputs can be loaded, while real model execution remains `NOT_RUN`.
- [x] **Step 5:** Use `gh project item-list 4 --owner @me --format json --limit 200` to verify the ten target titles are `In Progress`, while `test-gap-analysis`, `risk-based-testing`, `edge-case-discovery`, `negative-scenario-discovery`, and `test-data-requirement-analysis` remain `Todo`.
- [x] **Step 6:** Add a scoped trailing-whitespace check for new/modified files not covered by `git diff --check`, for example `rg -n "[[:blank:]]+$" scripts/tests/test_v11_ten_quality_skill_contracts.py docs/superpowers/plans/2026-09-14-v1-1-ten-quality-skills*.md skills/zh/testing-types/{business-rule-extraction,requirement-consistency-analysis,technical-design-quality-review,testability-analysis,api-design-quality-review,database-design-quality-review,observability-design-review,error-handling-design-review,test-scope-analysis,requirement-traceability-analysis} skills/en/testing-types/{business-rule-extraction,requirement-consistency-analysis,technical-design-quality-review,testability-analysis,api-design-quality-review,database-design-quality-review,observability-design-review,error-handling-design-review,test-scope-analysis,requirement-traceability-analysis}`; any match fails. Then report the final worktree file list, verification commands, and unexecuted boundaries; do not commit or push unless separately authorized.

## Plan Self-Review

### Review fixes applied (2026-09-14)

- Corrected the docs bilingual gate from `bash` to `python3` and supplied all four required trace-runner arguments.
- Added the refresh-before-`--check` generator sequence, included `generate_skill_inventory.py`, and made both language-root READMEs and count updates explicit.
- Strengthened enhancement contracts from generic keywords to mode markers, domain artifacts, case prefixes, physical-target `skill`, and candidate-alias prompt checks.
- Clarified alias-directory reuse and added a separate trailing-whitespace check for untracked files.

- Both design specs map all ten cards to Tasks 2–11; the seven `NEW` and three `ENHANCE` directory boundaries are covered.
- Every new package's entry, Prompt, metadata, Eval, three cases, trigger CSV, and local rule are listed; enhanced packages have explicit existing paths and added case/trigger paths.
- The RED contract test precedes package content, and every Skill still has independent validation, dry-run, contract, and diff checks.
- Registry, matching register, bilingual generated views, quality gates, and Project verification are centralized in Tasks 12–13 so intermediate states cannot be reported as Release complete.
- The plan contains no incomplete or “fill later” step; all commands, state boundaries, and file responsibilities are explicit. The review fixes cover command executability, bilingual entry points, physical alias boundaries, enhancement-contract strength, and the untracked-file verification blind spot.
