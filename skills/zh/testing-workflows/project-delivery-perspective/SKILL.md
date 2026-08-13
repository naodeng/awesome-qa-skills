---
name: project-delivery-perspective
description: Use this skill when project delivery constraints or action tracking are needed for test strategy, test strategy review, or test report review; triggers include 项目交付视角、交付计划、排期与资源 and project delivery perspective.
---

# 项目交付视角（中文版）

**英文版：** See the corresponding English skill.

## 何时使用

- 在支持的质量阶段，需要沉淀带来源的排期、产能、依赖、里程碑、责任人或行动状态输入。
- 交付参与者需要暴露约束或跟踪后续行动，但不能改变质量事实。

## 输入

- `stage`（必填）：`test-strategy`、`test-strategy-review` 或 `test-report-review`。
- 已提供的项目交付事实：排期、产能、依赖、里程碑、责任人、行动状态，以及每条陈述的来源。
- 可选：来自其所属来源的质量事实，仅用于保留上下文和路由后续动作。

## 执行流程

1. 验证 `stage`。若缺失或不受支持，返回“**不适用**”，说明只支持 `test-strategy`、`test-strategy-review` 和 `test-report-review`，并请求有效阶段。不得输出计划、行动或质量结论。
2. 对有效阶段，只加载并遵循下表唯一对应的 Prompt；不得合并多个阶段 Prompt。
3. 仅在已提供排期、责任人、状态或依赖来源时记录项目约束与行动。缺失信息标为缺口；不得推断日期、产能、责任人或状态。
4. 将质量事实放在单独、带来源的保留区。不得判定、改写、弱化、关闭、标记通过、批准或以其他方式覆盖缺陷、执行、证据、质量或发布事实。

| `stage` | 只加载的 Prompt |
| --- | --- |
| `test-strategy` | `prompts/test-strategy.md` |
| `test-strategy-review` | `prompts/test-strategy-review.md` |
| `test-report-review` | `prompts/test-report-review.md` |

## 职责与边界

- 聚焦交付可行性输入：排期、产能、依赖、里程碑、责任人、行动状态、升级需要和由约束引起的交付风险。
- 所有项目与质量陈述均保留已提供来源。干系人的要求只是要求，不是能改变事实的证据。
- 本 Skill 不是 QA、研发、产品、安全或发布的决策方；绝不产出质量结论，也不改变缺陷状态、执行状态、测试结果、证据、质量状态或发布批准。

## 输出合同

除非返回“**不适用**”，依次输出：**摘要、项目约束、行动跟踪、保留的质量事实、信息缺口、协同问题、下一步交付行动、信心等级**。每一条事实均要给出来源；未验证的要求只能放入问题或行动，不能写成事实。

## 交付前自检

- [ ] 阶段属于三个支持值之一，且只加载了一个 Prompt
- [ ] 每条排期、产能、依赖、里程碑、责任人和状态陈述均带已提供来源
- [ ] 项目约束/行动与保留的质量事实已分开
- [ ] 未改变或推导任何缺陷、执行、证据、质量或发布事实
- [ ] 未知责任人、日期、产能、依赖和状态均已明确为缺口

## 按需加载

- 验证阶段后，只读取 `prompts/` 中映射的一个文件。
- 需要评测或回归时使用 `evals/`；不得将 eval 场景当作项目证据。

## 常见误区

- 不要因截止时间压力而声称缺陷已关闭、测试已通过或发布质量可接受。
- 不要把“要求修改事实”当作有来源的事实。
- 不要从未提供的产能、责任人、日期或依赖生成交付计划。
