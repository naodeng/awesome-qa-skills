---
name: technical-quality-perspective
description: Use this skill when technical quality perspective is needed for requirements, strategy, code, test cases, or reports; triggers include 技术质量视角、技术评审、架构评审 and code review.
---

# 技术质量视角（中文版）

## 何时使用

在交付阶段需要基于已声明的架构、API、数据、代码、安全、性能、兼容性和可观测性证据，评估技术质量时使用。

## 输入与执行流程

- `stage` 必填：`requirements-analysis`、`test-strategy`、`test-strategy-review`、`code-review`、`test-case-writing`、`test-case-review`、`test-reporting` 或 `test-report-review`。
- 验证 `stage`；缺失或不支持时返回“**不适用**”、列出支持值并请求有效阶段。只加载唯一映射的 Prompt。
- `code-review` 必须同时具备代码身份（PR、提交、分支、发布版本或等价物）和可审查变更（diff、文件或代码）。任一缺失即阻断评审，不得推断发现或合并就绪状态。
- 按所选 Prompt 的适用门槛处理；只把提供材料作为事实，标注推断，并把缺失材料转化为问题和行动。

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

## 职责与边界

- 仅在所选阶段相关且有证据时，覆盖架构、API、数据、兼容性、安全、性能、可观测性和可维护性。
- 产出含证据、影响、严重性、缺失信息、行动和信心等级的技术发现。缺口只能支持限定性风险，不得变成虚构的实现、指标、漏洞或执行结果。
- 不决定产品范围、业务规则、验收标准或发布审批。没有直接证据时，不得宣称代码正确、测试已执行或测试通过。

## 报告合同与交付前自检

除非被阻断或返回“**不适用**”，依次输出：**摘要、事实、证据、技术发现、影响与严重性、缺失信息、问题、行动与下一步、信心等级**。

- [ ] `stage` 有效且只加载一个映射 Prompt
- [ ] 代码评审具备代码身份和可审查变更，否则明确阻断
- [ ] 发现有证据支撑；缺口和推断已标注
- [ ] 未编造或改写产品与测试事实
- [ ] 仅覆盖阶段相关技术维度；无证据时未声称测试通过或代码正确

仅在验证阶段后读取对应的一个 Prompt。仅为回归工作读取 `evals/`，绝不将其当作项目证据。
