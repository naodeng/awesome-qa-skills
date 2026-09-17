<div align="right"><a href="./ENHANCEMENT_SPRINT.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# Enhancement Sprint Cadence

Schedule one Enhancement / Merge / Eval Sprint after every two or three New Sprints so the project does not only add directories without maintaining existing capability. The v1.4 governance closeout is the first reusable application of this rule.

## Cadence and inputs

| Cadence | Goal | Required evidence |
| --- | --- | --- |
| New Sprint × 2–3 | Deliver an independent capability proven NEW by Match | Scope, Non-goals, bilingual package, Eval, Workflow, installation |
| Enhancement Sprint × 1 | Tighten boundaries, outputs, and maintenance cost | Prompt, before/after Eval, Quality Score, Matrix, README |
| Release Review | Summarize changes and residual risk | Quality gate, runtime evidence, human approval, migration/rollback |

## Enhancement checklist

1. Simplify the Prompt while retaining input audit, evidence boundaries, and Human Decision.
2. Tighten Scope and add Non-goals plus incomplete-information handling.
3. Strengthen Eval with success, incomplete-information, and scope/risk-boundary cases; re-evaluate after changes.
4. Check Chinese/English content, triggers, Workflow references, Matrix, README, and installation entry points.
5. Revisit similar Skills for Match/Merge and create a Deprecation proposal when justified.
6. Record before/after evidence and unassessed items; use `NOT_RUN` without execution and `NOT_SCORED` without scoring.

## Exit criteria

An Enhancement Sprint closes only after documentation, structure, Eval artifacts, and the quality gate are complete. `Done` means the Sprint deliverable is complete; it does not mean runtime effectiveness, release approval, or risk acceptance.

- [Candidate Skill 15-step template](./CANDIDATE_SKILL_15_STEP_TEMPLATE_EN.md)
- [Quality Score and minimum Eval contract](./QUALITY_SCORE_EVAL_CONTRACT_EN.md)
- [v1.4 closeout](./PHASE_0_V1_4_CLOSEOUT_EN.md)
