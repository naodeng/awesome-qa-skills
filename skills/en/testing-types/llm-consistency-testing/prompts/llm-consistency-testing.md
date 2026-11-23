# LLM Consistency Testing Prompt

Build an executable, reviewable, and traceable evidence boundary for repeat inputs, version/model/prompt factors, invariants, variance evidence, and comparison boundaries.

## Input

Start with an input audit and record known, missing, conflicting, stale, out_of_scope, and assumptions:

- known: scope, LLM consistency material, constraints, or results directly supported by a source.
- missing: material needed to assess repeat inputs, version/model/prompt factors, invariants, variance evidence, and comparison boundaries that has not been supplied.
- conflicting: inconsistent goals, definitions, conditions, or behaviors across sources.
- stale: architecture, version, model, dataset, or record that may be out of date.
- out_of_scope: actions outside this Skill, unauthorized actions, or actions requiring a real environment.
- assumptions: temporary assumptions for a bounded first pass, each with a validation method.

## What to do

1. Restate the objective, subject, scope, and success criteria in one sentence.
2. Audit completeness, credibility, recency, and comparability, focusing on repeat input, version factor, model factor, invariant, variance evidence.
3. Build a risk or failure model for LLM consistency, including triggers, expected concerns, impact, and evidence needs.
4. Convert the analysis into concrete scenarios, assertions, validation steps, decision gates, or improvement experiments.
5. Report residual risk, evidence gaps, and next actions without presenting assumptions as facts.

## Execution Rules

- Give a source, evidence state, and validation method for every important conclusion.
- Each scenario must include preconditions, action or stimulus, expected behavior or decision criterion, required evidence, and a stop condition.
- Use P0/P1/P2/P3 or an equivalent scale and explain business impact, likelihood, detectability, or decision cost.
- Make repeat inputs, version/model/prompt factors, invariants, variance evidence, and comparison boundaries concrete; do not substitute adjacent test types, tool names, or one example for domain reasoning.
- Never invent numbers, thresholds, model behavior, root causes, system behavior, execution records, all-passed claims, or safety approval.
- For user data, production, or safety work, default to least privilege, masked data, mocks, dry runs, or isolation.
- Separate facts, inferences, candidate recommendations, and Human decisions; only Human can confirm risk acceptance, exceptions, and safety judgments.

## Domain Procedure and Oracle

Apply these steps as design or static comparison of supplied material. Keep fixture decisions, proposed plans, and real execution evidence separate; missing project rules, gates, and authority remain open.

1. Fix sample ID, model/prompt/tool/data versions, temperature, seed where supported, and other sampling parameters, with project-supplied repetition counts. Equal seeds do not establish reproducibility across versions.
2. Check structural invariants first: schema, required fields, enums, and policy. Then compare semantic decisions using the project rubric; permitted paraphrases/order changes are not failures.
3. Report repeated-trial denominators, structural/semantic failure counts, and intermittent failures per sample. Variance needs a named numeric variable, unit, and formula; wording difference rates are not quality variance.
4. Single observations establish no repeated consistency. Missing rubrics leave semantic consistency UNKNOWN. Separate parameter/version groups rather than pooling them as stability evidence.

## Evaluation Evidence Status and Structured Traces

For evaluation, regression, or result review, include an `evaluation_status` field with one of `PASS`, `FAIL`, `BLOCKED`, `NOT_RUN`, or `UNKNOWN` for each conclusion. `PASS` requires traceable runtime records and evidence that every required assertion in scope passed. Use `NOT_RUN` when no run result is supplied, `BLOCKED` when an attempted run was prevented by the environment or permissions, and `UNKNOWN` when evidence cannot support a decision. A design, static check, or file presence alone cannot support `PASS`. Keep this evidence status separate from any domain gate or per-sample decision.

A structured trace records at least `trace_id`, input/sample ID, model/prompt/dataset/schema versions, result-affecting parameters, run/trial ID, parse status, schema status, semantic status, and evidence reference. Check JSON parsing, schema constraints, and domain semantics independently: a parse success does not prove schema or semantic success. Retain a redacted output or reviewable hash, repetition count, and denominator; missing evidence never becomes a pass.

## Model/Provider Migration Mode

For a model, provider, or version migration, bind the old baseline and new candidate to one migration evaluation. Use the same task/dataset version, prompt, tools, parameters, and stratified sampling; record exact model versions, run IDs, failure cases, and cost/latency for both sides.

- Record the source and deadline for old-model deprecation, migration owner, dual-run window, rollback point, and re-baseline approver. A production switch is not migration evidence.
- Use project-supplied quality/capability, refusal/safety, latency, and cost thresholds. Compare outputs and statistical uncertainty by task stratum. Missing candidate runs or pricing keeps that dimension `NOT_RUN`/`UNKNOWN`.
- Mark migration `PASS` only when both sides have complete evidence and all required gates pass. An expired baseline, incomparable tasks, or missing run ID on either side blocks the conclusion.

## Minimum Coverage Checklist

- repeat input, version factor, model factor, invariant, variance evidence
- confirmed facts, working assumptions, open questions, evidence quality, and recency
- high-risk paths, blockers, stop/escalation/rollback or human-handoff conditions
- smallest validation action, owner role, close condition, residual risk, and Human decision
- facts, evidence-backed inferences, candidate recommendations, Human decisions

## Output

### 1. Task Understanding and Scope

State the objective, subject, inclusions, exclusions, success criteria, and unauthorized actions.

### 2. Input Audit

List known, missing, conflicting, stale, out_of_scope, and assumptions with source, recency, and evidence quality.

### 3. LLM consistency Analysis and Priorities

Describe scenarios, triggers, expected behavior, impact, priority, and evidence gaps for repeat inputs, version/model/prompt factors, invariants, variance evidence, and comparison boundaries.

### LCT-## Finding Contract

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

List only items requiring Human confirmation, risk acceptance, exception authorization, rollback, or safety judgment.

The output must keep these sections separate: facts, evidence-backed inferences, candidate recommendations, Human decisions.

## Quality Bar

- Tailor the content to LLM consistency; do not merely rename a generic template.
- Make high-risk paths concrete with failure modes, expected behavior, and evidence.
- Never infer numbers, root causes, or system behavior without support.
- Static analysis, plans, or dry runs are not proof of real execution, all tests passing, or safety approval.
- Let an executor act without guessing and a reviewer trace the boundary between facts, inferences, recommendations, and Human decisions.
