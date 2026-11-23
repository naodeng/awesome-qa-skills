# RAG Retrieval Testing Prompt

Build an executable, reviewable, and traceable evidence boundary for query variants, chunking, filters, recall/precision proxies, ranking, freshness, and retrieval evidence.

## Input

Start with an input audit and record known, missing, conflicting, stale, out_of_scope, and assumptions:

- known: scope, retrieval result material, constraints, or results directly supported by a source.
- missing: material needed to assess query variants, chunking, filters, recall/precision proxies, ranking, freshness, and retrieval evidence that has not been supplied.
- conflicting: inconsistent goals, definitions, conditions, or behaviors across sources.
- stale: architecture, version, model, dataset, or record that may be out of date.
- out_of_scope: actions outside this Skill, unauthorized actions, or actions requiring a real environment.
- assumptions: temporary assumptions for a bounded first pass, each with a validation method.

## What to do

1. Restate the objective, subject, scope, and success criteria in one sentence.
2. Audit completeness, credibility, recency, and comparability, focusing on query variants, chunking, filters, recall proxy, ranking and freshness.
3. Build a risk or failure model for retrieval result, including triggers, expected concerns, impact, and evidence needs.
4. Convert the analysis into concrete scenarios, assertions, validation steps, decision gates, or improvement experiments.
5. Report residual risk, evidence gaps, and next actions without presenting assumptions as facts.

## Execution Rules
- Plans, static analysis, and Eval fixtures are not run evidence. When asked to assess real evaluation/execution and the trace lacks a valid run ID and raw result, output `evaluation_status: NOT_RUN`, `run_evidence: []`, and `domain_conclusion: UNASSESSED`; never claim PASS.


- Give a source, evidence state, and validation method for every important conclusion.
- Each scenario must include preconditions, action or stimulus, expected behavior or decision criterion, required evidence, and a stop condition.
- Use P0/P1/P2/P3 or an equivalent scale and explain business impact, likelihood, detectability, or decision cost.
- Make query variants, chunking, filters, recall/precision proxies, ranking, freshness, and retrieval evidence concrete; do not substitute adjacent test types, tool names, or one example for domain reasoning.
- Never invent numbers, thresholds, model behavior, root causes, system behavior, execution records, all-passed claims, or safety approval.
- For user data, production, or safety work, default to least privilege, masked data, mocks, dry runs, or isolation.
- Separate facts, inferences, candidate recommendations, and Human decisions; only Human can confirm risk acceptance, exceptions, and safety judgments.

## Domain Procedure and Oracle

Apply these steps as design or static comparison of supplied material. Keep fixture decisions, proposed plans, and real execution evidence separate; missing project rules, gates, and authority remain open.

1. Version queries, relevance annotations, document/chunk units, labelers and corpus. Recall@k uses the known relevant set; Precision@k uses actual returns with the supplied duplicate policy.
2. Check rank, relevance, permission/tenant filters, freshness and version for each hit. Relevant but unauthorized hits are failures; high scores cannot cure stale content.
3. Compare configurations under matched queries, index, filters and resources. Incomplete relevant sets allow proxy measurements, not claims of complete recall.
4. Distinguish missing retrieval from correct retrieval followed by wrong generation. Missing generation output cannot locate its failure; absent labels leave UNKNOWN.
5. Pin embedding model/dimensions/normalization, chunking, and index-build identity for migration. Compare old and new indexes on the same queries, relevance labels, permission filters, and top-k; do not attribute changes to one factor when models, chunking, and ranking all changed together.
6. For hybrid retrieval, record each retriever's contribution and the fusion rule. For reranking, pin the candidate set, input truncation, rank output, and model version; verify reranking never bypasses tenant or permission filters.
7. For rebuild/refresh, verify propagation of document additions, updates, and deletions plus index identity. Check tombstones, duplicate writes, partial failure, and rollback to old/new indexes. If the project supplies no freshness threshold, leave it open rather than inventing one.

## Minimum Coverage Checklist

- query variants, chunking, filters, recall proxy, ranking and freshness
- embedding/index migration, hybrid fusion, reranking, rebuilds, and freshness propagation
- confirmed facts, working assumptions, open questions, evidence quality, and recency
- high-risk paths, blockers, stop/escalation/rollback or human-handoff conditions
- smallest validation action, owner role, close condition, residual risk, and Human decision
- facts, evidence-backed inferences, candidate recommendations, Human decisions

## Output

### 1. Task Understanding and Scope

State the objective, subject, inclusions, exclusions, success criteria, and unauthorized actions.

### 2. Input Audit

List known, missing, conflicting, stale, out_of_scope, and assumptions with source, recency, and evidence quality.

### 3. retrieval result Analysis and Priorities

Describe scenarios, triggers, expected behavior, impact, priority, and evidence gaps for query variants, chunking, filters, recall/precision proxies, ranking, freshness, and retrieval evidence.

### RAGT-## Finding Contract

Each finding must include:

- object/rule
- source
- trigger or applicability
- expected concern/rationale
- evidence state
- impact/priority
- owner role
- close condition
- validation method

### 4. Candidate Validation and Residual Risk

Separate candidate recommendations from actual execution and state the smallest validation action, stop/escalation conditions, residual risk, and open questions.

### 5. Human Decisions

List only items requiring Human confirmation, risk acceptance, exception authorization, rollback, or safety judgment.

The output must keep these sections separate: facts, evidence-backed inferences, candidate recommendations, Human decisions.

## Quality Bar

- Tailor the content to retrieval result; do not merely rename a generic template.
- Make high-risk paths concrete with failure modes, expected behavior, and evidence.
- Never infer numbers, root causes, or system behavior without support.
- Static analysis, plans, or dry runs are not proof of real execution, all tests passing, or safety approval.
- Let an executor act without guessing and a reviewer trace the boundary between facts, inferences, recommendations, and Human decisions.
