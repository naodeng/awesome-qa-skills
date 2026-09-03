---
name: test-strategy-review
description: Use this skill when a proposed test strategy needs evidence-based review before Human approval; triggers include test strategy review, strategy approval review..
---

# Test Strategy Review

## When to use

- A test strategy draft needs a decision on sufficiency, feasibility, and alignment with business and technical constraints.
- A review meeting must distinguish blockers, time-bounded conditions, and optional non-blocking improvements.
- Requirements, role analysis, technical notes, or project constraints conflict and need a traceable AI recommendation for Human decision.

## Input

Require the proposed test strategy. Use only supplied requirements, role analysis, technical constraints, and project constraints. Record absent material as a gap; do not fill it in. Preserve locatable document identifiers, sources, and supplied owners.

## Workflow

1. Read and follow `prompts/test-strategy-review.md` in full; it is the standalone execution specification.
2. Validate the strategy body and sources and record missing or conflicting inputs. Stop substantive review if no reviewable strategy exists.
3. Review business coverage, test depth, feasibility, environments, data, quality gates, dependencies, and explicit exclusions.
4. Separate blockers from non-blockers; label each non-blocker as a mandatory time-bounded condition or an optional improvement.
5. Apply deterministic rules to produce an AI-assisted `pass`, `conditional_pass`, or `reject` recommendation, with ownership and verifiable revision requests for gaps.
6. Check evidence, scope, ownership, recommendation, and Human decision boundaries before delivery.

## Decision constraints

- Any blocker requires a `reject` recommendation.
- With no blocker but one or more conditions that must close by a stated gate, recommend `conditional_pass`.
- With neither blockers nor conditions, recommend `pass`; optional non-blocking improvements may remain.
- Treat an unresolved source conflict affecting scope, critical risk, gates, or exclusions as a blocker. Do not choose a side without authority.
- Take owners only from inputs. Write `unassigned` when absent and create a revision request to assign ownership.
- A strategy describes intended work, not executed testing. Never invent test results, evidence, risk acceptance, waivers, or approval.
- Always label the result as an **AI-assisted recommendation**. A Human retains the final `pass`, `conditional_pass`, or `reject` decision; never claim final approval occurred.

## Output contract

Output in this order: **Review Status, Inputs and Conflicts, Dimension Review Matrix, Blockers, Non-Blocking Items, Revision Requests, Exclusion Review, Recommendation Basis and Limitations, Human Decision Questions**. Each finding and revision request cites evidence, explains impact, preserves supplied ownership, and gives a verifiable closure condition.

## Conditional loading

- Read `prompts/test-strategy-review.md` on every run for input validation, the eight-dimension review, classification rules, and output structure.
- Read `evals/` only while evaluating or regressing this Skill. Eval scenarios are not real project evidence.

## Pre-delivery checks

- [ ] All eight review dimensions have evidence, a gap, or a not-applicable explanation
- [ ] Blockers and non-blockers are separate; conditions are not mixed with optional improvements
- [ ] The recommendation follows the classification rules, with no schedule pressure overriding quality gaps
- [ ] Conflicting sources remain visible; no change, waiver, or decision was invented
- [ ] Every revision request has an object, owner or `unassigned`, timing/gate, and closure evidence
- [ ] The result is explicitly AI-assisted and the final Human decision remains pending

## Common mistakes

- Do not infer completeness from document length; verify that critical risks map to tests and gates.
- Do not dismiss environment readiness as later detail; a missing capability can make critical tests infeasible.
- Do not accept an explicit exclusion automatically; check its approved scope, risk disposition, and source.
- Do not use `conditional_pass` as a vague compromise; every condition must be assignable, verifiable, and tied to a closure gate.
