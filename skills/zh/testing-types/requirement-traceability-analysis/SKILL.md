---
name: requirement-traceability-analysis
description: Use when requirements, acceptance criteria, design, code, tests, defects, or evidence must be mapped bidirectionally and coverage gaps made explicit; triggers include 需求可追踪性分析, requirement traceability, and traceability matrix.
---

# 需求可追踪性分析

把需求或控制项与验收标准、设计、代码、测试、缺陷和验证证据建立可回溯的双向映射。区分完整、部分、间接、缺失、陈旧和未执行证据，不把名称匹配、静态存在或报告文字写成真实执行结果。

## 何时使用

- 需要核对需求是否有验收标准、设计、实现、测试和缺陷闭环。
- 需要识别孤立需求、孤立测试、断开的链接、过期制品或缺少证据的覆盖关系。
- 需要为发布、变更评审、合规或风险治理提供可审计的追踪矩阵。

不适用于只需要编写测试用例、执行测试或替业务确认需求优先级的任务；本 Skill 只分析用户提供的映射和证据。

## 工作方式

1. 阅读并遵循 `prompts/requirement-traceability-analysis.md`，先审计目标、版本、范围、时间窗口和输入边界。
2. 使用稳定标识建立需求、验收、设计、代码、测试、缺陷和证据的双向映射；记录来源、版本和适用条件。
3. 将关系区分为 `direct`、`derived`、`indirect`、`contradictory` 或 `missing`，将覆盖状态区分为 `complete`、`partial`、`unverified`、`stale`、`unexecuted` 和 `unassessed`。
4. 保留孤立项、断链、重复映射、缺少执行记录和只存在名称的链接，给出缺口、责任角色、下一步和验证方式。
5. 结论只反映提供的材料；执行状态、缺陷关闭和发布结论必须有对应证据。

## 核心约束

- 使用 `RT-##` 标识追踪发现；每行至少有需求/控制项、来源、关联制品、关系类型、覆盖状态、证据和缺口行动。
- 双向检查：从需求追到下游制品，也从测试/缺陷/证据反查其上游需求；未找到对应项时明确标记孤立。
- 不把文件、链接、测试名称、报告摘要或代码存在当成已执行、已通过、已修复或已批准。
- 缺少制品、稳定 ID、版本、执行记录、数据或环境时，标记 `unassessed`/`unverified`/`unexecuted` 并提出补证问题。
- 不编造需求、关系、阈值、负责人、审批或运行结果；建议必须说明依据和关闭条件。

## 按需加载

- 每次产出前必须阅读 `prompts/requirement-traceability-analysis.md`。
- 需要回归本 Skill 时使用 `evals/eval.yaml` 和 `evals/cases/`；评测配置和静态映射不证明真实系统已执行。

## 交付前自检

- [ ] 已记录输入审计、范围、版本、时间窗口和关键假设
- [ ] 已做需求到下游、下游到需求的双向追踪
- [ ] 每个结论都有来源、证据、关系类型、覆盖状态和验证方法
- [ ] 已区分完整、部分、间接、缺失、陈旧、未验证和未执行
- [ ] 没有把静态存在、报告文字或测试名称写成执行结果

## 常见误区

- 看到测试文件名或工单链接就宣称需求已覆盖。
- 只做需求到测试的单向矩阵，漏掉孤立测试和未关联缺陷。
- 把“未找到证据”写成“没有问题”，或把报告中的 passed 当成实际执行证明。
- 用相似标题替代稳定标识，导致跨版本或跨范围错误关联。
