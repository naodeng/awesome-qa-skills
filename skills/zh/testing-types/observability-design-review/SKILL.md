---
name: observability-design-review
description: Use this skill when logging, metrics, tracing, alerting, or SLO design needs an evidence-bounded review before implementation; triggers include 可观测性设计评审, observability design review, and telemetry readiness review.
---

# 可观测性设计评审

在实现前评审日志、指标、Trace、上下文传播、SLO/SLI、告警、仪表板、采样、保留、隐私和成本设计。输出 `OBS-##` 发现与验证准备，不读取真实运行信号宣布健康，也不替团队决定 SLO 或事故等级。

## 何时使用

- 需要检查信号、字段/维度、语义、关联 ID、采样和保留设计是否可行动。
- 需要发现敏感信息、基数、告警噪声、盲区和成本风险。
- 需要在没有运行数据时评审观测设计，而不是伪造运行结论。

不适用于查询生产日志、执行探针、分析真实事故或宣布系统健康。

## 输出格式选项

- 默认输出 Markdown；用户要求表格、CSV 或 JSON 时，保留相同的证据、状态、影响、责任角色和验证字段。
- 不把结构化格式或静态清单写成执行、通过、批准或发布证据。

## 如何使用

1. 先读取本 Skill 的主 Prompt，并提供目标、范围、材料、环境和已有证据。
2. 按 Prompt 的输入审计和输出合同执行；缺少信息时交付带边界的初版。
3. 对每条发现保留来源、证据状态、影响、责任角色、关闭条件和验证方法。

## 工作方式

1. 阅读 `prompts/observability-design-review.md`，审计目标、服务范围、时间窗口、隐私和来源。
2. 将输入归入 `known`、`missing`、`conflicting`、`stale`、`out_of_scope`、`assumptions`。
3. 按信号和服务建立覆盖矩阵，使用 `OBS-##` 记录字段语义、检测动作、影响、责任角色和证据。
4. 分离设计事实、证据推断、建议和 Human 决策；没有运行信号时标记 `unverified` 或 `unassessed`。
5. 对敏感字段、无限基数、采样缺口和不可行动告警提出最小安全验证。

## 核心约束

- 不读取或修改真实生产信号，不执行探针，不把仪表板存在写成告警有效。
- 不默认选择 SLO、事故等级、采样率、保留期、成本预算或责任人。
- 每条 `OBS-##` 至少包含信号、对象、字段/维度、语义、来源/证据、缺口、影响、检测动作和验证方法。
- 未提供运行身份、时间、环境和原始信号时，运行结论只能是 `unverified`、`unexecuted` 或 `unassessed`。

## 参考文件

- 每次产出前必须阅读 `prompts/observability-design-review.md`。
- 回归时读取 `evals/eval.yaml` 与用例；设计检查不等于日志、Trace 或指标分析。
- 触发检查使用 `evals/trigger-prompts.csv` 和 `evals/local-rules.json`；缺 selection trace 时报告 `BLOCKED`。

## 最佳实践

- 优先处理高影响且可验证的缺口，使用最小实验或补证动作降低不确定性。
- 将事实、证据支持的推断、建议和 Human 决策分开，避免把假设升级为结论。

## 交付前自检

- [ ] 已审计服务、信号、范围、隐私、成本和证据
- [ ] 已覆盖日志、指标、Trace、传播、SLO/SLI、告警、仪表板、采样、保留和敏感数据
- [ ] 每条 `OBS-##` 有字段语义、影响、责任角色和验证方法
- [ ] 已区分设计存在与真实运行信号
- [ ] 没有替团队决定 SLO、事故等级或风险接受

## 常见误区

- 把有 dashboard 当成有可行动告警。
- 只列信号名称，不定义字段、维度、语义和关联方式。
- 忽略敏感信息、基数、采样、保留和成本约束。
