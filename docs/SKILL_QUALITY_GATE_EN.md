<div align="right"><a href="./SKILL_QUALITY_GATE.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# Skill Quality Gate

## Scoring model

| Dimension | Score |
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

`>=80` is Stable, `70–79` Beta, `60–69` Experimental, and `<60` Reject / Redesign. Scores require reviewable Prompt, Eval, documentation, or review evidence; they do not replace runtime evidence or human approval.

Every Enhance or Merge is rescored after change. Preserve before/after scores, evidence, and unassessed dimensions. Without rescore evidence, the adjustment cannot be claimed to pass the governance gate.

## Minimum Eval standard

Every new or modified Skill has `evals/eval.yaml` and at least success, insufficient-information, and scope/risk-boundary cases. Evals verify output contracts and evidence boundaries. Missing environments, dependencies, or permissions are `blocked`, never passed.
