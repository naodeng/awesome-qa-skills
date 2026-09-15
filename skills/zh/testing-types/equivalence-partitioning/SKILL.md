---
name: equivalence-partitioning
description: Use this skill when you need to partition inputs into evidence-backed valid, invalid, and unknown classes based on constraints, rules, and response differences; triggers include 等价类划分测试设计 and equivalence partitioning test design.
---

# 等价类划分测试设计

依据输入约束、业务规则和响应差异划分有证据的有效、无效和未知等价类，输出 EP-## 发现。它只整理可追溯的测试设计候选，不执行测试，也不把设计清单写成覆盖、通过或发布证据。

## 何时使用

- 需要从 输入约束、字段类型、业务规则、角色/状态差异、错误契约和已有用例 中提取 等价类划分测试设计 候选。
- 需要解释选择理由、适用约束、证据缺口和最小验证动作。
- 材料不完整但仍要交付受限初版，并明确 blocked 或 unassessed 边界。

不适用于直接执行测试、生成无来源规则、替代完整测试策略或替 Human 接受风险。

## 如何使用

1. 阅读 prompts/equivalence-partitioning.md，并提供目标、范围、材料、环境和已有证据。
2. 先完成 known、missing、conflicting、stale、out_of_scope、assumptions 六类输入审计。
3. 用 EP-## 记录 等价类、判定依据、代表值、有效/无效状态、来源证据、预期关注点和验证方法，保留来源、证据状态、影响/优先级、责任角色、关闭条件和验证方法。
4. 材料冲突、缺少约束或没有执行证据时，保留双方和待确认问题。

## 核心约束

- 不因字段名相似就合并类别，不补造错误码或规则，不把每类一个代表值当成完整覆盖。
- 文件存在、名称匹配、设计声明或 Eval 配置不等于真实执行证据。
- 未知项标为 unassessed、blocked 或待确认，不用常识补齐。
- 不修改需求、代码、测试资产或目标系统。

## 交付前自检

- [ ] 已记录六类输入审计。
- [ ] 每条 EP-## 有来源、最小证据、影响/优先级、责任角色、关闭条件和验证方法。
- [ ] 已区分事实、推断、建议、未执行和 Human 决策。
- [ ] 未把设计候选写成完整测试、执行结果、覆盖证明或发布结论。

## 参考文件

- 回归时读取 evals/eval.yaml 和匹配用例；配置不证明真实项目结果。
- 触发验证使用 evals/trigger-prompts.csv 和 evals/local-rules.json；缺少 skill.selection 证据时报告 BLOCKED。
