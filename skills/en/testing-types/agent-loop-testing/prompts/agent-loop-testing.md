# Agent Loop Testing Prompt

Build an executable, reviewable, and traceable evidence boundary for loop state, plan/action/observation cycles, stop conditions, budgets, repetition, and trace evidence.

## Input

Start with an input audit and record known, missing, conflicting, stale, out_of_scope, and assumptions:

- known: scope, Agent loop material, constraints, or results directly supported by a source.
- missing: material needed to assess loop state, plan/action/observation cycles, stop conditions, budgets, repetition, and trace evidence that has not been supplied.
- conflicting: inconsistent goals, definitions, conditions, or behaviors across sources.
- stale: architecture, version, model, dataset, or record that may be out of date.
- out_of_scope: actions outside this Skill, unauthorized actions, or actions requiring a real environment.
- assumptions: temporary assumptions for a bounded first pass, each with a validation method.

## What to do

1. Restate the objective, subject, scope, and success criteria in one sentence.
2. Audit completeness, credibility, recency, and comparability, focusing on loop state, plan/action/observation, stop condition, budget, repetition.
3. Build a risk or failure model for Agent loop, including triggers, expected concerns, impact, and evidence needs.
4. Convert the analysis into concrete scenarios, assertions, validation steps, decision gates, or improvement experiments.
5. Report residual risk, evidence gaps, and next actions without presenting assumptions as facts.

## Execution Rules
- Plans, static analysis, and Eval fixtures are not run evidence. When asked to assess real evaluation/execution and the trace lacks a valid run ID and raw result, output `evaluation_status: NOT_RUN`, `run_evidence: []`, and `domain_conclusion: UNASSESSED`; never claim PASS.


- Give a source, evidence state, and validation method for every important conclusion.
- Each scenario must include preconditions, action or stimulus, expected behavior or decision criterion, required evidence, and a stop condition.
- Use P0/P1/P2/P3 or an equivalent scale and explain business impact, likelihood, detectability, or decision cost.
- Make loop state, plan/action/observation cycles, stop conditions, budgets, repetition, and trace evidence concrete; do not substitute adjacent test types, tool names, or one example for domain reasoning.
- Never invent numbers, thresholds, model behavior, root causes, system behavior, execution records, all-passed claims, or safety approval.
- For user data, production, or safety work, default to least privilege, masked data, mocks, dry runs, or isolation.
- Separate facts, inferences, candidate recommendations, and Human decisions; only Human can confirm risk acceptance, exceptions, and safety judgments.

## Domain Procedure and Oracle

Apply these steps as design or static comparison of supplied material. Keep fixture decisions, proposed plans, and real execution evidence separate; missing project rules, gates, and authority remain open.

1. Record task/run/step IDs, plan, tool and normalized arguments, observation identity/digest, business state delta, and cumulative time/cost; redact sensitive values while preserving deduplication evidence.
2. Progress requires new goal-relevant evidence or state advancement. Repeated action/observation with no advancement counts as a no-progress cycle; successful calls or repeated prose do not establish progress.
3. Apply supplied no-progress limits, retry policy, and time/cost budgets. Safety/cancellation stops immediately; any exhausted hard budget precedes more planning. Ask for missing limits rather than invent numbers.
4. Repetition takes the project-authorized change-strategy, stop, or escalation branch. Report trigger step, termination class, remaining work, and absence of extra effects.
## Minimum Coverage Checklist

- loop state, plan/action/observation, stop condition, budget, repetition
- confirmed facts, working assumptions, open questions, evidence quality, and recency
- high-risk paths, blockers, stop/escalation/rollback or human-handoff conditions
- smallest validation action, owner role, close condition, residual risk, and Human decision
- facts, evidence-backed inferences, candidate recommendations, Human decisions

## Output

### 1. Task Understanding and Scope

State the objective, subject, inclusions, exclusions, success criteria, and unauthorized actions.

### 2. Input Audit

List known, missing, conflicting, stale, out_of_scope, and assumptions with source, recency, and evidence quality.

### 3. Agent loop Analysis and Priorities

Describe scenarios, triggers, expected behavior, impact, priority, and evidence gaps for loop state, plan/action/observation cycles, stop conditions, budgets, repetition, and trace evidence.

### ALT-## Finding Contract

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

- Tailor the content to Agent loop; do not merely rename a generic template.
- Make high-risk paths concrete with failure modes, expected behavior, and evidence.
- Never infer numbers, root causes, or system behavior without support.
- Static analysis, plans, or dry runs are not proof of real execution, all tests passing, or safety approval.
- Let an executor act without guessing and a reviewer trace the boundary between facts, inferences, recommendations, and Human decisions.
