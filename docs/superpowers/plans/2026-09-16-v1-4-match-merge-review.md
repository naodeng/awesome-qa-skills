# v1.4 Match/Merge Review Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 Phase 0 的 20 条典型 Match/Merge/Enhance/Existing 映射固化到 Registry 单一事实源，并生成 Matrix 与双语复核视图。

**Architecture:** `docs/governance/skill-governance-registry.yaml` 新增 `match_reviews` 集合，记录 13 条候选映射和 7 条 Existing 自映射。治理矩阵生成器校验这些关系、将关系摘要注入目标 Skill 的 Related 列，并生成双语 `PHASE_0_MATCH_MERGE_REVIEW` 视图；候选的六项证据仍由 `candidates` 和生成的 Matching Register 提供。

**Tech Stack:** JSON-compatible YAML、Python 3 标准库、Markdown、`unittest`、现有 `check_skills_quality.sh`。

**Spec:** `docs/governance/SKILL_MATCHING_GUIDE.md`、`docs/governance/QA_SKILLS_EVOLUTION_ROADMAP.md`，以及 Project #4 卡 `v1.0｜治理｜典型 Match Merge 映射复核`。

## Global Constraints

- Review 集合固定覆盖 20 条典型映射：13 个候选映射和 7 个 Existing 自映射。
- 只允许 `EXISTING`、`MATCH`、`ENHANCE`、`MERGE`；不得因本卡创建新物理 Skill 目录。
- `REVIEWED_WITH_LIMITATION` 只代表六项证据已结构化定位，不代表语义等价、运行效果、模型 Eval 或发布批准。
- Registry 是关系与候选结论的单一事实源；Matrix、Matching Register 和 Phase 0 复核文档均由生成器产生。
- 保持中文/英文文档结构一致，保留 `NOT_SCORED`、`NOT_RUN`、`UNASSESSED` 边界，不提交或推送 Git。

---

### Task 1: Add the focused mapping contract

**Files:**
- Modify: `docs/governance/skill-governance-registry.yaml`
- Modify: `scripts/generate_skill_governance_matrix.py`
- Modify: `scripts/tests/test_generate_skill_governance_matrix.py`

**Interfaces:**
- `GovernanceRegistry.match_reviews: tuple[dict[str, object], ...]`
- `validate_match_review(review: dict[str, object], physical: set[str], candidates: dict[str, dict[str, object]]) -> list[str]`
- `match_reviews_by_target(registry: GovernanceRegistry) -> dict[str, tuple[dict[str, object], ...]]`

- [x] **Step 1: Add a failing regression test for the exact 20-row review set.** Assert these candidate-to-target mappings and outcomes:

```python
EXPECTED_MATCH_REVIEWS = {
    "requirement-change-impact-analysis": ("MATCH", ("change-impact-analysis",)),
    "test-impact-analysis": ("MERGE", ("change-impact-analysis", "pr-test-impact-analysis")),
    "code-change-risk-analysis": ("MERGE", ("pr-test-impact-analysis",)),
    "workload-modeling": ("MATCH", ("performance-workload-modeling",)),
    "capacity-planning": ("MATCH", ("capacity-planning-analysis",)),
    "performance-bottleneck-analysis": ("EXISTING", ("performance-bottleneck-analysis",)),
    "performance-result-analysis": ("EXISTING", ("performance-result-analysis",)),
    "performance-regression-analysis": ("EXISTING", ("performance-regression-analysis",)),
    "flaky-test-analysis": ("EXISTING", ("flaky-test-analysis",)),
    "production-verification": ("EXISTING", ("production-verification",)),
    "regression-scope-selection": ("MERGE", ("regression-scope-analysis", "regression-test-selection")),
    "ai-test-case-review": ("MATCH", ("ai-generated-test-review",)),
    "ai-log-analysis": ("ENHANCE", ("log-analysis",)),
    "ai-root-cause-analysis": ("ENHANCE", ("root-cause-analysis",)),
    "quality-risk-identification": ("MATCH", ("quality-risk-analysis",)),
    "ai-test-data-generation": ("ENHANCE", ("test-data-generation",)),
    "llm-output-quality-testing": ("ENHANCE", ("llm-testing",)),
    "llm-evaluation": ("MATCH", ("llm-evaluation-design",)),
    "prompt-testing": ("EXISTING", ("prompt-testing",)),
    "agent-tool-testing": ("EXISTING", ("agent-tool-testing",)),
}
```

- [x] **Step 2: Run the focused Matrix test and confirm it fails because the Registry has no `match_reviews` contract.**

```bash
python3 -m unittest scripts.tests.test_generate_skill_governance_matrix.GovernanceMatrixTest.test_repository_match_reviews_cover_the_twenty_roadmap_mappings -v
```

- [x] **Step 3: Add the 20 `match_reviews` records.** Each record must contain `candidate`, `conclusion`, `review_state`, `target_skills`, `evidence_paths`, and `next_action`; candidate rows reference the existing six-field candidate evidence, while Existing rows reference bilingual target package evidence.
- [x] **Step 4: Parse and validate the new records.** Reject duplicate candidates, unknown conclusions/states, empty or non-physical targets, missing evidence paths, and candidate rows whose conclusion or target differs from the existing `candidates` record.
- [x] **Step 5: Run the focused Matrix tests and confirm the exact 20-row contract passes.**

### Task 2: Surface review relationships in generated governance views

**Files:**
- Modify: `scripts/generate_skill_governance_matrix.py`
- Modify: `scripts/tests/test_generate_skill_governance_matrix.py`
- Modify: `docs/SKILL_MATRIX.md`, `docs/SKILL_MATRIX_EN.md`
- Modify: `docs/SKILL_MATCHING_REGISTER.md`, `docs/SKILL_MATCHING_REGISTER_EN.md`

**Interfaces:**
- `render_matrix(registry, locale, root) -> str` uses `match_reviews_by_target()` for target Skill Related summaries.
- `render_match_review(registry, locale) -> str` produces the bilingual focused review document.
- `review_output_path(root: Path, locale: str) -> Path` resolves `docs/governance/PHASE_0_MATCH_MERGE_REVIEW*.md`.

- [x] **Step 1: Add renderer assertions.** Verify target rows expose `MATCH`/`MERGE`/`ENHANCE`/`EXISTING` relationship summaries and both locales render all 20 candidates in the same order and count.
- [x] **Step 2: Implement deterministic target grouping and localized review rendering.** Keep candidate six-field details in the generated Matching Register; the focused view is a generated summary and must link back to the Registry, Matrix, and Register.
- [x] **Step 3: Extend `--check` and the CLI to include the focused bilingual review files.** Preserve existing two Matrix and two Matching Register outputs.
- [x] **Step 4: Regenerate all governance views and run freshness checks.**

```bash
python3 scripts/generate_skill_governance_matrix.py
python3 scripts/generate_skill_governance_matrix.py --check
```

### Task 3: Synchronize matching guidance and phase documentation

**Files:**
- Create: `docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md`
- Create: `docs/governance/PHASE_0_MATCH_MERGE_REVIEW_EN.md`
- Modify: `docs/SKILL_MATCHING_GUIDE.md`, `docs/SKILL_MATCHING_GUIDE_EN.md`
- Modify: `docs/governance/SKILL_GOVERNANCE_ROADMAP.md`, `docs/governance/SKILL_GOVERNANCE_ROADMAP_EN.md`

- [x] **Step 1: Include the generated review scope, 20-row outcome counts, action rules, evidence limits, and no-new-directory boundary in both language views.**
- [x] **Step 2: Document the follow-up order: Deprecation rules, bilingual consistency contract, then Quality Score/minimum Eval standard; each remains a separate Project card.**
- [x] **Step 3: Add reciprocal links from the matching guide and current governance roadmap to the generated review view and reproduction commands.**
- [x] **Step 4: Run the bilingual documentation check.**

```bash
python3 scripts/check_docs_bilingual.py --repo-root .
git diff --check
```

### Task 4: Verify the card and update Project state

**Files:**
- External state: Project #4 card `v1.0｜治理｜典型 Match Merge 映射复核`.
- Read-only reference: Project #4 Status field `PVTSSF_lAHOAHP1as4BjBhVzhh3bSA`, `Done` option `98236657`.

- [x] **Step 1: Run focused tests, the full quality gate, freshness checks, bilingual checks, and `git diff --check`.**
- [x] **Step 2: Confirm only Registry matching data, generator/tests, generated views, and bilingual governance docs changed; no physical Skill package was added, removed, or renamed.**
- [x] **Step 3: Move only this Match/Merge card to `Done`; keep the remaining v1.4 cards in `In Progress`.**
- [x] **Step 4: Re-read Project #4 and report the exact card state and v1.4 counts; keep Draft markers unchanged.**

## Plan self-review

- Task 1 makes the 20-row mapping set auditable and rejects drift against existing candidate evidence.
- Task 2 makes Matrix and the focused review generated views of one Registry source.
- Task 3 keeps the Chinese and English matching guidance synchronized and preserves the evidence boundary.
- Task 4 gates the Project transition on fresh local checks and does not claim runtime effectiveness or release completion.
