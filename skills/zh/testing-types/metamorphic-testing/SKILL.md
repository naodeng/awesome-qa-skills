---
name: metamorphic-testing
description: Use this skill when you need to derive test candidates from input transformations and expected relations when a direct oracle is limited; triggers include 蜕变测试设计 and metamorphic test design.
---

# 蜕变测试设计

从输入变换与预期关系中发现缺少可靠预言机时的测试候选，输出 MT-##。它只产生证据边界内的设计候选，不执行测试，不宣称覆盖或通过。

## 何时使用

- 需要分析 基准输入、变换规则、预期关系、输出不变量、随机性和已有证据。
- 需要保留选择理由、证据缺口、优先级和验证动作。
- 输入不完整但需要交付受限初版，并标记 unassessed 或 blocked。

## 如何使用

1. 阅读 prompts/metamorphic-testing.md，先列出 known、missing、conflicting、stale、out_of_scope、assumptions。
2. 按方法合同形成 MT-##，保留来源、证据状态、影响、责任角色、关闭条件和验证方法。
3. 事实、推断、建议和 Human 决策必须分开。
4. 只提出后续验证意图，不写成已执行结果。

## 核心约束

- 不发明变换关系、输出结果或随机性结论，不把关系表当成执行证明。
- 文件存在、名称、模板和 Eval 配置不等于真实执行证据。
- 不修改需求、代码、测试资产或目标系统，不替 Human 接受风险。

## 交付前自检

- [ ] 六类输入审计完整。
- [ ] 每条 MT-## 有来源、证据、影响/优先级、责任角色、关闭条件和验证方法。
- [ ] 已明确未执行、未验证、未评估和待决策项。
