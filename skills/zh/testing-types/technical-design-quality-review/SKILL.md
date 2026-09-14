---
name: technical-design-quality-review
description: Use this skill when an architecture note, ADR, component design, or technical proposal needs an evidence-bounded quality review before implementation; triggers include 技术设计质量评审, technical design review, and design readiness review.
---

# 技术设计质量评审

在实现前从边界、依赖、失败模式、数据一致性、安全、性能、可观测性、兼容性、可维护性和验证准备度评审技术设计。它输出 `TD-##` 发现与验证准备，不审查未提供的代码，也不是架构批准或运行测试。

## 何时使用

- 需要评审 ADR、组件/数据流、技术方案或非功能约束是否足够可验证。
- 需要识别设计中的失败路径、依赖假设、兼容风险和证据缺口。
- 需要在材料不完整时形成带范围和假设的实施前质量初版。

不适用于直接运行构建、测试、生产探针或替 Human 选择最终架构。

## 工作方式

1. 阅读 `prompts/technical-design-quality-review.md`，先审计目标、版本、范围、来源和成功标准。
2. 将输入分为 `known`、`missing`、`conflicting`、`stale`、`out_of_scope`、`assumptions`。
3. 建立设计覆盖矩阵；每条重要缺口用 `TD-##` 绑定最小证据、影响、优先级和验证方法。
4. 分别输出事实、证据推断、建议和 Human 待决策，不把设计声明升级为实现结果。
5. 信息不足时保留受限结论和补证行动，避免用通用架构常识填空。

## 核心约束

- 不审查未提供的实现，不声称构建、兼容性、安全或性能测试已通过。
- 不凭组件名称推断数据一致性、容量、延迟、SLO、责任人或故障恢复行为。
- `TD-##` 至少包含主题、来源/证据、影响、优先级、缺口行动、责任角色、待决策问题和验证方式。
- 设计存在只能证明文档存在；真实执行证据必须有身份、时间、环境、输入和原始结果。

## 按需加载

- 每次产出前必须阅读 `prompts/technical-design-quality-review.md`。
- 回归时读取 `evals/eval.yaml` 与用例；静态设计评审不等于系统执行。
- 触发检查使用 `evals/trigger-prompts.csv` 和 `evals/local-rules.json`；没有 selection trace 时报告 `BLOCKED`。

## 交付前自检

- [ ] 已完成六类输入审计和设计范围声明
- [ ] 已覆盖边界、依赖/失败、数据、安全、性能、可观测、兼容、维护和验证准备度
- [ ] 每条 `TD-##` 有证据、影响、责任角色、行动和验证方式
- [ ] 已区分设计声明、证据推断、建议和 Human 决策
- [ ] 未把文档存在或静态检查写成实现/运行结果

## 常见误区

- 只检查架构图是否存在，不检查边界、失败和恢复条件。
- 把“支持高并发”“具备监控”等未定义声明当成验证标准。
- 把技术建议写成已经批准的架构或上线结论。
