<div align="right"><a href="./2026-09-15-v2-test-engineering-two-batch-design.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# v2.0 Test Engineering Two-Batch Skill Design

## Status

`APPROVED_FOR_IMPLEMENTATION` (2026-09-15). The confirmed meaning of “drag cards” is moving roadmap cards in GitHub Project #4. Local `develop` has fast-forwarded `origin/main` at `d63a9fa`. Implementation stays local on `develop`; no push is implied.

## Goal and boundaries

Implement the 25 `v2 P1` candidate Skill cards in Project #4 in two batches. Every card receives a Capability Match review first. No same-named physical directory exists in the current repository, so the initial decision is `NEW`; if implementation review shows that the primary inputs, outputs, and decision logic are already fully covered, change the decision to `ENHANCE` or `MATCH` before creating a package instead of duplicating capability.

Project cards are execution records, not runtime Skill dependencies. Move only the exact batch from `Todo` to `In Progress` after its contract test is confirmed RED. Move a card to `Done` only after bilingual synchronization and quality gates pass. A card state does not prove model quality, business approval, release, or risk acceptance.

## Two batches

### Batch 1: Test design methods (9 cards)

`decision-table-testing`, `state-transition-testing`, `boundary-value-testing`, `equivalence-partitioning`, `pairwise-testing`, `combinatorial-testing`, `model-based-testing`, `property-based-testing`, and `metamorphic-testing`.

These Skills turn requirements, rules, states, data domains, factors, or reference relations into reviewable test-design candidates. They record design rationale, selection, unknowns, and validation suggestions; they do not claim execution, replace a complete strategy, write full test cases, or run tests.

### Batch 2: API, UI, and test-engineering quality (16 cards)

`api-schema-validation`, `api-negative-testing`, `api-idempotency-testing`, `api-pagination-testing`, `api-rate-limit-testing`, `api-version-compatibility-testing`, `api-error-contract-testing`, `ui-test-strategy`, `ui-test-selector-review`, `ui-test-wait-strategy-review`, `visual-regression-testing`, `cross-browser-testing`, `test-code-review`, `mutation-testing-analysis`, `mock-quality-review`, and `test-suite-health-analysis`.

These Skills address contracts, failure semantics, compatibility, UI stability, and test-asset quality. They analyze user-provided specifications, code, test assets, or reports only; they do not call real APIs, browsers, databases, mutation runners, or production systems.

## Shared output contract

Every main Prompt starts with `known`, `missing`, `conflicting`, `stale`, `out_of_scope`, and `assumptions`. It then separates facts, evidence-backed inferences, candidate recommendations, and Human decisions.

Every finding uses the Skill's stable prefix and two-digit sequence and includes at least the object/rule, source, trigger or applicability, expected concern, evidence state, impact/priority, owner role, close condition, and validation method. Unknown thresholds, missing execution records, conflicting material, and stale information remain `unassessed`, `blocked`, or pending clarification; static file presence or Prompt wording cannot upgrade them to pass.

Each bilingual package is independently installable and contains:

- `SKILL.md` and `prompts/<slug>.md`;
- `agents/openai.yaml` with `metadata.key` equal to the directory slug;
- `evals/eval.yaml`;
- `basic-success.yaml`, `edge-incomplete-input.yaml`, and `edge-scope-boundary.yaml`;
- `evals/trigger-prompts.csv` covering `explicit`, `implicit`, `contextual`, and `negative`, with both positive and negative controls;
- `evals/local-rules.json` whose `skill` equals the physical directory slug.

Real-model Evals, external test targets, semantic equivalence, quality scores, and release state remain `NOT_RUN`, `NOT_SCORED`, or `UNASSESSED` unless independent evidence exists.

## Implementation order

1. Write the batch contract test and observe RED.
2. After confirming the RED cause, move only the exact batch cards to `In Progress`.
3. Complete every Skill through RED → minimal GREEN → REFACTOR, including both languages and three Eval cases.
4. Update the registry, Matrix/Register, bilingual README/Catalog/Graph, and any required routing documentation.
5. Run target checks, repository contracts, and quality gates; move only evidenced cards to `Done`.
6. Leave all other Project cards unchanged; do not create repository Issues, push, or create a Release.

## Acceptance

The minimum completion bar is evidence for all 25 exact cards passing through `In Progress` and `Done`; 25 matching physical Skill packages in each language; structural, metadata, Eval, independence, integrity, and bilingual gates passing; generated governance views reproducible from the current registry; `git diff --check` passing; and an explicit report separating static structure evidence from unrun model or external validation.
