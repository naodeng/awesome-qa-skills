<div align="right"><a href="./SHIFT_LEFT_MILESTONE.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# v1.1–v1.4 Shift Left Milestone

This milestone moves requirement, change, testing, performance, production, and AI quality concerns to composable Skill/Workflow entry points. The table describes governance scope and current physical capabilities; version labels and navigation relationships are not runtime evidence.

## Version track

| Version | Shift-left focus | Current entry points | Evidence boundary |
| --- | --- | --- | --- |
| v1.1 | Requirement, design, and test-design quality | `requirements-analysis`, `requirement-quality-review`, `test-gap-analysis`, `test-scope-analysis` | Preserve gaps when input is incomplete; do not infer coverage |
| v1.2 | Change impact, risk, and regression scope | `change-impact-analysis`, `pr-test-impact-analysis`, `regression-scope-analysis`, `regression-test-selection` | Requires a real Diff/test asset; no input means no impact claim |
| v1.3 | Execution intelligence, performance, and production evidence | `flaky-test-analysis`, `performance-result-analysis`, `production-verification`, `root-cause-analysis` | Keep results, thresholds, root causes, and production release evidence bounded |
| v1.4 | Existing/Match/Merge/Enhance governance closeout | Registry, Matrix, Lifecycle, Deprecation, Quality Gate, bilingual/installation checklists | Static delivery complete; runtime, model Eval, and release approval remain `NOT_RUN` |

## Composition principles

```text
Requirement → Change Impact → Regression Scope → Test Selection
                         ↘ Risk / Evidence Gap
```

- Composition is optional navigation; it creates no installation dependency or cross-Skill internal link.
- Revisit existing capability for `MATCH` / `MERGE` / `ENHANCE`; only `NEW` enters independent Skill design.
- Workflows compose, the Matrix governs, Eval validates output contracts and boundaries, and humans decide release/risk acceptance.

## Related documents

- [Governance Matrix](../SKILL_MATRIX_EN.md)
- [Skill Relationship Graph](../catalog/skills-graph_EN.md)
- [Candidate Skill 15-step template](./CANDIDATE_SKILL_15_STEP_TEMPLATE_EN.md)
- [v1.4 closeout](./PHASE_0_V1_4_CLOSEOUT_EN.md)
