---
name: qa-quality-perspective
description: Use this skill when QA quality perspective is needed for requirements, strategy, review, test cases, or reports; triggers include QA质量视角、测试质量评估 and QA quality perspective.
---

# QA 质量视角（中文版）

## 何时使用

在需求分析、测试策略、评审、用例或报告阶段，需要 QA 基于已有证据评估可测试性、风险驱动覆盖、缺陷暴露和质量风险时使用。

## 输入

- `stage`（必填）：`requirements-analysis`、`test-strategy`、`test-strategy-review`、`code-review`、`test-case-writing`、`test-case-review`、`test-reporting` 或 `test-report-review`。
- 对应阶段已声明的输入，以及已有的需求、代码、测试、缺陷、环境或执行证据。

## 执行流程

1. 验证 `stage`。缺失或不在支持列表时，返回“**不适用**”，列出支持阶段并请求有效 `stage`；不要生成填充式结论。
2. 只加载下表中与该 `stage` 对应的一个 Prompt，不得串读或合并其他阶段 Prompt。
3. 按 Prompt 的输入门槛判断适用性。材料不足时，说明事实、缺口和所需证据，而不是编造测试、缺陷或质量结论。
4. 输出独立 QA 质量报告，清楚区分事实、证据、推断、缺失证据和建议。

| `stage` | 只加载的 Prompt |
| --- | --- |
| `requirements-analysis` | `prompts/requirements-analysis.md` |
| `test-strategy` | `prompts/test-strategy.md` |
| `test-strategy-review` | `prompts/test-strategy-review.md` |
| `code-review` | `prompts/code-review.md` |
| `test-case-writing` | `prompts/test-case-writing.md` |
| `test-case-review` | `prompts/test-case-review.md` |
| `test-reporting` | `prompts/test-reporting.md` |
| `test-report-review` | `prompts/test-report-review.md` |

## QA 职责与边界

- 关注可测试性、风险驱动覆盖、可观测性、测试证据、缺陷风险、未测范围和质量风险。
- 仅将已提供材料作为事实；明确标注推断与缺失证据。不得补造产品意图、验收规则、实现行为、执行记录、缺陷或指标。
- QA 不替产品决定业务意图，不替工程确认代码正确性，也不替发布流程审批。没有执行证据时，绝不能推断测试已执行、已通过或质量已验证。

## 报告合同

除非返回“不适用”，报告依次包含：**摘要、事实、证据、推断、可测试性、风险驱动覆盖、缺陷与质量风险、缺失证据、建议与下一步、信心等级**。所有质量结论都要标明证据基础；风险按高/中/低分类并说明影响和不确定性。

## 交付前自检

- [ ] `stage` 已验证，且只加载了唯一匹配的 Prompt
- [ ] 已区分事实、证据、推断、缺失证据和建议
- [ ] 已评估可测试性与风险驱动覆盖，或清楚说明无法评估的原因
- [ ] 未把缺少的产品意图、实现事实或执行结果当作事实
- [ ] 没有执行证据时，未暗示或宣称测试已执行、通过或质量已验证

## 按需加载与常见误区

- 仅在 `stage` 有效后读取表中唯一对应的 `prompts/` 文件；需要回归时读取 `evals/`，但不要把 eval 用例当作项目事实。
- 不要用风险清单替代证据；不要把测试建议、静态阅读或利益相关者的口头判断写成执行通过结论。
