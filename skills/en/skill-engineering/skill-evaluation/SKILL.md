---
name: skill-evaluation
description: Use this skill when designing, running, interpreting, or reporting Agent Skill evaluations, selecting cases or judges, and analyzing trigger, benchmark, or regression evidence; triggers include Skill evaluation and evaluation design.
---

# Skill Evaluation

## When to use

- Design realistic eval cases, positive/negative triggers, or regression cases for a Skill.
- Validate or run evaluations with `skill-up` and interpret results and limitations.
- Select deterministic, script, or semantic judges, or distinguish a benchmark from a version regression.

## Workflow

1. Read the Skill contract, existing `evals/`, historical failures, and the current change scope.
2. Identify critical behavior and evidence dimensions: Outcome, Process, Style/Quality, and Efficiency; select only meaningful dimensions.
3. Design HAPPY, INCOMPLETE, EXPLICIT_TRIGGER, IMPLICIT_TRIGGER, CONTEXTUAL_TRIGGER, NEGATIVE_TRIGGER, BOUNDARY, or REGRESSION cases.
4. Prefer deterministic `rule_based`; use `script` for executable artifacts; use a calibrated `agent_judge` only when semantic judgment is necessary.
5. Run `skill-up validate`; run `skill-up run` or the local trace runner only with authorized credentials and targets. Record run metadata, traces, judges, artifacts, and limitations.
6. Check Eval validity and distinguish Skill Defect, Eval Defect, Infrastructure Defect, and Unknown.
7. Report results, evidence states, benchmark/regression conclusions, blocked checks, and recommended actions; add a regression case only after a real failure has a confirmed root cause.

## Constraints

- `skill-up` is the primary Eval Engine. Trace checks are a deep-evidence layer; do not create another Engine, Judge, Benchmark, or Quality Score.
- A similar output is not observed trigger evidence; missing `skill.selection` trace evidence is `BLOCKED`.
- `skill-up validate` is not runtime semantic validation. Static checks, CLI smoke, Project Done, and one semantic observation cannot be promoted automatically to release or business claims.
- Do not modify the Skill or enter an unlimited optimization loop. Keep Benchmark (with/without Skill) separate from Version Regression (previous/current).
- Use `unknown` for unknown values; preserve `NOT_RUN`, `UNASSESSED`, `BLOCKED`, or `INSUFFICIENT_EVIDENCE` when evidence is incomplete.

## Progressive disclosure

- Read `prompts/skill-evaluation.md` before producing the report.
- Read the target Skill's own `evals/` first, then load fixtures, examples, and scripts as needed.
- Repository Evaluation Contract and local trace rules are optional deep references; an independently installed Skill must not depend on their private files.

## Pre-delivery checklist

- [ ] Every conclusion maps to a case, judge, and evidence state
- [ ] Run metadata, environment, model, and unexecuted checks are explicit
- [ ] Skill/Eval/Infrastructure/Unknown classifications are not conflated
- [ ] Trigger, benchmark, regression, and Quality Score boundaries are clear
