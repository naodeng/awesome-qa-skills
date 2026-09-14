<div align="right"><a href="./2026-09-14-v1-1-following-five-quality-skills-design.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# v1.1 Following Five Quality Skill Cards Design

## Status

`APPROVED_FOR_IMPLEMENTATION` (2026-09-14, after plan-review fixes). This design covers the next five v1.1 P0 cards in Project #4. The five cards have been moved from `Todo` to `In Progress`; this document defines capability matching, package boundaries, and verification contracts. It does not create Skill packages or change the governance registry or generated views.

## Capability Match Decisions

The repository rule is “match first, enhance before adding; create an independent directory only for `NEW`.” This batch therefore uses four standalone new Skills and one enhancement of an existing Skill:

| Candidate card | Decision | Existing capability evidence | Batch boundary |
| --- | --- | --- | --- |
| `database-design-quality-review` | `NEW` | The repository has requirement, API, testability, and quality-risk analysis, but no standalone review contract for data models, constraints, migrations, and transactions | Create a bilingual standalone Skill; review database design only, without connecting to or modifying a target database |
| `observability-design-review` | `NEW` | `distributed-trace-analysis`, `log-analysis`, and `metrics-anomaly-analysis` analyze runtime evidence; `testability-analysis` treats observability as one test-readiness dimension | Create a bilingual standalone Skill; review implementation-time logs, metrics, traces, SLOs, and alert design only |
| `error-handling-design-review` | `NEW` | `production-incident-analysis` and `root-cause-analysis` use incident and cause evidence; API and testing Skills cover only local error behavior | Create a bilingual standalone Skill; review pre-implementation error classification, propagation, recovery, and consistency design only |
| `test-scope-analysis` | `NEW` | `regression-scope-analysis` is limited to change or release regression scope; `test-strategy` produces a full strategy rather than a standalone scope audit | Create a bilingual standalone Skill; define inclusion, exclusion, depth, and expansion triggers without replacing a full strategy or test selection |
| `test-coverage-analysis` | `ENHANCE` → `requirement-traceability-analysis` | The existing Skill already provides bidirectional requirement-to-test/evidence mapping and coverage states; a new directory would duplicate the coverage matrix | Add an optional coverage-analysis mode and a `TC-##` view to the existing Skill; preserve the `RT-##` traceability contract and create no duplicate directory |

If implementation evidence shows that any proposed `NEW` capability is fully covered by an existing Skill's primary inputs, outputs, and decision logic, change it to an evidenced `ENHANCE` or `MERGE` before creating its directory, and update this design accordingly.

## Shared Contract

- Chinese and English entry points, Prompts, metadata, Evals, and local trigger data remain structurally paired; directory names and `metadata.key` use the same lowercase hyphenated slug.
- Enhanced candidates do not get alias directories; their local `trigger-prompts.csv` / `local-rules.json` live under the physical target Skill's `evals/`, JSON `skill` remains the target slug, and CSV data covers the candidate name or mode phrase.
- Audit every input as `known`, `missing`, `conflicting`, `stale`, `out_of_scope`, or `assumptions`; keep source facts, evidence-backed inferences, recommendations, and Human decisions separate.
- Bind every finding to a source and minimum evidence. File presence, design claims, test names, report wording, or tool configuration cannot become execution results, compatibility passes, risk acceptance, or release approval.
- Four new Skills use stable finding IDs: `DB-##`, `OBS-##`, `EH-##`, and `TS-##`. The coverage enhancement preserves `RT-##` traceability findings and uses `TC-##` for coverage views; relation types and coverage states must remain separate.
- Every package has at least success, incomplete-input, and scope/risk-boundary Evals, plus explicit, implicit, contextual, and negative trigger data. Without `skill.selection` evidence, the local runner reports `BLOCKED` rather than inferring successful triggering.
- Design reviews produce AI-assisted findings, gaps, recommendations, and validation methods only; registry quality remains `NOT_SCORED`, and real model execution remains `NOT_RUN` until independent evidence exists.

## New Skill Designs

### `database-design-quality-review`

Review ERDs, data models, DDL, ORM schemas, migration plans, data ownership, retention/deletion rules, query constraints, and recovery design before implementation or migration.

Each `DB-##` finding includes at least: object and scope, source, evidence, design rule, finding, impact/severity, constraint or index risk, transaction/concurrency impact, migration and rollback concern, owner role, and verifiable closure condition. Review dimensions include model integrity, keys and constraints, indexes and query assumptions, transaction isolation, concurrency, lifecycle and privacy, migration compatibility, performance risk, backup/recovery, and test readiness.

It does not connect to, modify, or migrate a real database; execute queries or benchmarks; infer business rules from table names; invent data-volume or consistency thresholds; or approve a schema, risk acceptance, or launch for a Human.

### `observability-design-review`

Review logs, metrics, traces, context propagation, SLOs/SLIs, alerts, dashboards, sampling, retention, privacy, and cost design before implementation.

Each `OBS-##` finding includes at least: signal type, source, covered object, fields/dimensions, expected semantics, evidence, gap, impact, detection or alert action, owner role, and validation method. Review dimensions include critical-path coverage, cross-service correlation, field semantics, cardinality and sampling, SLO/SLI computability, alert actionability, failure-mode visibility, sensitive-data handling, retention cost, and verification readiness.

It does not read real runtime logs or metrics to declare system health, treat a dashboard's existence as alert effectiveness, execute production probes, choose an SLO or incident severity for the team, or treat a tool name as observability evidence.

### `error-handling-design-review`

Review error taxonomy, exception boundaries, timeouts, retries, backoff, circuit breaking, degradation, idempotency, transaction consistency, error propagation, user/consumer contracts, telemetry, and recovery design before implementation.

Each `EH-##` finding includes at least: failure mode, trigger, boundary, expected behavior, propagation/translation, retry or fallback condition, data-consistency impact, user/caller-visible result, observable evidence, owner role, and validation method. The review distinguishes retryable, non-retryable, human-intervention, and safe-rejection paths; one generic “return an error” response cannot cover different failure modes.

It does not run fault injection, conduct a real incident review, treat error-handling code presence as correct behavior, choose final user copy, SLA, risk acceptance, or recovery approval for the team, or treat an example error response as a complete contract.

### `test-scope-analysis`

Analyze test activity, iteration, release, or risk-review boundaries before testing begins: what is included, excluded, deeply covered, dependent, and eligible to trigger expansion.

Each `TS-##` finding includes at least: goal and object, included items, excluded items, risk/impact rationale, coverage depth, platform/role/data/environment dependencies, stop conditions, expansion triggers, residual risk, source evidence, and owner role. The analysis distinguishes core journeys, direct and transitive impact, non-functional concerns, migration/compatibility, and unassessed areas, and gives a verifiable reason for every scope tradeoff.

It does not produce a complete test strategy, select a concrete executable set from existing test assets, execute tests, or turn a scope statement into coverage proof; change or release regression selection remains with `regression-scope-analysis` and related selection capabilities.

## Enhanced Skill Design

### `test-coverage-analysis` → `requirement-traceability-analysis`

Add an optional `coverage_analysis` mode to the existing Skill without creating a `test-coverage-analysis` directory. The mode accepts requirements, risks, behaviors/scenarios, test assets, and execution evidence; it reuses the existing bidirectional trace model and adds a `TC-##` coverage view.

Each `TC-##` row includes at least: requirement/risk/behavior object, source, linked test asset, relation type, coverage state, execution identity/time/environment when supplied, evidence quality, orphan or duplicate signal, gap action, and validation method. Coverage states remain `complete`, `partial`, `unverified`, `stale`, `unexecuted`, and `unassessed`; without real execution evidence, `passed` is forbidden. Preserve existing `RT-##` bidirectional relationship findings and explicitly check both requirement-to-test and test-to-requirement directions.

The mode does not calculate code-line coverage without tool evidence, treat test-file presence, name matching, or report summaries as executed coverage, replace `test-scope-analysis` inclusion/exclusion decisions, or decide risk acceptance and release conclusions for a Human. Add Evals for a valid mapping, incomplete evidence, and scope boundaries while keeping the existing generic traceability cases passing.

## Components, Data Flow, and Failure Handling

Each new Skill's minimum components are `SKILL.md`, `prompts/<slug>.md`, `agents/openai.yaml`, `evals/eval.yaml`, and three case types under `evals/cases/`; local trigger validation adds `trigger-prompts.csv` and `local-rules.json`. The enhanced Skill keeps its existing directory and metadata while adding the mode description, Prompt guidance, Evals, and trigger data.

The shared data flow is: input materials → input audit → structured findings/mappings → evidence states and scope boundaries → risk/gap actions → Human questions. When primary material is missing, deliver a constrained result with explicit gaps; when source conflicts affect a core conclusion, preserve both sides and mark the blocker; without execution identity, time, environment, and raw results, coverage or runtime conclusions remain `unverified`, `unexecuted`, or `unassessed`.

## TDD, Eval, and Governance Delivery

1. Add the batch's local contract test first and run RED, proving that the four new directories are absent and the coverage enhancement contract is not yet satisfied; do not write Skill content before observing the expected failure.
2. Complete RED → minimal GREEN → REFACTOR independently for each Skill; batch generation cannot replace per-Skill verification. Finish the package's minimal content and three Evals before moving to the next package.
3. Create bilingual packages for the four new Skills; enhance the bilingual entry points and Prompt for `requirement-traceability-analysis`, adding the `coverage_analysis` cases, trigger data, and local rules.
4. Update the registry, Capability Match Register, bilingual READMEs/Catalog/Graph, and required generated views; record four `NEW` decisions, one `ENHANCE` decision, and their evidence paths.
5. Run target Skill `skill-up validate`, dry-runs, the local trigger runner, relevant contract tests, the full test suite, independence/integrity/bilingual quality gates, and `git diff --check`.
6. Finally verify that these five cards remain `In Progress` and the next Todo cards were not changed. Do not push or publish a version; real model execution remains `NOT_RUN`.

## Non-goals

- Do not create a duplicate `test-coverage-analysis` directory or change the meaning of `requirement-traceability-analysis` relation and coverage enums.
- Do not change the business semantics of the previous v1.1 Skills except where shared governance or validation synchronization is required.
- Do not connect to a real database, production observability system, or live incident environment; do not run real migrations, fault injection, tests, or releases.
- Do not present static package structure, Eval configuration, or local-rule results as real model effectiveness, system runtime results, Human approval, or Release completion.
