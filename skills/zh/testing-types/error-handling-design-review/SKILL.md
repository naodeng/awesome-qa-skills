---
name: error-handling-design-review
description: Use this skill when error taxonomy, retries, timeouts, fallback, or recovery design needs an evidence-bounded review before implementation; triggers include 错误处理设计评审, error handling design review, and failure-path review.
---

# 错误处理设计评审

在实现前评审错误分类、异常边界、超时、重试/退避、熔断、降级、幂等、事务一致性、错误传播、消费者契约、遥测和恢复设计。输出 `EH-##` 失败模式发现与验证准备，不执行故障注入或复盘真实事故。

## 何时使用

- 需要识别不同失败模式的预期行为、传播、重试条件和人工接管路径。
- 需要检查错误消息、状态、数据一致性、遥测、恢复和消费者契约。
- 需要在错误设计不完整时形成有证据边界的初版。

不适用于直接执行故障注入、替 Human 决定 SLA/文案/风险接受或把代码存在当成正确。

## 工作方式

1. 阅读 `prompts/error-handling-design-review.md`，审计目标、错误边界、版本、来源和证据。
2. 将输入归入 `known`、`missing`、`conflicting`、`stale`、`out_of_scope`、`assumptions`。
3. 按失败模式建立矩阵，使用 `EH-##` 保留触发、边界、预期行为、传播、重试/降级条件和数据影响。
4. 分离事实、证据推断、建议和 Human 决策；区分可重试、不可重试、人工接管和安全拒绝。
5. 信息不足时输出受限初版和最小验证动作，不把一个通用错误响应扩展为全部路径。

## 核心约束

- 不执行故障注入，不声称真实事故、恢复、SLA 或错误率已验证。
- 不把异常类、状态码、错误处理代码或文档存在当成行为正确。
- 每条 `EH-##` 至少包含失败模式、触发、边界、预期行为、传播/翻译、重试/回退、数据一致性、可观察证据、责任角色和验证方式。
- 缺少执行身份、时间、环境、输入和原始结果时标记 `unverified`、`unexecuted` 或 `unassessed`。

## 按需加载

- 每次产出前必须阅读 `prompts/error-handling-design-review.md`。
- 回归时读取 `evals/eval.yaml` 与用例；设计评审不等于真实事故分析或故障注入。
- 触发检查使用 `evals/trigger-prompts.csv` 和 `evals/local-rules.json`；缺少 selection trace 时报告 `BLOCKED`。

## 交付前自检

- [ ] 已完成六类输入审计和失败范围声明
- [ ] 已区分可重试、不可重试、人工接管和安全拒绝
- [ ] 每条 `EH-##` 有触发、预期行为、影响、责任角色和验证
- [ ] 已检查传播、幂等、数据一致性、遥测和恢复
- [ ] 未把单一错误响应或静态代码存在写成处理设计完整/正确

## 常见误区

- 一个“返回错误”覆盖所有超时、依赖失败、数据冲突和权限拒绝。
- 把重试次数写成常识，不检查幂等、退避、预算和重复副作用。
- 把日志存在当成恢复可见性或事故已解决。
