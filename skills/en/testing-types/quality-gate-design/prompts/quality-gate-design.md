# Quality Gate Design Prompt

Build an executable, reviewable, and traceable evidence boundary for entry criteria, evidence requirements, owners, and exception paths for a delivery or release gate.

## Input

Start with an input audit and record known, missing, conflicting, stale, out_of_scope, and assumptions:

- known: scope, quality gate material, constraints, or results directly supported by a source.
- missing: material needed to assess entry criteria, evidence requirements, owners, and exception paths for a delivery or release gate that has not been supplied.
- conflicting: inconsistent goals, definitions, conditions, or behaviors across sources.
- stale: architecture, version, metric, sample, or record that may be out of date.
- out_of_scope: actions outside this Skill, unauthorized actions, or actions requiring a real environment.
- assumptions: temporary assumptions for a bounded first pass, each with a validation method.

## What to do

1. Restate the objective, subject, scope, and success criteria in one sentence.
2. Audit completeness, credibility, recency, and comparability, focusing on gate objective, entry criteria, evidence source, owner role, exception and rollback.
3. Build a risk or failure model for quality gate, including triggers, expected concerns, impact, and evidence needs.
4. Convert the analysis into concrete scenarios, assertions, validation steps, decision gates, or improvement experiments.
5. Report residual risk, evidence gaps, and next actions without presenting assumptions as facts.

## Execution Rules

- Give a source, evidence state, and validation method for every important conclusion.
- Each scenario must include preconditions, action or stimulus, expected behavior or decision criterion, required evidence, and a stop condition.
- Use P0/P1/P2/P3 or an equivalent scale and explain business impact, likelihood, detectability, or decision cost.
- Make entry criteria, evidence requirements, owners, and exception paths for a delivery or release gate concrete; do not substitute adjacent test types, tool names, or one example for domain reasoning.
- Never invent numbers, thresholds, root causes, system behavior, execution records, all-passed claims, or release approval.
- For production, privacy, or security work, default to least privilege, masked data, mocks, dry runs, or isolation.
- Separate facts, inferences, candidate recommendations, and Human decisions; only Human can confirm risk acceptance, exceptions, and release decisions.

## Domain Procedure and Oracle

Apply these steps as design or static comparison of supplied material. Keep fixture decisions, proposed plans, and real execution evidence separate; missing project rules, gates, and authority remain open.

1. Define each obligation, evidence version/freshness, operator and PASS/FAIL/BLOCKED/UNKNOWN table. Execution prevented is BLOCKED; missing or indeterminate evidence is UNKNOWN; absence never means PASS.
2. Apply project aggregation and fail-closed rules. Preserve unknown/blocked causes and recommend advancement only when all required gates have fresh valid evidence.
3. Record exceptions separately with scope, authorizer, reason, approval, expiry, compensating controls and revocation. Invalid exceptions do not override or rewrite failures.
4. State triggers, owners, revalidation and stop/rollback conditions. Separate design, evidence comparison and pipeline implementation; missing policy needs Human resolution.

## Evaluation Evidence Status and Structured Traces

For evaluation, regression, or result review, include an `evaluation_status` field with one of `PASS`, `FAIL`, `BLOCKED`, `NOT_RUN`, or `UNKNOWN` for each conclusion. `PASS` requires traceable runtime records and evidence that every required assertion in scope passed. Use `NOT_RUN` when no run result is supplied, `BLOCKED` when an attempted run was prevented by the environment or permissions, and `UNKNOWN` when evidence cannot support a decision. A design, static check, or file presence alone cannot support `PASS`. Keep this evidence status separate from any domain gate or per-sample decision.

A structured trace records at least `trace_id`, input/sample ID, model/prompt/dataset/schema versions, result-affecting parameters, run/trial ID, parse status, schema status, semantic status, and evidence reference. Check JSON parsing, schema constraints, and domain semantics independently: a parse success does not prove schema or semantic success. Retain a redacted output or reviewable hash, repetition count, and denominator; missing evidence never becomes a pass.

## AI Evaluation Gate Mode

For an AI evaluation gate, bind each required check to `dataset_id/version`, model/prompt/judge versions, `run_id`, data provenance, and evidence references. From the project contract, record minimum sample/confidence requirements, quality thresholds, flake budget, and cost budget. Thresholds need an owner and source; the Skill must not invent business gates.

- Recommend PASS only when every required evaluation has a fresh, traceable run, approved sample requirements are met, and each required assertion has evidence.
- Missing run/version/provenance, insufficient samples, an uncalibrated judge, or `NOT_RUN`/`UNKNOWN` results must keep the gate BLOCKED/UNKNOWN; never turn a static plan, partial sample, or average score into green.
- Report quality failures, variance/flake, cost overrun, and production guardrail state separately. Exceptions require Human approval, scope, expiry, and compensating controls.

## Minimum Coverage Checklist

- gate objective, entry criteria, evidence source, owner role, exception and rollback
- confirmed facts, working assumptions, open questions, evidence quality, and recency
- high-risk paths, blockers, stop/escalation/rollback or human-handoff conditions
- smallest validation action, owner role, close condition, residual risk, and Human decision
- facts, evidence-backed inferences, candidate recommendations, Human decisions

## Output

### 1. Task Understanding and Scope

State the objective, subject, inclusions, exclusions, success criteria, and unauthorized actions.

### 2. Input Audit

List known, missing, conflicting, stale, out_of_scope, and assumptions with source, recency, and evidence quality.

### 3. quality gate Analysis and Priorities

Describe scenarios, triggers, expected behavior, impact, priority, and evidence gaps for entry criteria, evidence requirements, owners, and exception paths for a delivery or release gate.

### QGD-## Finding Contract

Each finding must include:

- object/rule
- source
- trigger or applicability
- expected concern/rationale
- evidence state
- impact/priority
- owner role
- close condition
- validation method

### 4. Candidate Validation and Residual Risk

Separate candidate recommendations from actual execution and state the smallest validation action, stop/escalation conditions, residual risk, and open questions.

### 5. Human Decisions

List only items requiring Human confirmation, risk acceptance, exception authorization, rollback, or release judgment.

The output must keep these sections separate: facts, evidence-backed inferences, candidate recommendations, Human decisions.

## Quality Bar

- Tailor the content to quality gate; do not merely rename a generic template.
- Make high-risk paths concrete with failure modes, expected behavior, and evidence.
- Never infer numbers, root causes, or system behavior without support.
- Static analysis, plans, or dry runs are not proof of real execution, all tests passing, or release approval.
- Let an executor act without guessing and a reviewer trace the boundary between facts, inferences, recommendations, and Human decisions.
