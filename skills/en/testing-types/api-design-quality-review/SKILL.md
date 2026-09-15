---
name: api-design-quality-review
description: Use this skill when an API, OpenAPI, or consumer contract needs a quality review before implementation or versioning; triggers include API design review, contract readiness review, and consumer compatibility audit.
---

# API Design Quality Review

Review API designs, OpenAPI/contracts, request/response examples, error models, authorization, idempotency, pagination, status codes, version evolution, and consumer impact before implementation. It produces `API-##` findings and validation preparation; it does not execute an API or approve a final versioning policy.

## When to Use

- Use it to check whether operations, inputs/outputs, errors, permissions, and compatibility evolution are verifiable.
- Use it to find contract gaps across consumers, versions, or migration plans.
- Use it when examples are incomplete, boundaries are undefined, or runtime evidence is missing.

Do not use it to send requests, load-test, execute security tests, or choose a final API versioning policy for a team.

## Output Format Options

- Use Markdown by default; when a table, CSV, or JSON is requested, preserve the same evidence, status, impact, owner, and validation fields.
- Do not present a structured format or static inventory as execution, pass, approval, or release evidence.

## How to Use

1. Read this Skill's primary prompt and provide the objective, scope, material, environment, and available evidence.
2. Follow the prompt's input audit and output contract; deliver a bounded first pass when information is incomplete.
3. Retain source, evidence status, impact, owner role, close condition, and validation method for every finding.

## Workflow

1. Read `prompts/api-design-quality-review.md` and audit objective, version, consumers, scope, and evidence.
2. Classify material as `known`, `missing`, `conflicting`, `stale`, `out_of_scope`, and `assumptions`.
3. Build an operation/field coverage matrix and bind each gap to an `API-##`, source, evidence, impact, and validation method.
4. Separate contract facts, evidence-backed inferences, recommendations, and Human decisions; state what compatibility, authorization, and error evidence is still needed.
5. Deliver a bounded first pass when incomplete; a request/response example is not a complete contract.

## Core Constraints

- Do not execute an API or claim security, compatibility, or performance tests passed.
- Do not infer all fields, errors, permissions, rate limits, idempotency, or version rules from one example.
- Every `API-##` includes operation, source/evidence, impact, compatibility risk, owner role, decision question, and validation method.
- Without execution identity, time, environment, inputs, responses, and raw results, runtime status remains `unverified`, `unexecuted`, or `unassessed`.

## Reference Files

- Always read `prompts/api-design-quality-review.md` before producing a review.
- For regression, read `evals/eval.yaml` and its cases; structural validation is not API behavior evidence.
- For trigger checks, use `evals/trigger-prompts.csv` and `evals/local-rules.json`; missing selection trace is `BLOCKED`.

## Best Practices

- Prioritize high-impact gaps with a verifiable next action, using the smallest useful experiment or evidence request.
- Separate facts, evidence-backed inferences, recommendations, and Human decisions; never upgrade an assumption into a conclusion.

## Delivery Checklist

- [ ] Audit operations, versions, consumers, scope, and evidence.
- [ ] Check input/output, errors, authorization, idempotency, pagination, status, evolution, and migration impact.
- [ ] Give each `API-##` minimum evidence, impact, owner, and validation method.
- [ ] Separate examples/design claims from runtime evidence.
- [ ] Do not choose compatibility policy, risk acceptance, or release approval for a Human.

## Common Pitfalls

- Treating one successful response as a complete OpenAPI contract.
- Checking status codes without error bodies, authorization, retry, idempotency, and consumer behavior.
- Treating a document version or linter pass as compatibility-test evidence.
