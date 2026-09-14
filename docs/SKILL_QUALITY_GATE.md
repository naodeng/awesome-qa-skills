<div align="right"><strong>🇨🇳 中文</strong> | <a href="./SKILL_QUALITY_GATE_EN.md">🇬🇧 English</a></div>

# Skill 质量门禁

## 评分模型

治理 registry 与双语 Matrix/Register 的新鲜度由 `python3 scripts/generate_skill_governance_matrix.py --check` 校验。`NOT_SCORED`、`NOT_RUN` 和 `UNASSESSED` 是证据状态，不是运行失败或质量结论。

| 维度 | 分值 |
| --- | ---: |
| Problem Value | 15 |
| Scope Clarity | 10 |
| Input Quality | 10 |
| Analysis Depth | 15 |
| Output Actionability | 15 |
| Evidence Quality | 10 |
| Reusability | 10 |
| Eval Coverage | 10 |
| Documentation | 5 |

`>=80` 为 Stable，`70–79` 为 Beta，`60–69` 为 Experimental，`<60` 应 Reject / Redesign。评分必须引用实际 Prompt、Eval、文档或可复核评审证据，不能替代运行效果或人工放行。

任何 Enhance 或 Merge 在变更后必须重新评分；保留变更前后分数、依据与未评估维度。没有重新评分证据，不得宣称该调整已通过治理门禁。

## 最低 Eval 标准

每个新增或修改的 Skill 必须有 `evals/eval.yaml` 与至少三类 case：成功路径、信息不完整、范围或风险边界。Eval 应验证输出契约和证据边界；无运行环境、依赖或权限时记录为 `blocked`，不得写作通过。
