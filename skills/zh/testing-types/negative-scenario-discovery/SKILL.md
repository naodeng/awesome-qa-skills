---
name: negative-scenario-discovery
description: Use this skill when you need to discover invalid, denied, failed, degraded, or unsafe-recovery scenarios from product evidence; triggers include 负向场景发现 and negative scenario discovery.
---

# 负向场景发现

从功能目标、输入约束、权限、依赖失败契约、超时/重试、幂等/事务和恢复设计中发现需要验证的失败、拒绝、降级和不安全恢复路径，输出 `NS-##`。它不写完整测试用例、不执行故障注入、不发明错误码，也不宣布系统行为正确。

## 何时使用

- 需要检查非法输入、未授权、依赖失败、超时、重试耗尽、重复请求、部分失败和数据不一致。
- 需要从设计或历史故障中发现 happy path 之外的失败刺激和可见结果。
- 需要在失败契约不完整时整理证据缺口、恢复选择和 Human 待决事项。

不适用于只发现边界值、编写完整用例、执行故障注入、复盘真实事故或替团队决定最终错误文案/SLA。

## 工作方式

1. 阅读并遵循 `prompts/negative-scenario-discovery.md`，先做六类输入审计。
2. 分析失败模式、触发刺激、前置条件、预期拒绝/降级/重试/人工接管和数据一致性影响。
3. 用 `NS-##` 记录来源、证据状态、优先级、调用方可见结果和验证方法。
4. 区分产品明确契约、基于证据的推断、待确认选择和执行前提。
5. 信息不足时交付受限失败路径，不把建议写成已验证行为。

## 核心约束

- 必须区分 invalid input、unauthorized、dependency failure、timeout、retry exhaustion、duplicate request、partial failure 和 unsafe recovery（适用时）。
- 不执行故障注入，不调用真实依赖，不修改数据或目标系统。
- 不发明错误码、重试次数、超时阈值、用户文案、SLA 或恢复批准。
- `NS-##` 是负向候选和证据需求，不是已执行、已通过、已恢复或安全证明。
- 不把负向场景发现扩写成完整测试用例或事故根因结论。

## 按需加载

- 每次产出前必须阅读 `prompts/negative-scenario-discovery.md`。
- 回归时读取 `evals/eval.yaml` 和匹配用例；配置不证明故障路径已执行。
- 触发验证使用 `evals/trigger-prompts.csv` 和 `evals/local-rules.json`；缺少 selection trace 时报告 `BLOCKED`。

## 交付前自检

- [ ] 已记录已知事实、信息缺口、冲突、过期信息、范围外和假设。
- [ ] 每条 `NS-##` 有失败模式、触发、前置、预期行为、可见结果、数据影响和证据需求。
- [ ] 已区分可重试、不可重试、人工接管和安全拒绝。
- [ ] 未执行故障注入、未编造错误码/阈值/恢复结果。
- [ ] 未将候选清单写成完整用例、测试通过、事故结论或发布批准。

## 常见误区

- 用一个“返回错误”覆盖所有失败模式。
- 只列异常名称，不说明触发条件、数据一致性和可见结果。
- 把代码存在或示例响应当作错误契约完整。
- 为了给出确定答案擅自决定重试、降级、SLA 或人工接管策略。
