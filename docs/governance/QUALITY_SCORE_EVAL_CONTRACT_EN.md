<div align="right"><a href="./QUALITY_SCORE_EVAL_CONTRACT.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# Quality Score and Minimum Eval Contract

This contract defines the minimum scoring and Eval artifacts. It does not invent scores for the current static governance record; without real evaluation execution, the Registry remains `NOT_SCORED` / `NOT_RUN`.

## Nine scoring dimensions

| Dimension | Points |
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

Thresholds are `>=80 Stable`, `70–79 Beta`, `60–69 Experimental`, and `<60 Reject / Redesign`. A score cites Prompt, Eval, documentation, or reviewable evidence; after an Enhance/Merge change, retain before/after scores and unassessed dimensions.

## Minimum Eval

Every new or modified Skill requires:

- `evals/eval.yaml`;
- a success-path case;
- an incomplete-information case;
- a scope-or-risk-boundary case.

Eval may verify only the declared output contract, input audit, and evidence boundary. Without a model, dependency, real target, or permission, record `blocked` / `NOT_RUN`; do not call it passing.

## Current Phase 0 state

The current v1.4 governance work verifies package structure, documentation, generators, and local quality rules. It did not run models or real test targets, so it produces no Quality Score and does not upgrade any Skill's runtime-effectiveness conclusion.

```bash
bash scripts/validate_skill_evals.sh
python3 scripts/validate_skill_eval_rules.py
bash scripts/check_skills_quality.sh
```

- [Skill Quality Gate](../SKILL_QUALITY_GATE_EN.md)
- [Skill Lifecycle](../SKILL_LIFECYCLE_EN.md)
- [v1.4 Release DoD](./RELEASE_DOD_V1_4_EN.md)
