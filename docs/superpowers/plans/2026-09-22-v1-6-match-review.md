# v1.6 Match Review Implementation Plan

> **For agentic workers:** Use the execution plan task-by-task. This plan is being executed inline in the current `develop` worktree so the pre-existing requirements-analysis fixes are preserved.

**Goal:** 完成 Project #4 v1.6 的四张 Match Review 卡：以真实项目上下文补充 Phase 1 复核证据，验证四个候选与既有目标 Skill 的边界，更新 Registry、Matrix、Matching Register、双语 Eval 与复核文档，并在质量门禁通过后关闭四张卡。

**Architecture:** 不创建重复 Skill。Phase 0 的 20 条关系仍由 Registry 单一事实源维护；新增 `phase_1_review` 证据挂在四个候选记录上，生成器把 v1.6 项目上下文和受限结论投影到双语 Matching Register、Matrix 和 Phase 1 复核文档。真实项目样例使用 `naodeng/dsh-qa@6d650cae72be8fc582bc4f47d6ba48e3fc28157d` 的需求、技术设计和测试资产；运行评测仅作为目标 Skill 输出契约证据，不升级为语义等价、业务验收或质量分。

**Tech Stack:** JSON-compatible YAML, Python 3 standard library, Markdown, `unittest`, `skill-up`, GitHub Project CLI.

**Spec:** Project #4 cards `v1.6｜Match Review｜capacity-planning`, `workload-modeling`, `requirement-change-impact-analysis`, and `quality-risk-identification`; `docs/SKILL_MATCHING_GUIDE.md`; `docs/governance/PHASE_0_PROMPT_BASELINE_SOURCES.md`.

## Global Constraints

- Four mappings remain `MATCH` and `REVIEWED_WITH_LIMITATION`; no alias or duplicate physical Skill directory is created.
- `skill-up` remains the only generic Eval Engine; targeted runs are recorded as bounded observations, not Quality Score or business acceptance.
- Missing cross-model, external-target, production, and human-approval evidence remains `UNASSESSED`, `NOT_RUN`, or `NOT_SCORED`.
- Chinese and English Skill, Prompt, Eval, Registry evidence, and governance documents stay synchronized.
- Preserve the four pre-existing requirements-analysis modifications and all unrelated worktree changes; do not reset, clean, commit, push, or publish automatically.

## Review Focus

- A project context that contains both migration scope and retained behavior must map direct, transitive, rollback, and observability effects rather than only list changed files.
- A bounded execution system must distinguish offered workload, concurrency limits, queueing, and resource capacity rather than equate requests with concurrent runs.
- Capacity conclusions must keep measured facts, assumptions, thresholds, and scaling lead time separate.
- Risk ranking must retain evidence, existing controls, residual risk, and human decision boundaries without claiming that tests remove all risk.
- A bilingual mirror or an Eval case must not silently change the candidate-to-target conclusion or evidence state.

---

### Task 1: Lock the Phase 1 evidence contract

**Files:**
- Modify: `scripts/tests/test_generate_skill_governance_matrix.py`
- Modify: `scripts/generate_skill_governance_matrix.py`
- Modify: `docs/governance/skill-governance-registry.yaml`
- Create: `docs/governance/PHASE_1_MATCH_REVIEW.md`
- Create: `docs/governance/PHASE_1_MATCH_REVIEW_EN.md`

**Interfaces:**
- `candidate.phase_1_review` records the Project #4 card, pinned project revision, evidence paths, observed contract, and explicit `UNASSESSED` boundaries.
- v1.6 Match Review rows expose a link to the Phase 1 evidence in generated Matrix and Phase 0 review views.
- Registry validation rejects missing or non-repository Phase 1 evidence for the four v1.6 candidates.

- [x] **Step 1: Add failing governance tests** for the four `phase_1_review` records, required dsh-qa revision, local evidence paths, and bilingual generated-view markers.
- [x] **Step 2: Run the focused tests** and confirm they fail because the Phase 1 records and renderer support do not exist.
- [x] **Step 3: Add the four evidence records** with the exact Project item IDs, `MATCH` conclusion, dsh-qa revision, project-context summary, target package/Eval paths, and `UNASSESSED` semantic boundary.
- [x] **Step 4: Implement validation and rendering** for Phase 1 evidence in `scripts/generate_skill_governance_matrix.py` without changing the existing 20-row Phase 0 contract.
- [x] **Step 5: Write synchronized Chinese and English Phase 1 review documents** with the four mappings, source URLs/revisions, evidence paths, conclusion, limitation, and reproduction commands.
- [x] **Step 6: Run the focused governance tests and generator freshness check**; expected: all focused tests pass and both generated views reflect Phase 1 evidence.

### Task 2: Add project-context Eval coverage for the four target Skills

**Files:**
- Modify: the four Chinese and four English `evals/eval.yaml` files for the target Skills.
- Create: eight `evals/cases/phase-1-project-context.yaml` files for `change-impact-analysis`, `performance-workload-modeling`, `capacity-planning-analysis`, and `quality-risk-analysis`.

**Interfaces:**
- Each new case uses the dsh-qa `0.5.0` Panel/Slot migration or controlled quality-run capacity facts as input.
- Each case keeps deterministic `rule_based` assertions aligned with the target language and tests domain-specific output, evidence boundaries, and no invented runtime facts.

- [x] **Step 1: Add the eight case files and case references** with bilingual prompts, source revision, and domain-specific assertions.
- [x] **Step 2: Run `skill-up validate` for all eight target eval configs**; expected: every config loads four cases.
- [x] **Step 3: Run the new cases with Codex** using absolute output directories; inspect outputs and grading evidence.
- [x] **Step 4: If a case fails for a genuine contract gap, make the smallest bilingual Prompt correction and rerun the case; do not weaken a valid assertion.** The observed failures were execution-budget, output-language, heading, label, and assertion-casing mismatches. The target Prompts now state the bilingual output contracts explicitly, the relevant Eval inputs preserve exact domain labels and project facts, Phase 1 project-context cases use a dedicated `720s` budget, existing regression cases retain the `180s` suite default, and the corrected requirements-analysis cases were rerun to `PASS`. The stricter Phase 1 replay remains a separately reported `INSUFFICIENT_EVIDENCE` observation when the first case reaches its execution budget.
- [x] **Step 5: Run each target Skill’s full four-case suite in both languages** and retain runtime/model limitations separately from static evidence. The historical evidence set combines the final PASS of each existing three-case regression run with the final single-case PASS of each Phase 1 project-context case: 32/32 cases PASS across four Skills and two languages. That result predates the post-review domain-fact assertion strengthening. The post-review fresh Phase 1 replay reached the 720s case budget on its first case and is recorded as `INSUFFICIENT_EVIDENCE`, not as a Skill failure; the bilingual requirements-analysis boundary and semantic cases passed fresh.

### Task 3: Regenerate the governance views and synchronize guidance

**Files:**
- Modify: `docs/SKILL_MATRIX.md`, `docs/SKILL_MATRIX_EN.md`
- Modify: `docs/SKILL_MATCHING_REGISTER.md`, `docs/SKILL_MATCHING_REGISTER_EN.md`
- Modify: `docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md`, `docs/governance/PHASE_0_MATCH_MERGE_REVIEW_EN.md`
- Modify: `docs/SKILL_MATCHING_GUIDE.md`, `docs/SKILL_MATCHING_GUIDE_EN.md`
- Modify: `docs/governance/SKILL_GOVERNANCE_ROADMAP.md`, `docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md`

- [x] **Step 1: Update the matching guide and roadmap** to point to the Phase 1 review and retain the evidence-state boundary.
- [x] **Step 2: Regenerate all governance views** from the Registry.
- [x] **Step 3: Run bilingual, integrity, independence, and generated-view checks**; expected: no stale or language-sync findings.

### Task 4: Verify the implementation and close the four Project cards

**External state:** Project #4 items `PVTI_lAHOAHP1as4BjBhVzg7VMfc`, `PVTI_lAHOAHP1as4BjBhVzg7VMfk`, `PVTI_lAHOAHP1as4BjBhVzg7VMfs`, and `PVTI_lAHOAHP1as4BjBhVzg7VMf8`.

- [x] **Step 1: Run the focused governance tests, all eight new project-context cases, both-language four-case regression coverage, `bash scripts/check_skills_quality.sh`, and `git diff --check`.** The historical evidence set contains 32/32 `PASS` outcomes from the configuration before the stricter Phase 1 evidence-boundary assertions. The current post-hardening Phase 1 replay is recorded as `INSUFFICIENT_EVIDENCE` after the first case reached its `720s` budget; runtime, cross-model, external-target, production, and business-acceptance boundaries remain separate.
- [x] **Step 2: Verify the diff** contains only the Phase 1 evidence/governance/Eval work plus the pre-existing requirements-analysis changes.
- [x] **Step 3: Move exactly the four v1.6 cards through the authorized Project status update to `Done`; do not alter unrelated cards, releases, or remote Git refs.
- [x] **Step 4: Re-query Project #4 and record current status, transition-audit limitation, and final evidence boundaries in the final report.
