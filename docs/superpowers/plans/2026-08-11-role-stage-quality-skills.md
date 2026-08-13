# Role and Stage Quality Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add eight bilingual, independently installable Skills and enhance six existing bilingual Skills so the AI quality MVP can combine stage capabilities, role perspectives, and traceable multi-role synthesis.

**Architecture:** Stage Skills remain complete standalone capabilities. Five role-perspective Skills route an explicit `stage` to a self-contained stage Prompt, and one synthesis Skill combines role Artifacts without creating facts or overwriting disagreements. The consuming project references Skills only by stable key and version and owns its Artifact Schema.

**Tech Stack:** Markdown Agent Skills, YAML `agents/openai.yaml`, skill-up YAML evals, repository Python/Bash quality scripts.

## Global Constraints

- Follow [the approved design](../specs/2026-08-11-role-stage-quality-skills-design.md).
- Create and modify Chinese and English Skill directories together; directory names and `metadata.key` must match.
- Each language directory must be independently installable and must not link to another Skill or the other language directory.
- A stage Prompt must be executable without loading another stage Prompt.
- Require an explicit supported `stage`; return a clear not-applicable result for unsupported stages instead of guessing.
- Stage Skills remain useful without role Skills; role Skills remain useful without stage Skills; composition only enhances output.
- Keep `SKILL.md` concise and route detailed stage instructions to `prompts/`.
- Every new or modified Skill must maintain `evals/eval.yaml` and cases covering success, incomplete input, and scope/risk boundaries.
- Use rule-based judges wherever deterministic content assertions are sufficient.
- Never claim runtime eval success unless `skill-up` actually ran and its output was inspected.
- Do not commit, push, or change Git configuration unless the user explicitly requests it.
- Preserve unrelated worktree changes and stage only task paths if staging is later requested.

---

## File Structure

### New cross-stage workflow Skills

Create under both `skills/zh/testing-workflows/` and `skills/en/testing-workflows/`:

```text
product-quality-perspective/
qa-quality-perspective/
ux-quality-perspective/
technical-quality-perspective/
project-delivery-perspective/
multi-role-quality-synthesis/
```

Every new directory contains:

```text
SKILL.md
agents/openai.yaml
prompts/*.md
evals/eval.yaml
evals/cases/*.yaml
```

### New stage review Skills

Create under both `skills/zh/testing-types/` and `skills/en/testing-types/`:

```text
test-strategy-review/
test-report-review/
```

### Existing Skills to modify

Modify both language variants of:

```text
skills/{zh|en}/testing-types/requirements-analysis-plus/
skills/{zh|en}/testing-types/test-strategy-plus/
skills/{zh|en}/testing-types/code-review/
skills/{zh|en}/testing-types/test-case-writing/
skills/{zh|en}/testing-types/test-case-reviewer-plus/
skills/{zh|en}/testing-types/test-reporting/
```

### Index files to modify

```text
README.md
README_EN.md
skills-index.md
skills/zh/README.md
skills/en/README.md
```

Only modify additional installer or generated index files if repository scripts prove they derive from the new Skill inventory.

---

### Task 1: Add the product quality perspective Skill

**Files:**

- Create: `skills/zh/testing-workflows/product-quality-perspective/SKILL.md`
- Create: `skills/zh/testing-workflows/product-quality-perspective/agents/openai.yaml`
- Create: `skills/zh/testing-workflows/product-quality-perspective/prompts/requirements-analysis.md`
- Create: `skills/zh/testing-workflows/product-quality-perspective/prompts/test-strategy.md`
- Create: `skills/zh/testing-workflows/product-quality-perspective/prompts/test-strategy-review.md`
- Create: `skills/zh/testing-workflows/product-quality-perspective/prompts/code-review.md`
- Create: `skills/zh/testing-workflows/product-quality-perspective/prompts/test-case-writing.md`
- Create: `skills/zh/testing-workflows/product-quality-perspective/prompts/test-case-review.md`
- Create: `skills/zh/testing-workflows/product-quality-perspective/prompts/test-reporting.md`
- Create: `skills/zh/testing-workflows/product-quality-perspective/prompts/test-report-review.md`
- Create: `skills/zh/testing-workflows/product-quality-perspective/evals/eval.yaml`
- Create: `skills/zh/testing-workflows/product-quality-perspective/evals/cases/basic-requirements-analysis.yaml`
- Create: `skills/zh/testing-workflows/product-quality-perspective/evals/cases/edge-incomplete-input.yaml`
- Create: `skills/zh/testing-workflows/product-quality-perspective/evals/cases/edge-role-boundary.yaml`
- Create the exact English mirror under `skills/en/testing-workflows/product-quality-perspective/`.

**Interfaces:**

- Consumes: `stage`, supplied project materials, optional stage context.
- Produces: a standalone product quality report containing summary, facts, evidence, findings, risks, missing information, questions, actions, and confidence.

- [ ] **Step 1: Write the bilingual eval cases first**

  Use case IDs `basic-requirements-analysis`, `edge-incomplete-input`, and `edge-role-boundary`. Assert that the normal case covers user value, business rules, scope, and acceptance criteria; the incomplete case separates facts from gaps; the boundary case refuses to invent code correctness or a test-pass conclusion.

- [ ] **Step 2: Run eval schema validation and confirm the new cases fail because the Skill is absent**

  Run: `bash scripts/validate_skill_evals.sh`

  Expected: failure identifying the missing Skill path or referenced local Skill.

- [ ] **Step 3: Implement the Chinese and English Skill metadata and router**

  `SKILL.md` must validate `stage`, load exactly one matching Prompt, summarize product responsibilities, and return not applicable for unsupported stages. `agents/openai.yaml` must use key `product-quality-perspective` and natural language metadata for each language.

- [ ] **Step 4: Implement all eight independent stage Prompts**

  Each Prompt repeats the stage-specific inputs, product questions, output contract, evidence rules, and boundary rules required to run alone. Conditional stages must first decide applicability and explain a non-applicable result without producing filler findings.

- [ ] **Step 5: Validate the Skill directories**

  Run: `python3 scripts/validate_agents_metadata.py`

  Run: `python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings`

  Run: `python3 scripts/validate_skills_integrity.py --fail-on-findings`

  Expected: all commands exit 0.

---

### Task 2: Add the QA quality perspective Skill

**Files:**

- Create the bilingual directories `skills/{zh|en}/testing-workflows/qa-quality-perspective/`.
- Create in each directory: `SKILL.md`, `agents/openai.yaml`, and `evals/eval.yaml`.
- Create in each `prompts/`: `requirements-analysis.md`, `test-strategy.md`, `test-strategy-review.md`, `code-review.md`, `test-case-writing.md`, `test-case-review.md`, `test-reporting.md`, `test-report-review.md`.
- Create in each `evals/cases/`: `basic-test-strategy.yaml`, `edge-insufficient-evidence.yaml`, `edge-role-boundary.yaml`.

**Interfaces:**

- Consumes: explicit `stage`, declared stage inputs, existing evidence where available.
- Produces: a standalone QA report with testability, coverage, evidence, defect, and quality-risk conclusions.

- [ ] **Step 1: Add bilingual failing eval cases**

  Assert testability and risk-based coverage in the success case, an explicit “not executed or insufficient evidence” result when execution evidence is absent, and refusal to invent product intent or implementation facts in the boundary case.

- [ ] **Step 2: Implement the bilingual router and metadata**

  Require explicit stage selection, support all eight stages, and keep the core boundary that QA cannot infer a pass result without evidence.

- [ ] **Step 3: Implement eight standalone Prompts per language**

  Give each Prompt its own allowed inputs, QA checks, evidence threshold, risk classification, and output structure. Test-report stages must distinguish facts, inference, missing evidence, and recommendations.

- [ ] **Step 4: Run the three structural validators from Task 1**

  Expected: all exit 0 with both language variants present.

---

### Task 3: Add the UI/UX quality perspective Skill

**Files:**

- Create the bilingual directories `skills/{zh|en}/testing-workflows/ux-quality-perspective/`.
- Create in each directory: `SKILL.md`, `agents/openai.yaml`, and `evals/eval.yaml`.
- Create in each `prompts/`: `requirements-analysis.md`, `test-strategy.md`, `test-strategy-review.md`, `code-review.md`, `test-case-writing.md`, `test-case-review.md`, `test-reporting.md`, `test-report-review.md`.
- Create in each `evals/cases/`: `basic-requirements-analysis.yaml`, `edge-no-prototype.yaml`, `edge-not-applicable.yaml`, `edge-role-boundary.yaml`.

**Interfaces:**

- Consumes: explicit `stage`, prototype or UI evidence when supplied, user-flow and product materials.
- Produces: UX findings covering information architecture, interaction states, consistency, responsive behavior, and accessibility.

- [ ] **Step 1: Add bilingual failing eval cases**

  Assert useful UX analysis with a prototype, explicit missing-evidence impact without a prototype, not-applicable output for a backend-only conditional stage, and refusal to invent backend implementation conclusions.

- [ ] **Step 2: Implement the bilingual router and metadata**

  Support all eight stages but mark test strategy, strategy review, code review, case writing, and test reporting as conditional participation.

- [ ] **Step 3: Implement eight standalone Prompts per language**

  Every conditional Prompt must define an applicability test before its analysis procedure. No Prompt may fabricate screens, states, or cross-device behavior absent from evidence.

- [ ] **Step 4: Run the three structural validators from Task 1**

  Expected: all exit 0.

---

### Task 4: Add the technical quality perspective Skill

**Files:**

- Create the bilingual directories `skills/{zh|en}/testing-workflows/technical-quality-perspective/`.
- Create in each directory: `SKILL.md`, `agents/openai.yaml`, and `evals/eval.yaml`.
- Create in each `prompts/`: `requirements-analysis.md`, `test-strategy.md`, `test-strategy-review.md`, `code-review.md`, `test-case-writing.md`, `test-case-review.md`, `test-reporting.md`, `test-report-review.md`.
- Create in each `evals/cases/`: `basic-code-review.yaml`, `edge-missing-code.yaml`, `edge-incomplete-tech-doc.yaml`, `edge-role-boundary.yaml`.

**Interfaces:**

- Consumes: explicit `stage`, declared architecture, API, data, code, security, performance, and observability evidence.
- Produces: technical findings with evidence, impact, severity, missing information, and actions.

- [ ] **Step 1: Add bilingual failing eval cases**

  Assert evidence-backed code findings, a blocked code-review result when no code version or diff exists, qualified conclusions for incomplete technical documentation, and refusal to change product or test facts.

- [ ] **Step 2: Implement the bilingual router and metadata**

  Support all eight stages and make code review explicitly require code identity and reviewable changes.

- [ ] **Step 3: Implement eight standalone Prompts per language**

  Cover architecture, APIs, data, compatibility, security, performance, observability, and maintainability only where relevant to the selected stage.

- [ ] **Step 4: Run the three structural validators from Task 1**

  Expected: all exit 0.

---

### Task 5: Add the project delivery perspective Skill

**Files:**

- Create the bilingual directories `skills/{zh|en}/testing-workflows/project-delivery-perspective/`.
- Create in each directory: `SKILL.md`, `agents/openai.yaml`, and `evals/eval.yaml`.
- Create in each `prompts/`: `test-strategy.md`, `test-strategy-review.md`, `test-report-review.md`.
- Create in each `evals/cases/`: `basic-test-strategy-input.yaml`, `edge-unsupported-stage.yaml`, `edge-quality-fact-override.yaml`.

**Interfaces:**

- Consumes: explicit supported `stage`, schedule, capacity, dependencies, milestones, owners, and action status.
- Produces: project-constraint input or action tracking; never a quality verdict.

- [ ] **Step 1: Add bilingual failing eval cases**

  Assert usable schedule/resource input, clear not-applicable output for unsupported stages, and refusal to rewrite defect, execution, or quality facts even when prompted.

- [ ] **Step 2: Implement the bilingual router and metadata**

  Support only `test-strategy`, `test-strategy-review`, and `test-report-review`. Do not create empty Prompts for the other five stages.

- [ ] **Step 3: Implement three standalone Prompts per language**

  Separate constraints and actions from quality facts using explicit headings and preserve the source of every schedule or ownership statement.

- [ ] **Step 4: Run the three structural validators from Task 1**

  Expected: all exit 0.

---

### Task 6: Add the multi-role quality synthesis Skill

**Files:**

- Create: `skills/zh/testing-workflows/multi-role-quality-synthesis/SKILL.md`
- Create: `skills/zh/testing-workflows/multi-role-quality-synthesis/prompts/multi-role-quality-synthesis.md`
- Create: `skills/zh/testing-workflows/multi-role-quality-synthesis/agents/openai.yaml`
- Create: `skills/zh/testing-workflows/multi-role-quality-synthesis/evals/eval.yaml`
- Create: `skills/zh/testing-workflows/multi-role-quality-synthesis/evals/cases/basic-synthesis.yaml`
- Create: `skills/zh/testing-workflows/multi-role-quality-synthesis/evals/cases/edge-conflicting-findings.yaml`
- Create: `skills/zh/testing-workflows/multi-role-quality-synthesis/evals/cases/edge-missing-optional-role.yaml`
- Create: `skills/zh/testing-workflows/multi-role-quality-synthesis/evals/cases/edge-no-new-facts.yaml`
- Create: `skills/zh/testing-workflows/multi-role-quality-synthesis/evals/cases/edge-pm-override.yaml`
- Create the exact English mirror under `skills/en/testing-workflows/multi-role-quality-synthesis/`.

**Interfaces:**

- Consumes: one or more role reports with `stage`, `source_role`, facts, evidence, findings, risks, gaps, questions, actions, and confidence.
- Produces: a synthesis with source-preserving findings, consensus, disagreements, blockers, open questions, and actions.

- [ ] **Step 1: Add bilingual failing eval cases**

  Use distinct source IDs in fixtures embedded in each prompt. Assert source preservation, conflict visibility, optional-role absence handling, no unsupported new facts, and protection of quality facts from PM input.

- [ ] **Step 2: Implement metadata and the standalone synthesis Prompt**

  Define deterministic merge rules: normalize equivalent findings, retain all source roles, never average severity without explanation, keep minority P0/P1 findings visible, and separate project constraints from quality facts.

- [ ] **Step 3: Add output self-check requirements**

  Require every synthesized finding to reference at least one input source and require an explicit conflict section even when it states that no conflicts exist.

- [ ] **Step 4: Run the three structural validators from Task 1**

  Expected: all exit 0.

---

### Task 7: Add the test strategy review Skill

**Files:**

- Create bilingual directories `skills/{zh|en}/testing-types/test-strategy-review/`.
- Create in each directory: `SKILL.md`, `prompts/test-strategy-review.md`, `agents/openai.yaml`, and `evals/eval.yaml`.
- Create in each `evals/cases/`: `basic-pass.yaml`, `basic-conditional-pass.yaml`, `edge-blocking-gap.yaml`, `edge-incomplete-input.yaml`, `edge-conflicting-input.yaml`.

**Interfaces:**

- Consumes: test strategy plus available role analysis, requirements, technical constraints, and project constraints.
- Produces: AI-assisted review evidence with recommendation `pass`, `conditional_pass`, or `reject`; Human retains final decision.

- [ ] **Step 1: Add bilingual failing eval cases**

  Assert each recommendation, concrete blocking and non-blocking items, ownership, revision requests, and no fabricated final Human approval.

- [ ] **Step 2: Implement the bilingual Skill and Prompt**

  Review business coverage, test depth, feasibility, environments, data, quality gates, dependencies, and explicit exclusions. Clearly label the result as an AI recommendation for Human review.

- [ ] **Step 3: Run the three structural validators from Task 1**

  Expected: all exit 0.

---

### Task 8: Add the test report review Skill

**Files:**

- Create bilingual directories `skills/{zh|en}/testing-types/test-report-review/`.
- Create in each directory: `SKILL.md`, `prompts/test-report-review.md`, `agents/openai.yaml`, and `evals/eval.yaml`.
- Create in each `evals/cases/`: `basic-pass.yaml`, `basic-conditional-pass.yaml`, `edge-insufficient-evidence.yaml`, `edge-hidden-untested-scope.yaml`, `edge-pm-override.yaml`.

**Interfaces:**

- Consumes: test report, execution evidence, defect evidence, tested and untested scope, role reports, and project actions.
- Produces: evidence-consistency review with recommendation `pass`, `conditional_pass`, or `reject`; Human retains final decision.

- [ ] **Step 1: Add bilingual failing eval cases**

  Assert evidence alignment in the pass case, explicit conditions in conditional pass, rejection of false pass claims, visibility of untested scope, and protection from PM fact override.

- [ ] **Step 2: Implement the bilingual Skill and Prompt**

  Enforce the invariant that absent execution and defect evidence yields “not executed or insufficient evidence.” Require contradictions, residual risk, open actions, and source versions in the review.

- [ ] **Step 3: Run the three structural validators from Task 1**

  Expected: all exit 0.

---

### Task 9: Enhance requirements analysis and test strategy composition

**Files:**

- Modify: `skills/{zh|en}/testing-types/requirements-analysis-plus/SKILL.md`
- Modify: `skills/{zh|en}/testing-types/requirements-analysis-plus/prompts/requirements-analysis-plus.md`
- Modify: `skills/{zh|en}/testing-types/requirements-analysis-plus/evals/eval.yaml`
- Create: `skills/{zh|en}/testing-types/requirements-analysis-plus/evals/cases/edge-role-artifact-input.yaml`
- Modify: `skills/{zh|en}/testing-types/test-strategy-plus/SKILL.md`
- Modify: `skills/{zh|en}/testing-types/test-strategy-plus/prompts/test-strategy-plus.md`
- Modify: `skills/{zh|en}/testing-types/test-strategy-plus/evals/eval.yaml`
- Create: `skills/{zh|en}/testing-types/test-strategy-plus/evals/cases/edge-pm-constraint-input.yaml`

**Interfaces:**

- Consumes: optional role reports identified by source role; existing direct inputs remain valid.
- Produces: the existing standalone report plus traceable facts, assumptions, risks, sources, and open questions.

- [ ] **Step 1: Add regression cases before changing Prompts**

  Require role-source preservation for requirements analysis and require PM schedule constraints to remain separate from test quality conclusions in test strategy.

- [ ] **Step 2: Verify existing standalone evals still describe supported behavior**

  Do not weaken or remove basic, incomplete-input, or risk-priority assertions.

- [ ] **Step 3: Add optional composition inputs to both bilingual Skills**

  Keep direct use unchanged. Define role reports as optional declared inputs and require source attribution when their content is used.

- [ ] **Step 4: Run targeted eval validation and structural validators**

  Run: `bash scripts/validate_skill_evals.sh`

  Then run the three validators from Task 1. Expected: all exit 0.

---

### Task 10: Enhance code review and test-case authoring composition

**Files:**

- Modify: `skills/{zh|en}/testing-types/code-review/SKILL.md`
- Modify: `skills/{zh|en}/testing-types/code-review/prompts/code-review.md`
- Modify: `skills/{zh|en}/testing-types/code-review/evals/eval.yaml`
- Create: `skills/{zh|en}/testing-types/code-review/evals/cases/edge-missing-code-version.yaml`
- Modify: `skills/{zh|en}/testing-types/test-case-writing/SKILL.md`
- Modify: `skills/{zh|en}/testing-types/test-case-writing/prompts/test-case-writing.md`
- Modify: `skills/{zh|en}/testing-types/test-case-writing/evals/eval.yaml`
- Create: `skills/{zh|en}/testing-types/test-case-writing/evals/cases/edge-role-source-deduplication.yaml`

**Interfaces:**

- Code review consumes optional role reports but requires identifiable code and changes.
- Test-case writing consumes role scenario candidates and produces a unified case set with `source_role` and requirement traceability.

- [ ] **Step 1: Add bilingual regression cases**

  Make code review block without code identity or diff. Make case writing merge duplicate role suggestions while retaining all contributing roles.

- [ ] **Step 2: Enhance code review without changing its standalone review contract**

  Add explicit code-version blocking and conditional product/UI role input. Preserve severity-ranked, evidence-backed findings.

- [ ] **Step 3: Enhance test-case writing without generating per-role duplicate suites**

  Require one unified case set, source-role attribution, requirement links, and deterministic handling of equivalent scenario candidates.

- [ ] **Step 4: Inspect the `test-case-writing` versus `testcase-writer-plus` boundary**

  Record the result in the changed Prompt or Skill only if it affects routing. Do not merge or rename either Skill in this task.

- [ ] **Step 5: Run targeted eval validation and structural validators**

  Expected: all exit 0.

---

### Task 11: Enhance test-case review and test reporting composition

**Files:**

- Modify: `skills/{zh|en}/testing-types/test-case-reviewer-plus/SKILL.md`
- Modify: `skills/{zh|en}/testing-types/test-case-reviewer-plus/prompts/test-case-reviewer-plus.md`
- Modify: `skills/{zh|en}/testing-types/test-case-reviewer-plus/evals/eval.yaml`
- Create: `skills/{zh|en}/testing-types/test-case-reviewer-plus/evals/cases/edge-human-decision-boundary.yaml`
- Modify: `skills/{zh|en}/testing-types/test-reporting/SKILL.md`
- Modify: `skills/{zh|en}/testing-types/test-reporting/prompts/test-reporting.md`
- Modify: `skills/{zh|en}/testing-types/test-reporting/evals/eval.yaml`
- Create: `skills/{zh|en}/testing-types/test-reporting/evals/cases/edge-no-execution-evidence.yaml`

**Interfaces:**

- Test-case review produces AI findings and a recommendation but never records final Human approval.
- Test reporting produces evidence-qualified quality status and never converts missing execution evidence into pass.

- [ ] **Step 1: Add bilingual regression cases**

  Assert that AI review cannot impersonate Human approval and that missing execution plus defect evidence produces only “not executed or insufficient evidence.”

- [ ] **Step 2: Add multi-role review inputs and Human decision boundary**

  Preserve blockers, high-risk coverage gaps, maintainability findings, and low-value cases as separate categories.

- [ ] **Step 3: Add evidence levels to test reporting**

  Separate confirmed facts, inference, missing evidence, residual risk, and recommendations. Keep existing standalone inputs supported.

- [ ] **Step 4: Run targeted eval validation and structural validators**

  Expected: all exit 0.

---

### Task 12: Update indexes and verify the complete bilingual inventory

**Files:**

- Modify: `README.md`
- Modify: `README_EN.md`
- Modify: `skills-index.md`
- Modify: `skills/zh/README.md`
- Modify: `skills/en/README.md`
- Modify only generated inventory files identified by repository scripts after running them.

**Interfaces:**

- Consumes: the final set of eight new bilingual Skills.
- Produces: discoverable bilingual documentation with accurate names, categories, descriptions, and counts.

- [ ] **Step 1: Run inventory organization before manual index edits**

  Run: `python3 scripts/organize_project_dirs.py`

  Inspect `git diff --name-only`. Accept only changes caused by the new Skill inventory; do not include unrelated rewrites.

- [ ] **Step 2: Update all five human-facing indexes**

  Add six workflow Skills and two testing-type Skills in both languages. Recalculate counts from the filesystem rather than editing remembered totals.

- [ ] **Step 3: Run the full repository quality gate**

  Run: `bash scripts/check_skills_quality.sh`

  Expected: exit 0, including metadata, independence, integrity, eval schema, and external snapshot checks.

- [ ] **Step 4: Run isolated-copy checks for all sixteen new language directories**

  For each new directory, copy only that directory to a temporary root and run the applicable integrity/independence checks against the isolated copy. Confirm no cross-Skill or cross-language file is needed.

- [ ] **Step 5: Run representative skill-up validation**

  Run `skill-up validate` or the repository wrapper for all new `eval.yaml` files if the CLI is available. Record exact `ok` and `fail` counts. If unavailable, report that only repository YAML validation ran.

- [ ] **Step 6: Run representative runtime evals**

  Run these exact representative commands:

  ```bash
  bash scripts/run_skill_eval.sh skills/zh/testing-workflows/product-quality-perspective/evals/eval.yaml --include-case-name basic-requirements-analysis
  bash scripts/run_skill_eval.sh skills/zh/testing-workflows/project-delivery-perspective/evals/eval.yaml --include-case-name edge-unsupported-stage
  bash scripts/run_skill_eval.sh skills/zh/testing-workflows/multi-role-quality-synthesis/evals/eval.yaml --include-case-name edge-conflicting-findings
  bash scripts/run_skill_eval.sh skills/zh/testing-types/test-report-review/evals/eval.yaml --include-case-name edge-insufficient-evidence
  bash scripts/run_skill_eval.sh skills/en/testing-workflows/product-quality-perspective/evals/eval.yaml --include-case-name basic-requirements-analysis
  bash scripts/run_skill_eval.sh skills/en/testing-workflows/multi-role-quality-synthesis/evals/eval.yaml --include-case-name edge-conflicting-findings
  bash scripts/run_skill_eval.sh skills/en/testing-types/test-report-review/evals/eval.yaml --include-case-name edge-insufficient-evidence
  ```

  Record each command and outcome. Do not claim all cases ran if only representatives ran.

- [ ] **Step 7: Perform final static review**

  Run: `git diff --check`

  Run: `rg -n -e 'TBD' -e 'TODO' -e '/Users/' -e 'AI-Quality-Workforce/' skills README.md README_EN.md skills-index.md`

  Expected: no placeholders, local absolute paths, secrets, or project-internal path coupling. Review legitimate angle-bracket documentation matches manually rather than suppressing them silently.

- [ ] **Step 8: Report the final scope without committing**

  Report new and modified paths, Chinese/English parity, quality-gate results, actual skill-up validation/runtime evidence, and any remaining risk. Ask separately before staging, committing, pushing, or opening a PR.
