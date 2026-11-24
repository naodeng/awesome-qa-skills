# Quality Productivity Metrics Prompt

Build an executable, reviewable, and traceable evidence boundary for quality and delivery metrics, denominators, attribution limits, gaming risk, and the Human-use boundary.

## Input

Start with an input audit and record known, missing, conflicting, stale, out_of_scope, and assumptions:

- known: scope, quality productivity material, constraints, or results directly supported by a source.
- missing: material needed to assess quality and delivery metrics, denominators, attribution limits, gaming risk, and the Human-use boundary that has not been supplied.
- conflicting: inconsistent goals, definitions, conditions, or behaviors across sources.
- stale: architecture, version, metric, sample, or record that may be out of date.
- out_of_scope: actions outside this Skill, unauthorized actions, or actions requiring a real environment.
- assumptions: temporary assumptions for a bounded first pass, each with a validation method.

## What to do

1. Restate the objective, subject, scope, and success criteria in one sentence.
2. Audit completeness, credibility, recency, and comparability, focusing on quality metric, delivery metric, denominator, attribution limit, gaming risk.
3. Build a risk or failure model for quality productivity, including triggers, expected concerns, impact, and evidence needs.
4. Convert the analysis into concrete scenarios, assertions, validation steps, decision gates, or improvement experiments.
5. Report residual risk, evidence gaps, and next actions without presenting assumptions as facts.

## Execution Rules

- Give a source, evidence state, and validation method for every important conclusion.
- Each scenario must include preconditions, action or stimulus, expected behavior or decision criterion, required evidence, and a stop condition.
- Use P0/P1/P2/P3 or an equivalent scale and explain business impact, likelihood, detectability, or decision cost.
- Make quality and delivery metrics, denominators, attribution limits, gaming risk, and the Human-use boundary concrete; do not substitute adjacent test types, tool names, or one example for domain reasoning.
- Never invent numbers, thresholds, root causes, system behavior, execution records, all-passed claims, or release approval.
- For production, privacy, or security work, default to least privilege, masked data, mocks, dry runs, or isolation.
- Separate facts, inferences, candidate recommendations, and Human decisions; only Human can confirm risk acceptance, exceptions, and release decisions.

## Domain Procedure and Oracle

Apply these steps as design or static comparison of supplied material. Keep fixture decisions, proposed plans, and real execution evidence separate; missing project rules, gates, and authority remain open.

1. Balance effort/cost, accepted output, defects/escapes and waiting/rework with explicit windows, team/task units, complexity and product risk.
2. Deduplicate split or merged cases and verify acceptance. Case/commit counts do not equal value; missing quality/rework evidence prevents productivity claims.
3. Compare only matched tasks, complexity, tools and windows. Different team work mixes cannot support direct ranking or personal performance evaluation; expose context and uncertainty.
4. Check dropped hard tests, unreported defects, deferred time and rerun counts. Metrics trigger investigations and experiments, not automatic causal or reward decisions.
5. For AI assistance, place model/token or call cost, human review, rework, acceptance, and quality outcomes in the same task window. Generation speed is not accepted output; absent a human baseline or same-quality comparison, do not claim productivity improvement.
6. State denominators such as human-accepted artifacts or completed tasks, and track escaped defects, false-green/false-positive outcomes, rework, and review burden. Acceptance counts, generated volume, or tokens alone are not value.

## Minimum Coverage Checklist

- quality metric, delivery metric, denominator, attribution limit, gaming risk
- AI token/call cost, review time, rework, acceptance, and quality outcomes when applicable
- confirmed facts, working assumptions, open questions, evidence quality, and recency
- high-risk paths, blockers, stop/escalation/rollback or human-handoff conditions
- smallest validation action, owner role, close condition, residual risk, and Human decision
- facts, evidence-backed inferences, candidate recommendations, Human decisions

## Output

### 1. Task Understanding and Scope

State the objective, subject, inclusions, exclusions, success criteria, and unauthorized actions.

### 2. Input Audit

List known, missing, conflicting, stale, out_of_scope, and assumptions with source, recency, and evidence quality.

### 3. quality productivity Analysis and Priorities

Describe scenarios, triggers, expected behavior, impact, priority, and evidence gaps for quality and delivery metrics, denominators, attribution limits, gaming risk, and the Human-use boundary.

### QPM-## Finding Contract

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

- Tailor the content to quality productivity; do not merely rename a generic template.
- Make high-risk paths concrete with failure modes, expected behavior, and evidence.
- Never infer numbers, root causes, or system behavior without support.
- Static analysis, plans, or dry runs are not proof of real execution, all tests passing, or release approval.
- Let an executor act without guessing and a reviewer trace the boundary between facts, inferences, recommendations, and Human decisions.
