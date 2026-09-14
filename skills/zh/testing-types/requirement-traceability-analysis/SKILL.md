---
name: requirement-traceability-analysis
description: Use this skill when requirements, acceptance criteria, design, code, tests, defects, or evidence must be mapped bidirectionally and coverage gaps made explicit; triggers include 需求可追踪性分析, requirement traceability, and traceability matrix.
---

# 需求可追踪性分析

把需求或控制项与验收标准、设计、代码、测试、缺陷和验证证据建立可回溯的双向映射。区分关系类型与覆盖状态，不把名称匹配、静态存在或报告文字写成真实执行结果。

## 何时使用

- 需要核对需求是否有验收标准、设计、实现、测试和缺陷闭环。
- 需要识别孤立需求、孤立测试、断开的链接、过期制品或缺少证据的覆盖关系。
- 需要为发布、变更评审、合规或风险治理提供可审计的追踪矩阵。

不适用于只需要编写测试用例、执行测试或替业务确认需求优先级的任务；本 Skill 只分析用户提供的映射和证据。

## 输出格式选项

- 默认输出 Markdown；用户要求表格、CSV 或 JSON 时，保留相同的证据、状态、影响、责任角色和验证字段。
- 不把结构化格式或静态清单写成执行、通过、批准或发布证据。

## 如何使用

1. 先读取本 Skill 的主 Prompt，并提供目标、范围、材料、环境和已有证据。
2. 按 Prompt 的输入审计和输出合同执行；缺少信息时交付带边界的初版。
3. 对每条发现保留来源、证据状态、影响、责任角色、关闭条件和验证方法。

## 工作方式

1. 阅读并遵循 `prompts/requirement-traceability-analysis.md`，先审计目标、版本、范围、时间窗口和输入边界。
2. 使用稳定标识建立需求、验收、设计、代码、测试、缺陷和证据的双向映射；记录来源、版本和适用条件。
3. 关系类型使用 `direct`、`derived`、`indirect`、`contradictory` 或 `missing`；覆盖状态使用 `complete`、`partial`、`unverified`、`stale`、`unexecuted` 和 `unassessed`，两组枚举不可混用。
4. 当任务要求 `coverage_analysis` 或 `test-coverage-analysis` 模式时，在保留 `RT-##` 双向追踪的基础上增加 `TC-##` 覆盖视图，记录测试资产、覆盖状态、执行身份/时间/环境、证据质量和孤立项。
5. 保留孤立项、断链、重复映射、缺少执行记录和只存在名称的链接，给出缺口、责任角色、下一步和验证方式。
6. 结论只反映提供的材料；执行状态、缺陷关闭和发布结论必须有对应证据。

## 核心约束

- 使用 `RT-##` 标识追踪发现；每行至少有需求/控制项、来源、关联制品、关系类型、覆盖状态、证据和缺口行动。
- 关系类型：`direct`、`derived`、`indirect`、`contradictory`、`missing`。
- 覆盖状态：`complete`、`partial`、`unverified`、`stale`、`unexecuted`、`unassessed`。
- `coverage_analysis` 模式额外使用 `TC-##` 表示覆盖视图；保留 `RT-##` 关系发现，关系类型与覆盖状态不可混用。
- 双向检查：从需求追到下游制品，也从测试/缺陷/证据反查其上游需求；未找到对应项时明确标记孤立。
- 不把文件、链接、测试名称、报告摘要或代码存在当成已执行、已通过、已修复或已批准。
- 缺少制品、稳定 ID、版本、执行记录、数据或环境时，标记 `unassessed`/`unverified`/`unexecuted` 并提出补证问题。
- 不编造需求、关系、阈值、负责人、审批或运行结果；建议必须说明依据和关闭条件。

## 参考文件

- 每次产出前必须阅读 `prompts/requirement-traceability-analysis.md`。
- 需要回归本 Skill 时使用 `evals/eval.yaml` 和 `evals/cases/`；评测配置和静态映射不证明真实系统已执行。
- 需要验证发现行为时，使用 `evals/trigger-prompts.csv` 与 `evals/local-rules.json` 运行仓库的 `scripts/run_skill_trace_eval.py`；缺少 `skill.selection` 证据时必须报告 `BLOCKED`，不能推断触发成功。
- 以上是仓库根目录下的开发验证步骤；独立安装的 Skill 包不包含仓库级 runner，运行时不依赖该脚本。
- 需要回归 `test-coverage-analysis` 时使用 `coverage-*` Eval 和包含 coverage analysis 短语的本地触发数据；目标仍是本 Skill 的物理目录，不创建别名目录。

## 最佳实践

- 优先处理高影响且可验证的缺口，使用最小实验或补证动作降低不确定性。
- 将事实、证据支持的推断、建议和 Human 决策分开，避免把假设升级为结论。

## 交付前自检

- [ ] 已记录输入审计、范围、版本、时间窗口和关键假设
- [ ] 已做需求到下游、下游到需求的双向追踪
- [ ] 每个结论都有来源、证据、关系类型、覆盖状态和验证方法
- [ ] 已分别区分关系类型 `direct`、`derived`、`indirect`、`contradictory`、`missing` 与覆盖状态 `complete`、`partial`、`unverified`、`stale`、`unexecuted`、`unassessed`
- [ ] 没有把静态存在、报告文字或测试名称写成执行结果

## 常见误区

- 看到测试文件名或工单链接就宣称需求已覆盖。
- 只做需求到测试的单向矩阵，漏掉孤立测试和未关联缺陷。
- 把“未找到证据”写成“没有问题”，或把报告中的 passed 当成实际执行证明。
- 用相似标题替代稳定标识，导致跨版本或跨范围错误关联。
