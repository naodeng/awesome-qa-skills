<div align="right"><a href="./2026-08-29-four-stage-qa-skills-evolution-design.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Awesome QA Skills Four-Stage Evolution Design

## Decision Summary

The repository evolves through:

```text
Core QA Skills → Engineering QA Skills → Production Quality Skills → AI Native QA Skills
```

Physical directories and Skill names remain unchanged. Capability stages are logical navigation, so existing install commands and external paths remain valid. The completed target is 78 Skills per language: 10 workflows, 65 testing types, and 3 Skill Engineering packages, for 156 bilingual directories.

## Goals and Non-goals

Goals:

- Let users select Skills by quality maturity and lifecycle outcome.
- Preserve workflow, testing-type, tool-specific, and governance structures.
- Fill Engineering QA, Production Quality, and AI Native QA gaps through six verifiable iterations.
- Use one capability map across bilingual README files, indexes, and `discover-testing`.

Non-goals:

- Do not move, rename, or remove Skill directories.
- Do not split overlapping topics into duplicate Skills.
- Do not present `ai-assisted-testing` as AI product testing; it remains AI for QA.

## Capability Architecture

| Stage | Primary question | Coverage |
| --- | --- | --- |
| Core QA Skills | How do we understand, design, execute, and report foundational testing? | Requirements, strategy, cases, functional/API/manual/security/accessibility testing, defects, reporting |
| Engineering QA Skills | How do we shift quality left and improve change, execution, diagnosis, and performance decisions? | Shift Left, change intelligence, contracts, regression, execution intelligence, performance engineering |
| Production Quality Skills | How do we decide from release and production evidence? | Production verification, incidents, traces, metric anomalies |
| AI Native QA Skills | How do we test AI features, LLMs, prompts, agents, tools, and safety? | Testing for AI, evaluation, agent/tool behavior, prompt security |

`skill-engineering` is a cross-cutting governance layer, not a fifth user capability stage.

## Routing and Documentation

`discover-testing` routes by capability stage and lifecycle outcome, recommends one primary Skill and at most one complement, then applies workflow, tool-specific, or Plus variants. It distinguishes AI for QA from Testing for AI.

Documentation retains two views: capability navigation for selection and physical paths for installation.

## Prompt Baseline Boundary

`awesome-qa-prompt` is a reference, not a runtime dependency. Adapt its input audit, non-invention, incomplete-information fallback, Human Task boundaries, structured output, and anti-hardcoded-KPI principles. Do not copy framework-variant directories or cross-repository links.

## Six Iterations

| Iteration | Capability | Added Skills |
| --- | --- | --- |
| 1 | Engineering QA / Shift Left | `acceptance-criteria-review`, `requirement-gap-analysis`, `quality-risk-analysis`, `testability-analysis` |
| 2 | Engineering QA / Change Intelligence | `change-impact-analysis`, `pr-test-impact-analysis`, `regression-scope-analysis`, `regression-test-selection` |
| 3 | Engineering QA / Execution Intelligence | `test-data-generation`, `api-contract-testing`, `flaky-test-analysis`, `root-cause-analysis`, `log-analysis` |
| 4 | Engineering QA / Performance | `performance-workload-modeling`, `performance-result-analysis`, `performance-bottleneck-analysis`, `performance-regression-analysis`, `capacity-planning-analysis` |
| 5 | Production Quality | `production-verification`, `production-incident-analysis`, `distributed-trace-analysis`, `metrics-anomaly-analysis` |
| 6 | AI Native QA | `ai-feature-testing`, `llm-testing`, `llm-evaluation-design`, `prompt-testing`, `ai-agent-testing`, `agent-tool-testing`, `prompt-injection-testing` |

The implementation adds 29 logical Skills and 58 bilingual directories. Exploratory testing, release-readiness assessment, and prompt regression remain explicit modes rather than duplicate packages.

## Definition of Done

Every added or modified Skill requires:

1. Equivalent Chinese and English boundaries.
2. `SKILL.md`, a primary prompt, OpenAI metadata, and three eval categories.
3. Independent installation without cross-Skill internal links.
4. Synchronized capability maps, indexes, routing, and install guidance.
5. A passing `bash scripts/check_skills_quality.sh` run.

## Acceptance Criteria

- Public counts report 78 Skills per language and 156 bilingual directories.
- Users can identify a capability stage and unique primary Skill from every navigation entry.
- Existing directories, commands, and Skill names remain compatible.
- All 29 additions have explicit boundaries, iteration ownership, and relationships to existing assets.
