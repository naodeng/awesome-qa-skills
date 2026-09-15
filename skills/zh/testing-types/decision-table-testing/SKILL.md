---
name: decision-table-testing
description: Use this skill when you need to turn conditions, rules, actions, and outcomes into an auditable set of rule combinations; triggers include 决策表测试设计 and decision table test design.
---

# 决策表测试设计

把条件、规则、动作和结果整理为可审计的规则组合，输出 DTT-## 发现。它只整理可追溯的测试设计候选，不执行测试，也不把设计清单写成覆盖、通过或发布证据。

## 何时使用

- 需要从 业务规则、条件、动作、例外、优先级、适用范围和已有测试材料 中提取 决策表测试设计 候选。
- 需要解释选择理由、适用约束、证据缺口和最小验证动作。
- 材料不完整但仍要交付受限初版，并明确 blocked 或 unassessed 边界。

不适用于直接执行测试、生成无来源规则、替代完整测试策略或替 Human 接受风险。

## 如何使用

1. 阅读 prompts/decision-table-testing.md，并提供目标、范围、材料、环境和已有证据。
2. 先完成 known、missing、conflicting、stale、out_of_scope、assumptions 六类输入审计。
3. 用 DTT-## 记录 规则 ID、条件组合、适用范围、动作/结果、例外、来源证据和验证方法，保留来源、证据状态、影响/优先级、责任角色、关闭条件和验证方法。
4. 材料冲突、缺少约束或没有执行证据时，保留双方和待确认问题。

## 核心约束

- 不执行表中的测试，不假设未提供的规则，不把表格行数当作覆盖证明。
- 文件存在、名称匹配、设计声明或 Eval 配置不等于真实执行证据。
- 未知项标为 unassessed、blocked 或待确认，不用常识补齐。
- 不修改需求、代码、测试资产或目标系统。

## 交付前自检

- [ ] 已记录六类输入审计。
- [ ] 每条 DTT-## 有来源、最小证据、影响/优先级、责任角色、关闭条件和验证方法。
- [ ] 已区分事实、推断、建议、未执行和 Human 决策。
- [ ] 未把设计候选写成完整测试、执行结果、覆盖证明或发布结论。

## 参考文件

- 回归时读取 evals/eval.yaml 和匹配用例；配置不证明真实项目结果。
- 触发验证使用 evals/trigger-prompts.csv 和 evals/local-rules.json；缺少 skill.selection 证据时报告 BLOCKED。
