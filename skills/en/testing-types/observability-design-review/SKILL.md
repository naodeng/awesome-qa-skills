---
name: observability-design-review
description: Use this skill when logging, metrics, tracing, alerting, or SLO design needs an evidence-bounded review before implementation; triggers include observability design review, telemetry readiness review, and alert actionability audit.
---

# Observability Design Review

Review logging, metrics, tracing, context propagation, SLO/SLI, alerts, dashboards, sampling, retention, privacy, and cost designs before implementation. It produces `OBS-##` findings and validation preparation; it does not read runtime signals to declare health or choose SLO/incident severity.

## When to Use

- Use it to check whether signal fields/dimensions, semantics, correlation IDs, sampling, retention, and alerts are actionable.
- Use it to identify sensitive-data, cardinality, alert-noise, blind-spot, and cost risks.
- Use it when runtime data is unavailable and the telemetry design itself needs review.

Do not use it to query production logs, execute probes, analyze a real incident, or declare system health.

## Output Format Options

- Use Markdown by default; when a table, CSV, or JSON is requested, preserve the same evidence, status, impact, owner, and validation fields.
- Do not present a structured format or static inventory as execution, pass, approval, or release evidence.

## How to Use

1. Read this Skill's primary prompt and provide the objective, scope, material, environment, and available evidence.
2. Follow the prompt's input audit and output contract; deliver a bounded first pass when information is incomplete.
3. Retain source, evidence status, impact, owner role, close condition, and validation method for every finding.

## Workflow

1. Read `prompts/observability-design-review.md` and audit objective, service scope, time window, privacy, and sources.
2. Classify material as `known`, `missing`, `conflicting`, `stale`, `out_of_scope`, and `assumptions`.
3. Build a signal/service coverage matrix and record field semantics, detection action, impact, owner, and evidence in `OBS-##` findings.
4. Separate design facts, evidence-backed inferences, recommendations, and Human decisions; without runtime signals mark conclusions `unverified` or `unassessed`.
5. Give safe minimum validations for sensitive fields, unbounded cardinality, sampling gaps, and non-actionable alerts.

## Core Constraints

- Do not read or modify real production signals or execute probes; a dashboard is not proof of alert effectiveness.
- Do not choose SLOs, incident severity, sample rate, retention, cost budget, or owners by default.
- Every `OBS-##` includes signal, object, fields/dimensions, semantics, source/evidence, gap, impact, detection action, owner, and validation.
- Without runtime identity, time, environment, and raw signals, runtime conclusions remain `unverified`, `unexecuted`, or `unassessed`.

## Reference Files

- Always read `prompts/observability-design-review.md` before producing a review.
- For regression, read `evals/eval.yaml` and its cases; a design check is not log, trace, or metric analysis.
- For trigger checks, use `evals/trigger-prompts.csv` and `evals/local-rules.json`; missing selection trace is `BLOCKED`.

## Best Practices

- Prioritize high-impact gaps with a verifiable next action, using the smallest useful experiment or evidence request.
- Separate facts, evidence-backed inferences, recommendations, and Human decisions; never upgrade an assumption into a conclusion.

## Delivery Checklist

- [ ] Audit services, signals, scope, privacy, cost, and evidence.
- [ ] Cover logs, metrics, traces, propagation, SLO/SLI, alerts, dashboards, sampling, retention, and sensitive data.
- [ ] Give every `OBS-##` field semantics, impact, owner, and validation method.
- [ ] Separate design presence from real runtime signals.
- [ ] Do not choose SLOs, incident severity, or risk acceptance for a Human.

## Common Pitfalls

- Treating a dashboard as an actionable alert.
- Listing signal names without fields, dimensions, semantics, or correlation.
- Ignoring sensitive data, cardinality, sampling, retention, and cost constraints.
