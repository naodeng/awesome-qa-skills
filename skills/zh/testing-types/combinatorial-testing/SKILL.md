---
name: combinatorial-testing
description: Use this skill when you need to select high-risk multi-factor combinations after factors, values, and constraints are explicit; triggers include 组合测试设计 and combinatorial test design.
---

# 组合测试设计

在因素、取值和约束明确后选择高风险的多因素组合，输出 CT-##。它只产生证据边界内的设计候选，不执行测试，不宣称覆盖或通过。

## 何时使用

- 需要分析 因素、取值、组合约束、交互风险和已有组合。
- 需要保留选择理由、证据缺口、优先级和验证动作。
- 输入不完整但需要交付受限初版，并标记 unassessed 或 blocked。

## 如何使用

1. 阅读 prompts/combinatorial-testing.md，先列出 known、missing、conflicting、stale、out_of_scope、assumptions。
2. 按方法合同形成 CT-##，保留来源、证据状态、影响、责任角色、关闭条件和验证方法。
3. 事实、推断、建议和 Human 决策必须分开。
4. 只提出后续验证意图，不写成已执行结果。

## 核心约束

- 不把多因素组合数量写成覆盖证明，不忽略约束或凭经验补造取值。
- 文件存在、名称、模板和 Eval 配置不等于真实执行证据。
- 不修改需求、代码、测试资产或目标系统，不替 Human 接受风险。

## 交付前自检

- [ ] 六类输入审计完整。
- [ ] 每条 CT-## 有来源、证据、影响/优先级、责任角色、关闭条件和验证方法。
- [ ] 已明确未执行、未验证、未评估和待决策项。
