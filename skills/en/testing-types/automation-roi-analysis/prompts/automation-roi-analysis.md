# Automation ROI Analysis Prompt

Build an executable, reviewable, and traceable evidence boundary for automation candidates, build/run/maintenance costs, benefit assumptions, time horizon, and sensitivity.

## Input

Start with an input audit and record known, missing, conflicting, stale, out_of_scope, and assumptions:

- known: scope, automation ROI material, constraints, or results directly supported by a source.
- missing: material needed to assess automation candidates, build/run/maintenance costs, benefit assumptions, time horizon, and sensitivity that has not been supplied.
- conflicting: inconsistent goals, definitions, conditions, or behaviors across sources.
- stale: architecture, version, metric, sample, or record that may be out of date.
- out_of_scope: actions outside this Skill, unauthorized actions, or actions requiring a real environment.
- assumptions: temporary assumptions for a bounded first pass, each with a validation method.

## What to do

1. Restate the objective, subject, scope, and success criteria in one sentence.
2. Audit completeness, credibility, recency, and comparability, focusing on candidate scenario, build cost, run cost, maintenance cost, benefit assumption.
3. Build a risk or failure model for automation ROI, including triggers, expected concerns, impact, and evidence needs.
4. Convert the analysis into concrete scenarios, assertions, validation steps, decision gates, or improvement experiments.
5. Report residual risk, evidence gaps, and next actions without presenting assumptions as facts.

## Execution Rules

- Give a source, evidence state, and validation method for every important conclusion.
- Each scenario must include preconditions, action or stimulus, expected behavior or decision criterion, required evidence, and a stop condition.
- Use P0/P1/P2/P3 or an equivalent scale and explain business impact, likelihood, detectability, or decision cost.
- Make automation candidates, build/run/maintenance costs, benefit assumptions, time horizon, and sensitivity concrete; do not substitute adjacent test types, tool names, or one example for domain reasoning.
- Never invent numbers, thresholds, root causes, system behavior, execution records, all-passed claims, or release approval.
- For production, privacy, or security work, default to least privilege, masked data, mocks, dry runs, or isolation.
- Separate facts, inferences, candidate recommendations, and Human decisions; only Human can confirm risk acceptance, exceptions, and release decisions.

## Domain Procedure and Oracle

Apply these steps as design or static comparison of supplied material. Keep fixture decisions, proposed plans, and real execution evidence separate; missing project rules, gates, and authority remain open.

1. Fix candidate, window, and units. Separate Human time, machine occupancy, review, maintenance, and money; conversions need sourced rates.
2. For one window, net saving = runs×(manual cost/run−automated cost/run)−maintenance−build cost. Define ROI numerator/denominator; absent monetary conversion, report labor only.
3. If recurring net saving >0, break-even windows = build cost/recurring net saving, rounding up for whole execution windows. If <=0, no break-even under those assumptions.
4. Vary frequency and change-driven maintenance in project-supplied low/base/high scenarios with sources and sign changes. Missing inputs yield formulas/conditional ranges, never precise invented returns or automatic adoption.
5. For AI automation, include token/provider calls, infrastructure, human review, rework, and maintenance in the same window. Compare equally high-quality, human-accepted output; keep unquantified costs open and never equate generation speed with value.
6. Treat false greens, missed defects, false positives, and human takeover as negative value or risk with sourced evidence. Sensitivity analysis varies task frequency, model cost, review time, and rework; it cannot automatically approve procurement or deployment.
## Minimum Coverage Checklist

- candidate scenario, build cost, run cost, maintenance cost, benefit assumption
- AI token/call, review, rework, false-green, and false-positive costs when applicable
- confirmed facts, working assumptions, open questions, evidence quality, and recency
- high-risk paths, blockers, stop/escalation/rollback or human-handoff conditions
- smallest validation action, owner role, close condition, residual risk, and Human decision
- facts, evidence-backed inferences, candidate recommendations, Human decisions

## Output

### 1. Task Understanding and Scope

State the objective, subject, inclusions, exclusions, success criteria, and unauthorized actions.

### 2. Input Audit

List known, missing, conflicting, stale, out_of_scope, and assumptions with source, recency, and evidence quality.

### 3. automation ROI Analysis and Priorities

Describe scenarios, triggers, expected behavior, impact, priority, and evidence gaps for automation candidates, build/run/maintenance costs, benefit assumptions, time horizon, and sensitivity.

### ARO-## Finding Contract

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

- Tailor the content to automation ROI; do not merely rename a generic template.
- Make high-risk paths concrete with failure modes, expected behavior, and evidence.
- Never infer numbers, root causes, or system behavior without support.
- Static analysis, plans, or dry runs are not proof of real execution, all tests passing, or release approval.
- Let an executor act without guessing and a reviewer trace the boundary between facts, inferences, recommendations, and Human decisions.
