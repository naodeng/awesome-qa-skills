---
name: property-based-testing
description: Use this skill when you need to turn invariants, generation domains, and shrinking strategies into reviewable property-test candidates; triggers include property-based test design.
---

# Property-Based Test Design

turn invariants, generation domains, and shrinking strategies into reviewable property-test candidates，输出 PBT-##。它只产生证据边界内的设计候选，不执行测试，不宣称覆盖或通过。

## 何时使用

- 需要分析 domain invariants, input generation domains, constraints, failure examples, shrinking strategies, and existing properties。
- 需要保留选择理由、证据缺口、优先级和验证动作。
- 输入不完整但需要交付受限初版，并标记 unassessed 或 blocked。

## 如何使用

1. 阅读 prompts/property-based-testing.md，先列出 known、missing、conflicting、stale、out_of_scope、assumptions。
2. 按方法合同形成 PBT-##，保留来源、证据状态、影响、责任角色、关闭条件和验证方法。
3. 事实、推断、建议和 Human 决策必须分开。
4. 只提出后续验证意图，不写成已执行结果。

## 核心约束

- Do not invent invariants, generation domains, or shrink results, or treat a generator as proof of a finding.
- 文件存在、名称、模板和 Eval 配置不等于真实执行证据。
- 不修改需求、代码、测试资产或目标系统，不替 Human 接受风险。

## 交付前自检

- [ ] 六类输入审计完整。
- [ ] 每条 PBT-## 有来源、证据、影响/优先级、责任角色、关闭条件和验证方法。
- [ ] 已明确未执行、未验证、未评估和待决策项。
