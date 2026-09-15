---
name: state-transition-testing
description: Use this skill when you need to derive test candidates for reachable, unreachable, and abnormal transitions from states, events, guards, and actions; triggers include 状态迁移测试设计 and state transition test design.
---

# 状态迁移测试设计

从状态、事件、守卫和动作中发现可达、不可达及异常迁移的测试候选，输出 STT-## 发现。它只整理可追溯的测试设计候选，不执行测试，也不把设计清单写成覆盖、通过或发布证据。

## 何时使用

- 需要从 状态模型、事件、守卫条件、动作、角色、错误迁移和状态持久化证据 中提取 状态迁移测试设计 候选。
- 需要解释选择理由、适用约束、证据缺口和最小验证动作。
- 材料不完整但仍要交付受限初版，并明确 blocked 或 unassessed 边界。

不适用于直接执行测试、生成无来源规则、替代完整测试策略或替 Human 接受风险。

## 输出格式选项

- 默认输出 Markdown；表格、JSON 或 CSV 仅在用户明确需要或现有交付格式要求时使用。
- 把静态分析、未执行项、证据状态和 Human 决策分开；没有运行证据时保持 unassessed、blocked 或 NOT_RUN。

## 如何使用

1. 阅读 prompts/state-transition-testing.md，并提供目标、范围、材料、环境和已有证据。
2. 先完成 known、missing、conflicting、stale、out_of_scope、assumptions 六类输入审计。
3. 用 STT-## 记录 状态、事件、前置守卫、动作、目标状态、可达性、来源证据和验证方法，保留来源、证据状态、影响/优先级、责任角色、关闭条件和验证方法。
4. 材料冲突、缺少约束或没有执行证据时，保留双方和待确认问题。

## 核心约束

- 不创造状态或事件，不把静态状态图当成运行结果，不声称所有路径已执行。
- 文件存在、名称匹配、设计声明或 Eval 配置不等于真实执行证据。
- 未知项标为 unassessed、blocked 或待确认，不用常识补齐。
- 不修改需求、代码、测试资产或目标系统。

## 交付前自检

- [ ] 已记录六类输入审计。
- [ ] 每条 STT-## 有来源、最小证据、影响/优先级、责任角色、关闭条件和验证方法。
- [ ] 已区分事实、推断、建议、未执行和 Human 决策。
- [ ] 未把设计候选写成完整测试、执行结果、覆盖证明或发布结论。

## 参考文件

- 回归时读取 evals/eval.yaml 和匹配用例；配置不证明真实项目结果。
- 触发验证使用 evals/trigger-prompts.csv 和 evals/local-rules.json；缺少 skill.selection 证据时报告 BLOCKED。

## 常见误区

- 范围或证据不完整时，不要把方法名称、文件存在或候选数量写成测试已执行、覆盖、通过或发布证据。
- 不要用常识补齐未提供的规则、阈值、数据、环境或结果；保留 unassessed、blocked 和待确认项。
- 不要把本 Skill 的专项候选扩写成完整策略、完整测试用例、真实执行或发布决定。

## 最佳实践

- 先完成六类输入审计，再选择最小、可追溯且可验证的发现范围。
- 每条发现保留来源、证据状态、影响/优先级、责任角色、关闭条件和验证方法，并明确剩余风险。
- 把验证建议写成下一步动作，不把 Skill 包结构、候选数量或本地 Eval 配置升级为真实质量结论。
