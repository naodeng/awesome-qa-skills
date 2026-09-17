<div align="right"><strong>🇨🇳 中文</strong> | <a href="./QUALITY_SCORE_EVAL_CONTRACT_EN.md">🇬🇧 English</a></div>

# Quality Score 与最低 Eval 契约

本契约规定评分和 Eval 的最低工件要求。它不为当前静态治理记录虚构分数；没有真实评测执行时，Registry 保持 `NOT_SCORED` / `NOT_RUN`。

## 九维评分

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

阈值：`>=80 Stable`、`70–79 Beta`、`60–69 Experimental`、`<60 Reject / Redesign`。评分必须引用 Prompt、Eval、文档或可复核评审证据；Enhance/Merge 变更后保留变更前后分数与未评估维度。

## 最低 Eval

新增或修改 Skill 必须有：

- `evals/eval.yaml`；
- 成功路径 case；
- 信息不完整 case；
- 范围或风险边界 case。

Eval 只能验证声明的输出契约、输入审计和证据边界。无模型、依赖、真实目标或权限时标记 `blocked` / `NOT_RUN`，不能写成通过。

## 当前 Phase 0 状态

当前 v1.4 治理工作验证了包结构、文档、生成器和本地质量规则；它没有运行模型或真实测试目标，因此不产生 Quality Score，不升级任何 Skill 的运行有效性结论。

```bash
bash scripts/validate_skill_evals.sh
python3 scripts/validate_skill_eval_rules.py
bash scripts/check_skills_quality.sh
```

- [Skill 质量门禁](../SKILL_QUALITY_GATE.md)
- [Skill 生命周期](../SKILL_LIFECYCLE.md)
- [v1.4 Release DoD](./RELEASE_DOD_V1_4.md)
