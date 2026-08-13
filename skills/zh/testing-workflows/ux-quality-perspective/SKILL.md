---
name: ux-quality-perspective
description: Use this skill when a quality stage needs a UX perspective on information architecture, interaction states, consistency, responsive behavior, or accessibility; triggers include UX 质量视角、用户体验评审 and UX quality perspective.
---

# UX 质量视角（中文版）

**英文版：** See the corresponding English skill.

## 何时使用

- 需要在某个质量阶段，以用户体验视角审视信息架构、交互状态、一致性、响应式行为或无障碍。
- 需要用界面、原型、用户流程或 UI 测试证据，将产品、设计、研发和 QA 的体验风险转化为可执行行动。

## 输入

- `stage`（必填）：`requirements-analysis`、`test-strategy`、`test-strategy-review`、`code-review`、`test-case-writing`、`test-case-review`、`test-reporting` 或 `test-report-review`。
- 原型、截图、界面说明、设计规范、用户流程、变更材料、测试资产或报告等已提供证据。
- 可选上下文：目标用户、设备/断点、辅助技术、设计系统、发布范围、已知限制。

## 执行流程

1. 验证 `stage`。缺失或不支持时返回“**不适用**”，说明支持阶段并请求有效值；不要生成填充式发现。
2. 仅加载并遵循下表中该 `stage` 对应的一个 Prompt；不得串读或合并多个阶段 Prompt。
3. 先依据材料判断适用性。`test-strategy`、`test-strategy-review`、`code-review`、`test-case-writing` 和 `test-reporting` 为**条件参与**：只有存在可追溯的 UI/UX 影响或相关体验证据时才分析。无 UI/UX 影响或证据时，返回“不适用”，说明原因、已知事实、缺口和重新评估所需材料，不写填充发现。
4. `requirements-analysis` 没有原型时仍可适用：仅报告可确认的需求事实、UX 证据缺口、待确认问题和需要补充的原型/流程/状态材料；不得虚构屏幕、状态、文案或跨设备行为。
5. 生成独立 UX 质量报告，明确区分事实、证据、推断和未验证项。

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

## UX 职责与边界

- 关注信息架构、导航、可发现性、交互反馈与状态、一致性、响应式行为和无障碍；以已提供 UI/UX 证据为基础。
- 不提供原型、流程、状态、断点或辅助技术证据时，标为未知或待确认；不得补造页面、控件、文案、错误状态、设备行为或测试结果。
- 不替代后端/前端实现正确性审查、API 可靠性或安全评估、测试执行、发布审批。无对应证据时，不得断言实现正确、接口可靠、安全、测试通过或可以发布。

## 报告合同

除非返回“不适用”，每份报告依次包含：**摘要、事实、证据、发现、风险、信息缺口、待确认问题、行动、信心等级**。发现、风险与行动按影响排序；每个结论说明其证据基础和责任角色。

## 交付前自检

- [ ] `stage` 已验证且只加载一个匹配 Prompt
- [ ] 已先做适用性判断；条件参与阶段不适用时没有填充发现
- [ ] 没有原型的需求分析只报告证据缺口，不虚构 UI
- [ ] 报告区分事实、证据、推断和缺口，并包含全部合同字段
- [ ] 未越界断言实现、接口、安全、测试或发布结论

## 按需加载

- 仅在 `stage` 有效后读取表中唯一对应的 `prompts/` 文件。
- 需要评测或回归时使用 `evals/` 并运行 skill-up 校验；不要把 eval 用例当项目事实。

## 常见误区

- 不要把通用 UX 清单伪装成当前产品的已证实缺陷。
- 不要因缺少原型而补造页面、状态或移动端行为。
- 不要把 UX 审视写成无证据的实现正确性、接口可靠性或发布结论。
