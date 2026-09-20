---
name: skill-evaluation
description: Use this skill when designing, running, interpreting, or reporting Agent Skill evaluations, selecting cases or judges, and analyzing trigger, benchmark, or regression evidence; triggers include Skill 评测、评测设计、回归评测。
---

# Skill 评测

## 何时使用

- 需要为一个 Skill 设计 realistic eval cases、positive/negative trigger 或 regression case。
- 需要用 `skill-up` 验证/运行评测并解释结果和限制。
- 需要选择 deterministic、script 或 semantic judge，或区分 benchmark 与 version regression。

## 输出格式选项

- 默认输出简洁的 Markdown 评测报告，用表格呈现 case 结果和 evidence state。
- 下游脚本需要机器可读结果时才输出 JSON；仍使用同一套证据词汇并保留限制。

## 如何使用

1. 读取 Skill 契约、已有 `evals/`、历史失败和本次变更范围。
2. 识别关键行为与证据维度：Outcome、Process、Style/Quality、Efficiency；只选择有意义的维度。
3. 设计 HAPPY、INCOMPLETE、EXPLICIT_TRIGGER、IMPLICIT_TRIGGER、CONTEXTUAL_TRIGGER、NEGATIVE_TRIGGER、BOUNDARY 或 REGRESSION 用例。
4. 按确定性优先选择 `rule_based`；可执行工件使用 `script`；只有需要语义判断时使用校准后的 `agent_judge`。
5. 运行 `skill-up validate`；有授权凭据和目标时再运行 `skill-up run` 或本地 trace runner。记录 run metadata、trace、judge、产物和限制。
6. 判断 Eval validity，区分 Skill Defect、Eval Defect、Infrastructure Defect 和 Unknown。
7. 按固定报告结构输出结果、证据状态、benchmark/regression 结论、blocked checks 和推荐行动；真实失败经根因确认后才添加 regression case。

## 核心约束

- `skill-up` 是主 Eval Engine；trace checks 只是深证据层，不得再造 Engine、Judge、Benchmark 或 Quality Score。
- 不能把输出相似度写成 observed trigger；缺少 `skill.selection` trace 时标记 `BLOCKED`。
- `skill-up validate` 不是 runtime 语义验证；静态、CLI smoke、Project Done 和单次语义观察不能自动升级为发布或业务结论。
- 不自动修改 Skill，不自动无限优化；不把 Benchmark（with/without Skill）和 Version Regression（previous/current）混为一谈。
- 值未知时写 `unknown`；证据不足保留 `NOT_RUN`、`UNASSESSED`、`BLOCKED` 或 `INSUFFICIENT_EVIDENCE`。

## 参考文件

- 完整执行和报告契约见 `prompts/skill-evaluation.md`。
- 选择 judge 前先读取目标 Skill 的 `evals/` 和 fixtures。
- 仓库治理契约与 trace rules 只作为可选深资料，复制后的 Skill 不得依赖其私有路径。

## 常见误区

- 把 `skill-up validate` 或 dry-run 当成 runtime 或语义效果证据。
- 缺少 trigger 事件时写成未触发，而不是 `BLOCKED`。
- 把 with/without Skill 的 benchmark 与 previous/current 的版本回归混为一谈。

## 最佳实践

- 从能够证明目标行为的最小确定性 case 开始。
- 记录准确的 run identity、judge、environment、未获得的证据和限制。
- 只有确认真实失败根因后才转成 regression case，并保留原始证据。

## 按需加载

- 产出前读取 `prompts/skill-evaluation.md`。
- 先读取目标 Skill 自己的 `evals/`，再按需读取 fixtures、examples 和脚本。
- 仓库级 Evaluation Contract 或 local trace rules 只作为可选深资料；独立安装的 Skill 不得硬依赖它们。

## 交付前自检

- [ ] 每个结论对应具体 case、judge 和 evidence state
- [ ] run metadata、环境、模型和未执行项明确
- [ ] Skill/Eval/Infrastructure/Unknown 分类没有被混淆
- [ ] trigger、benchmark、regression 和 Quality Score 边界清楚
