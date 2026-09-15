---
name: property-based-testing
description: Use this skill when you need to turn invariants, generation domains, and shrinking strategies into reviewable property-test candidates; triggers include 性质测试设计 and property-based test design.
---

# 性质测试设计

把不变量、生成域和收缩策略整理为可复核的性质测试候选，输出 PBT-##。它只产生证据边界内的设计候选，不执行测试，不宣称覆盖或通过。

## 何时使用

- 需要分析 领域不变量、输入生成域、约束、失败样例、收缩策略和已有性质。
- 需要保留选择理由、证据缺口、优先级和验证动作。
- 输入不完整但需要交付受限初版，并标记 unassessed 或 blocked。

## 如何使用

1. 阅读 prompts/property-based-testing.md，先列出 known、missing、conflicting、stale、out_of_scope、assumptions。
2. 按方法合同形成 PBT-##，保留来源、证据状态、影响、责任角色、关闭条件和验证方法。
3. 事实、推断、建议和 Human 决策必须分开。
4. 只提出后续验证意图，不写成已执行结果。

## 核心约束

- 不发明不变量、生成域或收缩结果，不把生成器存在当成失败已发现。
- 文件存在、名称、模板和 Eval 配置不等于真实执行证据。
- 不修改需求、代码、测试资产或目标系统，不替 Human 接受风险。

## 交付前自检

- [ ] 六类输入审计完整。
- [ ] 每条 PBT-## 有来源、证据、影响/优先级、责任角色、关闭条件和验证方法。
- [ ] 已明确未执行、未验证、未评估和待决策项。
