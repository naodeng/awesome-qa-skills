# Awesome QA Skills Evolution Roadmap

> Status: completed. This document preserves delivery order and boundaries; all 29 listed Skills are now installable.

## Direction

```text
Core QA Skills → Engineering QA Skills → Production Quality Skills → AI Native QA Skills
```

This is a logical navigation model, not a directory migration. Existing and future Skills keep the stable package layout:

```text
skills/{zh|en}/{testing-types|testing-workflows|skill-engineering}/<skill-name>/
```

The repository currently has 78 Skills per language (10 workflows, 65 testing types, and 3 Skill Engineering packages), or 156 bilingual directories.

## Capability map

| Stage | Question answered | Current anchors | Next focus |
| --- | --- | --- | --- |
| Core QA Skills | How do we understand, design, execute, and report foundational testing? | requirements, strategy, cases, functional, API, security, reporting | Preserve a complete foundation without duplicate packages |
| Engineering QA Skills | How do we shift quality left, assess changes, and improve diagnostic and performance decisions? | requirements-analysis, code-review, automation-testing, performance-testing | Shift Left, change intelligence, execution intelligence, performance engineering |
| Production Quality Skills | How do we make and close quality decisions from release and production evidence? | release-testing-workflow, test-reporting | Production verification, incidents, and observability |
| AI Native QA Skills | How do we test AI features, LLMs, prompts, agents, and safety boundaries? | No Testing-for-AI package yet | Eval, prompts, agents/tools, and security |

`ai-assisted-testing` remains cross-cutting **AI for QA**. It is not a substitute for AI Native QA, which is Testing for AI. `skill-engineering` is a horizontal governance layer, not a fifth capability stage.

## Iteration roadmap and Prompt Baseline references

Every candidate first references the closest Prompt Baseline in `awesome-qa-prompt`, then adapts it into an independently installable Skill. The reference is not a runtime dependency: do not copy `Standard-version/`, framework-variant directories, or cross-repository relative links.

| Iteration | Stage | New Skill | Priority | Prompt Baseline reference | Boundary with current Skills |
| --- | --- | --- | --- | --- | --- |
| 1 | Engineering QA / Shift Left | `acceptance-criteria-review` | P0 | `acceptance-criteria-reviewer` | Reviews AC testability, not full requirements analysis |
| 1 | Engineering QA / Shift Left | `requirement-gap-analysis` | P0 | `requirement-gap-analyzer` | Produces gaps and questions, not a test strategy |
| 1 | Engineering QA / Shift Left | `quality-risk-analysis` | P0 | `quality-risk-analysis` | Ranks quality risks and evidence gaps |
| 1 | Engineering QA / Shift Left | `testability-analysis` | P0 | `testability-analysis` | Produces testability conclusions and improvements |
| 2 | Engineering QA / Change Intelligence | `change-impact-analysis` | P0 | `change-impact-analysis` | Maps change to impacted areas |
| 2 | Engineering QA / Change Intelligence | `pr-test-impact-analysis` | P0 | `pr-risk-analysis` | Uses PR/diff input to identify test impact |
| 2 | Engineering QA / Change Intelligence | `regression-scope-analysis` | P0 | `regression-scope-analysis` | Defines regression scope, not execution selection |
| 2 | Engineering QA / Change Intelligence | `regression-test-selection` | P0 | `regression-test-selection` | Selects a regression set from known test assets |
| 3 | Engineering QA / Execution Intelligence | `test-data-generation` | P0 | `test-data-generation` | Produces reviewable data plans with privacy constraints |
| 3 | Engineering QA / Execution Intelligence | `api-contract-testing` | P0 | `api-contract-analysis` | Tests contract and compatibility, not generic API testing |
| 3 | Engineering QA / Execution Intelligence | `flaky-test-analysis` | P0 | `flaky-test-analysis` | Finds unstable-test patterns and evidence |
| 3 | Engineering QA / Execution Intelligence | `root-cause-analysis` | P0 | `root-cause-analysis` | Forms evidence-based hypotheses; never claims unproven causes |
| 3 | Engineering QA / Execution Intelligence | `log-analysis` | P0 | `log-analysis` | Extracts timelines, symptoms, and evidence gaps |
| 4 | Engineering QA / Performance | `performance-workload-modeling` | P0 | `workload-model-design` | Builds workload models and labels missing assumptions |
| 4 | Engineering QA / Performance | `performance-result-analysis` | P0 | `performance-result-analysis` | Explains results without inventing thresholds |
| 4 | Engineering QA / Performance | `performance-bottleneck-analysis` | P1 | `performance-bottleneck-analysis` | Produces testable bottleneck hypotheses |
| 4 | Engineering QA / Performance | `performance-regression-analysis` | P1 | `performance-regression-analysis` | Compares version evidence and regression risk |
| 4 | Engineering QA / Performance | `capacity-planning-analysis` | P1 | `capacity-planning-analysis` | Produces capacity assumptions, gaps, and open metrics |
| 5 | Production Quality | `production-verification` | P0 | `production-verification-generation` / `production-verification-review` | Verifies production evidence; never replaces human release approval |
| 5 | Production Quality | `production-incident-analysis` | P1 | `production-incident-analysis` | Organizes incident evidence and follow-up analysis |
| 5 | Production Quality | `distributed-trace-analysis` | P1 | `distributed-trace-analysis` | Correlates call chains and evidence |
| 5 | Production Quality | `metrics-anomaly-analysis` | P1 | `metrics-anomaly-analysis` | Identifies anomaly signals without inventing telemetry |
| 6 | AI Native QA | `ai-feature-testing` | P0 | `ai-feature-test-design` | Tests AI-feature behavior and risks, not AI-assisted QA |
| 6 | AI Native QA | `llm-testing` | P0 | `llm-test-case-generation` | Tests model behavior, boundaries, and failure modes |
| 6 | AI Native QA | `llm-evaluation-design` | P0 | `ai-evaluation-design` / `llm-output-quality-evaluation` | Designs datasets, metrics, and human review |
| 6 | AI Native QA | `prompt-testing` | P0 | `prompt-test-analysis` | Tests prompt behavior; includes a regression mode |
| 6 | AI Native QA | `ai-agent-testing` | P0 | `ai-agent-test-design` | Tests goals, state, tools, and recovery |
| 6 | AI Native QA | `agent-tool-testing` | P0 | `agent-tool-call-test-design` | Tests tool-call contracts and side effects |
| 6 | AI Native QA | `prompt-injection-testing` | P1 | `prompt-injection-test-design` | Tests injection attacks and protective boundaries |

This is 29 logical Skills, implemented once per language: 58 new directories.

## Deliberate non-additions

| Requested name | Owned by | Reason |
| --- | --- | --- |
| `exploratory-testing` | `manual-testing` exploration mode | Existing manual testing already owns session-based exploration |
| `release-readiness-assessment` | `release-testing-workflow` readiness mode | Do not split workflow gates into duplicate packages |
| `prompt-regression-testing` | `prompt-testing` regression mode | Shares the same behavioral assertions and evidence model |

## Definition of done per iteration

Each new or extended Skill must:

1. Use paired Chinese/English directories with equivalent scope and standalone installation.
2. Include `SKILL.md`, a primary `prompts/` file, `agents/openai.yaml`, `evals/eval.yaml`, and success / insufficient-information / risk-boundary cases.
3. Audit known inputs, missing inputs, assumptions, and risks; never fabricate requirements, metrics, environments, execution facts, or root causes.
4. Produce a minimum executable draft or a clear blocked/TBD state when material inputs are missing.
5. Organize evidence and recommendations but never replace Human Tasks such as approval, release, waiver, or risk acceptance.
6. Update capability maps, bilingual indexes, routing, and installation guidance; pass `bash scripts/check_skills_quality.sh`.

## Delivery order

First deliver this repository's capability map, routing, indexes, and contributor rules. Then create Skills in iterations 1 through 6. Before each creation, recheck the mapped Prompt Baseline and adapt its quality constraints rather than its directory structure.
