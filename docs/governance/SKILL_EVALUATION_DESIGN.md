<div align="right"><strong>🇨🇳 中文</strong> | <a href="./SKILL_EVALUATION_DESIGN_EN.md">🇬🇧 English</a></div>

# Skill Evaluation Quality Loop 设计

> v1.5.1 最小可运营切片。完整设计来源为本次任务提供的 `SKILL_EVALUATION_DESIGN.md`；本文件是仓库内的可执行摘要。

## 目标

本设计回答三个问题：

1. Skill 是否在应该触发的任务上被选中？
2. Skill 是否产生了契约要求的行为和产物？
3. Skill 变更后，现有证据能支持哪些结论？

仓库在现有 `skill-up` 之上建立 Skill Engineering Quality Loop，不创建第二个通用 Eval Engine。

## 架构边界

```text
Skill authoring → Static review → Runtime evaluation → Evidence Package
       ↑                                  ↓
 Real-world failure ← Regression case ← Interpretation and report
```

- `skill-up` 是通用评测引擎，负责配置、执行、judge、benchmark 和报告。
- `scripts/skill_eval_rules.py` 是只读的 trace/产物深证据层，不执行 trace 中的命令。
- `skill-quality-review` 负责完整 Skill 包的静态工程审查。
- `skill-evaluation` 负责设计、运行、解释和报告评测。
- `skill-change-verification` 负责变更后的证据选择。
- Quality Score 仍由 [`QUALITY_SCORE_EVAL_CONTRACT.md`](./QUALITY_SCORE_EVAL_CONTRACT.md) 负责。

## 非目标

- 不再造 Eval、Judge、Benchmark 或仓库级 Quality Score。
- 不强制跨模型评测，不做模型排名。
- 不把 trigger 输出相似度当作 Skill 已触发的证据。
- 不自动修改 Skill，不自动进入无限优化循环。
- 不把静态、CLI install smoke、Project 状态写成运行效果、业务验收或发布批准。

## Source of Truth

| 责任 | 唯一主来源 |
| --- | --- |
| Skill 编写 | `skills/SKILL_AUTHORING.md` |
| 评测架构 | 本文件与 English mirror |
| 评测语义和证据状态 | [`SKILL_EVALUATION_CONTRACT.md`](./SKILL_EVALUATION_CONTRACT.md) |
| 本地 trace 规则 | [`../SKILL_EVAL_RULES.md`](../SKILL_EVAL_RULES.md) |
| Quality Score | [`QUALITY_SCORE_EVAL_CONTRACT.md`](./QUALITY_SCORE_EVAL_CONTRACT.md) |
| 单个 Skill 行为 | `<skill>/SKILL.md` |
| 单个 Skill 用例 | `<skill>/evals/` |
| 运行证据 | runner 生成的 metadata、trace、judge 和 report |

规则不得在多个文件中重新定义；文档应引用主来源。

## 两个 Meta Skill

### `skill-quality-review`

检查 metadata、触发词、范围、包完整性、渐进披露、独立安装、双语一致性、证据边界和 Eval readiness。它是静态 package review，不能声称 runtime behavior。

### `skill-evaluation`

按“设计 → 运行 → 解释 → 报告 → 建议”工作。它区分 HAPPY、INCOMPLETE、EXPLICIT_TRIGGER、IMPLICIT_TRIGGER、CONTEXTUAL_TRIGGER、NEGATIVE_TRIGGER、BOUNDARY 和 REGRESSION；优先 deterministic `rule_based`，其次 `script`，最后才是校准后的 `agent_judge`。

## Case、Judge 与证据

新 Skill 至少有成功、不完整信息、边界/负向三类 meaningful cases。用例必须包含真实输入、明确期望、合适 judge 和可诊断的失败信号。真实失败经过根因分析后才能成为回归用例。

触发评测分成 expected selection 和 observed selection；后者必须有 `skill.selection` trace。缺少选择事件时结果为 `BLOCKED`，不推断为未触发。

评测前检查 Eval validity：prompt、expect、judge、fixture 和 environment 都必须匹配契约；失败要区分 Skill Defect、Eval Defect、Infrastructure Defect 和 Unknown。

## 运行层级与演进

1. Level 0：Skill 结构、YAML 和仓库 deterministic checks。
2. Level 1：`skill-up validate`。
3. Level 2：变更 Skill 的评测，先 report-only。
4. Level 3：稳定、关键、deterministic regression 才可成为 gate。
5. Level 4：judge calibration 和 variance 充分后再做 semantic governance。

路线：v0.1 契约与架构 → v0.2 Meta Skills → v0.3 双 pilot → v0.4 trigger/neighbor → v0.5 regression metadata → v0.6 CI → v1.0 稳定 Quality Loop；cross-engine/cross-model 属于 v1.x 后续。

## Definition of Done

- EN/ZH 两个 Meta Skill 存在且可独立安装。
- 两者都有 `skill-up` 可验证的 eval suite。
- analysis 与 executable pilot 的配置、judge 和限制已记录。
- Evidence Contract 明确 `PASS`、`FAIL`、`BLOCKED`、`NOT_RUN`、`NOT_SCORED`、`UNASSESSED` 和 `INSUFFICIENT_EVIDENCE`。
- run metadata、failure classification 和回归 case 转换路径可复核。
- CI 至少运行 static + eval validation。
- 不存在第二套 Eval Framework 或第二个 Quality Score。
- 没有真实模型或目标时，runtime/semantic 结论保持 `NOT_RUN` 或 `INSUFFICIENT_EVIDENCE`。
