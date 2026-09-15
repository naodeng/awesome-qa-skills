<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-09-15-v2-test-engineering-two-batch-design_EN.md">🇬🇧 English</a></div>

# v2.0 Test Engineering 两批 Skill 设计

## 状态

`IMPLEMENTED_PENDING_ACCEPTANCE`（2026-09-15）。本设计已经确认“拖动卡片”指 GitHub Project #4 的路线图卡片状态流转；本地 `develop` 已将 `origin/main` 的 `d63a9fa` 快进合入。两批实现、修复和静态门禁已完成，代码通过现有 PR #12 交付；但 Project 历史状态事件仍未取得，整体验收保持未完成。

## 目标与边界

v2.0 先实现 Project #4 中 25 张 `v2 P1` 候选 Skill 卡片，分成两批交付。每张卡片均先做 Capability Match；当前仓库不存在同名物理目录，因此初始按 `NEW` 设计，但若实现审查发现主输入、输出和决策逻辑已被完整覆盖，必须在建包前改为 `ENHANCE` 或 `MATCH`，不能为了完成卡片数量复制能力。

卡片是执行看板记录，不是 Skill 的运行时依赖。卡片从 `Todo` 移到 `In Progress` 只在对应批次合同测试确认 RED 后发生；质量门禁和双语同步完成后才移到 `Done`。卡片状态不代表真实模型效果、业务批准、发布或风险接受。

## 两批范围

### Batch 1：测试设计方法（9 张卡片）

`decision-table-testing`、`state-transition-testing`、`boundary-value-testing`、`equivalence-partitioning`、`pairwise-testing`、`combinatorial-testing`、`model-based-testing`、`property-based-testing`、`metamorphic-testing`。

这些 Skill 把需求、规则、状态、数据域、因素或参考关系整理为可复核的测试设计候选。它们输出设计依据、覆盖选择、未知项和验证建议，不生成已执行结果，不替代完整策略、测试用例编写或测试执行。

### Batch 2：API、UI 与测试工程质量（16 张卡片）

`api-schema-validation`、`api-negative-testing`、`api-idempotency-testing`、`api-pagination-testing`、`api-rate-limit-testing`、`api-version-compatibility-testing`、`api-error-contract-testing`、`ui-test-strategy`、`ui-test-selector-review`、`ui-test-wait-strategy-review`、`visual-regression-testing`、`cross-browser-testing`、`test-code-review`、`mutation-testing-analysis`、`mock-quality-review`、`test-suite-health-analysis`。

这些 Skill 面向契约、失败语义、兼容性、UI 稳定性和测试资产质量。它们只基于用户提供的规格、代码、测试资产或报告提出结构化发现和后续验证动作，不调用真实 API、浏览器、数据库、变异执行器或生产系统。

## 共享输出合同

每个 Skill 的主 Prompt 必须先列出 `known`、`missing`、`conflicting`、`stale`、`out_of_scope` 和 `assumptions`。之后分离事实、证据支持的推断、候选建议和 Human 决策。

每条发现使用该 Skill 的稳定前缀和两位序号，至少包含：对象/规则、来源、触发条件或适用范围、预期关注点、证据状态、影响/优先级、责任角色、关闭条件和验证方法。未知阈值、缺少执行记录、冲突材料和过期信息必须保持 `unassessed`、`blocked` 或待确认，不能由 Prompt 模板或静态文件存在升级为通过。

每个中英文 Skill 包必须独立可复制安装，包含：

- `SKILL.md` 与主 `prompts/<slug>.md`；
- `agents/openai.yaml`，且 `metadata.key` 与目录 slug 相同；
- `evals/eval.yaml`；
- `basic-success.yaml`、`edge-incomplete-input.yaml`、`edge-scope-boundary.yaml` 三类用例；
- `evals/trigger-prompts.csv`，覆盖 `explicit`、`implicit`、`contextual`、`negative`，并同时包含应触发与反向控制样本；
- `evals/local-rules.json`，其中 `skill` 必须等于物理目录 slug。

真实模型 Eval、外部测试目标、业务语义等价、质量评分和发布状态本批保持 `NOT_RUN`、`NOT_SCORED` 或 `UNASSESSED`，除非存在独立证据。

## 实现顺序

1. 先写批次合同测试并观察 RED。
2. RED 原因确认后，只移动对应批次的精确 Project 卡片到 `In Progress`。
3. 每个 Skill 按 RED → 最小 GREEN → REFACTOR 完成中英文包与三类 Eval。
4. 更新 registry、Matrix/Register、双语 README/Catalog/Graph 和必要的路由文档。
5. 运行目标验证、全仓合同与质量门禁；只有证据完整的卡片才在验收结论中标记为完成。
6. 其他 Project 卡片保持原状态；不创建仓库 Issue 或 Release；本次代码交付通过现有 PR 完成。

## 验收条件与当前结论

完整验收的最低条件是：25 张精确卡片均有经过 `In Progress` 和 `Done` 的历史状态证据；中文/英文各新增 25 个同名物理 Skill 包；所有包通过结构、metadata、Eval、独立性、完整性和双语门禁；治理生成视图可从当前 registry 复现；`git diff --check` 通过；报告明确静态结构证据与未运行的真实模型/外部验证之间的边界。

当前已完成 25 个双语物理 Skill 包、结构与质量门禁、治理生成视图和静态边界记录。Project #4 仅能由 `gh project item-list 4 --owner naodeng --format json --limit 200` 核实 25 张卡片的当前 `Done` 状态，无法返回 `In Progress -> Done` 历史事件；因此 registry 将 25 条记录标为 `acceptance_state: INCOMPLETE`，整体验收保持 `INCOMPLETE`，不能声称 25 张卡片均已完成状态流转验收。
