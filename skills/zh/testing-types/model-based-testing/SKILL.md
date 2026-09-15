---
name: model-based-testing
description: Use this skill when you need to derive test-path candidates from sourced behavior, state, or process models; triggers include 基于模型的测试设计 and model-based test design.
---

# 基于模型的测试设计

从有来源的行为模型、状态图或流程模型导出测试路径候选，输出 MBT-##。它只产生证据边界内的设计候选，不执行测试，不宣称覆盖或通过。

## 何时使用

- 需要分析 行为模型、状态/节点、事件、路径约束、模型版本和已有执行证据。
- 需要保留选择理由、证据缺口、优先级和验证动作。
- 输入不完整但需要交付受限初版，并标记 unassessed 或 blocked。

## 输出格式选项

- 默认输出 Markdown；表格、JSON 或 CSV 仅在用户明确需要或现有交付格式要求时使用。
- 把静态分析、未执行项、证据状态和 Human 决策分开；没有运行证据时保持 unassessed、blocked 或 NOT_RUN。

## 如何使用

1. 阅读 prompts/model-based-testing.md，先列出 known、missing、conflicting、stale、out_of_scope、assumptions。
2. 按方法合同形成 MBT-##，保留来源、证据状态、影响、责任角色、关闭条件和验证方法。
3. 事实、推断、建议和 Human 决策必须分开。
4. 只提出后续验证意图，不写成已执行结果。

## 核心约束

- 不创造模型节点、路径或版本，不把模型静态存在当作运行结果。
- 文件存在、名称、模板和 Eval 配置不等于真实执行证据。
- 不修改需求、代码、测试资产或目标系统，不替 Human 接受风险。

## 交付前自检

- [ ] 六类输入审计完整。
- [ ] 每条 MBT-## 有来源、证据、影响/优先级、责任角色、关闭条件和验证方法。
- [ ] 已明确未执行、未验证、未评估和待决策项。

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
