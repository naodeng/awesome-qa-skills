---
name: product-quality-perspective
description: Use this skill when product-quality responsibility is needed across requirements, strategy, review, test-case, or reporting stages; triggers include 产品质量视角、产品质量评审 and product quality perspective.
---

# 产品质量视角（中文版）

**英文版：** See the corresponding English skill.

## 何时使用

- 需要从用户价值、业务规则、范围、验收与发布风险的产品视角审视某一质量阶段。
- 需要让产品、研发与 QA 基于同一事实、缺口和行动项推进质量决策。

## 输入

- `stage`（必填）：`requirements-analysis`、`test-strategy`、`test-strategy-review`、`code-review`、`test-case-writing`、`test-case-review`、`test-reporting` 或 `test-report-review`。
- 项目材料：需求、PR/Diff、测试资产、报告或其他已提供证据。
- 可选阶段上下文：目标用户、发布目标、范围、依赖、限制、已知风险。

## 执行流程

1. 验证 `stage`。若缺失或不在支持列表内，返回“**不适用**”，说明支持阶段并请求有效 `stage`；不要生成填充式发现。
2. 只加载并遵循下表中该 `stage` 对应的一个 Prompt；不得串读或合并多个阶段 Prompt。
3. 依据已提供材料先判断该阶段是否适用。材料不足或阶段不适用时，说明原因、已有事实、缺口和需要补充的材料，不生成虚构发现。
4. 生成一份独立的产品质量报告，并把事实、证据、推断和未验证项明确分开。

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

## 产品职责与边界

- 关注用户价值、业务规则、范围、验收标准、可理解性、一致性、决策风险与后续行动。
- 以项目材料为证据；没有材料时明确“未知”或“待确认”，不得补造规则、指标、测试结果、缺陷或代码行为。
- 不替代工程代码审查、测试设计/执行、安全评估或发布审批；没有相应证据时，不得判断代码正确性，也不得宣称测试已通过或发布可行。

## 报告合同

除非返回“不适用”，每份报告均包含：摘要、事实、证据、发现、风险、信息缺口、待确认问题、行动与信心等级。发现、风险与行动应按影响排序；结论要标明其证据基础。

## 交付前自检

- [ ] `stage` 已验证，且只加载了一个匹配 Prompt
- [ ] 已先判断适用性；不适用时没有填充发现
- [ ] 报告包含完整合同字段，并区分事实、证据、推断与缺口
- [ ] 未编造业务规则、代码正确性、测试通过或发布结论
- [ ] 行动项可由明确角色推进，信心等级反映证据完整度

## 按需加载

- 仅在 `stage` 有效后读取表中唯一对应的 `prompts/` 文件。
- 需要评测或回归时使用 `evals/` 并运行 skill-up 校验；不要把 eval 用例当项目事实。

## 常见误区

- 不要把产品质量视角写成无证据的代码评审或测试结论。
- 不要把“需求满足”误写成“代码正确”或“测试已通过”。
- 不要在材料不完整时用通用清单掩盖关键缺口。
