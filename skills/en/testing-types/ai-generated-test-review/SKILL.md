---
name: ai-generated-test-review
description: Use this skill when reviewing AI-generated unit, functional, API, or end-to-end tests for false confidence, weak assertions, missing risks, or unsafe test behavior; triggers include AI-generated test review and functional test review.
---

# AI-Generated Test Review

Determine whether AI-generated tests prove real behavior instead of merely raising coverage or producing green builds.

## When to Use

- Reviewing, changing, or accepting AI-generated unit, functional, API, or E2E tests.
- A test passes but its assertions, isolation, data, or coverage value is doubtful.

## Workflow

1. Inventory test types and files actually present in scope: unit, functional test, API, E2E, or a combination. Review only discovered or user-specified types.
2. Establish the behavior, risk, and available requirement or implementation evidence. Mark missing evidence; do not invent findings.
3. Read `prompts/review-test.md` and report actionable findings by severity, tied to a test, risk, and repair direction.
4. Load rules only for discovered layers: unit, functional test, API, or E2E. Load more than one only for cross-layer concerns; do not perform a global review just because multiple rule files exist.
5. Separate merge-blocking faults from improvements; do not call an effective test defective because of style preference.

## Core Constraints

- Judge observable behavior, failure signals, and risk coverage—not line coverage, test names, or mock-call counts alone.
- When a broken implementation could still pass, state the smallest break and the assertion needed to catch it.
- Never recommend deleting assertions, swallowing errors, loosening timeouts, or changing production behavior merely to obtain green tests.
- Do not expose credentials, personal data, or production write operations in tests, logs, or examples.

## Progressive Disclosure

- Always read `prompts/review-test.md` before reviewing; its test-type routing precedes per-test review.
- For fake tests, excessive mocks, or ineffective assertions, read `references/fake-test-patterns.md`.
- Read `references/unit-test-rules.md`, `references/functional-test-rules.md`, `references/api-test-rules.md`, or `references/e2e-test-rules.md` for the applicable layer.
- Read related material under `examples/good/` or `examples/bad/` when an example is useful.

## Pre-delivery Checklist

- [ ] States scope, evidence, and open questions
- [ ] Ranks findings and includes location, impact, and repair direction
- [ ] Reviews real assertions, negative paths, boundaries, isolation, and repeatability
- [ ] Does not present speculation as fact
