---
name: ai-generated-test-review
description: Use this skill when reviewing AI-generated unit, functional, API, or end-to-end tests for false confidence, weak assertions, missing risks, or unsafe test behavior; triggers include AI-generated test review and functional test review.
license: PolyForm-Noncommercial-1.0.0
metadata:
  version: "1.0.0"
  compatibility: ""
  author: "Awesome QA Skills contributors"
  language: "en"
  category: "testing-types"
  source: "https://github.com/naodeng/awesome-qa-skills"
  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"
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

## Domain Execution Essentials

1. Evaluate assertions against the actual contract; mock, snapshot, or status-only syntax alone does not imply WEAK/FAKE.
2. A boundary mock may replace a confirmed external dependency while real production logic executes. Mocking the subject itself and asserting its preset return offers no protection.
3. A reviewed, independent snapshot of stable business structure can detect meaningful mutations. A snapshot that discards all business fields cannot. A status assertion can be STRONG when status fully expresses the supplied contract; persistence obligations require business postconditions.
4. Support each classification with a concrete escaping/detected mutation and contract source. Retain confidence/gaps when evidence is missing, using the same bilingual rationale.

## Core Constraints

- Judge observable behavior, failure signals, and risk coverage—not line coverage, test names, or mock-call counts alone.
- When a broken implementation could still pass, state the smallest break and the assertion needed to catch it.
- Never recommend deleting assertions, swallowing errors, loosening timeouts, or changing production behavior merely to obtain green tests.
- Do not expose credentials, personal data, or production write operations in tests, logs, or examples.

## Progressive Disclosure

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- Always read `prompts/review-test.md` before reviewing; its test-type routing precedes per-test review.
- For fake tests, excessive mocks, or ineffective assertions, read `references/fake-test-patterns.md`.
- Read `references/unit-test-rules.md`, `references/functional-test-rules.md`, `references/api-test-rules.md`, or `references/e2e-test-rules.md` for the applicable layer.
- Read related material under `examples/good/` or `examples/bad/` when an example is useful.

## Pre-delivery Checklist

- [ ] States scope, evidence, and open questions
- [ ] Ranks findings and includes location, impact, and repair direction
- [ ] Reviews real assertions, negative paths, boundaries, isolation, and repeatability
- [ ] Does not present speculation as fact
