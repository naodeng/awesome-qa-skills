<div align="right"><strong>🇨🇳 中文</strong></div>

# v2.0 Test Engineering 两批 Skill 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`[ ]`) syntax for tracking.

**Goal:** 在已合入 `origin/main` 的 `develop` 上，将 Project #4 的 25 张 v2 P1 Skill 卡片分两批实现为独立双语 Skill 包，并完成治理同步与证据边界验收。

**Architecture:** 每张卡片对应 `skills/zh/testing-types/<slug>/` 和 `skills/en/testing-types/<slug>/` 两个独立包。包内只使用 Markdown、YAML、CSV 和 JSON 描述输入审计、发现合同、Eval 和触发样本；不引入跨 Skill 内部链接、运行时代码或外部服务。Batch 1 先交付 9 个测试设计方法，Batch 2 再交付 16 个 API/UI/测试质量能力。

**Tech Stack:** Markdown、YAML、CSV、JSON、Python 3 标准库、`unittest`、`skill-up validate`、现有治理生成器、GitHub Project CLI 和 `bash scripts/check_skills_quality.sh`。

**Spec:** `docs/superpowers/specs/2026-09-15-v2-test-engineering-two-batch-design.md`

## Global Constraints

- 当前基线是本地 `develop` 的 `d63a9fa`；该提交已快进包含 `origin/main`，不 push。
- Batch 1 精确卡片为：`decision-table-testing`、`state-transition-testing`、`boundary-value-testing`、`equivalence-partitioning`、`pairwise-testing`、`combinatorial-testing`、`model-based-testing`、`property-based-testing`、`metamorphic-testing`。
- Batch 2 精确卡片为：`api-schema-validation`、`api-negative-testing`、`api-idempotency-testing`、`api-pagination-testing`、`api-rate-limit-testing`、`api-version-compatibility-testing`、`api-error-contract-testing`、`ui-test-strategy`、`ui-test-selector-review`、`ui-test-wait-strategy-review`、`visual-regression-testing`、`cross-browser-testing`、`test-code-review`、`mutation-testing-analysis`、`mock-quality-review`、`test-suite-health-analysis`。
- 每个语言包必须有 `SKILL.md`、主 Prompt、`agents/openai.yaml`、`evals/eval.yaml`、三类 case、四模式 trigger CSV 和物理 slug 对齐的 `local-rules.json`。
- Prompt 必须先做 `known`、`missing`、`conflicting`、`stale`、`out_of_scope`、`assumptions` 输入审计，并分离事实、推断、建议与 Human 决策。
- 文件存在、结构检查、dry-run 和本地触发数据不证明真实模型质量、测试执行、兼容性、覆盖、缺陷关闭、审批或发布。
- 每批只移动精确卡片；不移动其他卡片，不创建 Issue，不 push，不发布版本。

---

### Task 1: 建立 Batch 1 合同测试并观察 RED

**Files:**

- Create: `scripts/tests/test_v20_batch1_skill_contracts.py`
- Read-only reference: `scripts/tests/test_v11_ten_quality_skill_contracts.py`
- Read-only reference: `scripts/validate_skills_integrity.py`

**Interfaces:**

- Consumes: Batch 1 的 9 个 slug 和统一包结构。
- Produces: 对每个语言、每个 slug 的物理目录、metadata、Eval、三类 case、四模式 CSV 和 local rules 的可重复合同测试。
- Boundary: 只证明静态结构与文案标记，不执行真实模型或目标系统。

- [ ] **Step 1: 写失败合同测试。**

  测试 `BATCH_1` 的精确 slug 集合；每个 `skills/{zh,en}/testing-types/<slug>/` 都必须包含 `SKILL.md`、`prompts/<slug>.md`、`agents/openai.yaml`、`evals/eval.yaml`、三类 case、`trigger-prompts.csv` 和 `local-rules.json`。测试 frontmatter `name`、metadata key、YAML case 引用、四种 trigger mode、正反向触发样本和 `local-rules.json.skill` 的物理目录一致性，并要求每个 Prompt 含该 Skill 的专属稳定 ID 前缀。

- [ ] **Step 2: 运行单一合同测试确认 RED。**

  ```bash
  python3 -m unittest scripts.tests.test_v20_batch1_skill_contracts -v
  ```

  预期：因 9 个双语目录不存在而失败；若错误来自测试拼写或导入问题，先修测试后重新确认目标缺失导致的 RED。

- [ ] **Step 3: 检查 RED 期间的范围。**

  ```bash
  git diff --check
  git status --short
  ```

  只保留本计划和合同测试新增内容，不撤销已存在改动。

### Task 2: 移动 Batch 1 卡片到 `In Progress`

**Files:**

- External state: GitHub Project #4 items `PVTI_lAHOAHP1as4BjBhVzg6ScMA`、`PVTI_lAHOAHP1as4BjBhVzg6ScNk`、`PVTI_lAHOAHP1as4BjBhVzg6ScPM`、`PVTI_lAHOAHP1as4BjBhVzg6ScQ8`、`PVTI_lAHOAHP1as4BjBhVzg6ScSQ`、`PVTI_lAHOAHP1as4BjBhVzg6ScUU`、`PVTI_lAHOAHP1as4BjBhVzg6ScW0`、`PVTI_lAHOAHP1as4BjBhVzg6ScZs`、`PVTI_lAHOAHP1as4BjBhVzg6SccE`
- Read-only reference: Project #4 Status field `PVTSSF_lAHOAHP1as4BjBhVzhh3bSA`, option `47fc9ee4` (`In Progress`)

- [ ] **Step 1: 确认 RED 后逐张更新状态。**

  对上述 9 个 Project item 使用 `gh project item-edit --project-id PVT_kwHOAHP1as4BjBhV --id <item-id> --field-id PVTSSF_lAHOAHP1as4BjBhVzhh3bSA --single-select-option-id 47fc9ee4`。

- [ ] **Step 2: 重新读取 Project #4，确认只有这 9 张 v2 卡片变为 `In Progress`。**

  ```bash
  gh project item-list 4 --owner naodeng --format json --limit 200
  ```

### Task 3: 实现 Batch 1 的 9 个双语 Skill 包

**Files:**

- Create under `skills/zh/testing-types/`: `decision-table-testing`、`state-transition-testing`、`boundary-value-testing`、`equivalence-partitioning`、`pairwise-testing`、`combinatorial-testing`、`model-based-testing`、`property-based-testing`、`metamorphic-testing`。
- Create matching packages under `skills/en/testing-types/`.

**Interfaces:**

- Consumes: 对应测试方法的需求、规则、状态、字段、因素、模型或参考关系材料。
- Produces: 专属稳定 ID、证据来源、选择理由、未知项、验证建议和 Human 待决问题。
- Boundary: 不生成已执行结果，不宣称覆盖/通过，不替代通用测试策略或目标系统执行。

- [ ] **Step 1: 为每个 slug 写三类 Eval、四模式 trigger CSV 和 local rules。**
- [ ] **Step 2: 运行 18 个 `skill-up validate`，确认配置可加载。**
- [ ] **Step 3: 写中英文 SKILL、主 Prompt 和 metadata，保持目录 slug、frontmatter name 和 metadata key 一致。**
- [ ] **Step 4: 运行 Batch 1 合同测试、目标 dry-run/规则检查和 `git diff --check`。**

  ```bash
  python3 -m unittest scripts.tests.test_v20_batch1_skill_contracts -v
  bash scripts/validate_skill_evals.sh
  python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings
  git diff --check
  ```

### Task 4: 更新 Batch 1 治理记录并验收卡片

**Files:**

- Modify: `docs/governance/skill-governance-registry.yaml`
- Regenerate: `docs/SKILL_MATRIX.md`, `docs/SKILL_MATRIX_EN.md`, `docs/generated/skill-governance-inventory.md`, `docs/generated/skill-governance-inventory_EN.md`
- Modify: `docs/catalog/skills-index.md`, `docs/catalog/skills-index_EN.md`, `docs/catalog/skills-graph.md`, `docs/catalog/skills-graph_EN.md`, `README.md`, `README_EN.md`

- [ ] **Step 1: 为 9 个 slug 记录 `Planned-P1`、`NOT_SCORED`、`NOT_RUN` 和双语证据路径。**
- [ ] **Step 2: 运行 registry/matrix 生成器并检查只新增 Batch 1。**
- [ ] **Step 3: 运行完整质量门禁。**

  ```bash
  bash scripts/check_skills_quality.sh
  ```

- [ ] **Step 4: 质量门禁和双语差异检查通过后，将上述 9 张卡片移到 `Done`，并再次读取状态验证其他卡片不变。**

### Task 5: 建立 Batch 2 合同测试并观察 RED

**Files:**

- Create: `scripts/tests/test_v20_batch2_skill_contracts.py`

- [ ] **Step 1: 用 Batch 2 的 16 个精确 slug 写同样的结构合同，并增加 API、UI、mutation/mock/test-suite 专属稳定 ID 标记检查。**
- [ ] **Step 2: 运行 `python3 -m unittest scripts.tests.test_v20_batch2_skill_contracts -v`，在实现前确认因目录缺失而 RED。**
- [ ] **Step 3: 运行 `git diff --check` 和 `git status --short`，确认不影响 Batch 1 和其他卡片。**

### Task 6: 移动 Batch 2 卡片到 `In Progress`

**Files:**

- External state: Project #4 中标题分别为 `v2 P1｜候选 Skill｜<slug>` 的 16 个精确 item；以最新 `gh project item-list` 返回的 item ID 为准。
- Read-only reference: Project #4 Status field `PVTSSF_lAHOAHP1as4BjBhVzhh3bSA`, option `47fc9ee4` (`In Progress`)

- [ ] **Step 1: 只在 Batch 2 RED 已确认后更新这 16 张卡片到 `In Progress`。**
- [ ] **Step 2: 重新读取并核对 Batch 1 为 `Done`、Batch 2 为 `In Progress`、其他卡片状态未改变。**

### Task 7: 实现 Batch 2 的 16 个双语 Skill 包

**Files:**

- Create under `skills/zh/testing-types/`: `api-schema-validation`、`api-negative-testing`、`api-idempotency-testing`、`api-pagination-testing`、`api-rate-limit-testing`、`api-version-compatibility-testing`、`api-error-contract-testing`、`ui-test-strategy`、`ui-test-selector-review`、`ui-test-wait-strategy-review`、`visual-regression-testing`、`cross-browser-testing`、`test-code-review`、`mutation-testing-analysis`、`mock-quality-review`、`test-suite-health-analysis`。
- Create matching packages under `skills/en/testing-types/`.

**Interfaces:**

- Consumes: API contract/spec/response examples, UI behavior/locator/wait/browser evidence, test source/reports/mutation or mock configuration and suite history.
- Produces: 专属稳定发现、证据状态、影响、责任角色、关闭条件和最小验证动作。
- Boundary: 不调用真实 API/浏览器/数据库/变异运行器，不把静态审查变成执行或质量分。

- [ ] **Step 1: 为每个 slug 写三类 Eval、四模式 trigger CSV 和 local rules。**
- [ ] **Step 2: 运行 32 个 `skill-up validate`。**
- [ ] **Step 3: 写 32 个双语入口、Prompt 和 metadata，保持各领域边界清晰。**
- [ ] **Step 4: 运行 Batch 2 合同测试、Eval 配置验证、独立性检查和 `git diff --check`。**

### Task 8: 更新 Batch 2 治理记录并完成两批验收

**Files:**

- Modify: `docs/governance/skill-governance-registry.yaml`
- Regenerate: `docs/SKILL_MATRIX.md`, `docs/SKILL_MATRIX_EN.md`, `docs/generated/skill-governance-inventory.md`, `docs/generated/skill-governance-inventory_EN.md`
- Modify: `docs/catalog/skills-index.md`, `docs/catalog/skills-index_EN.md`, `docs/catalog/skills-graph.md`, `docs/catalog/skills-graph_EN.md`, `README.md`, `README_EN.md`

- [ ] **Step 1: 为 Batch 2 记录 16 个 `Planned-P1` 条目，保留 `NOT_SCORED`/`NOT_RUN` 边界。**
- [ ] **Step 2: 重新生成治理视图，检查中英文条目、物理路径和数量一致。**
- [ ] **Step 3: 运行完整质量门禁、全仓 unittest 和 `git diff --check`。**

  ```bash
  python3 -m unittest discover -s scripts/tests -v
  bash scripts/check_skills_quality.sh
  git diff --check
  ```

- [ ] **Step 4: 证据通过后将 Batch 2 的 16 张卡片移到 `Done`，再读取 Project #4 做最终范围核对。**
- [ ] **Step 5: 汇报本地 `develop` 合入 SHA、两批卡片状态、文件/包数量、验证命令、未运行的真实模型 Eval 和未 push 的事实。**

