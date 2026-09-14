<div align="right"><a href="./2026-09-14-v1-1-next-five-quality-skills-design.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# v1.1 Next Five Quality Skill Cards Design

## Status

`APPROVED_FOR_IMPLEMENTATION` (2026-09-14, after plan-review fixes). This design covers the next five v1.1 P0 cards in Project #4. All five cards have been moved to `In Progress`; this document defines capability matching and implementation boundaries only. Skill packages, the governance registry, and generated views are not changed by this design step.

## Capability Match Decisions

The repository rule is “match first, enhance before adding; create an independent directory only for `NEW`.” This batch therefore does not mechanically create five same-named directories:

| Candidate card | Decision | Existing boundary | Batch action |
| --- | --- | --- | --- |
| `business-rule-extraction` | `NEW` | `requirements-analysis` is an entry point and `requirement-quality-review` is an overview; neither has an atomic, source-traceable business-rule extraction contract | Create an independent bilingual Skill |
| `business-rule-consistency-review` | `ENHANCE` | `requirement-consistency-analysis` already compares terminology, states, rules, and behavior across sources | Add a business-rule mode, rule invariants, applicability/precedence, and rule-level evidence fields; do not create a duplicate directory |
| `technical-design-quality-review` | `NEW` | `technical-quality-perspective` routes stages and `code-review` reviews reviewable code changes; no standalone pre-implementation technical-design quality contract exists | Create an independent bilingual Skill |
| `architecture-testability-review` | `ENHANCE` | `testability-analysis` already covers observability, controllability, isolation, determinism, data, and fault injection | Add architecture-artifact inputs, test seams, dependency substitutes, environment topology, and architecture-level evidence; do not create a duplicate directory |
| `api-design-quality-review` | `NEW` | `api-contract-testing` verifies contracts and compatibility while `api-testing` executes tests; no pre-implementation API design quality contract exists | Create an independent bilingual Skill |

If implementation evidence shows that a proposed `NEW` scope is already covered semantically, change the registry and Matching Register to an evidenced `ENHANCE`/`MERGE` and stop duplicate creation.

## Shared Contract

All new and enhanced content follows the repository conventions:

- Chinese and English entry points, Prompts, metadata, Evals, and local trigger data stay structurally paired.
- Enhanced candidates do not get alias directories; their local `trigger-prompts.csv` / `local-rules.json` live under the physical target Skill's `evals/`, JSON `skill` remains the target slug, and CSV data covers the candidate name or mode phrase.
- Input audits separate `known`, `missing`, `conflicting`, `stale`, `out_of_scope`, and `assumptions`; source facts, evidence-backed inferences, recommendations, and Human decisions stay separate.
- Conclusions cite sources and minimum evidence; file presence, name matching, report wording, and design declarations are not execution, compatibility, or release evidence.
- Each package maintains success, incomplete-input, and scope/risk-boundary Evals plus explicit, implicit, contextual, and negative trigger samples; absent `skill.selection` evidence is `BLOCKED` in the local runner.
- Scope boundaries use semantic `agent_judge` cases. Registry quality and real model execution remain `NOT_SCORED`/`NOT_RUN` until independent execution evidence exists.

## New Skill Designs

### `business-rule-extraction`

Extract traceable atomic business rules from PRDs, policies, contracts, workflows, acceptance criteria, and supplied examples. Each `BR-##` finding includes the rule statement, source, applicable actor/object, trigger, preconditions, action/outcome, constraint or invariant, exception, evidence, unknowns, impact, and validation/test hint.

It does not invent thresholds, precedence, state transitions, or default exceptions; turn recommendations into facts; or approve rules for Product, Compliance, or Business. Combine statements only when the material supports the grouping; otherwise preserve separate sources and open questions.

### `technical-design-quality-review`

Review architecture notes, ADRs, component/data-flow designs, technical proposals, and non-functional constraints before implementation or test design. Assess architecture boundaries, dependencies and failure modes, data consistency, security, performance, observability, compatibility, maintainability, and verification readiness, producing `TD-##` findings with impact/severity, missing information, actions, owner roles, and validation methods.

It does not review code that was not supplied, run builds or tests, turn design presence into implementation correctness, or approve architecture or risk acceptance for a Human.

### `api-design-quality-review`

Review API designs, OpenAPI/contracts, request/response examples, error models, authentication/authorization, idempotency, pagination, status codes, version evolution, compatibility, consumer impact, and observability before implementation. Produce `API-##` findings retaining operation, source, evidence, impact, compatibility risk, migration questions, owner role, and validation method.

It does not execute an API, decide consumer semantics, treat examples as a complete contract, claim compatibility or security tests passed, or choose the final versioning policy for the team.

## Enhanced Skill Designs

### `business-rule-consistency-review` → `requirement-consistency-analysis`

Add an optional business-rule comparison mode to the existing Prompt. Use stable rule ID, subject/object, trigger, applicability, precedence/override relation, action, outcome, and exception as comparison keys; keep relation values separate from evidence statuses. Preserve both original statements, rule-level evidence, and unresolved precedence; never treat “stricter” as automatically higher priority.

Add business-rule success, single-source incomplete, and cross-version/region boundary Evals, and state when to choose the mode in the Skill entry. Existing generic consistency cases and the `RC-##` contract remain valid.

### `architecture-testability-review` → `testability-analysis`

Add an architecture mode to the existing Prompt. Inputs may include architecture diagrams, component boundaries, dependency topology, asynchronous flows, data stores, external services, configuration, and deployment environments. In addition to general testability dimensions, output test seams, substitute/mock strategy, isolation boundaries, fault-injection entry points, environment reproducibility, and evidence gaps.

Add architecture-testability success, incomplete-architecture-material, and unsafe-test-seam boundary Evals. Do not treat a test-framework choice as architecture testability or recommend unsafe backdoors.

## Delivery and Verification Boundary

After implementation:

1. Create bilingual standalone packages, metadata, primary Prompts, three case types, `trigger-prompts.csv`, and `local-rules.json` for the three `NEW` Skills.
2. Modify the existing bilingual entries/Prompts and add matching Evals and trigger data for the two `ENHANCE` Skills without creating duplicate directories.
3. Update the registry, Matching Register, bilingual README/Catalog/Graph, and generated views with evidenced `NEW`/`ENHANCE` decisions and paths.
4. Run target Eval validation/dry-runs, the local trigger runner, the full test suite, independence/integrity/bilingual quality gates, and `git diff --check`.
5. Reconfirm these five Project cards are `In Progress` and all other card states are unchanged. Do not push or publish; real model execution remains `NOT_RUN`.

## Non-goals

- Do not change the existing semantics of the first five v1.1 Skills except where shared governance or validation synchronization is required.
- Do not create repository Issues or execute real business-rule, API, architecture, or test targets.
- Do not present `NEW`/`ENHANCE`, quality scores, runtime results, or release conclusions as final facts without evidence.
