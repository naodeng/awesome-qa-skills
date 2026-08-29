# API Testing: Quick Start

Use the `api-testing` Skill to design risk-based tests for REST, GraphQL, SOAP, gRPC, or WebSocket interfaces.

## 1. Prepare the Minimum Context

Provide what is available from this list:

- API specification
- business flows
- auth model
- environment
- dependencies
- scope, version, environment, time budget, and prohibited actions
- known failures, existing tests, and evidence links

If some information is unavailable, say so explicitly. The Skill should still return a bounded first pass with assumptions and open questions.

## 2. Invoke the Skill

```text
@skill api-testing

Scenario: Validate an order API with idempotent creation, payment failure, and role boundaries.
Prioritize the highest risks, distinguish facts from assumptions, and provide an executable result with evidence requirements and open questions.
```

## 3. Follow the Execution Flow

1. Confirm the objective, subject, scope, and success criteria.
2. Audit the completeness and credibility of the supplied material.
3. Identify failure modes and rank them by impact, likelihood, and detectability.
4. Produce concrete scenarios, checks, or decisions with expected results.
5. Record evidence gaps, residual risk, and the smallest useful next action.

## 4. Minimum Coverage

Unless the request narrows scope, cover:

- contracts
- positive and negative paths
- validation
- auth and permissions
- idempotency
- errors
- data cleanup
- integration
- confirmed facts, working assumptions, and open questions
- P0/P1 priorities and the rationale for lower-priority deferral
- blockers, stop conditions, and residual risk

## 5. Review the Result

- Every high-risk item has a concrete failure mode and expected behavior.
- Priorities are justified rather than evenly distributed.
- No field, API, metric, environment, or execution result is invented.
- The artifact can be executed or reviewed without guessing the next step.
- Production, security, and privacy work uses least privilege and sanitized data.

## 6. Continue

Add missing evidence and ask the Skill to refine the same artifact. Keep confirmed facts separate from newly introduced assumptions so changes remain reviewable.
