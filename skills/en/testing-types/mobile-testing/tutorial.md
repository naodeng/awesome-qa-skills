# Mobile Testing: Practical Tutorial

This tutorial shows how to cover mobile behavior across devices, operating systems, networks, permissions, and lifecycle events with a repeatable, evidence-driven workflow.

## Learning Objectives

By the end, you should be able to:

- frame a bounded testing objective;
- identify the evidence needed before making decisions;
- turn domain risk into executable scenarios and assertions;
- choose priorities without treating every check as equally important;
- report residual risk without inventing certainty.

## Scenario

Validate login and payment across Android versions with network switching and app resume.

Use the scenario as a starting point. Replace it with real project material whenever possible.

## Step 1: Establish the Input Contract

Collect:

- supported devices
- OS versions
- app build
- backend
- permissions
- network profile
- the exact build, version, environment, and test window
- authorized accounts, sanitized data, and allowed side effects
- existing tests, defects, monitoring, and rollback constraints

Create three lists before analysis:

1. **Confirmed facts** — directly supported by supplied material.
2. **Working assumptions** — necessary for a first pass but not yet proven.
3. **Open questions** — missing information that changes scope or risk.

## Step 2: Build the Risk Model

For each capability or user journey, record:

| Field | Meaning |
| --- | --- |
| Failure mode | What can go wrong |
| Impact | User, business, security, or operational consequence |
| Likelihood | Why the failure is plausible |
| Detectability | Whether existing checks or telemetry reveal it |
| Priority | P0, P1, P2, or P3 with rationale |
| Evidence | What would confirm correct or incorrect behavior |

Start with irreversible data loss, security exposure, financial impact, critical journey failure, and release blockers.

## Step 3: Design Coverage

Minimum domain coverage:

- installation
- navigation
- interruptions
- backgrounding
- permissions
- connectivity
- battery
- accessibility

For each important scenario, specify:

```text
Preconditions:
Test data:
Action or stimulus:
Expected behavior:
Evidence to capture:
Cleanup or rollback:
```

Avoid generic statements such as “test positive and negative cases” unless the concrete cases are listed.

## Step 4: Execute Safely

- Use the lowest environment and privilege level that can answer the question.
- Prefer mocks, sandboxes, dry runs, and synthetic or masked data.
- Do not run destructive production actions without explicit authorization.
- Record timestamps, versions, configuration, and identifiers needed for reproduction.
- Stop when a predefined safety, data-integrity, or customer-impact condition is met.

## Step 5: Interpret Evidence

Separate observation from explanation:

```text
Observation: what the system or test actually showed
Hypothesis: a possible explanation
Counter-evidence: facts that weaken the hypothesis
Verification: the smallest experiment that can distinguish alternatives
Conclusion: only what the available evidence supports
```

One failure message, high resource value, or correlated metric is not automatically a root cause.

## Step 6: Report the Result

Use this order:

1. Task understanding and scope
2. Input audit
3. Risks and priorities
4. Executed or proposed coverage
5. Results and evidence
6. Blockers and residual risk
7. Next actions and owners

## Reusable Request

```text
@skill mobile-testing

Analyze this real project context using the Skill's complete prompt contract.
Separate confirmed facts, working assumptions, and open questions.
Prioritize P0/P1 risks, provide executable scenarios with expected results and evidence, and state stop conditions and residual risk.
```

## Completion Checklist

- [ ] The objective and success criteria are explicit.
- [ ] The environment, version, and data boundary are recorded.
- [ ] High-risk paths have concrete scenarios and expected results.
- [ ] Evidence supports conclusions.
- [ ] Missing information and assumptions remain visible.
- [ ] Cleanup, rollback, or human-handoff conditions are defined.
- [ ] The next action is small, owned, and verifiable.
