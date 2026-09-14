<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-09-14-v1-1-requirements-quality-skills_EN.md">🇬🇧 English</a></div>

# v1.1 前五个需求质量 Skill 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 `develop` 上创建并验证 v1.1 P0 前五个需求质量 Skill 的中英文独立包，并同步 Project、目录、治理和生成视图。

**Architecture:** 五个 Skill 分别承担总览质量评审、歧义、一致性、冲突和可追踪性；每个包有自己的 Prompt 与 Eval，不共享运行时代码。所有包使用统一的输入审计、来源、状态、风险优先级、证据和人工决策边界，再由治理 registry 交叉验证物理目录并生成 Matrix、Matching Register 与库存。

**Tech Stack:** Markdown、YAML、Bash、Python 3 标准库、`skill-up validate/run`、仓库现有质量门禁和 GitHub Project CLI。

**Spec:** `docs/superpowers/specs/2026-09-14-v1-1-requirements-quality-skills-design.md`

## Global Constraints

- 只新增这五个 logical Skill 的中英文目录，共 10 个目录；不修改现有 `requirements-analysis` 或 `requirements-analysis-plus` 的行为。
- 每个包必须包含 `SKILL.md`、`prompts/<slug>.md`、`agents/openai.yaml`、`evals/eval.yaml`，以及 `basic-success`、`edge-incomplete-input`、`edge-scope-boundary` 三类 case。
- `SKILL.md` frontmatter 的 `name`、目录名、`agents/openai.yaml` 的 `metadata.key` 和中英文版本必须一致；description 以 `Use when...` 开头并只描述触发条件。
- Prompt 必须先做 `known/missing/conflicting/stale/out_of_scope/assumptions` 输入审计；事实、推断、建议和 Human decision 分开；不编造阈值、字段、接口、环境、责任人、根因、执行结果或审批结果。
- Project #4 仅保持这五张卡片为 `In Progress`；不改变其他卡片，不创建 GitHub Issue，不 push，不发布版本。
- 不在 Skill 内用相对路径链接其他 Skill 的内部文件；推荐组合只写 Skill 名称或外部 URL。
- 没有真实模型执行证据时，registry 的 `quality_score` 保持 `NOT_SCORED`，`eval_execution` 保持 `NOT_RUN`；结构门禁通过不等于运行效果通过。
- 每个 Skill 完成自己的 RED/GREEN/REFACTOR 检查后才能进入下一个；不以一次批量生成代替逐项验证。
- 仓库 pre-commit 门禁会把物理目录与 registry 全局交叉校验，因此 Task 1–5 只逐项验证并保持改动可审查；不在 registry 尚未同步时提交单个包，所有包与治理记录在 Task 6 原子提交。

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
- Consumes: one or more supplied requirement artifacts, acceptance criteria, context, constraints, risks, and evidence.
- Produces: an input audit; a quality-dimension table for completeness, clarity, verifiability, feasibility, scope, and evidence quality; prioritized findings; specialist routing suggestions; assumptions and human decisions.
- Boundary: it summarizes and routes; it does not run the four specialist Skills, assign a numeric score, or make a release decision.

- [ ] **Step 1: Write the three failing/boundary cases first.**

  - `basic-success`: order requirement says points may offset payment, but only “offset succeeds” is specified; require findings for missing insufficient-points and callback-retry behavior, plus `P0/P1` priority and specialist routing.
  - `edge-incomplete-input`: input is only “the new release adds points redemption”; require a usable draft, `known`, `missing`, `assumptions`, and 3–5 closeable questions instead of refusal.
  - `edge-scope-boundary`: user asks for a numeric “quality score” and Go/No-Go from one paragraph; require evidence-bounded findings, no numeric score, and an explicit Human decision boundary.

  Each Chinese case must assert `输入审计`, `假设` or `信息缺口`, and `待确认`; each English case must assert `input audit`, `assumption` or `gap`, and `open question`. Boundary cases must reject unsupported release/score claims.

- [ ] **Step 2: Run `skill-up validate` on both new `eval.yaml` files and record the baseline.**

  Expected before package files exist: validation may report the missing skill layout; after the case files and package structure are added it must return exit code 0. Do not call YAML validation a behavior pass.

- [ ] **Step 3: Write the minimum bilingual package.**

  Use these exact frontmatter identities:

  ```yaml
  ---
  name: requirement-quality-review
  description: Use when a requirement, acceptance-criteria set, or change brief needs an evidence-bounded quality review before design or testing; triggers include requirement quality review and requirements quality gate.
  ---
  ```

  The Prompt must contain the headings `输入审计与范围` / `Input Audit and Scope`, `质量维度`, `结构化发现`, `专项路由与下一步`, and `自检` (English equivalents in the English Prompt). The result must use `RQ-##` finding IDs and distinguish `missing`, `ambiguous`, `untestable`, `conflict`, and `unassessed`.

  `agents/openai.yaml` must set `metadata.key` to `requirement-quality-review`, a bilingual display name, a short description under 160 characters, a default prompt naming the Skill, and `allow_implicit_invocation: true`.

- [ ] **Step 4: Validate and review behavior.**

  Run:

  ```bash
  skill-up validate skills/zh/testing-types/requirement-quality-review/evals/eval.yaml
  skill-up validate skills/en/testing-types/requirement-quality-review/evals/eval.yaml
  skill-up run skills/zh/testing-types/requirement-quality-review/evals/eval.yaml --dry-run
  skill-up run skills/en/testing-types/requirement-quality-review/evals/eval.yaml --dry-run
  python3 scripts/validate_agents_metadata.py --report /tmp/v11-requirement-quality-metadata.md
  ```

  If a configured Agent Engine is available, run the three cases in both languages and inspect the actual reports. Otherwise record execution as `NOT_RUN`; never infer behavior from `--dry-run`.

- [ ] **Step 5: Refactor only confirmed gaps and leave the verified package ready for the registry sync.**

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
- Consumes: requirement statements, user stories, acceptance criteria, examples, terminology, actors, conditions, and supplied source context.
- Produces: ambiguity findings with the exact phrase, source, missing discriminator, possible readings without selecting one, priority, owner, clarification question, and validation method.
- Boundary: it diagnoses under-specification; it does not classify explicit incompatible statements as ordinary ambiguity and does not invent a default interpretation.

- [ ] **Step 1: Write cases before the Skill.**

  - `basic-success`: “管理员可以在必要时导出订单” with no definition of administrator, necessary condition, scope, format, or timing; require `RA-##` findings for the missing actor/condition/scope and at least one testability impact.
  - `edge-incomplete-input`: a single sentence “支持快速退款”; require a minimum audit and high-value questions, not a fabricated SLA or refund rule.
  - `edge-scope-boundary`: two artifacts explicitly say “refund is immediate” and “refund is processed within 3 business days”; require the output to route this to conflict detection and preserve both sources.

- [ ] **Step 2: Validate the case YAML and run the no-execution dry run.**

  ```bash
  skill-up validate skills/zh/testing-types/requirement-ambiguity-analysis/evals/eval.yaml
  skill-up validate skills/en/testing-types/requirement-ambiguity-analysis/evals/eval.yaml
  skill-up run skills/zh/testing-types/requirement-ambiguity-analysis/evals/eval.yaml --dry-run
  skill-up run skills/en/testing-types/requirement-ambiguity-analysis/evals/eval.yaml --dry-run
  ```

- [ ] **Step 3: Write the bilingual package.**

  The Prompt must require a phrase-level ambiguity table with `source`, `quoted statement`, `ambiguity type`, `missing discriminator`, `possible readings`, `risk/impact`, `clarification question`, `owner`, and `validation method`. It must explicitly forbid choosing a reading or filling in a threshold from common practice. Use `RA-##` IDs and statuses `ambiguous`, `missing`, `untestable`, and `out_of_scope`.

  Use `name: requirement-ambiguity-analysis`, a trigger-only `Use when...` description, matching `agents/openai.yaml`, and no cross-Skill file links.

- [ ] **Step 4: Run validation and, if configured, both-language cases; manually inspect that explicit contradiction is routed rather than resolved.**

  ```bash
  python3 scripts/validate_agents_metadata.py --report /tmp/v11-requirement-ambiguity-metadata.md
  python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings --report-md /tmp/v11-ambiguity-independence.md
  git diff --check
  ```

- [ ] **Step 5: Leave only this verified package as the next uncommitted scope.**

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
- Produces: a comparison matrix for terms, identifiers, formats, states, rules, behavior, and version/time scope; each row has source pair, relation, status, evidence, impact, action, and owner.
- Boundary: `aligned`, `inconsistent`, `missing`, `stale`, and `unassessed` are evidence states; explicit mutual exclusion is handed to conflict detection, not silently normalized.

- [ ] **Step 1: Write the cases first.**

  - `basic-success`: PRD calls the actor `buyer`, API contract calls it `customer`; one source permits `pending → cancelled`, another lists only `pending → paid`; require comparison evidence, not a guessed synonym or normalized state machine.
  - `edge-incomplete-input`: only one short requirement is supplied; require the missing comparison set and a bounded single-source result.
  - `edge-scope-boundary`: two versioned documents differ because one is explicitly for v1 and one for v2; require `stale`/scope qualification and no conflict claim without same-scope evidence.

- [ ] **Step 2: Validate and dry-run the cases.**

  ```bash
  skill-up validate skills/zh/testing-types/requirement-consistency-analysis/evals/eval.yaml
  skill-up validate skills/en/testing-types/requirement-consistency-analysis/evals/eval.yaml
  skill-up run skills/zh/testing-types/requirement-consistency-analysis/evals/eval.yaml --dry-run
  skill-up run skills/en/testing-types/requirement-consistency-analysis/evals/eval.yaml --dry-run
  ```

- [ ] **Step 3: Write the bilingual package.**

  The Prompt must define a stable comparison key and require a table with `topic`, `source A`, `source B`, `relation`, `status`, `evidence`, `scope/version`, `impact`, `question`, `owner`, and `validation method`. It must keep different versions or applicability scopes separate and route explicit mutual exclusion to `requirement-conflict-detection` by Skill name only. Use `RC-##` IDs.

- [ ] **Step 4: Validate metadata, independence, and the package-specific boundary cases; refactor only evidence-backed gaps.**

  ```bash
  python3 scripts/validate_agents_metadata.py --report /tmp/v11-requirement-consistency-metadata.md
  python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings --report-md /tmp/v11-consistency-independence.md
  git diff --check
  ```

- [ ] **Step 5: Leave only this verified package as the next uncommitted scope.**

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
- Produces: conflict pairs with both statements, source evidence, affected scope, conflict type, impact, priority, missing precedence rule, decision owner, and a validation plan.
- Boundary: reports conflicts and decision needs; never chooses precedence, assigns risk acceptance, declares a final rule, or claims a defect without evidence.

- [ ] **Step 1: Write the cases first.**

  - `basic-success`: one source says “guest checkout is allowed”; another says “login is required before checkout”; require both source statements, `conflict` status, P0/P1 impact, and a suggested decision owner.
  - `edge-incomplete-input`: one rule is supplied with no scope/version/owner; require a provisional missing-precedence finding and questions, not a conflict invented from absent evidence.
  - `edge-scope-boundary`: a product note says “may” while a legal rule says “must not”; require the difference to remain source-attributed and the final decision to stay Human-owned.

- [ ] **Step 2: Validate and dry-run.**

  ```bash
  skill-up validate skills/zh/testing-types/requirement-conflict-detection/evals/eval.yaml
  skill-up validate skills/en/testing-types/requirement-conflict-detection/evals/eval.yaml
  skill-up run skills/zh/testing-types/requirement-conflict-detection/evals/eval.yaml --dry-run
  skill-up run skills/en/testing-types/requirement-conflict-detection/evals/eval.yaml --dry-run
  ```

- [ ] **Step 3: Write the bilingual package.**

  The Prompt must require a conflict table containing `conflict ID`, `statement A`, `source A`, `statement B`, `source B`, `applicability`, `conflict type`, `evidence`, `impact`, `priority`, `decision needed`, `suggested owner`, `validation method`, and `what remains unknown`. Use `RF-##` IDs, distinguish `conflict` from `ambiguous` and `missing`, and include an explicit “do not resolve on behalf of Human” rule.

- [ ] **Step 4: Run metadata, independence, and boundary checks; manually inspect that no output silently selects the stronger-sounding rule.**

  ```bash
  python3 scripts/validate_agents_metadata.py --report /tmp/v11-requirement-conflict-metadata.md
  python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings --report-md /tmp/v11-conflict-independence.md
  git diff --check
  ```

- [ ] **Step 5: Leave only this verified package as the next uncommitted scope.**

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
- Consumes: requirements, acceptance criteria, designs, code/change references, test assets, defects, logs, metrics, or other explicitly supplied evidence.
- Produces: bidirectional traceability map with stable IDs, relationship type, coverage state, evidence, orphan/uncovered items, data/environment evidence requirements, risks, and next actions.
- Boundary: distinguishes complete, partial, indirect, missing, stale, and unexecuted evidence; a link or matching name alone cannot prove coverage or execution.

- [ ] **Step 1: Write the cases first, based on the local external baseline without copying its directory structure.**

  - `basic-success`: requirements `REQ-1/REQ-2`, acceptance `AC-1`, tests `TC-1`, defect `DEF-1`; require bidirectional rows, `partial` or `missing` for the unlinked item, source/evidence references, and next action.
  - `edge-incomplete-input`: only a requirement and a test name are supplied; require `indirect`/`unverified` treatment and a request for the actual artifact/evidence, not a claimed covered path.
  - `edge-scope-boundary`: a test report says “all passed” but no execution record is provided; require the report claim to remain source-attributed and execution evidence to be `UNASSESSED`/missing.

- [ ] **Step 2: Validate and dry-run.**

  ```bash
  skill-up validate skills/zh/testing-types/requirement-traceability-analysis/evals/eval.yaml
  skill-up validate skills/en/testing-types/requirement-traceability-analysis/evals/eval.yaml
  skill-up run skills/zh/testing-types/requirement-traceability-analysis/evals/eval.yaml --dry-run
  skill-up run skills/en/testing-types/requirement-traceability-analysis/evals/eval.yaml --dry-run
  ```

- [ ] **Step 3: Write the bilingual package.**

  Adapt the inspected `awesome-qa-prompt` baseline into the repository contract. The Prompt must require `input audit`, a timeline/model/evidence chain where applicable, a result table with requirement/control, source, linked artifact, relationship type, coverage status, evidence, gap/action, and a self-check. Use `RT-##` IDs and keep `complete`, `partial`, `indirect`, `missing`, `stale`, and `not executed` separate.

- [ ] **Step 4: Run metadata, independence, and boundary checks; inspect that “all passed” is not upgraded to execution evidence.**

  ```bash
  python3 scripts/validate_agents_metadata.py --report /tmp/v11-requirement-traceability-metadata.md
  python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings --report-md /tmp/v11-traceability-independence.md
  git diff --check
  ```

- [ ] **Step 5: Leave only this verified package as the next uncommitted scope.**

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
- Governance source: registry has 84 logical bilingual pairs after the five additions; each new record points to both language packages and all required evidence files.
- Generated views: `generate_skill_governance_matrix.py`, `generate_skill_governance_inventory.py`, and `generate_skill_inventory.py` remain the only writers for their generated outputs.
- Navigation: each new row appears in the Chinese and English requirements/discovery sections and points only to its own directory.

- [ ] **Step 1: Add the Phase 1 note before editing generated views.**

  Record the five Project card IDs/titles, the five boundaries, provisional `PROPOSED`/`NEW` match state, the source-only evidence limit, and the five-card `In Progress` status. Add English mirror navigation.

- [ ] **Step 2: Add exactly five registry Skill records.**

  Use these exact role sets: `requirement-quality-review` → `[QA, BA, Product, Engineering]`; `requirement-ambiguity-analysis` → `[QA, BA, Product]`; `requirement-consistency-analysis` → `[QA, BA, Engineering]`; `requirement-conflict-detection` → `[QA, BA, Product, Engineering]`; `requirement-traceability-analysis` → `[QA, BA, Engineering]`. For every slug use `section: testing-types`, `virtual_domain: Engineering QA`, `sdlc_stage: requirements`, `status: Planned-P0`, `priority: P0`, `quality_score.state: NOT_SCORED`, `eval_execution.state: NOT_RUN`, and evidence paths for the eight required bilingual files. The `inputs`, `outputs`, `related`, and `workflow` fields must name only the actual package files or Skill names.

- [ ] **Step 3: Add exactly five registry candidate records.**

  Each candidate uses the exact slug, `decision_state: PROPOSED`, `conclusion: NEW`, a concrete `scope`, `non_goals`, six non-empty evidence fields, `target` equal to its own slug, and `target_evidence_paths` covering its Chinese and English `SKILL.md` and Prompt. If a package boundary proves existing coverage instead, change the record to the evidenced conclusion before generation.

- [ ] **Step 4: Update bilingual navigation and graph composition.**

  Add the five rows under discovery/requirements in every README and index. Add a graph composition showing `requirement-quality-review` as an optional overview before `requirements-analysis`, with the four specialists as optional focused checks; keep the order optional and state that the links are navigation, not dependencies.

- [ ] **Step 5: Generate and validate all governance outputs.**

  ```bash
  python3 scripts/generate_skill_inventory.py
  python3 scripts/generate_skill_governance_inventory.py
  python3 scripts/generate_skill_governance_matrix.py
  python3 scripts/generate_skill_governance_inventory.py --check
  python3 scripts/generate_skill_governance_matrix.py --check
  ```

  Expected structural counts are 168 physical Skill directories and 84 logical bilingual pairs. Any mismatch, missing evidence path, or stale generated file is a failure to fix before proceeding.

- [ ] **Step 6: Commit governance and navigation as one scoped commit.**

  ```bash
  git add docs/governance/PHASE_1_REQUIREMENTS_QUALITY.md docs/governance/PHASE_1_REQUIREMENTS_QUALITY_EN.md docs/governance/skill-governance-registry.yaml docs/generated docs/SKILL_MATRIX.md docs/SKILL_MATRIX_EN.md docs/SKILL_MATCHING_REGISTER.md docs/SKILL_MATCHING_REGISTER_EN.md docs/catalog README.md README_EN.md skills/zh/README.md skills/en/README.md
  git commit -m "feat(governance): register v1.1 requirement quality skills"
  ```

---

### Task 7: Run the complete delivery gate and verify Project state

**Files:**
- Test: all changed files from Tasks 1–6; no additional product files.

- [ ] **Step 1: Run the focused structural checks.**

  ```bash
  python3 scripts/validate_agents_metadata.py --report /tmp/v11-final-metadata.md
  python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings --report-md /tmp/v11-final-independence.md
  python3 scripts/validate_skills_integrity.py --fail-on-findings --report-md /tmp/v11-final-integrity.md
  bash scripts/validate_skill_evals.sh
  ```

- [ ] **Step 2: Run the repository gate and whitespace check.**

  ```bash
  bash scripts/check_skills_quality.sh
  git diff --check HEAD~1
  ```

  Read the complete output and record exit code, physical directory count, logical pair count, metadata findings, independence findings, integrity findings, and Eval YAML failures. Do not call a model Eval passed unless a real `skill-up run` report exists.

- [ ] **Step 3: Verify the five Project cards without changing other cards.**

  ```bash
  gh project item-list 4 --owner naodeng --format json --limit 200 \
    | jq -r '.items[] | select(.title | test("^v1\\.1 P0")) | [.id,.status,.title] | @tsv'
  ```

  Expected: the first five named slugs are `In Progress`; the sixth and later v1.1 cards remain `Todo`.

- [ ] **Step 4: Inspect Git state and report boundaries.**

  ```bash
  git status --short --branch
  git log --oneline --decorate -8
  ```

  Confirm no push occurred, no unrelated files were staged, and all commits are on `develop`. Report model/runtime Eval state separately from static gate results.
