---
name: technical-design-quality-review
description: Use this skill when an architecture note, ADR, component design, or technical proposal needs an evidence-bounded quality review before implementation; triggers include technical design review, design readiness review, and non-functional design audit.
---

# Technical Design Quality Review

Review a technical design before implementation for boundaries, dependencies, failure modes, data consistency, security, performance, observability, compatibility, maintainability, and verification readiness. It produces `TD-##` findings and validation preparation; it does not review unsupplied code or approve architecture.

## When to Use

- Use it for ADRs, component/data-flow designs, technical proposals, and non-functional constraints.
- Use it to identify failure paths, dependency assumptions, compatibility risks, and evidence gaps.
- Use it when an incomplete design still needs a bounded implementation-readiness pass.

Do not use it to run builds, tests, production probes, or choose a final architecture for a Human.

## Workflow

1. Read `prompts/technical-design-quality-review.md` and audit objective, version, scope, sources, and success criteria.
2. Classify input as `known`, `missing`, `conflicting`, `stale`, `out_of_scope`, and `assumptions`.
3. Build a design-coverage matrix; bind each material gap to a `TD-##`, minimum evidence, impact, priority, and validation method.
4. Separate facts, evidence-backed inferences, recommendations, and Human decisions; never upgrade a design claim to an implementation result.
5. Deliver bounded conclusions and evidence actions when information is missing instead of filling gaps with generic architecture knowledge.

## Core Constraints

- Do not review implementation that was not supplied or claim build, compatibility, security, or performance tests passed.
- Do not infer consistency, capacity, latency, SLOs, owners, or recovery behavior from component names.
- Each `TD-##` includes topic, source/evidence, impact, priority, gap action, owner role, decision question, and validation method.
- Design presence proves only that a document exists; execution evidence requires identity, time, environment, inputs, and raw results.

## On-Demand Loading

- Always read `prompts/technical-design-quality-review.md` before producing a review.
- For regression, read `evals/eval.yaml` and its cases; a static design review is not system execution.
- For trigger checks, use `evals/trigger-prompts.csv` and `evals/local-rules.json`; without a selection trace report `BLOCKED`.

## Delivery Checklist

- [ ] Complete the six input-audit categories and state design scope.
- [ ] Cover boundaries, dependencies/failures, data, security, performance, observability, compatibility, maintainability, and verification readiness.
- [ ] Give every `TD-##` evidence, impact, owner, action, and validation method.
- [ ] Separate design claims, evidence-backed inference, recommendations, and Human decisions.
- [ ] Do not present document presence or static checks as implementation/runtime results.

## Common Pitfalls

- Checking that a diagram exists without checking boundaries, failures, or recovery.
- Treating “supports high concurrency” or “has monitoring” as a verification criterion.
- Turning technical recommendations into an approved architecture or release conclusion.
