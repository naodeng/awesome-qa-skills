<div align="right"><a href="./2026-09-14-v1-1-requirements-quality-skills.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# v1.1 First Five Requirement-Quality Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create and validate the first five v1.1 P0 requirement-quality Skills as independently installable bilingual packages on `develop`, then synchronize Project, catalog, governance, and generated views.

> **Status note (2026-09-14):** This is a historical implementation plan; its original checkbox state is preserved for process traceability and unchecked items are not evidence that the implementation is incomplete. The current acceptance source is the [Phase 1 requirement-quality record](../../governance/PHASE_1_REQUIREMENTS_QUALITY_EN.md). Real-model Evals were explicitly deferred and remain `NOT_RUN`.

**Architecture:** Five separate Skills own overall quality review, ambiguity, consistency, conflict, and traceability analysis. Each package has its own Prompt and Evals and no shared runtime code. All packages use a common audit/evidence/risk/Human-decision boundary; the governance registry cross-checks physical directories and renders the Matrix, Matching Register, and inventory.

**Tech Stack:** Markdown, YAML, Bash, Python 3 standard library, `skill-up validate/run`, the repository quality gate, and GitHub Project CLI.

**Spec:** `docs/superpowers/specs/2026-09-14-v1-1-requirements-quality-skills-design_EN.md`

## Global Constraints

- Add only these five logical Skills in both languages: 10 directories total. Do not change the behavior of `requirements-analysis` or `requirements-analysis-plus`.
- Each package must contain `SKILL.md`, `prompts/<slug>.md`, `agents/openai.yaml`, `evals/eval.yaml`, and `basic-success`, `edge-incomplete-input`, and `edge-scope-boundary` cases.
- Each package's `evals/` also maintains `trigger-prompts.csv` covering explicit, implicit, contextual, and negative controls plus `local-rules.json`; the local runner reports `BLOCKED` when `skill.selection` evidence is absent.
- The frontmatter `name`, directory name, `agents/openai.yaml` `metadata.key`, and both language versions must agree. Descriptions start with `Use when...` and contain triggers only.
- Prompts start with an input audit for `known/missing/conflicting/stale/out_of_scope/assumptions`; facts, inferences, recommendations, and Human decisions stay separate; no invented thresholds, fields, endpoints, environments, owners, root causes, execution results, or approvals.
- Keep only these five Project #4 cards `In Progress`; do not change other cards, create GitHub Issues, push, or publish.
- Do not use relative links to another Skill's internal files; recommended compositions mention Skill names or external URLs only.
- Without real model execution evidence, keep registry `quality_score` at `NOT_SCORED` and `eval_execution` at `NOT_RUN`; a structural gate is not a behavior pass.
- Finish each Skill's RED/GREEN/REFACTOR check before starting the next; batch generation is not per-Skill verification.
- The pre-commit gate cross-checks physical directories against the registry globally, so Tasks 1–5 validate each package in order but do not commit while the registry is stale; all packages and governance records are committed atomically in Task 6.

---

### Task 1: Implement `requirement-quality-review`

**Files:**
- Create: `skills/zh/testing-types/requirement-quality-review/SKILL.md`
- Create: `skills/zh/testing-types/requirement-quality-review/prompts/requirement-quality-review.md`
- Create: `skills/zh/testing-types/requirement-quality-review/agents/openai.yaml`
- Create: `skills/zh/testing-types/requirement-quality-review/evals/eval.yaml`
- Create: `skills/zh/testing-types/requirement-quality-review/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: matching files under `skills/en/testing-types/requirement-quality-review/`

**Interfaces:**
- Consumes: supplied requirement artifacts, acceptance criteria, context, constraints, risks, and evidence.
- Produces: input audit; quality-dimension table for completeness, clarity, verifiability, feasibility, scope, and evidence quality; prioritized findings; specialist-routing suggestions; assumptions and Human decisions.
- Boundary: summarizes and routes; does not run the four specialists, assign a numeric quality score, or make a release decision.

- [x] **Step 1: Write the three failing/boundary cases first.**

  - `basic-success`: an order requirement says points may offset payment, but only “offset succeeds” is specified; require missing insufficient-points and callback-retry findings, `P0/P1` priority, and specialist routing.
  - `edge-incomplete-input`: the only input is “the new release adds points redemption”; require a usable draft, `known`, `missing`, `assumptions`, and 3–5 closeable questions instead of refusal.
  - `edge-scope-boundary`: the user asks for a numeric “quality score” and Go/No-Go from one paragraph; require evidence-bounded findings, no numeric score, and an explicit Human decision boundary.

  Each Chinese case asserts `输入审计`, `假设` or `信息缺口`, and `待确认`; each English case asserts `input audit`, `assumption` or `gap`, and `open question`. Boundary cases reject unsupported release/score claims.

- [x] **Step 2: Run `skill-up validate` on both new `eval.yaml` files and record the baseline.**

  Before package files exist, validation may report a missing skill layout; after the cases and package structure exist it must exit 0. Do not call YAML validation a behavior pass.

- [x] **Step 3: Write the minimum bilingual package.**

  Use these exact frontmatter identities:

  ```yaml
  ---
  name: requirement-quality-review
  description: Use when a requirement, acceptance-criteria set, or change brief needs an evidence-bounded quality review before design or testing; triggers include requirement quality review and requirements quality gate.
  ---
  ```

  The Prompt must contain `Input Audit and Scope`, `Quality Dimensions`, `Structured Findings`, `Specialist Routing and Next Steps`, and `Self-Check` headings, with Chinese equivalents in the Chinese Prompt. Results use `RQ-##` finding IDs and distinguish `missing`, `ambiguous`, `untestable`, `conflict`, and `unassessed`.

  `agents/openai.yaml` sets `metadata.key` to `requirement-quality-review`, a bilingual display name, a short description under 160 characters, a default prompt naming the Skill, and `allow_implicit_invocation: true`.

- [x] **Step 4: Validate and review behavior.**

  ```bash
  skill-up validate skills/zh/testing-types/requirement-quality-review/evals/eval.yaml
  skill-up validate skills/en/testing-types/requirement-quality-review/evals/eval.yaml
  skill-up run skills/zh/testing-types/requirement-quality-review/evals/eval.yaml --dry-run
  skill-up run skills/en/testing-types/requirement-quality-review/evals/eval.yaml --dry-run
  python3 scripts/validate_agents_metadata.py --report /tmp/v11-requirement-quality-metadata.md
  ```

  If an Agent Engine is configured, run all three cases in both languages and inspect the reports. Otherwise record execution as `NOT_RUN`; never infer behavior from `--dry-run`.

- [x] **Step 5: Refactor only confirmed gaps and leave the verified package ready for registry sync.**

  ```bash
  git diff --check
  git status --short
  ```

---

### Task 2: Implement `requirement-ambiguity-analysis`

**Files:**
- Create: `skills/zh/testing-types/requirement-ambiguity-analysis/{SKILL.md,prompts/requirement-ambiguity-analysis.md,agents/openai.yaml,evals/eval.yaml}`
- Create: `skills/zh/testing-types/requirement-ambiguity-analysis/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: matching files under `skills/en/testing-types/requirement-ambiguity-analysis/`

**Interfaces:**
- Consumes: requirement statements, stories, acceptance criteria, examples, terminology, actors, conditions, and source context.
- Produces: ambiguity findings with exact phrase, source, missing discriminator, possible readings without selecting one, priority, owner, clarification question, and validation method.
- Boundary: diagnoses under-specification; does not classify explicit incompatible statements as ordinary ambiguity or invent a default interpretation.

- [x] **Step 1: Write cases before the Skill.**

  - `basic-success`: “管理员可以在必要时导出订单” lacks the administrator, necessary condition, scope, format, and timing; require `RA-##` findings and a testability impact.
  - `edge-incomplete-input`: only “支持快速退款” is supplied; require a minimum audit and high-value questions, not a fabricated SLA or refund rule.
  - `edge-scope-boundary`: two artifacts explicitly say “refund is immediate” and “refund is processed within 3 business days”; require routing to conflict detection while preserving both sources.

- [x] **Step 2: Validate and dry-run.**

  ```bash
  skill-up validate skills/zh/testing-types/requirement-ambiguity-analysis/evals/eval.yaml
  skill-up validate skills/en/testing-types/requirement-ambiguity-analysis/evals/eval.yaml
  skill-up run skills/zh/testing-types/requirement-ambiguity-analysis/evals/eval.yaml --dry-run
  skill-up run skills/en/testing-types/requirement-ambiguity-analysis/evals/eval.yaml --dry-run
  ```

- [x] **Step 3: Write the bilingual package.**

  The Prompt requires a phrase-level ambiguity table with `source`, `quoted statement`, `ambiguity type`, `missing discriminator`, `possible readings`, `risk/impact`, `clarification question`, `owner`, and `validation method`. It explicitly forbids choosing a reading or filling in a threshold from common practice. Use `RA-##` IDs and `ambiguous`, `missing`, `untestable`, and `out_of_scope` statuses.

  Use `name: requirement-ambiguity-analysis`, a trigger-only `Use when...` description, matching `agents/openai.yaml`, and no cross-Skill file links.

- [x] **Step 4: Run validation and, if configured, both-language cases; inspect that explicit contradiction is routed rather than resolved.**

  ```bash
  python3 scripts/validate_agents_metadata.py --report /tmp/v11-requirement-ambiguity-metadata.md
  python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings --report-md /tmp/v11-ambiguity-independence.md
  git diff --check
  ```

- [x] **Step 5: Leave only this verified package as the next uncommitted scope.**

  ```bash
  git diff --check
  git status --short
  ```

---

### Task 3: Implement `requirement-consistency-analysis`

**Files:**
- Create: `skills/zh/testing-types/requirement-consistency-analysis/{SKILL.md,prompts/requirement-consistency-analysis.md,agents/openai.yaml,evals/eval.yaml}`
- Create: `skills/zh/testing-types/requirement-consistency-analysis/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: matching files under `skills/en/testing-types/requirement-consistency-analysis/`

**Interfaces:**
- Consumes: at least two supplied artifacts, or one artifact with repeated terminology/rule/state declarations.
- Produces: comparison matrix for terms, identifiers, formats, states, rules, and behavior; each row has source pair, relation, status, evidence, impact, action, and owner.
- Boundary: relation values are `aligned`, `inconsistent`, and `conflict`; evidence statuses are `assessed`, `missing`, `stale`, and `unassessed`. Explicit mutual exclusion is preserved and routed to conflict detection, not silently normalized.

- [x] **Step 1: Write the cases first.**

  - `basic-success`: PRD calls the actor `buyer`, API contract calls it `customer`; one source permits `pending → cancelled`, another lists only `pending → paid`; require comparison evidence, not a guessed synonym or normalized state machine.
  - `edge-incomplete-input`: only one short requirement is supplied; require the missing comparison set and a bounded single-source result.
  - `edge-scope-boundary`: two versioned documents differ because one is explicitly for v1 and one for v2; require `stale`/scope qualification and no same-scope conflict claim.

- [x] **Step 2: Validate and dry-run.**

  ```bash
  skill-up validate skills/zh/testing-types/requirement-consistency-analysis/evals/eval.yaml
  skill-up validate skills/en/testing-types/requirement-consistency-analysis/evals/eval.yaml
  skill-up run skills/zh/testing-types/requirement-consistency-analysis/evals/eval.yaml --dry-run
  skill-up run skills/en/testing-types/requirement-consistency-analysis/evals/eval.yaml --dry-run
  ```

- [x] **Step 3: Write the bilingual package.**

  The Prompt requires a stable comparison key and a table with `topic`, `source A`, `source B`, `relation`, `status`, `evidence`, `scope/version`, `impact`, `question`, `owner`, and `validation method`. It keeps different versions or applicability scopes separate and routes explicit mutual exclusion to `requirement-conflict-detection` by Skill name only. Use `RC-##` IDs.

- [x] **Step 4: Validate metadata, independence, and package boundary cases; refactor only evidence-backed gaps.**

  ```bash
  python3 scripts/validate_agents_metadata.py --report /tmp/v11-requirement-consistency-metadata.md
  python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings --report-md /tmp/v11-consistency-independence.md
  git diff --check
  ```

- [x] **Step 5: Leave only this verified package as the next uncommitted scope.**

  ```bash
  git diff --check
  git status --short
  ```

---

### Task 4: Implement `requirement-conflict-detection`

**Files:**
- Create: `skills/zh/testing-types/requirement-conflict-detection/{SKILL.md,prompts/requirement-conflict-detection.md,agents/openai.yaml,evals/eval.yaml}`
- Create: `skills/zh/testing-types/requirement-conflict-detection/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: matching files under `skills/en/testing-types/requirement-conflict-detection/`

**Interfaces:**
- Consumes: multiple requirement, acceptance, rule, contract, configuration, or versioned artifacts with source identity and applicability scope where available.
- Produces: conflict pairs with both statements, source evidence, affected scope, conflict type, impact, priority, missing precedence rule, decision owner, and validation plan.
- Boundary: reports conflicts and decision needs; never chooses precedence, assigns risk acceptance, declares the final business rule, or claims a defect without evidence.

- [x] **Step 1: Write the cases first.**

  - `basic-success`: one source says “guest checkout is allowed”; another says “login is required before checkout”; require both statements, `conflict` status, P0/P1 impact, and a suggested decision owner.
  - `edge-incomplete-input`: one rule is supplied with no scope/version/owner; require a provisional missing-precedence finding and questions, not a conflict invented from absent evidence.
  - `edge-scope-boundary`: a product note says “may” while a legal rule says “must not”; keep the difference source-attributed and the final decision Human-owned.

- [x] **Step 2: Validate and dry-run.**

  ```bash
  skill-up validate skills/zh/testing-types/requirement-conflict-detection/evals/eval.yaml
  skill-up validate skills/en/testing-types/requirement-conflict-detection/evals/eval.yaml
  skill-up run skills/zh/testing-types/requirement-conflict-detection/evals/eval.yaml --dry-run
  skill-up run skills/en/testing-types/requirement-conflict-detection/evals/eval.yaml --dry-run
  ```

- [x] **Step 3: Write the bilingual package.**

  The Prompt requires `conflict ID`, both statements and sources, applicability, conflict type, evidence, impact, priority, decision needed, suggested owner, validation method, and unknowns. Use `RF-##` IDs, distinguish `conflict` from `ambiguous` and `missing`, and explicitly forbid resolving on behalf of a Human.

- [x] **Step 4: Run metadata, independence, and boundary checks; inspect that no output silently selects the stronger-sounding rule.**

  ```bash
  python3 scripts/validate_agents_metadata.py --report /tmp/v11-requirement-conflict-metadata.md
  python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings --report-md /tmp/v11-conflict-independence.md
  git diff --check
  ```

- [x] **Step 5: Leave only this verified package as the next uncommitted scope.**

  ```bash
  git diff --check
  git status --short
  ```

---

### Task 5: Implement `requirement-traceability-analysis`

**Files:**
- Create: `skills/zh/testing-types/requirement-traceability-analysis/{SKILL.md,prompts/requirement-traceability-analysis.md,agents/openai.yaml,evals/eval.yaml}`
- Create: `skills/zh/testing-types/requirement-traceability-analysis/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: matching files under `skills/en/testing-types/requirement-traceability-analysis/`

**Interfaces:**
- Consumes: requirements, acceptance criteria, designs, code/change references, test assets, defects, logs, metrics, or explicitly supplied evidence.
- Produces: bidirectional traceability map with stable IDs, relationship type, coverage state, evidence, orphan/uncovered items, data/environment evidence requirements, risks, and next actions.
- Boundary: relationship types are `direct`, `derived`, `indirect`, `contradictory`, and `missing`; coverage statuses are `complete`, `partial`, `unverified`, `stale`, `unexecuted`, and `unassessed`. A matching name alone cannot prove coverage or execution.

- [x] **Step 1: Write the cases first, using the inspected local external baseline without copying its directory structure.**

  - `basic-success`: requirements `REQ-1/REQ-2`, acceptance `AC-1`, tests `TC-1`, defect `DEF-1`; require bidirectional rows, `partial` or `missing` for the unlinked item, evidence references, and next action.
  - `edge-incomplete-input`: only a requirement and a test name are supplied; require `indirect` as the relationship type and `unverified` as the coverage status, plus a request for the actual artifact/evidence, not claimed coverage.
  - `edge-scope-boundary`: a report says “all passed” but no execution record is supplied; keep the report claim source-attributed and execution evidence `unverified`/`unexecuted`/`unassessed` as supported by the supplied material.

- [x] **Step 2: Validate and dry-run.**

  ```bash
  skill-up validate skills/zh/testing-types/requirement-traceability-analysis/evals/eval.yaml
  skill-up validate skills/en/testing-types/requirement-traceability-analysis/evals/eval.yaml
  skill-up run skills/zh/testing-types/requirement-traceability-analysis/evals/eval.yaml --dry-run
  skill-up run skills/en/testing-types/requirement-traceability-analysis/evals/eval.yaml --dry-run
  ```

- [x] **Step 3: Write the bilingual package.**

  Adapt the inspected `awesome-qa-prompt` baseline into the repository contract. The Prompt requires an input audit, a timeline/model/evidence chain where applicable, a result table with requirement/control, source, linked artifact, relationship type, coverage status, evidence, gap/action, and a self-check. Use `RT-##` IDs and keep relationship types `direct`, `derived`, `indirect`, `contradictory`, `missing` separate from coverage statuses `complete`, `partial`, `unverified`, `stale`, `unexecuted`, `unassessed`.

- [x] **Step 4: Run metadata, independence, and boundary checks; inspect that “all passed” is not upgraded to execution evidence.**

  ```bash
  python3 scripts/validate_agents_metadata.py --report /tmp/v11-requirement-traceability-metadata.md
  python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings --report-md /tmp/v11-traceability-independence.md
  git diff --check
  ```

- [x] **Step 5: Leave only this verified package as the next uncommitted scope.**

  ```bash
  git diff --check
  git status --short
  ```

---

### Task 6: Synchronize Phase 1 governance and navigation

**Files:**
- Create: `docs/governance/PHASE_1_REQUIREMENTS_QUALITY.md`
- Create: `docs/governance/PHASE_1_REQUIREMENTS_QUALITY_EN.md`
- Modify: `skills/zh/README.md`, `skills/en/README.md`
- Modify: `docs/catalog/skills-index.md`, `docs/catalog/skills-index_EN.md`
- Modify: `README.md`, `README_EN.md`
- Modify: `docs/catalog/skills-graph.md`, `docs/catalog/skills-graph_EN.md`
- Modify: `docs/governance/skill-governance-registry.yaml`
- Generated: `docs/generated/skill-inventory.md`, `docs/generated/skill-governance-inventory.md`, `docs/generated/skill-governance-inventory_EN.md`, `docs/SKILL_MATRIX.md`, `docs/SKILL_MATRIX_EN.md`, `docs/SKILL_MATCHING_REGISTER.md`, `docs/SKILL_MATCHING_REGISTER_EN.md`

**Interfaces:**
- Governance source: the registry contains 84 logical bilingual pairs after the additions; each new record points to both packages and all required evidence files.
- Generated views: `generate_skill_governance_matrix.py`, `generate_skill_governance_inventory.py`, and `generate_skill_inventory.py` remain the only writers for their generated outputs.
- Navigation: each new row appears in Chinese and English discovery/requirements sections and points only to its own directory.

- [x] **Step 1: Add the Phase 1 note before editing generated views.**

  Record the five Project card IDs/titles, the five boundaries, provisional `PROPOSED`/`NEW` match state, the source-only evidence limit, and the five-card `In Progress` status. Add English mirror navigation.

- [x] **Step 2: Add exactly five registry Skill records.**

  Use these exact role sets: `requirement-quality-review` → `[QA, BA, Product, Engineering]`; `requirement-ambiguity-analysis` → `[QA, BA, Product]`; `requirement-consistency-analysis` → `[QA, BA, Engineering]`; `requirement-conflict-detection` → `[QA, BA, Product, Engineering]`; `requirement-traceability-analysis` → `[QA, BA, Engineering]`. For every slug use `section: testing-types`, `virtual_domain: Engineering QA`, `sdlc_stage: requirements`, `status: Planned-P0`, `priority: P0`, `quality_score.state: NOT_SCORED`, `eval_execution.state: NOT_RUN`, and evidence paths for the eight required bilingual files. `inputs`, `outputs`, `related`, and `workflow` name only actual package files or Skill names.

- [x] **Step 3: Add exactly five registry candidate records.**

  Each exact slug uses `decision_state: PROPOSED`, `conclusion: NEW`, concrete `scope`, `non_goals`, six non-empty evidence fields, `target` equal to its slug, and target evidence paths covering both language `SKILL.md` and Prompt files. If a package boundary proves existing coverage, change the record to the evidenced conclusion before generation.

- [x] **Step 4: Update bilingual navigation and graph composition.**

  Add five rows under discovery/requirements in every README and index. Add a graph composition with `requirement-quality-review` as an optional overview before `requirements-analysis` and the four specialists as optional focused checks; state that the order is optional and links are navigation, not dependencies.

- [x] **Step 5: Generate and validate all governance outputs.**

  ```bash
  python3 scripts/generate_skill_inventory.py
  python3 scripts/generate_skill_governance_inventory.py
  python3 scripts/generate_skill_governance_matrix.py
  python3 scripts/generate_skill_governance_inventory.py --check
  python3 scripts/generate_skill_governance_matrix.py --check
  ```

  Expected counts are 168 physical Skill directories and 84 logical bilingual pairs. Any mismatch, missing evidence path, or stale generated file is a failure to fix before proceeding.

- [x] **Step 6: Commit governance and navigation as one scoped commit.**

  ```bash
  git add docs/governance/PHASE_1_REQUIREMENTS_QUALITY.md docs/governance/PHASE_1_REQUIREMENTS_QUALITY_EN.md docs/governance/skill-governance-registry.yaml docs/generated docs/SKILL_MATRIX.md docs/SKILL_MATRIX_EN.md docs/SKILL_MATCHING_REGISTER.md docs/SKILL_MATCHING_REGISTER_EN.md docs/catalog README.md README_EN.md skills/zh/README.md skills/en/README.md
  git commit -m "feat(governance): register v1.1 requirement quality skills"
  ```

---

### Task 7: Run the complete delivery gate and verify Project state

**Files:**
- Test: all changed files from Tasks 1–6; no additional product files.

- [x] **Step 1: Run focused structural checks.**

  ```bash
  python3 scripts/validate_agents_metadata.py --report /tmp/v11-final-metadata.md
  python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings --report-md /tmp/v11-final-independence.md
  python3 scripts/validate_skills_integrity.py --fail-on-findings --report-md /tmp/v11-final-integrity.md
  bash scripts/validate_skill_evals.sh
  ```

- [x] **Step 2: Run the repository gate and whitespace check.**

  ```bash
  bash scripts/check_skills_quality.sh
  git diff --check HEAD~1
  ```

  Read complete output and record exit code, physical directory count, logical pair count, metadata findings, independence findings, integrity findings, and Eval YAML failures. Do not call a model Eval passed without a real `skill-up run` report.

- [x] **Step 3: Verify the five Project cards without changing other cards.**

  ```bash
  gh project item-list 4 --owner naodeng --format json --limit 200 \
    | jq -r '.items[] | select(.title | test("^v1\\.1 P0")) | [.id,.status,.title] | @tsv'
  ```

  Expected: the first five named slugs are `In Progress`; the sixth and later v1.1 cards remain `Todo`.

- [x] **Step 4: Inspect Git state and report boundaries.**

  ```bash
  git status --short --branch
  git log --oneline --decorate -8
  ```

  Confirm no push occurred, no unrelated files were staged, and all commits are on `develop`. Report model/runtime Eval state separately from static gate results.
