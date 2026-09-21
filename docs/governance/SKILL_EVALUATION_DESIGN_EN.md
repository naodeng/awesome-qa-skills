<div align="right"><a href="./SKILL_EVALUATION_DESIGN.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Skill Evaluation Quality Loop Design

> v1.5.1 minimum operational slice. The complete design source is the user-supplied `SKILL_EVALUATION_DESIGN.md`; this file is the repository's executable summary.

## Goal

This design answers three questions:

1. Is a Skill selected for the tasks where it should activate?
2. Does it produce the behavior and artifacts in its contract?
3. Which conclusions are supported by the available evidence after a Skill changes?

The repository establishes a Skill Engineering Quality Loop on top of `skill-up`; it does not create a second generic Eval Engine.

## Architecture boundary

```text
Skill authoring → Static review → Runtime evaluation → Evidence Package
       ↑                                  ↓
 Real-world failure ← Regression case ← Interpretation and report
```

- `skill-up` is the generic evaluation engine for configuration, execution, judges, benchmarks, and reports.
- `scripts/skill_eval_rules.py` is a read-only deep-evidence layer for traces and artifacts; it never executes commands from a trace.
- `skill-quality-review` performs static package-level engineering review.
- `skill-evaluation` designs, runs, interprets, and reports evaluations.
- `skill-change-verification` selects evidence after a change.
- Quality Score remains owned by [`QUALITY_SCORE_EVAL_CONTRACT_EN.md`](./QUALITY_SCORE_EVAL_CONTRACT_EN.md).

## Non-goals

- No second Eval, Judge, Benchmark, or repository-level Quality Score.
- No mandatory cross-model evaluation or model ranking.
- Output similarity is not trigger evidence.
- No silent Skill modification or unlimited optimization loop.
- Static checks, CLI install smoke, or Project status are not runtime effectiveness, business acceptance, or release approval.

## Source of truth

| Responsibility | Primary source |
| --- | --- |
| Skill authoring | `skills/SKILL_AUTHORING_EN.md` |
| Evaluation architecture | This document and its Chinese mirror |
| Evaluation semantics and evidence states | [`SKILL_EVALUATION_CONTRACT_EN.md`](./SKILL_EVALUATION_CONTRACT_EN.md) |
| Local trace rules | [`../SKILL_EVAL_RULES_EN.md`](../SKILL_EVAL_RULES_EN.md) |
| Quality Score | [`QUALITY_SCORE_EVAL_CONTRACT_EN.md`](./QUALITY_SCORE_EVAL_CONTRACT_EN.md) |
| Individual Skill behavior | `<skill>/SKILL.md` |
| Individual Skill cases | `<skill>/evals/` |
| Runtime evidence | Runner-generated metadata, traces, judge results, and reports |

Rules must not be redefined independently across documents; documents should reference the primary source.

## The two Meta Skills

### `skill-quality-review`

Reviews metadata, triggers, scope, package completeness, progressive disclosure, independent installation, bilingual consistency, evidence boundaries, and Eval readiness. It is a static package review and must not claim runtime behavior.

### `skill-evaluation`

Follows “Design → Run → Interpret → Report → Recommend”. It distinguishes HAPPY, INCOMPLETE, EXPLICIT_TRIGGER, IMPLICIT_TRIGGER, CONTEXTUAL_TRIGGER, NEGATIVE_TRIGGER, BOUNDARY, and REGRESSION. Select deterministic `rule_based` first, then `script`, and use calibrated `agent_judge` only when semantic judgment is necessary.

## Cases, judges, and evidence

Every new Skill needs meaningful success, incomplete-information, and boundary/negative cases. A case contains realistic input, an explicit expectation, an appropriate judge, and a diagnosable failure signal. A real failure becomes a regression case only after root-cause analysis.

Trigger evaluation separates expected selection from observed selection; observed selection requires a `skill.selection` trace event. Router cases also require structured `route`, `primary`, `optional`, and `selected_skills` fields, where `selected_skills` is limited to one primary plus at most one optional Skill. Missing or malformed structured evidence is `BLOCKED`; mismatches or extra selections are `FAIL`, not proof of non-selection.

Before interpreting results, check Eval validity: prompt, expectation, judge, fixture, and environment must match the contract. Failures are classified as Skill Defect, Eval Defect, Infrastructure Defect, or Unknown.

## Levels and evolution

1. Level 0: Skill structure, YAML, and repository deterministic checks.
2. Level 1: `skill-up validate`.
3. Level 2: changed-Skill evaluation, report-only at first.
4. Level 3: only stable, critical, deterministic regressions become gates.
5. Level 4: semantic governance follows judge calibration and variance analysis.

Roadmap: v0.1 contract and architecture → v0.2 Meta Skills → v0.3 dual pilot → v0.4 trigger/neighbor → v0.5 regression metadata → v0.6 CI → v1.0 stable Quality Loop; cross-engine and cross-model work is deferred to v1.x.

## Definition of Done

- The two EN/ZH Meta Skills exist and are independently installable.
- Both have `skill-up`-valid eval suites.
- Analysis and executable pilot configuration, judges, and limitations are recorded.
- The Evidence Contract defines `PASS`, `FAIL`, `BLOCKED`, `NOT_RUN`, `NOT_SCORED`, `UNASSESSED`, and `INSUFFICIENT_EVIDENCE`.
- Run metadata, failure classification, and regression-case conversion are reviewable.
- CI runs at least static and eval validation.
- No second Eval Framework or Quality Score exists.
- Without a real model or target, runtime and semantic claims remain `NOT_RUN` or `INSUFFICIENT_EVIDENCE`.
