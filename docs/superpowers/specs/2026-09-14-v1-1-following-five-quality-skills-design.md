<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-09-14-v1-1-following-five-quality-skills-design_EN.md">🇬🇧 English</a></div>

# v1.1 后续五张质量 Skill 卡片设计

## 状态

`APPROVED_FOR_IMPLEMENTATION`（2026-09-14，完成计划 review 修复）。本设计覆盖 Project #4 中本批次的五张 v1.1 P0 卡片。五张卡片已从 `Todo` 移动到 `In Progress`；本文件定义能力匹配、包边界和验证契约，不创建 Skill 包，也不改变治理 registry 或生成视图。

## Capability Match 决策

仓库规则是“先匹配，后增强；仅在结论为 `NEW` 时创建独立目录”。本批采用 4 个独立新 Skill 加 1 个现有 Skill 增强：

| 候选卡片 | 决策 | 现有能力证据 | 本批边界 |
| --- | --- | --- | --- |
| `database-design-quality-review` | `NEW` | 当前有需求、API、可测试性和质量风险分析，但没有面向数据模型、约束、迁移和事务设计的独立审查契约 | 创建双语独立 Skill；只审查数据库设计，不连接或操作目标数据库 |
| `observability-design-review` | `NEW` | `distributed-trace-analysis`、`log-analysis`、`metrics-anomaly-analysis` 分析运行证据；`testability-analysis` 只把可观测性作为测试准备度维度 | 创建双语独立 Skill；只审查实现前的日志、指标、Trace、SLO 和告警设计 |
| `error-handling-design-review` | `NEW` | `production-incident-analysis`、`root-cause-analysis` 面向事故和根因证据；API/测试 Skill 只覆盖局部错误行为 | 创建双语独立 Skill；只审查实现前错误分类、传播、恢复和一致性设计 |
| `test-scope-analysis` | `NEW` | `regression-scope-analysis` 限定变更或发布后的回归范围；`test-strategy` 输出完整策略而非独立范围审计 | 创建双语独立 Skill；只确定测试纳入、排除、深度和追加触发条件，不替代完整策略或测试选择 |
| `test-coverage-analysis` | `ENHANCE` → `requirement-traceability-analysis` | 现有 Skill 已建立需求到测试/证据的双向映射和覆盖状态，直接新建会重复覆盖矩阵 | 在现有 Skill 增加可选覆盖分析模式和 `TC-##` 视图；保留 `RT-##` 追踪契约，不创建同名目录 |

实现期间如发现任何 `NEW` 能力已经被现有 Skill 的主输入、主输出和决策逻辑完整覆盖，必须在创建目录前改为有证据的 `ENHANCE` 或 `MERGE`，并同步修改本设计的结论。

## 共同契约

- 中文和英文入口、Prompt、metadata、Eval 与本地触发数据结构对等；目录名和 `metadata.key` 使用同一小写连字符 slug。
- 增强候选不创建别名目录；其本地 `trigger-prompts.csv` / `local-rules.json` 放在物理目标 Skill 的 `evals/` 下，JSON `skill` 保持目标 slug，CSV 至少覆盖候选名称或模式短语。
- 所有输入先分为 `known`、`missing`、`conflicting`、`stale`、`out_of_scope` 和 `assumptions`；来源事实、证据推断、建议和 Human 决策分开。
- 每个发现绑定来源和最小证据。文件存在、设计声明、测试名称、报告文字或工具配置不能升级为运行结果、兼容性通过、风险接受或发布批准。
- 四个新 Skill 使用各自稳定发现 ID：`DB-##`、`OBS-##`、`EH-##`、`TS-##`。覆盖增强保留 `RT-##` 双向追踪发现，并用 `TC-##` 表示覆盖视图；关系类型与覆盖状态不可混用。
- 每个包至少有成功路径、信息不足、范围/风险边界三类 Eval，并覆盖显式、隐式、上下文和反向触发数据。缺少 `skill.selection` 证据时，本地 runner 必须报告 `BLOCKED`，不推断触发成功。
- 设计审查只输出 AI 辅助发现、缺口、建议和验证方法；registry 质量评分保持 `NOT_SCORED`，真实模型执行保持 `NOT_RUN`，直到有独立证据。

## 新增 Skill 设计

### `database-design-quality-review`

在实现或迁移前审查 ERD、数据模型、DDL、ORM schema、迁移方案、数据所有权、保留/删除策略、查询约束和恢复设计。

每条 `DB-##` 至少包含：对象与范围、来源、证据、设计规则、发现、影响/严重性、约束或索引风险、事务/并发影响、迁移与回滚问题、责任角色和可验证关闭条件。评审维度包括模型完整性、主外键与约束、索引和查询假设、事务隔离、并发、数据生命周期与隐私、迁移兼容性、性能风险、备份恢复和测试准备度。

它不连接、修改或迁移真实数据库，不执行查询或性能基准，不从表名推断业务规则，不发明数据量/一致性阈值，也不替 Human 批准 schema、风险接受或上线。

### `observability-design-review`

在实现前审查日志、指标、Trace、上下文传播、SLO/SLI、告警、仪表板、采样、保留、隐私和成本设计。

每条 `OBS-##` 至少包含：信号类型、来源、覆盖对象、字段/维度、预期语义、证据、缺口、影响、检测或告警动作、责任角色和验证方法。评审维度包括关键路径覆盖、跨服务关联、字段语义、基数与采样、SLO/SLI 可计算性、告警可行动性、失败模式可见性、敏感信息与脱敏、保留成本和验证准备度。

它不读取真实运行日志或指标来宣布系统健康，不把仪表板存在写成告警有效，不执行生产探针，不替团队决定 SLO 或事故等级，也不把工具名称当作可观测性证据。

### `error-handling-design-review`

在实现前审查错误分类、异常边界、超时、重试、退避、熔断、降级、幂等、事务一致性、错误传播、用户/消费者契约、遥测和恢复设计。

每条 `EH-##` 至少包含：失败模式、触发条件、边界、预期行为、传播/转换、重试或降级条件、数据一致性影响、用户/调用方可见结果、可观测证据、责任角色和验证方法。评审必须区分可重试、不可重试、需人工接管和安全拒绝；不能用一个通用“返回错误”覆盖不同失败模式。

它不执行故障注入，不复盘真实事故，不把错误处理代码存在写成行为正确，不替团队选择最终用户文案、SLA、风险接受或恢复批准，也不把样例错误响应当成完整契约。

### `test-scope-analysis`

在测试活动、迭代、版本或风险评审开始前，分析测试对象的纳入范围、排除范围、覆盖深度、依赖和追加触发条件。

每条 `TS-##` 至少包含：目标与对象、纳入项、排除项、风险/影响依据、覆盖深度、平台/角色/数据/环境依赖、停止条件、扩大范围触发器、剩余风险、来源证据和责任角色。分析应区分核心路径、直接影响、传递影响、非功能、迁移/兼容和未评估区域，并说明每个范围取舍的可验证理由。

它不生成完整测试策略，不从现有测试资产选择具体执行集合，不执行测试，不把范围声明写成覆盖证明；变更或发布后的回归选择仍由 `regression-scope-analysis` 和相关测试选择能力负责。

## 增强 Skill 设计

### `test-coverage-analysis` → `requirement-traceability-analysis`

在现有 Skill 中增加可选的 `coverage_analysis` 模式，不创建 `test-coverage-analysis` 目录。该模式以需求、风险、行为/场景、测试资产和执行证据为输入，复用现有双向追踪模型，另外输出 `TC-##` 覆盖视图。

每条 `TC-##` 至少包含：需求/风险或行为对象、来源、关联测试资产、关系类型、覆盖状态、执行身份/时间/环境（若提供）、证据质量、孤立项或重复项、缺口行动和验证方法。覆盖状态继续使用 `complete`、`partial`、`unverified`、`stale`、`unexecuted` 和 `unassessed`；缺少真实执行证据时不能写 `passed`。保留原有 `RT-##` 双向关系发现，并明确需求到测试和测试反查需求两个方向。

该模式不计算未提供工具证据的代码行覆盖率，不把测试文件存在、名称匹配或报告摘要当作执行覆盖，不替代 `test-scope-analysis` 的纳入/排除决策，也不替代 Human 对风险接受和发布结论的决定。新增 Eval 覆盖有效映射、信息不足和范围边界，原有通用追踪 Eval 必须继续通过。

## 组件、数据流和失败处理

每个新 Skill 的最小组件为 `SKILL.md`、`prompts/<slug>.md`、`agents/openai.yaml`、`evals/eval.yaml` 和三类 `evals/cases/`；本地触发验证增加 `trigger-prompts.csv` 与 `local-rules.json`。增强 Skill 沿用现有目录和 metadata，只增补模式说明、Prompt、Eval 与触发数据。

数据流统一为：输入材料 → 输入审计 → 结构化发现/映射 → 证据状态与范围边界 → 风险/缺口行动 → Human 待决问题。缺少主材料时交付受限结果并标记缺口；来源冲突影响核心结论时保留双方并标记阻塞；没有执行身份、时间、环境和原始结果时，覆盖或运行结论保持 `unverified`、`unexecuted` 或 `unassessed`。

## TDD、Eval 与治理交付

1. 先增加本批次的本地合同测试并运行 RED，确认不存在五个新目录、覆盖增强契约尚未满足；未观察到预期失败前不得写 Skill 内容。
2. 按每个 Skill 独立完成 RED → 最小 GREEN → REFACTOR；不要以批量生成替代逐个验证。新 Skill 先完成包内最小内容和三类 Eval，再处理下一个包。
3. 创建 4 个新 Skill 的中英文包；增强 `requirement-traceability-analysis` 的中英文入口和 Prompt，补充 `coverage_analysis` 的三类 Eval、触发数据和本地规则。
4. 更新 registry、Capability Match Register、双语 README/Catalog/Graph 和必要生成视图；记录 4 个 `NEW`、1 个 `ENHANCE` 及匹配证据路径。
5. 运行目标 Skill 的 `skill-up validate`、dry-run、本地触发 runner、相关合同测试、全仓单测、独立性/完整性/双语质量门禁和 `git diff --check`。
6. 最终核验本批五张卡片为 `In Progress`，下一批 Todo 卡片状态未被改变；不 push、不发布版本，真实模型执行保持 `NOT_RUN`。

## 非目标

- 不创建 `test-coverage-analysis` 的重复目录，不改变 `requirement-traceability-analysis` 的既有关系和覆盖枚举含义。
- 不修改上一批 v1.1 Skill 的业务语义，除非共享治理或验证脚本必须同步。
- 不连接真实数据库、生产可观测性系统或线上事故环境，不执行真实测试、迁移、故障注入或发布。
- 不把静态包结构、Eval 配置或本地规则结果写成真实模型效果、系统运行结果、Human 批准或 Release 完成。
