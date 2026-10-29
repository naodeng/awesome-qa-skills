---
name: quality-metrics-design
description: Use this skill when you need evidence-bounded quality metric definitions, calculation rules, data sources, freshness, and anti-gaming boundaries; triggers include 质量指标 and quality metric.
license: PolyForm-Noncommercial-1.0.0
metadata:
  version: "1.0.0"
  compatibility: ""
  author: "Awesome QA Skills contributors"
  language: "zh-CN"
  category: "testing-types"
  source: "https://github.com/naodeng/awesome-qa-skills"
  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"
---

# 质量指标设计（中文版）

## 何时使用

- 需要围绕质量指标的定义、计算口径、数据源、时效与反操纵边界开展有证据的分析、设计或验证准备。
- 需要评审现有方案、结果或指标，并形成可执行的改进项。
- 输入不完整，但仍需交付带假设、信息缺口和人工决策边界的受限初版。

## 输出格式选项

- 默认输出 Markdown，按领域风险、证据状态、优先级和边界组织。
- 用户要求表格、CSV、JSON 或工单格式时，保留相同的发现字段、证据和决策边界。
- 输出进入自动化流程前，先确认 schema、枚举值、必填项和证据来源。

## 如何使用

1. 先阅读并遵循 `prompts/quality-metrics-design.md`，包括输入审计、领域覆盖和输出顺序。
2. 提取范围、环境、版本、时间窗口、约束、成功标准和可用证据，重点检查指标定义、分子分母、数据源、刷新时效、解释限制。
3. 先区分已确认事实、证据支持的推断、候选建议和 Human 决策，再按风险与证据强度排序。
4. 把高风险项转成前置条件、步骤、预期结果或判断标准、所需证据和验证方法。
5. 信息不足时交付受限初版，明确哪些结论不能成立，不把静态材料写成执行结果。

## 参考文件

- 校准领域结果、正确对照或证据缺口时，读取 [references/domain-decision-example.md](references/domain-decision-example.md) 的脱敏输入、逐项预期与复算依据。

- 每次执行必须读取 `prompts/quality-metrics-design.md`；它是本 Skill 的完整执行规范。
- 需要评测时读取 `evals/eval.yaml` 和 `evals/cases/` 下的匹配用例。
- 只有目录实际存在且任务需要时，才读取 `references/`、`examples/`、`scripts/` 或 `output-formats.md`，不要假设不存在的资产。

## 领域执行要点

1. 建立指标字典：决策目的、统计单位、分子/分母、时窗/时区、筛选/去重、缺失处理、版本、来源与lineage；率的分母不能隐式变化。
2. 区分缺陷实体与状态事件、首次执行与重跑、关闭与重开；按项目唯一键和事件时间聚合，避免把重复ID/重开计成新缺陷或重试冲高通过率。
3. 复算样本并核对分母覆盖、延迟与排除理由；缺记录保持未知，不能补0。数据异常先标测量问题，未有证据不归因产品质量。
4. 输出计算例、解释限制、监控阈值来源与行动；跨项目比较要对齐定义与窗口，不把指标相关性写成因果。

## 核心约束

- 只分析质量指标的定义、计算口径、数据源、时效与反操纵边界，不替代业务负责人或 Human 的风险接受、例外批准和发布决定。
- 不编造系统行为、字段、指标、阈值、数据、根因、执行记录或通过结论。
- 静态设计、计划、文件存在或 dry-run 只能保留原证据状态，不能升级为真实执行证明。
- 证据不足时使用待确认、blocked、unassessed 或 NOT_SCORED，并给出最小验证方法。
- 涉及生产、隐私或安全时采用最小权限、脱敏数据、mock、dry-run 或隔离环境。

## 交付前自检

- [ ] 已覆盖指标定义、分子分母、数据源、刷新时效、解释限制，并为每项记录来源、证据状态和验证方法。
- [ ] 已分开事实、推断、候选建议、信息缺口和 Human 决策。
- [ ] 高风险项有 P0/P1/P2/P3 或等价优先级、责任角色和关闭条件。
- [ ] 未把计划、静态检查或 dry-run 写成测试执行、全部通过或发布批准。
- [ ] 已说明剩余风险、停止/升级条件和下一步。

## 常见误区

- 只列检查点，不说明触发条件、预期关注点、责任角色、关闭条件和证据。
- 把相邻领域的指标或工具名当成质量指标的完整判断。
- 用未经说明的数字制造伪精确，或把相关性写成因果关系。
- 输入不完整时直接拒绝，或反过来假装结论已经确定。

## 最佳实践

- 从最可能造成业务损失、质量回退或决策阻塞的路径开始。
- 使用最小可验证实验缩小不确定性，并记录条件、版本、来源和证据。
- 让另一位工程师能够独立安装、执行和复核本 Skill 的产出。
