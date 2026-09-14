---
name: requirement-quality-review
description: Use this skill when a requirement, acceptance-criteria set, or change brief needs an evidence-bounded quality review before design or testing; triggers include 需求质量评审, requirement quality review, and requirements quality gate.
---

# 需求质量评审

从 QA 与交付角度评审需求材料的完整性、清晰度、可验证性、可行性、范围和证据质量，输出可追踪的缺口、风险和下一步。它是质量总览与专项路由入口，不是发布审批或数值评分器。

## 何时使用

- 需要在测试设计、技术设计或排期前检查需求质量。
- 验收标准看似完整，但异常路径、约束、角色或判定条件可能缺失。
- 需要把一份需求分流给歧义、一致性、冲突或可追踪性专项分析。

不适用于只要求编写测试用例、执行测试、批准发布或从无证据材料直接给质量分的任务。

## 工作方式

1. 先阅读并遵循 `prompts/requirement-quality-review.md`；它定义完整输入审计、质量维度和输出顺序。
2. 盘点用户明确提供的需求、故事、验收标准、变更说明、约束、版本和证据，并区分已知、缺失、冲突、过期和范围外信息。
3. 按交付、质量和可测性影响排序发现；每条发现保留来源、证据、状态、优先级、责任角色和可关闭的下一步。
4. 只提出专项路由建议，不读取或链接其他 Skill 的内部文件，不把推荐顺序当作安装依赖。
5. 信息不足时先输出最小可用初版，再列 3–5 个高价值待确认问题；无法安全判断时明确阻塞。

## 核心约束

- 直接材料事实、证据支持的推断、建议和 Human 决策项必须分开。
- 不补造业务规则、字段、接口、阈值、SLA、环境、责任人、根因、执行结果或审批结果。
- 不输出统一数值质量分，不从一段需求推断 Go/No-Go。
- 用 `RQ-##` 标识发现；至少区分 `missing`、`ambiguous`、`untestable`、`conflict` 和 `unassessed`。
- P0/P1 发现必须有影响、建议责任角色、待决策问题和验证方式。

## 按需加载

- 每次产出前必须阅读 `prompts/requirement-quality-review.md`。
- 需要回归本 Skill 时使用 `evals/eval.yaml` 和 `evals/cases/`；Eval 文件是结构与行为约束，不是已执行质量证明。
- 需要验证发现行为时，使用 `evals/trigger-prompts.csv` 与 `evals/local-rules.json` 运行仓库的 `scripts/run_skill_trace_eval.py`；缺少 `skill.selection` 证据时必须报告 `BLOCKED`，不能推断触发成功。
- 以上是仓库根目录下的开发验证步骤；独立安装的 Skill 包不包含仓库级 runner，运行时不依赖该脚本。

## 交付前自检

- [ ] 已说明输入范围、已知事实、缺失信息、冲突/时效性和假设
- [ ] 已分别检查完整性、清晰度、可验证性、可行性、范围和证据质量
- [ ] 发现包含来源、状态、影响、优先级、问题、责任角色、行动和验证方式
- [ ] 未把专项建议、静态检查或文档映射写成执行结果或审批结论
- [ ] 高优先级问题可指派、可关闭，信息不足时保留 `UNASSESSED`

## 常见误区

- 把“需求能读懂”当成“需求可验证”。
- 只复述需求，不指出会阻塞实现或测试的缺口。
- 用常识补全未提供的规则，或用数值分掩盖证据缺失。
- 直接替产品、研发或发布负责人做最终裁决。
