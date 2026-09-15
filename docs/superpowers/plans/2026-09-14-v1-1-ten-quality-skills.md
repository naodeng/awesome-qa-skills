<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-09-14-v1-1-ten-quality-skills_EN.md">🇬🇧 English</a></div>

# v1.1 十个质量 Skill 统一实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** 在 `develop` 工作区内一次完成上一批 5 个和本批 5 个 v1.1 P0 质量 Skill 的双语包、增强能力、Eval、本地触发规则、治理记录和验证。

**Architecture:** 本计划覆盖 7 个独立新 Skill 和 3 个现有 Skill 增强。新 Skill 各自拥有独立的 `SKILL.md`、主 Prompt、metadata 和 Eval；增强项保留原目录与稳定契约，仅增加业务规则、架构可测试性和覆盖分析模式。所有包共享证据边界，但不共享跨 Skill 的内部文件链接或运行时代码。

**Tech Stack:** Markdown、YAML、CSV、JSON、Python 3 标准库、`skill-up validate/run`、仓库本地 trace runner、GitHub Project CLI 和现有质量门禁。

**Spec:**

- `docs/superpowers/specs/2026-09-14-v1-1-next-five-quality-skills-design.md`
- `docs/superpowers/specs/2026-09-14-v1-1-following-five-quality-skills-design.md`

## Global Constraints

- 本计划一次纳入这 10 个逻辑候选：`business-rule-extraction`、`business-rule-consistency-review`、`technical-design-quality-review`、`architecture-testability-review`、`api-design-quality-review`、`database-design-quality-review`、`observability-design-review`、`error-handling-design-review`、`test-scope-analysis`、`test-coverage-analysis`。
- 仅创建 7 个 `NEW` 逻辑 Skill 的双语目录；`business-rule-consistency-review` 增强 `requirement-consistency-analysis`，`architecture-testability-review` 增强 `testability-analysis`，`test-coverage-analysis` 增强 `requirement-traceability-analysis`，不创建三个重复目录。
- 每个新包必须包含 `SKILL.md`、`prompts/<slug>.md`、`agents/openai.yaml`、`evals/eval.yaml`、`basic-success.yaml`、`edge-incomplete-input.yaml`、`edge-scope-boundary.yaml`、`trigger-prompts.csv` 和 `local-rules.json`；增强包沿用目录并补齐对应三类 Eval 和本地触发数据。
- 增强候选不创建别名目录：本地 `trigger-prompts.csv` 和 `local-rules.json` 放在物理目标 Skill 的 `evals/` 下；JSON 的 `skill` 保持物理目标 slug，CSV 至少包含候选名称或模式短语，用于验证候选模式路由。
- 中英文 `name`、目录名、`agents/openai.yaml` 的 `metadata.key`、Prompt 结构和 Eval 语义必须对等；description 以 `Use when...` 开头，只描述触发条件，不摘要流程。
- 所有 Prompt 先做 `known`、`missing`、`conflicting`、`stale`、`out_of_scope`、`assumptions` 输入审计；事实、证据推断、建议和 Human 决策分开。
- 不把文件存在、名称匹配、设计声明、报告文字或静态门禁升级为执行结果、兼容性通过、质量分、风险接受、Human 批准或 Release 完成。
- 每个 Skill 独立执行 RED → 最小 GREEN → REFACTOR 和目标 Eval 检查；统一计划不等于跳过逐 Skill 证据。
- Project #4 的这 10 张卡片保持 `In Progress`；不改变其他卡片，不创建 Issue，不 push，不发布版本。现有 `requirement-*` 五个 Skill 的未提交修改必须保留。
- 质量 registry 中真实模型执行保持 `NOT_RUN`，质量分保持 `NOT_SCORED`，除非有独立执行证据；本地 trace runner 缺少 `skill.selection` 时只能报告 `BLOCKED`。
- 不提交或推送；所有改动留在当前工作区，除非用户另行授权 Git 交付。

---

### Task 1: 建立十 Skill 合同测试并观察 RED

**Files:**

- Create: `scripts/tests/test_v11_ten_quality_skill_contracts.py`
- Read-only reference: `scripts/tests/test_v11_requirement_quality_contracts.py`
- Read-only reference: `scripts/run_skill_trace_eval.py`
- Read-only reference: `scripts/skill_eval_rules.py`

**Interfaces:**

- Consumes: 7 个待创建新 Skill、3 个待增强目标包的固定路径和模式标记。
- Produces: 可重复的物理包、双语对等、本地触发数据和增强模式合同检查。
- Boundary: 只检查仓库结构和文字契约，不执行真实模型，不证明 Skill 效果。

- [x] **Step 1: 先写失败合同测试。**

  测试固定以下集合，并为每个语言检查同一合同：

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
          "artifact_markers": ("seam", "替身", "fault injection"),
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

  新包测试 `SKILL.md`、Prompt、metadata、`eval.yaml`、三个 case、CSV 和 JSON 的存在；CSV 必须包含 `explicit`、`implicit`、`contextual`、`negative` 且同时有正向和反向控制；JSON 的 `skill` 必须等于物理目录 slug。增强测试必须同时检查目标包的 SKILL/Prompt 含精确模式标记和领域产物标记，新增 case 使用对应前缀，`local-rules.json` 的 `skill` 仍为物理目标 slug，CSV 至少有一条包含候选名称或模式别名的 prompt；覆盖增强还必须保留 `RT-##` 与覆盖状态契约。这样不能仅靠泛化的 “business rule”/“architecture”/“coverage” 单词取得假通过。

- [x] **Step 2: 只运行这一个合同测试确认 RED。**

  ```bash
  python3 -m unittest scripts.tests.test_v11_ten_quality_skill_contracts -v
  ```

  Expected: FAIL because the seven new bilingual package directories and three enhancement-mode contracts do not exist yet. If it passes, tighten the assertion until the failure is caused by missing target behavior rather than a test typo.

- [x] **Step 3: 检查 RED 差异并保留现有工作。**

  ```bash
  git diff --check
  git status --short
  ```

  不删除、重置或覆盖已有 `requirement-*` 修改；合同测试作为本批新增文件保留。

---

### Task 2: 新增 `business-rule-extraction`

**Files:**

- Create: `skills/zh/testing-types/business-rule-extraction/SKILL.md`
- Create: `skills/zh/testing-types/business-rule-extraction/prompts/business-rule-extraction.md`
- Create: `skills/zh/testing-types/business-rule-extraction/agents/openai.yaml`
- Create: `skills/zh/testing-types/business-rule-extraction/evals/eval.yaml`
- Create: `skills/zh/testing-types/business-rule-extraction/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: `skills/zh/testing-types/business-rule-extraction/evals/{trigger-prompts.csv,local-rules.json}`
- Create: matching files under `skills/en/testing-types/business-rule-extraction/`

**Interfaces:**

- Consumes: PRD、政策、契约、流程、验收标准和用户提供的例子。
- Produces: `BR-##` 原子规则，包含规则、来源、角色/对象、触发、前置条件、动作/结果、约束/不变量、例外、证据、未知项、影响和验证提示。
- Boundary: 不发明阈值、优先级、状态迁移或例外，不把建议写成事实，不替业务/合规审批。

- [x] **Step 1: 写三类 Eval 和触发数据，覆盖一条可追溯规则、一份不完整材料和规则范围边界。**
- [x] **Step 2: 运行 zh/en `skill-up validate`；预期在包最小文件齐全后通过，行为效果仍保持未执行。**

  ```bash
  skill-up validate skills/zh/testing-types/business-rule-extraction/evals/eval.yaml
  skill-up validate skills/en/testing-types/business-rule-extraction/evals/eval.yaml
  ```

- [x] **Step 3: 写最小双语入口、Prompt 和 metadata。** Prompt 必须按输入审计、原子化、来源保留、例外/未知项和输出合同顺序执行，description 仅写触发条件。
- [x] **Step 4: 运行两种语言 dry-run、本地触发数据结构检查和合同测试；确认输出不能把示例或建议升级为业务事实。**

  ```bash
  skill-up run skills/zh/testing-types/business-rule-extraction/evals/eval.yaml --dry-run
  skill-up run skills/en/testing-types/business-rule-extraction/evals/eval.yaml --dry-run
  python3 -m unittest scripts.tests.test_v11_ten_quality_skill_contracts -v
  ```

- [x] **Step 5: `git diff --check`，记录该包的结构证据，再进入下一包。**

---

### Task 3: 增强 `business-rule-consistency-review` → `requirement-consistency-analysis`

**Files:**

- Modify: `skills/zh/testing-types/requirement-consistency-analysis/SKILL.md`
- Modify: `skills/zh/testing-types/requirement-consistency-analysis/prompts/requirement-consistency-analysis.md`
- Add: `skills/zh/testing-types/requirement-consistency-analysis/evals/cases/{business-rule-success,business-rule-incomplete-input,business-rule-scope-boundary}.yaml`
- Modify: `skills/zh/testing-types/requirement-consistency-analysis/evals/{eval.yaml,trigger-prompts.csv,local-rules.json}`
- Modify: matching English files under `skills/en/testing-types/requirement-consistency-analysis/`

**Interfaces:**

- Consumes: 两份或多份带适用范围的业务规则、版本或地区材料。
- Produces: 业务规则模式下的稳定规则键、主体/对象、触发、适用范围、优先级/覆盖关系、动作、结果和例外对照；保留 `RC-##` 和关系/状态分离。
- Boundary: 不把“更严格”当作更高优先级，不覆盖现有通用一致性分析，不创建 `business-rule-consistency-review` 目录。

- [x] **Step 1: 在不覆盖当前未提交内容的前提下，先补业务规则三类失败/边界 Eval 和触发数据。** 成功场景要求保留双方原文与规则级证据；不完整场景要求缺口；跨版本/地区场景要求保留范围差异。
- [x] **Step 2: 运行增强合同测试确认当前模式标记缺失或不完整，记录 RED。**
- [x] **Step 3: 最小修改中英文 SKILL/Prompt，加入业务规则模式选择、稳定比较键、优先级未决和规则级证据；保留已有通用 case 与 `RC-##` 契约。**
- [x] **Step 4: 运行目标 `skill-up validate`/dry-run、既有合同测试和独立性检查；确认没有新增重复目录。**

  ```bash
  skill-up validate skills/zh/testing-types/requirement-consistency-analysis/evals/eval.yaml
  skill-up validate skills/en/testing-types/requirement-consistency-analysis/evals/eval.yaml
  skill-up run skills/zh/testing-types/requirement-consistency-analysis/evals/eval.yaml --dry-run
  skill-up run skills/en/testing-types/requirement-consistency-analysis/evals/eval.yaml --dry-run
  python3 scripts/validate_skills_independence.py --skills-root skills --fail-on-findings
  ```

- [x] **Step 5: 运行合同测试和 `git diff --check`，确认原有通用能力未被改写。**

---

### Task 4: 新增 `technical-design-quality-review`

**Files:**

- Create: `skills/zh/testing-types/technical-design-quality-review/{SKILL.md,agents/openai.yaml}`
- Create: `skills/zh/testing-types/technical-design-quality-review/prompts/technical-design-quality-review.md`
- Create: `skills/zh/testing-types/technical-design-quality-review/evals/eval.yaml`
- Create: `skills/zh/testing-types/technical-design-quality-review/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: `skills/zh/testing-types/technical-design-quality-review/evals/{trigger-prompts.csv,local-rules.json}`
- Create: matching files under `skills/en/testing-types/technical-design-quality-review/`

**Interfaces:**

- Consumes: 架构说明、ADR、组件/数据流设计、技术方案和非功能约束。
- Produces: `TD-##` 发现，覆盖边界、依赖/失败模式、数据一致性、安全、性能、可观测性、兼容性、可维护性和验证准备度。
- Boundary: 不审查未提供的代码，不运行构建/测试，不把设计存在写成实现正确，不替 Human 批准架构。

- [x] **Step 1:** 写成功、不完整和设计/实现边界三类 Eval，并加入四种触发模式。
- [x] **Step 2:** 运行 zh/en `skill-up validate` 和 dry-run，确认 case schema 正确。
- [x] **Step 3:** 写最小双语包，输出合同固定为输入审计、设计覆盖矩阵、`TD-##` 发现、缺口行动、责任角色、验证方法和 Human 待决问题。
- [x] **Step 4:** 运行合同测试、metadata/独立性检查和 `git diff --check`；真实模型执行保持 `NOT_RUN`。

---

### Task 5: 增强 `architecture-testability-review` → `testability-analysis`

**Files:**

- Modify: `skills/zh/testing-types/testability-analysis/SKILL.md`
- Modify: `skills/zh/testing-types/testability-analysis/prompts/testability-analysis.md`
- Add: `skills/zh/testing-types/testability-analysis/evals/cases/{architecture-success,architecture-incomplete-input,architecture-unsafe-seam-boundary}.yaml`
- Modify: `skills/zh/testing-types/testability-analysis/evals/{eval.yaml,trigger-prompts.csv,local-rules.json}`
- Modify: matching English files under `skills/en/testing-types/testability-analysis/`

**Interfaces:**

- Consumes: 架构图、组件边界、依赖拓扑、异步链路、数据存储、外部服务、配置和部署环境。
- Produces: 架构模式下的测试接缝、替身策略、隔离边界、故障注入入口、环境复现和证据缺口，并保留通用可测试性维度。
- Boundary: 不把测试框架名称当作可测试性，不建议不安全后门，不创建 `architecture-testability-review` 目录。

- [x] **Step 1:** 增加三类架构 Eval 和触发数据，成功场景必须产生架构级证据，不完整场景必须保留缺口，不安全接缝场景必须拒绝后门。
- [x] **Step 2:** 运行增强合同测试记录 RED，然后最小修改中英文入口/Prompt；保留既有可观察、可控制、隔离、确定性和数据维度。
- [x] **Step 3:** 运行目标 validate/dry-run、合同测试、独立性检查和 diff check。

---

### Task 6: 新增 `api-design-quality-review`

**Files:**

- Create: `skills/zh/testing-types/api-design-quality-review/{SKILL.md,agents/openai.yaml}`
- Create: `skills/zh/testing-types/api-design-quality-review/prompts/api-design-quality-review.md`
- Create: `skills/zh/testing-types/api-design-quality-review/evals/eval.yaml`
- Create: `skills/zh/testing-types/api-design-quality-review/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: `skills/zh/testing-types/api-design-quality-review/evals/{trigger-prompts.csv,local-rules.json}`
- Create: matching files under `skills/en/testing-types/api-design-quality-review/`

**Interfaces:**

- Consumes: API 设计、OpenAPI/契约、请求响应样例、错误模型、鉴权授权、幂等、分页、状态码、版本演进和消费者影响。
- Produces: `API-##` 发现，保留 operation、来源、证据、影响、兼容性风险、迁移问题、责任角色和验证方式。
- Boundary: 不执行 API，不把样例当完整契约，不声称兼容性/安全测试通过，不替团队选择最终版本策略。

- [x] **Step 1:** 写三类 Eval 和四种触发数据，边界场景必须阻止“样例完整”“安全通过”“兼容通过”等无证据结论。
- [x] **Step 2:** validate/dry-run 后写双语入口、Prompt、metadata，保持与 `api-contract-testing` 的验证边界分离。
- [x] **Step 3:** 运行合同测试、metadata/独立性检查和 diff check。

---

### Task 7: 新增 `database-design-quality-review`

**Files:**

- Create: `skills/zh/testing-types/database-design-quality-review/{SKILL.md,agents/openai.yaml}`
- Create: `skills/zh/testing-types/database-design-quality-review/prompts/database-design-quality-review.md`
- Create: `skills/zh/testing-types/database-design-quality-review/evals/eval.yaml`
- Create: `skills/zh/testing-types/database-design-quality-review/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: `skills/zh/testing-types/database-design-quality-review/evals/{trigger-prompts.csv,local-rules.json}`
- Create: matching files under `skills/en/testing-types/database-design-quality-review/`

**Interfaces:**

- Consumes: ERD、DDL、ORM schema、迁移方案、数据所有权、生命周期、查询约束、事务/并发和恢复设计。
- Produces: `DB-##` 发现，包含对象、证据、约束/索引、事务/并发、迁移回滚、影响、责任角色和关闭证据。
- Boundary: 不连接或迁移真实数据库，不运行查询/基准，不凭表名发明业务规则或阈值，不替 Human 批准上线。

- [x] **Step 1:** 写成功、不完整、数据库执行边界三类 Eval 与本地触发数据。
- [x] **Step 2:** validate/dry-run 后写双语包，覆盖模型完整性、约束、索引、生命周期/隐私、事务隔离、迁移兼容、性能风险、备份恢复和测试准备度。
- [x] **Step 3:** 运行合同测试、metadata/独立性检查和 diff check；确认所有样例使用脱敏占位数据。

---

### Task 8: 新增 `observability-design-review`

**Files:**

- Create: `skills/zh/testing-types/observability-design-review/{SKILL.md,agents/openai.yaml}`
- Create: `skills/zh/testing-types/observability-design-review/prompts/observability-design-review.md`
- Create: `skills/zh/testing-types/observability-design-review/evals/eval.yaml`
- Create: `skills/zh/testing-types/observability-design-review/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: `skills/zh/testing-types/observability-design-review/evals/{trigger-prompts.csv,local-rules.json}`
- Create: matching files under `skills/en/testing-types/observability-design-review/`

**Interfaces:**

- Consumes: 日志、指标、Trace、上下文传播、SLO/SLI、告警、仪表板、采样、保留、隐私和成本设计。
- Produces: `OBS-##` 发现，包含信号、对象、字段/维度、语义、缺口、影响、检测动作、责任角色和验证方法。
- Boundary: 不读取真实运行信号宣布健康，不把仪表板存在当作告警有效，不执行生产探针，不替团队决定 SLO/事故等级。

- [x] **Step 1:** 写三类 Eval 和四种触发数据，边界场景覆盖敏感信息、基数、采样和告警可行动性。
- [x] **Step 2:** validate/dry-run 后写双语包，明确与 `log-analysis`、`distributed-trace-analysis`、`metrics-anomaly-analysis` 的运行证据边界。
- [x] **Step 3:** 运行合同测试、metadata/独立性检查和 diff check。

---

### Task 9: 新增 `error-handling-design-review`

**Files:**

- Create: `skills/zh/testing-types/error-handling-design-review/{SKILL.md,agents/openai.yaml}`
- Create: `skills/zh/testing-types/error-handling-design-review/prompts/error-handling-design-review.md`
- Create: `skills/zh/testing-types/error-handling-design-review/evals/eval.yaml`
- Create: `skills/zh/testing-types/error-handling-design-review/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: `skills/zh/testing-types/error-handling-design-review/evals/{trigger-prompts.csv,local-rules.json}`
- Create: matching files under `skills/en/testing-types/error-handling-design-review/`

**Interfaces:**

- Consumes: 错误分类、异常边界、超时、重试/退避、熔断、降级、幂等、事务一致性、错误传播、消费者契约、遥测和恢复设计。
- Produces: `EH-##` 失败模式发现，区分可重试、不可重试、人工接管和安全拒绝，并给出证据、影响、责任和验证方法。
- Boundary: 不执行故障注入，不复盘真实事故，不把错误处理代码存在当作正确，不替 Human 决定 SLA、文案或风险接受。

- [x] **Step 1:** 写三类 Eval 和四种触发数据，边界场景防止把一个通用错误响应当作完整处理设计。
- [x] **Step 2:** validate/dry-run 后写双语包，明确与 `production-incident-analysis`、`root-cause-analysis` 的运行/事故边界。
- [x] **Step 3:** 运行合同测试、metadata/独立性检查和 diff check。

---

### Task 10: 新增 `test-scope-analysis`

**Files:**

- Create: `skills/zh/testing-types/test-scope-analysis/{SKILL.md,agents/openai.yaml}`
- Create: `skills/zh/testing-types/test-scope-analysis/prompts/test-scope-analysis.md`
- Create: `skills/zh/testing-types/test-scope-analysis/evals/eval.yaml`
- Create: `skills/zh/testing-types/test-scope-analysis/evals/cases/{basic-success,edge-incomplete-input,edge-scope-boundary}.yaml`
- Create: `skills/zh/testing-types/test-scope-analysis/evals/{trigger-prompts.csv,local-rules.json}`
- Create: matching files under `skills/en/testing-types/test-scope-analysis/`

**Interfaces:**

- Consumes: 测试目标、产品面、变更/风险、约束、已有资产、平台/角色、数据和环境。
- Produces: `TS-##` 纳入/排除、深度、依赖、停止条件、扩大范围触发器、剩余风险、证据和责任角色。
- Boundary: 不生成完整测试策略，不选具体执行测试集，不执行测试，不把范围声明当作覆盖证明。

- [x] **Step 1:** 写三类 Eval，成功场景覆盖核心/传递影响和范围取舍，不完整场景给出受限初版，边界场景拒绝未经授权的全量/零覆盖结论。
- [x] **Step 2:** validate/dry-run 后写双语包，明确与 `regression-scope-analysis`、`regression-test-selection`、`test-strategy` 的边界。
- [x] **Step 3:** 运行合同测试、metadata/独立性检查和 diff check。

---

### Task 11: 增强 `test-coverage-analysis` → `requirement-traceability-analysis`

**Files:**

- Modify: `skills/zh/testing-types/requirement-traceability-analysis/SKILL.md`
- Modify: `skills/zh/testing-types/requirement-traceability-analysis/prompts/requirement-traceability-analysis.md`
- Add: `skills/zh/testing-types/requirement-traceability-analysis/evals/cases/{coverage-success,coverage-incomplete-input,coverage-scope-boundary}.yaml`
- Modify: `skills/zh/testing-types/requirement-traceability-analysis/evals/{eval.yaml,trigger-prompts.csv,local-rules.json}`
- Modify: matching English files under `skills/en/testing-types/requirement-traceability-analysis/`

**Interfaces:**

- Consumes: 需求、风险、行为/场景、测试资产和真实执行证据（若提供）。
- Produces: 保留 `RT-##` 双向关系，并增加 `TC-##` 覆盖视图：对象、来源、测试资产、关系类型、覆盖状态、执行身份/时间/环境、证据质量、孤立项、缺口行动和验证方法。
- Boundary: 不创建 `test-coverage-analysis` 目录，不把测试文件/名称/报告摘要当作执行覆盖，不计算未提供工具证据的代码行覆盖率。

- [x] **Step 1:** 写覆盖有效映射、信息不足、范围/执行证据边界三类 Eval 和四种触发数据；保留现有通用追踪 cases。
- [x] **Step 2:** 运行增强合同测试记录 RED，再最小修改中英文 SKILL/Prompt，增加可选 `coverage_analysis` 模式、`TC-##` 合同和覆盖状态边界。
- [x] **Step 3:** validate/dry-run、合同测试、独立性检查和 diff check；确认 `RT-##` 关系枚举与覆盖状态枚举仍分离。

---

### Task 12: 同步十 Skill 治理 registry、匹配登记和生成视图

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

- Consumes: 已通过合同/结构门禁的 7 个新包、3 个增强目标和两份设计说明中的 Capability Match 证据。
- Produces: 7 个物理 Skill registry 记录、3 个 `ENHANCE` 候选记录、双语 Matrix/Matching Register/Inventory/Catalog/Graph 和入口索引。
- Boundary: registry 只记录结构与治理状态；`quality_score.state=NOT_SCORED`、`eval_execution.state=NOT_RUN`，不伪造语义效果。

- [x] **Step 1:** 在 registry 中增加 7 个 `skills` 记录和 3 个 candidate 记录；`NEW` 记录必须有 scope/non-goals，增强记录必须指向现有目标路径和六字段证据。
- [x] **Step 2:** 运行 registry/matrix 校验，修复 slug、zh/en path、metadata、evidence path 和物理目录交叉错误。

  ```bash
  python3 scripts/generate_skill_inventory.py
  python3 scripts/generate_skill_governance_inventory.py
  python3 scripts/generate_skill_governance_matrix.py
  python3 scripts/generate_skill_governance_inventory.py --check
  python3 scripts/generate_skill_governance_matrix.py --check
  ```

- [x] **Step 3:** 用仓库既有生成器刷新双语生成视图；只保留本批相关的生成差异，不覆盖无关文档修改。
- [x] **Step 4:** 更新 Phase 1、Catalog、Graph、根 README 以及 `skills/zh/README.md` / `skills/en/README.md` 的双语入口与能力边界；按生成器实际结果更新语言 Skill 数和双语目录总数（当前基线为 84/168，若只有 7 个新逻辑包增加则预期为 91/182），不要把候选别名写成物理 Skill 目录。
- [x] **Step 5:** 运行文档双语和独立性检查，确认十个候选都可从 registry 追到物理包或增强目标。

---

### Task 13: 运行统一质量门禁并核验 Project 卡片

**Files:**

- Test: `scripts/tests/test_v11_requirement_quality_contracts.py`
- Test: `scripts/tests/test_v11_ten_quality_skill_contracts.py`
- Verify: all 7 new bilingual packages and 3 enhanced bilingual target packages
- Verify: Project #4 item IDs for the ten cards

**Interfaces:**

- Consumes: 全部十个 Skill 的包、Eval、本地规则、治理记录和生成视图。
- Produces: 可复核的静态质量、Eval schema/dry-run、本地触发和 Project 状态证据；真实模型执行仍标记 `NOT_RUN`。
- Boundary: 不推送、不发布、不执行真实 API/数据库/生产观测/事故/测试目标。

- [x] **Step 1:** 运行所有目标包 `skill-up validate` 和 `--dry-run`；七个新包与三个增强目标均须通过结构检查。
- [x] **Step 2:** 运行两份本地合同测试和全仓测试。

  ```bash
  python3 -m unittest discover -s scripts/tests -p 'test_*.py'
  ```

- [x] **Step 3:** 运行仓库质量门禁。

  ```bash
  bash scripts/check_skills_quality.sh
  bash scripts/validate_skill_evals.sh
  python3 scripts/check_docs_bilingual.py --repo-root .
  git diff --check
  ```

- [x] **Step 4:** 对每个目标包运行 `scripts/run_skill_trace_eval.py` 的默认 dry-run；命令必须显式提供 `--prompts`、`--config`、`--project-root` 和 `--output-dir`，且不加 `--run`：

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

  若没有 `skill.selection` 的真实 trace，报告 `BLOCKED`，不报告 PASS；dry-run 只证明命令和输入数据可装载，真实模型执行仍为 `NOT_RUN`。
- [x] **Step 5:** 用 `gh project item-list 4 --owner @me --format json --limit 200` 精确核验十个目标标题为 `In Progress`，并核对下一批 `test-gap-analysis`、`risk-based-testing`、`edge-case-discovery`、`negative-scenario-discovery`、`test-data-requirement-analysis` 状态仍为 `Todo`。
- [x] **Step 6:** 对新增/修改且未被 `git diff --check` 覆盖的文件补做作用域化尾随空白检查，例如 `rg -n "[[:blank:]]+$" scripts/tests/test_v11_ten_quality_skill_contracts.py docs/superpowers/plans/2026-09-14-v1-1-ten-quality-skills*.md skills/zh/testing-types/{business-rule-extraction,requirement-consistency-analysis,technical-design-quality-review,testability-analysis,api-design-quality-review,database-design-quality-review,observability-design-review,error-handling-design-review,test-scope-analysis,requirement-traceability-analysis} skills/en/testing-types/{business-rule-extraction,requirement-consistency-analysis,technical-design-quality-review,testability-analysis,api-design-quality-review,database-design-quality-review,observability-design-review,error-handling-design-review,test-scope-analysis,requirement-traceability-analysis}`；命中即失败。随后输出最终工作区文件清单、验证命令和未执行边界；不提交、不 push，除非用户另行授权。

## Plan Self-Review

### Review fixes applied (2026-09-14)

- 将 docs bilingual gate 从错误的 `bash` 调整为 `python3`，并补齐 trace runner 的四个必需参数。
- 明确生成视图的“先刷新、后 `--check`”顺序，并加入 `generate_skill_inventory.py`；补齐两个语言根 README 和 Skill 数量更新责任。
- 将增强合同从泛化关键词收紧为模式、领域产物、case 前缀、物理目标 `skill` 和候选 alias prompt 的组合检查。
- 明确增强候选只复用目标目录，且为未跟踪文件增加独立尾随空白检查。

- 两份设计说明的 10 张卡片均有对应 Task 2–11；7 个 `NEW` 和 3 个 `ENHANCE` 的目录边界均被覆盖。
- 所有新包的入口、Prompt、metadata、Eval、三类 case、触发 CSV 和本地规则均在对应 Task 文件清单中；增强包的现有目录和新增 case/触发数据也有明确路径。
- RED 合同测试先于包内容，且每个 Skill 仍有独立的 validate、dry-run、合同测试和 diff check。
- registry、匹配登记、双语生成视图、质量门禁和 Project 卡片核验集中在 Task 12–13，避免中间状态被误报为发布完成。
- 本计划不包含占位式或“稍后补充”步骤；所有执行命令、状态边界和文件责任已明确。上述 review fix 已覆盖命令可执行性、双语入口、别名物理目录边界、增强合同强度和未跟踪文件验证盲区。
