---
name: disaster-recovery-testing
description: Use this skill when you need evidence-bounded disaster-recovery-testing analysis and validation preparation; triggers include 灾备测试 and disaster-recovery-testing.
---

# 灾备测试（中文版）

## 何时使用

- 需要围绕灾难场景、恢复优先级、备份证据、Runbook 和恢复验证设计测试分析或验证准备。
- 需要在资料不完整时交付可复核的初版，并明确假设、缺口和人工决策。
- 需要区分静态设计证据、计划中的验证和已经发生的执行。

## 输出格式选项

- 默认输出 Markdown，按风险、证据和优先级组织。
- 用户要求表格、CSV、JSON 或工单格式时，保留同样的发现字段和证据状态。
- 输出进入自动化流程前，先确认字段 schema、枚举值和必填项。

## 如何使用

1. 先读取 prompts/disaster-recovery-testing.md，按其中的输入审计、覆盖清单和输出顺序执行。
2. 提取范围、环境、版本、依赖、限制、成功标准和可用证据。
3. 对灾难场景、恢复优先级、备份证据、Runbook 和恢复验证建立场景和判断标准，优先处理高影响或难探测项。
4. 把事实、证据支持的推断、候选建议和 Human 决策分开。
5. 信息不足时交付受限初版，并列出最小补证动作，不把建议写成执行结果。

## 参考文件

- 每次执行必须读取 prompts/disaster-recovery-testing.md；它是本 Skill 的完整执行规范。
- 需要评测时读取 evals/eval.yaml 和匹配的 evals/cases/。
- 只有目录实际存在且任务需要时，才读取 references/、examples/、scripts/ 或 output-formats.md。

## 核心约束

- 只分析灾难场景、恢复优先级、备份证据、Runbook 和恢复验证，不注入故障、不访问真实依赖、不调用生产系统。
- 不编造阈值、可用性、恢复时间、漏洞状态或已经执行的测试。
- 证据不足时使用待确认、blocked 或 unassessed，并给出验证方法。
- 任何风险接受、发布批准和人工接管都必须留给 Human。

## 交付前自检

- [ ] 已完成六类输入审计并标出证据时效性。
- [ ] 已覆盖灾备目标、失败模式、预期关注点和验证方法。
- [ ] 已区分事实、推断、建议、缺口和 Human 决策。
- [ ] 未把静态设计或 dry-run 写成真实执行、通过或发布结论。

## 常见误区

- 把相邻性能、事故或 API 分析当成灾备测试的完整替代。
- 只列步骤，不写触发条件、预期结果、责任角色和关闭条件。
- 信息不足时直接拒绝，或用模板假设补齐关键事实。

## 最佳实践

- 先从最可能造成业务损失或恢复失败的路径开始。
- 使用最小、隔离、可回滚的验证建议，并记录停止条件。
- 让另一位工程师可以依据证据和边界复核每个结论。
