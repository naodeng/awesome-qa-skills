<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-09-14-v1-1-next-five-quality-skills-design_EN.md">🇬🇧 English</a></div>

# v1.1 下一批五张质量 Skill 卡片设计

## 状态

`APPROVED_FOR_IMPLEMENTATION`（2026-09-14，完成计划 review 修复）。本设计覆盖 Project #4 中接下来的五张 v1.1 P0 卡片。五张卡片已移动到 `In Progress`；本文件只完成能力匹配和实现边界，尚未修改 Skill 包、治理 registry 或生成视图。

## Capability Match 决策

仓库规则是“先匹配，后增强；仅在结论为 `NEW` 时创建独立目录”。因此本批不机械创建五个同名目录：

| 候选卡片 | 决策 | 现有能力边界 | 本批动作 |
| --- | --- | --- | --- |
| `business-rule-extraction` | `NEW` | `requirements-analysis` 是需求总入口，`requirement-quality-review` 是质量总览，均没有把分散材料提取为原子业务规则的独立契约 | 创建双语独立 Skill |
| `business-rule-consistency-review` | `ENHANCE` | `requirement-consistency-analysis` 已负责跨来源术语、状态、规则和行为一致性 | 为现有 Skill 增加业务规则模式、规则不变量、优先级/适用范围和规则级证据字段；不创建重复目录 |
| `technical-design-quality-review` | `NEW` | `technical-quality-perspective` 是阶段路由器，`code-review` 面向可审查代码变更；没有独立的实现前技术设计质量契约 | 创建双语独立 Skill |
| `architecture-testability-review` | `ENHANCE` | `testability-analysis` 已覆盖可观察、可控制、隔离、确定性、数据和故障注入 | 为现有 Skill 增加架构制品输入、测试接缝、依赖替身、环境拓扑和架构级可测试性证据；不创建重复目录 |
| `api-design-quality-review` | `NEW` | `api-contract-testing` 面向契约验证和兼容性测试，`api-testing` 面向执行；没有设计阶段 API 质量审查契约 | 创建双语独立 Skill |

若实现阶段发现上述 `NEW` 范围仍被现有 Skill 语义覆盖，必须将 registry 和 Matching Register 改为有证据的 `ENHANCE`/`MERGE`，停止重复创建。

## 共同契约

所有新增或增强内容保持现有仓库约定：

- 中文和英文入口、Prompt、metadata、Eval 和本地触发数据保持结构对等。
- 增强候选不创建别名目录；其本地 `trigger-prompts.csv` / `local-rules.json` 放在物理目标 Skill 的 `evals/` 下，JSON `skill` 保持目标 slug，CSV 至少覆盖候选名称或模式短语。
- 输入审计区分 `known`、`missing`、`conflicting`、`stale`、`out_of_scope` 和 `assumptions`；直接事实、证据推断、建议和 Human 决策分开。
- 结论必须绑定来源和最小证据；文件存在、名称匹配、报告文字和设计声明不能升级为运行结果、兼容性通过或发布批准。
- 每个包维护成功路径、信息不足、范围/风险边界三类 Eval，并覆盖显式、隐式、上下文和反向触发样本；缺少 `skill.selection` 证据时本地 runner 报告 `BLOCKED`。
- 范围边界用语义 `agent_judge` 表达，registry 的质量评分和真实模型执行保持 `NOT_SCORED`/`NOT_RUN`，直到有独立执行证据。

## 新增 Skill 设计

### `business-rule-extraction`

从 PRD、政策、契约、流程、验收标准和用户提供的例子中提取可追溯的原子业务规则。每条 `BR-##` 至少包含规则陈述、来源、适用角色/对象、触发条件、前置条件、动作/结果、约束或不变量、例外、证据、未知项、影响和验证/测试提示。

它不发明阈值、优先级、状态迁移或默认例外，不把建议写成事实，也不代替产品、合规或业务角色批准规则。只有材料明确支持时，才把多个句子归并为同一规则；否则保留独立来源和待确认问题。

### `technical-design-quality-review`

在实现或测试设计前，审查架构说明、ADR、组件/数据流设计、技术方案和非功能约束。按证据覆盖架构边界、依赖与失败模式、数据一致性、安全、性能、可观测性、兼容性、可维护性和验证准备度，输出 `TD-##` 技术发现、影响/严重性、缺失信息、行动、责任角色和验证方法。

它不审查未提供的代码、不运行构建或测试、不把设计存在写成实现正确，也不替 Human 做架构批准或风险接受。

### `api-design-quality-review`

在 API 实现前审查 API 设计、OpenAPI/契约、请求响应示例、错误模型、认证授权、幂等、分页、状态码、版本演进、兼容性、消费者影响和可观测性。输出 `API-##` 发现，保留 endpoint/operation、来源、证据、影响、兼容性风险、迁移问题、责任角色和验证方式。

它不执行 API、替消费者确认语义、不把样例当完整契约、不宣称兼容性测试或安全测试通过，也不替团队决定最终版本策略。

## 增强 Skill 设计

### `business-rule-consistency-review` → `requirement-consistency-analysis`

在现有 Prompt 中增加可选的业务规则比较模式：使用稳定的规则 ID、主体/对象、触发条件、适用范围、优先级/覆盖关系、动作、结果和例外作为比较键；关系值仍与证据状态分离。输出保留双方原文、规则级证据和未决优先级，不把“更严格”自动当作更高优先级。

增加业务规则成功、单来源缺失、跨版本/地区范围边界三类 Eval，并在 Skill 入口写明何时选择业务规则模式。现有通用一致性用例和 `RC-##` 契约继续有效。

### `architecture-testability-review` → `testability-analysis`

在现有 Prompt 中增加架构模式：输入可包括架构图、组件边界、依赖拓扑、异步链路、数据存储、外部服务、配置和部署环境；输出除通用可测试性维度外，增加测试接缝、替身/模拟策略、隔离边界、故障注入入口、环境复现和证据缺口。

增加架构可测试性成功、架构材料不完整、不可安全暴露测试接缝三类 Eval。不得把“使用某测试框架”当作架构可测试性，也不得建议不安全后门。

## 交付与验证边界

实现完成后必须：

1. 为 3 个 `NEW` Skill 创建双语独立包、metadata、主 Prompt、三类 Eval、`trigger-prompts.csv` 和 `local-rules.json`。
2. 为 2 个 `ENHANCE` Skill 修改现有双语入口/Prompt，并增加对应 Eval 与触发数据，不创建重复目录。
3. 更新 registry、Matching Register、双语 README/Catalog/Graph 和生成视图；记录 `NEW`/`ENHANCE` 及证据路径。
4. 运行目标 Eval validate/dry-run、本地触发 runner、全仓单测、独立性/完整性/双语质量门禁和 `git diff --check`。
5. 再次确认这五张 Project 卡片为 `In Progress`，其他卡片状态不变；不 push、不发布版本，真实模型执行继续保持 `NOT_RUN`。

## 非目标

- 不修改前五个 v1.1 Skill 的既有语义，除非共享治理或验证脚本必须同步。
- 不创建 repository Issue，不执行真实项目的 API、架构、业务规则或测试运行。
- 不在证据不足时把 `NEW`/`ENHANCE`、质量分、运行结果或发布结论写成最终事实。
