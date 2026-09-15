---
name: api-negative-testing
description: Use this skill when you need to design evidence-bounded API failure and rejection scenarios; triggers include API 负向测试 and API negative testing.
---

# API 负向测试

从契约、约束和错误证据中设计非法输入、拒绝和降级候选，输出 ANT-## 发现。它只整理可追溯的 API 质量候选，不执行测试，也不把设计清单写成覆盖、通过或发布证据。

## 何时使用

- 需要从 API 契约、认证授权约束、参数规则、错误码、限流规则、历史缺陷和原始响应 中提取 API 负向测试 候选。
- 需要解释选择理由、适用约束、证据缺口和最小验证动作。
- 材料不完整但仍要交付受限初版，并明确 blocked 或 unassessed 边界。

不适用于直接执行测试、生成无来源的契约或行为、替代完整测试策略，或替 Human 接受风险。

## 输出格式选项

- 默认输出 Markdown；表格、JSON 或 CSV 仅在用户明确需要或现有交付格式要求时使用。
- 把静态分析、未执行项、证据状态和 Human 决策分开；没有运行证据时保持 unassessed、blocked 或 NOT_RUN。

## 如何使用

1. 阅读 prompts/api-negative-testing.md，并提供目标、范围、材料、环境和已有证据。
2. 先完成 known、missing、conflicting、stale、out_of_scope、assumptions 六类输入审计。
3. 用 ANT-## 记录对象、前置条件、关注行为、来源证据和验证方法，保留影响/优先级、责任角色、关闭条件和证据状态。
4. 材料冲突、缺少约束或没有执行证据时，保留双方和待确认问题。

## 核心约束

- 不执行测试，不假设未提供的规则、版本、阈值、数据或响应，不把候选数量当作覆盖证明。
- 文件存在、名称匹配、设计声明或 Eval 配置不等于真实执行证据。
- 未知项标为 unassessed、blocked 或待确认，不用常识补齐。
- 不修改需求、代码、测试资产或目标系统。

## 交付前自检

- [ ] 已记录 known、missing、conflicting、stale、out_of_scope、assumptions 六类输入审计。
- [ ] 每条 ANT-## 有来源、证据状态、影响/优先级、责任角色、关闭条件和验证方法。
- [ ] 已区分事实、推断、建议、未执行和 Human 决策。
- [ ] 未把设计候选写成执行结果、覆盖证明或发布结论。

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
