---
name: api-error-contract-testing
description: Use this skill when you need to review API error shape, status, code, and disclosure behavior against sourced contracts; triggers include API 错误契约测试 and API error contract testing.
---

# API 错误契约测试

从错误契约、状态码、错误码、字段结构和敏感信息证据设计一致性候选，输出 AEC-## 发现。它只整理可追溯的 API 质量候选，不执行测试，也不把设计清单写成覆盖、通过或发布证据。

## 何时使用

- 需要从 错误响应 Schema、HTTP 状态码约定、错误码目录、鉴权规则、日志和脱敏要求 中提取 undefined 候选。
- 需要解释选择理由、适用约束、证据缺口和最小验证动作。
- 材料不完整但仍要交付受限初版，并明确 blocked 或 unassessed 边界。

不适用于直接执行测试、生成无来源的契约或行为、替代完整测试策略，或替 Human 接受风险。

## 如何使用

1. 阅读 prompts/api-error-contract-testing.md，并提供目标、范围、材料、环境和已有证据。
2. 先完成 known、missing、conflicting、stale、out_of_scope、assumptions 六类输入审计。
3. 用 AEC-## 记录对象、前置条件、关注行为、来源证据和验证方法，保留影响/优先级、责任角色、关闭条件和证据状态。
4. 材料冲突、缺少约束或没有执行证据时，保留双方和待确认问题。

## 核心约束

- 不执行测试，不假设未提供的规则、版本、阈值、数据或响应，不把候选数量当作覆盖证明。
- 文件存在、名称匹配、设计声明或 Eval 配置不等于真实执行证据。
- 未知项标为 unassessed、blocked 或待确认，不用常识补齐。
- 不修改需求、代码、测试资产或目标系统。

## 交付前自检

- [ ] 已记录 known、missing、conflicting、stale、out_of_scope、assumptions 六类输入审计。
- [ ] 每条 AEC-## 有来源、证据状态、影响/优先级、责任角色、关闭条件和验证方法。
- [ ] 已区分事实、推断、建议、未执行和 Human 决策。
- [ ] 未把设计候选写成执行结果、覆盖证明或发布结论。

## 参考文件

- 回归时读取 evals/eval.yaml 和匹配用例；配置不证明真实项目结果。
- 触发验证使用 evals/trigger-prompts.csv 和 evals/local-rules.json；缺少 skill.selection 证据时报告 BLOCKED。
