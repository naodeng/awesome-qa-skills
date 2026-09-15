<div align="right"><a href="./2026-09-15-v3-v4-two-batch-design.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# v3-v4 Reliability, Security, QE, and AI Native Two-Batch Skill Design

## Status

“DRAFT_FOR_REVIEW” (2026-09-15). The two-batch split was approved in chat; this document is the written specification before the implementation plan and still needs user review.

This design uses develop commit 15c3804 as its baseline. That commit fast-forwarded the latest origin/main into develop. This work does not push, create a Release, or turn roadmap implementation into an automatic version-release claim.

Project #4 (Awesome QA Skills — Governance & Roadmap) currently contains 42 cards whose titles start with v3-v4 P2｜候选 Skill｜; all are Todo. “Dragging cards” means updating those Project cards through the implementation gates, not adding a repository UI.

## Goal

Advance the 42 v3-v4 P2 candidate cards in two capability batches:

1. Batch 1: Reliability + Security, 17 cards.
2. Batch 2: Quality Engineering + AI Native, 25 cards.

Run Capability Match for every card before deciding whether to create a new bilingual physical Skill, enhance an existing Skill, merge into an existing capability, or record an existing match. Card count must not be converted into physical-directory count by duplicating existing capabilities.

## Batch Scope and Cards

### Batch 1: Reliability + Security (17)

| Group | Skill | Project item |
| --- | --- | --- |
| Reliability | reliability-testing | PVTI_lAHOAHP1as4BjBhVzg6Sc5w |
| Reliability | resilience-testing | PVTI_lAHOAHP1as4BjBhVzg6Sc68 |
| Reliability | chaos-testing | PVTI_lAHOAHP1as4BjBhVzg6Sc8M |
| Reliability | failover-testing | PVTI_lAHOAHP1as4BjBhVzg6Sc90 |
| Reliability | recovery-testing | PVTI_lAHOAHP1as4BjBhVzg6Sc_w |
| Reliability | retry-testing | PVTI_lAHOAHP1as4BjBhVzg6SdAw |
| Reliability | timeout-testing | PVTI_lAHOAHP1as4BjBhVzg6SdCU |
| Reliability | circuit-breaker-testing | PVTI_lAHOAHP1as4BjBhVzg6SdEM |
| Reliability | dependency-failure-testing | PVTI_lAHOAHP1as4BjBhVzg6SdFo |
| Reliability | disaster-recovery-testing | PVTI_lAHOAHP1as4BjBhVzg6SdHI |
| Security | authentication-testing | PVTI_lAHOAHP1as4BjBhVzg6SdJA |
| Security | authorization-testing | PVTI_lAHOAHP1as4BjBhVzg6SdLg |
| Security | session-security-testing | PVTI_lAHOAHP1as4BjBhVzg6SdNI |
| Security | api-security-testing | PVTI_lAHOAHP1as4BjBhVzg6SdPY |
| Security | security-requirement-review | PVTI_lAHOAHP1as4BjBhVzg6SdQ0 |
| Security | threat-modeling | PVTI_lAHOAHP1as4BjBhVzg6SdSk |
| Security | secrets-exposure-review | PVTI_lAHOAHP1as4BjBhVzg6SdUg |

Reliability Skills analyze reliability objectives, failure modes, degradation, failover, recovery design, and verification readiness. They do not inject faults, access dependencies, run load tests, or execute disaster-recovery exercises. Security Skills use supplied requirements, code, configuration, logs, or policy material to propose security test/review candidates. They do not log in, call live APIs, read credentials, or turn static findings into a security-pass claim.

### Batch 2: Quality Engineering + AI Native (25)

| Group | Skill | Project item |
| --- | --- | --- |
| Quality Engineering | quality-gate-design | PVTI_lAHOAHP1as4BjBhVzg6SdWc |
| Quality Engineering | quality-metrics-design | PVTI_lAHOAHP1as4BjBhVzg6SdY4 |
| Quality Engineering | quality-dashboard-design | PVTI_lAHOAHP1as4BjBhVzg6SdaY |
| Quality Engineering | quality-debt-analysis | PVTI_lAHOAHP1as4BjBhVzg6SdcE |
| Quality Engineering | quality-maturity-assessment | PVTI_lAHOAHP1as4BjBhVzg6Sddo |
| Quality Engineering | test-effectiveness-analysis | PVTI_lAHOAHP1as4BjBhVzg6SdfA |
| Quality Engineering | automation-roi-analysis | PVTI_lAHOAHP1as4BjBhVzg6Sdg8 |
| Quality Engineering | testing-bottleneck-analysis | PVTI_lAHOAHP1as4BjBhVzg6Sdig |
| Quality Engineering | regression-optimization | PVTI_lAHOAHP1as4BjBhVzg6SdkQ |
| Quality Engineering | ci-test-optimization | PVTI_lAHOAHP1as4BjBhVzg6SdnA |
| Quality Engineering | test-runtime-optimization | PVTI_lAHOAHP1as4BjBhVzg6Sdo4 |
| Quality Engineering | test-maintenance-cost-analysis | PVTI_lAHOAHP1as4BjBhVzg6Sdqc |
| Quality Engineering | quality-productivity-metrics | PVTI_lAHOAHP1as4BjBhVzg6SdsA |
| AI Native | prompt-regression-testing | PVTI_lAHOAHP1as4BjBhVzg6SdtI |
| AI Native | rag-quality-testing | PVTI_lAHOAHP1as4BjBhVzg6Sdus |
| AI Native | rag-retrieval-testing | PVTI_lAHOAHP1as4BjBhVzg6Sdwg |
| AI Native | agent-loop-testing | PVTI_lAHOAHP1as4BjBhVzg6SdyQ |
| AI Native | agent-memory-testing | PVTI_lAHOAHP1as4BjBhVzg6Sdzo |
| AI Native | agent-permission-testing | PVTI_lAHOAHP1as4BjBhVzg6Sd1E |
| AI Native | agent-failure-recovery-testing | PVTI_lAHOAHP1as4BjBhVzg6Sd2I |
| AI Native | agent-long-running-testing | PVTI_lAHOAHP1as4BjBhVzg6Sd3w |
| AI Native | multi-agent-testing | PVTI_lAHOAHP1as4BjBhVzg6Sd5g |
| AI Native | llm-hallucination-testing | PVTI_lAHOAHP1as4BjBhVzg6Sd7Q |
| AI Native | llm-consistency-testing | PVTI_lAHOAHP1as4BjBhVzg6Sd8Q |
| AI Native | ai-safety-testing | PVTI_lAHOAHP1as4BjBhVzg6Sd9w |

Quality Engineering Skills define evidence, metrics, gates, and efficiency analyses. They do not invent numbers, replace release approval, or rank individuals. AI Native Skills design reviewable model, retrieval, Agent, and safety verification; they do not call models, retrievers, tools, or production systems.

## Capability Match Gate

Review every candidate and write the conclusion into the registry and Matching Register:

1. Read current bilingual Skills, Prompts, Evals, governance matrix, and adjacent Workflows to establish existing-capability evidence.
2. Compare the candidate's name, purpose, primary inputs, outputs, decision logic, and Workflow role.
3. Record EXISTING, ENHANCE, MERGE, MATCH, or NEW; every result needs concrete file paths and a difference statement.
4. Create skills/{zh,en}/.../<slug>/ only for NEW. ENHANCE changes the selected existing package, MERGE combines the capability while preserving boundaries, and MATCH records governance/routing evidence only.

prompt-regression-testing follows the existing four-stage roadmap by default: review it as a regression mode of prompt-testing, using Match/Enhance rather than an alias directory. Reclassify it as NEW only if new evidence proves that the existing Skill cannot carry an independent input, output, and decision contract.

This design does not pre-label every candidate as NEW. A batch may close with new packages, enhancements, and Match/Merge records, but every card must have an independent, traceable deliverable.

## Skill Package and Prompt Contract

For every new or enhanced language package:

- Keep Chinese and English directory names aligned. A new package contains SKILL.md, prompts/<slug>.md, agents/openai.yaml, evals/eval.yaml, three case files, trigger-prompts.csv, and local-rules.json.
- SKILL.md contains when to use, execution flow, core constraints, on-demand loading, pre-delivery self-check, common pitfalls, and best practices.
- The main Prompt starts with known, missing, conflicting, stale, out_of_scope, and assumptions, then separates facts, evidence-backed inferences, candidate recommendations, and Human decisions.
- Each domain finding uses a stable <PREFIX>-## identifier and records object/rule, source, trigger or applicability, expected concern/rationale, evidence state, impact/priority, owner role, close condition, and validation method.
- If thresholds, execution records, version relations, baselines, credential boundaries, or business approval are missing, preserve unknown, unassessed, blocked, or open questions. Do not infer a pass from file presence, names, or templates.
- Trigger CSV files cover explicit, implicit, contextual, and negative, with both triggering and reverse-control samples. Chinese samples are Chinese; English package bodies contain no Chinese.
- Eval environments default to pure text with no external target. Three cases cover success, incomplete input, and near-neighbor/out-of-scope misuse. Boundary cases reject unsupported claims such as “tests were executed,” “all tests passed,” and “release approved.”

Use these stable prefixes as the starting mapping; the contract tests are the final authority:

| Skill | Prefix | Skill | Prefix |
| --- | --- | --- | --- |
| reliability-testing | RLT- | resilience-testing | RES- |
| chaos-testing | CHS- | failover-testing | FOV- |
| recovery-testing | RCV- | retry-testing | RTY- |
| timeout-testing | TMO- | circuit-breaker-testing | CBR- |
| dependency-failure-testing | DPF- | disaster-recovery-testing | DRT- |
| authentication-testing | AUT- | authorization-testing | AZT- |
| session-security-testing | SST- | api-security-testing | AST- |
| security-requirement-review | SRR- | threat-modeling | THM- |
| secrets-exposure-review | SER- | quality-gate-design | QGD- |
| quality-metrics-design | QMD- | quality-dashboard-design | QDD- |
| quality-debt-analysis | QDA- | quality-maturity-assessment | QMA- |
| test-effectiveness-analysis | TEA- | automation-roi-analysis | ARO- |
| testing-bottleneck-analysis | TBA- | regression-optimization | RGO- |
| ci-test-optimization | CTO- | test-runtime-optimization | TRO- |
| test-maintenance-cost-analysis | TMC- | quality-productivity-metrics | QPM- |
| prompt-regression-testing | PRT- | rag-quality-testing | RAGQ- |
| rag-retrieval-testing | RAGT- | agent-loop-testing | ALT- |
| agent-memory-testing | AMT- | agent-permission-testing | AGP- |
| agent-failure-recovery-testing | AFR- | agent-long-running-testing | ALR- |
| multi-agent-testing | MAT- | llm-hallucination-testing | LHT- |
| llm-consistency-testing | LCT- | ai-safety-testing | AIS- |

## Card State and Batch Flow

Card state is execution evidence, not runtime quality, business approval, risk acceptance, or Release evidence. Each batch follows this flow:

1. Write the batch contract tests first and confirm RED because target directories/contracts are missing before creating packages.
2. Move only the exact batch item IDs from Todo to In Progress, using live Project field and option IDs rather than guesses or fuzzy title matching.
3. Complete the Match ledger, Skill packages/enhancements, Evals, governance synchronization, and target quality gates.
4. Read Project #4 again and confirm that only the batch changed. Move only evidence-complete cards to Done; preserve actual states and reasons for the rest.
5. gh project item-list proves current status only, not that a card historically passed through In Progress -> Done. If event history is unavailable, record that historical evidence as UNASSESSED.

## Documentation and Governance Synchronization

After each batch, update according to the actual Match results:

- docs/governance/skill-governance-registry.yaml
- Generated docs/SKILL_MATRIX.md, docs/SKILL_MATRIX_EN.md, and docs/generated/
- docs/SKILL_MATCHING_REGISTER.md and docs/SKILL_MATCHING_REGISTER_EN.md
- docs/catalog/skills-index* and docs/catalog/skills-graph*
- README.md, README_EN.md, and the corresponding language Skill READMEs
- Necessary Workflow routing and lifecycle-stage documentation

Do not add cross-Skill internal Markdown links. Recommendations remain names and navigation text so a copied Skill directory stays independently installable. Governance quality_score remains NOT_SCORED and eval_execution remains NOT_RUN unless independent evidence outside this implementation exists.

## Acceptance and Non-Goals

### Acceptance Conditions

- All 17 Batch 1 cards and 25 Batch 2 cards have a Match conclusion, delivery path, current Project status, and acceptance evidence.
- Every NEW package passes bilingual structure, metadata, Eval, trigger, independence, and integrity checks; every ENHANCE/MERGE target passes the corresponding relevant checks.
- Bilingual Matrix, Register, Inventory, Catalog, Graph, and README files are reproducible from current repository content without generated-file drift.
- Batch contract tests, target Eval configuration checks, full repository unit tests, bash scripts/check_skills_quality.sh, and git diff --check pass.
- Reporting separates static structure evidence, Prompt-text evidence, current card state, and unrun model/external/business validation.

### Non-Goals

- Do not create repository Issues, change Project cards outside these batches, push, or create a Release.
- Do not execute real APIs, browsers, databases, CI, Chaos, disaster recovery, retrievers, LLMs, Agents, or production systems.
- Do not infer semantic effectiveness, coverage, absence of vulnerabilities, quality scores, Go/No-Go, or release completion from static files, Skill names, trigger dry-runs, or quality gates.
- Do not mix v4.1 Existing Enhance Review, v4.0 Workflow, v3.4 Performance Review, or Release DoD cards into these two v3-v4 P2 Skill batches.

## Pre-Plan Decision

The confirmed order is: write the specification and implementation plan; after Batch 1 RED, move its 17 cards; complete Batch 1 acceptance; then write the Batch 2 RED contract and move its 25 cards. If Capability Match finds duplication, evidence controls the result—enhance, merge, or record an existing capability—rather than card count defining completion.
