<div align="right"><a href="./2026-09-14-v1-1-test-design-discovery-five-design.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# v1.1 Test-Design Discovery Five-Card Skill Design

## Status

`APPROVED_FOR_IMPLEMENTATION` (2026-09-14, after plan-review fixes). This document covers the next five v1.1 P0 Todo cards in Project #4. It defines capability matching, package boundaries, and verification contracts only; it does not create Skill packages or change the governance registry or generated views.

## Capability Match Decisions

The repository rule is “match first, enhance before adding; create an independent directory only when the primary inputs, outputs, and decision logic are genuinely different.” All five candidates have a distinct deliverable, with the boundaries below:

| Candidate card | Decision | Closest capability evidence | Independent boundary |
| --- | --- | --- | --- |
| `test-gap-analysis` | `NEW` | `requirement-traceability-analysis` maps stable-ID artifact relationships; `test-case-reviewer` reviews existing cases; neither has a standalone missing-test-obligation discovery contract | Discover missing test obligations from requirements, risks, changes, defects, and test assets; output `TG-##`; do not produce a full traceability matrix or call a gap a coverage/pass result |
| `risk-based-testing` | `NEW` | `quality-risk-analysis` identifies and ranks quality risks; `test-strategy` creates a complete strategy; `regression-scope-analysis` focuses on change/release regression boundaries | Translate known risks into test priority, depth, methods, and time-box tradeoffs; output `RBT-##`; do not replace a risk register, complete strategy, or existing-test selection |
| `edge-case-discovery` | `NEW` | `requirements-analysis` and `test-case-writing` require boundary consideration; `test-case-reviewer` finds boundary omissions in existing cases, but none has a standalone boundary-discovery deliverable | Enumerate boundary candidates across input, time, state, resource, concurrency, platform, and combination dimensions; output `EC-##`; do not perform requirement-quality review or write full cases |
| `negative-scenario-discovery` | `NEW` | `requirements-analysis` and `test-case-writing` can include exception paths; `test-case-reviewer` reviews existing negative coverage, but none has a standalone failure/denial/recovery discovery contract | Discover `NS-##` from invalid input, authorization denial, dependency failure, timeout, retry, idempotency, and inconsistency paths; do not run fault injection or write full cases |
| `test-data-requirement-analysis` | `NEW` | `test-data-generation` produces data models, generation rules, and datasets; it consumes data requirements rather than owning a standalone prerequisite/blocker analysis | Analyze fields, relationships, states, roles, privacy, sources, lifecycle, cleanup, and environment prerequisites; output `TDR-##`; do not generate data, copy production data, or replace data-generation planning |

### Six-field match evidence

- **name**: The candidate names differ from existing target `SKILL.md` names; similarity alone is not the reason for adding a package. The differences below are supported by purpose, inputs, outputs, and decision logic.
- **purpose**: The five capabilities focus respectively on missing test obligations, risk-to-test decisions, boundary candidates, failure-path candidates, and data prerequisites. Their neighboring Skills have different primary purposes.
- **inputs**: The first four may consume requirements/design/risk/change/test evidence, but each uses a different evidence slice and minimum input. Data-requirement analysis consumes field relationships, lifecycle, privacy, and environment constraints and does not require a dataset that can already be generated.
- **outputs**: The five use stable finding IDs `TG-##`, `RBT-##`, `EC-##`, `NS-##`, and `TDR-##`, with evidence, impact, priority, gap action, and validation method. These are not the default output contracts of the neighboring Skills.
- **decision_logic**: Discovery Skills separate facts, inferences, and candidates by source, trigger, expected/failure result, and evidence state. Risk-based testing explains priority and depth tradeoffs. Data analysis first decides missing/conflicting/privacy/cleanup blockers and must not jump straight to generation.
- **workflow_role**: All five belong to Engineering QA / Test Design and Preparation, before strategy or execution. `discover-testing` may route to one as the primary capability. They are not runtime executors, production probes, or Human release gates.

If implementation evidence shows that a candidate is fully covered by an existing Skill's primary inputs, outputs, and decision logic, change it to `ENHANCE` or `MATCH` before creating its directory and update this design and plan. Do not duplicate capability merely to complete a card count.

## Shared Contract

- Chinese and English entry points, Prompts, metadata, Evals, and local trigger data remain structurally paired. Directory names, frontmatter `name`, and `agents/openai.yaml` `metadata.key` use the same lowercase hyphenated slug.
- Each package contains `SKILL.md`, `prompts/<slug>.md`, `agents/openai.yaml`, `evals/eval.yaml`, success/incomplete/scope-or-risk-boundary cases, `trigger-prompts.csv`, and `local-rules.json`.
- Every analysis records `known`, `missing`, `conflicting`, `stale`, `out_of_scope`, and `assumptions`; facts, evidence-backed inference, candidate recommendations, and Human decisions remain separate.
- Every finding has a source and minimum evidence plus impact/priority, owner role, close condition, and validation method. File presence, name matching, report wording, static configuration, or a prompt template is not execution evidence.
- When primary material is missing, return a bounded first pass and mark `unassessed`/`blocked`; when a conflict affects a core decision, preserve both sides rather than silently merging them.
- This batch does not connect to real projects, databases, production observability, or external services, and does not execute real tests, fault injection, data generation, migration, release, or approval.
- Local trigger data covers `explicit`, `implicit`, `contextual`, and `negative`, with both positive and negative samples. Without real `skill.selection` evidence, the runner reports `BLOCKED`.

## Minimum Design for the Five Skills

### `test-gap-analysis`

Inputs are requirements/acceptance criteria, risks, changes, defect history, test assets, and execution evidence when supplied. Each `TG-##` contains the test obligation or behavior, source, gap type, impact/priority, existing controls, evidence state, proposed test intent, owner role, close condition, and validation method. Gap types distinguish missing requirement-to-test links, orphan tests, unverified execution, stale evidence, uncovered risk, and duplicate/low-value coverage. It does not build a full RT/TC matrix, claim coverage or pass status, or accept risk for a Human.

### `risk-based-testing`

Inputs are business criticality, failure modes, change surface, user/data impact, past defects, detectability, environment/resources, and time box. Each `RBT-##` contains risk source, assumptions, test objective, level/method, depth, priority basis, scope tradeoff, stop condition, scope-expansion trigger, and required evidence. It does not calculate pseudo-precise risk scores, produce a full test strategy, select concrete existing test IDs, execute tests, or turn “high risk” into a Human release-blocking decision.

### `edge-case-discovery`

Inputs are requirements, data domains, state models, time rules, resource/concurrency limits, platform differences, and existing test/defect evidence. Each `EC-##` contains dimension, boundary or combination, trigger, expected concern, source, evidence state, impact/priority, validation suggestion, and open question. At minimum consider numeric/length, null/type, time/timezone, state transition, capacity/resource, concurrency/order, platform/localization, and combination boundaries; never present invented thresholds as facts.

### `negative-scenario-discovery`

Inputs are functional goals, roles/permissions, input constraints, dependency/failure contracts, idempotency/transaction rules, past failures, and recovery design. Each `NS-##` contains failure mode, stimulus, preconditions, expected rejection/degradation/retry/human-handoff behavior, user/caller-visible result, data-consistency impact, evidence need, and validation method. Distinguish invalid input, unauthorized access, dependency failure, timeout, retry exhaustion, duplicate request, partial failure, and unsafe recovery; do not execute fault injection or invent error codes.

### `test-data-requirement-analysis`

Inputs are requirements/scenarios, field schema, relationships/constraints, roles/permissions, states, privacy/compliance, data sources, environment, lifecycle, and cleanup limits. Each `TDR-##` contains scenario/test goal, required entities and fields, valid/invalid/boundary/combination conditions, referential integrity, state/role prerequisites, source/construction constraints, masking requirements, setup/cleanup, blockers, owner role, and validation method. It analyzes preparation requirements and gaps only; it does not create records, call real data sources, or promise that data already exists.

## Data Flow, Evals, and Governance Delivery

The shared data flow is: input material → input audit → structured findings → evidence/priority → test intent or preparation action → Human questions. Each package has at least one success, incomplete-input, and scope/risk-boundary Eval and all four local trigger modes. Real model quality remains `NOT_SCORED`; model Evals remain `NOT_RUN`; local dry-run only proves that configuration loads.

The implementation order is: write the batch contract test and observe RED; after RED, move the five exact Project cards from `Todo` to `In Progress`; complete each Skill independently through RED → minimal GREEN → REFACTOR; then update the registry, Capability Match Register, bilingual READMEs/Catalog/Graph, and generated views. Leave all other Project cards unchanged.

## Non-goals

- Do not create a traceability-matrix replacement under `test-gap-analysis` or change `requirement-traceability-analysis` `RT-##`/`TC-##` semantics.
- Do not turn `risk-based-testing` into an alias for `test-strategy`, `quality-risk-analysis`, or `regression-test-selection`.
- Do not turn edge/negative discovery into full test-case authoring, execution, or fault injection.
- Do not turn data-requirement analysis into a `test-data-generation` dataset generator.
- Do not commit, push, or publish; preserve existing uncommitted worktree changes.
