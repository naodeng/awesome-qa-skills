# Chaos Testing Prompt

## Input

Start with an input audit and record known, missing, conflicting, stale, out_of_scope, and assumptions:

- known: scope, fault-injection hypothesis, or constraints directly supported by a source.
- missing: material needed to judge fault-injection hypotheses, blast radius, stop conditions, and safety guardrails that has not been supplied.
- conflicting: incompatible objectives, conditions, or behaviors across sources.
- stale: architecture, version, metric, or run evidence that may be out of date.
- out_of_scope: work outside this Skill, unauthorized actions, or actions requiring a real environment.
- assumptions: temporary assumptions used for a bounded draft; include a validation method.

## What to do

1. Restate the objective, object, scope, and success criteria in one sentence.
2. Model failure scenarios, triggers, expected concerns, and evidence needs around fault-injection hypotheses, blast radius, stop conditions, and safety guardrails.
3. Assign priority, owner role, close condition, and the smallest validation method to each scenario.
4. Separate confirmed facts, evidence-backed inferences, candidate recommendations, and Human decisions.
5. State which material is design preparation and which needs isolated validation; never claim that tests ran.

## Execution Rules

- Audit known, missing, conflicting, stale, out_of_scope, and assumptions before analysis.
- Trace every conclusion to a source; mark unsupported content as pending or a validation recommendation.
- Use fault-injection hypothesis as the domain anchor and CHS-## as the finding identifier.
- Each scenario needs preconditions, stimulus or action, expected result, evidence, and stop condition.
- Do not inject faults, access real dependencies, read credentials, or call production systems.
- Do not upgrade file presence, names, templates, or dry-runs into execution, passing, coverage, or release evidence.

## Minimum Coverage Checklist

- fault-injection hypothesis and applicability
- Primary failure modes and triggers
- Exposure window, impact, and priority
- Existing controls, dependencies, and isolation boundary
- Expected result, evidence state, and validation method
- Close condition, residual risk, and Human decision
- facts, evidence-backed inferences, candidate recommendations, Human decisions

## Output

### 1. Scope and Task Understanding

State the objective, object, included and excluded work, success criteria, and unauthorized actions.

### 2. Input Audit

List known, missing, conflicting, stale, out_of_scope, and assumptions with source and freshness.

### 3. fault-injection hypothesis and Failure Model

Describe fault-injection hypotheses, blast radius, stop conditions, and safety guardrails scenarios, triggers, expected behavior, impact, priority, and evidence gaps.

### CHS-## Finding Contract

Every finding must include:

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

Separate candidate recommendations from completed execution. State the smallest validation action, stop/escalation conditions, residual risks, and open questions.

### 5. Human Decisions

List only items requiring Human confirmation, risk acceptance, authorization, or release judgment.

The output must preserve these sections: facts, evidence-backed inferences, candidate recommendations, Human decisions.

## Quality Bar

- The content must target fault-injection hypotheses, blast radius, stop conditions, and safety guardrails, not be a generic template with a substituted title.
- Never write “tests were executed”, “all tests passed”, or “release approved” without direct evidence.
- Numbers, thresholds, root causes, recovery capability, and security claims require sources.
- Make the next action clear to the executor and the boundaries of facts, inferences, recommendations, and Human decisions reviewable.
