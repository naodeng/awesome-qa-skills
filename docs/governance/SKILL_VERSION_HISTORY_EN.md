<div align="right"><a href="./SKILL_VERSION_HISTORY.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# Skill Version and Update History

This history tracks each Skill package's independent `metadata.version`; it is not the repository-wide release version. New Skills record their initial version; modified Skills record the previous/current version and a concise update note.

## 2026-11-23

### New Skills / Workflow

| Skill | Initial version (zh/en) | Update note |
| --- | --- | --- |
| `mcp-server-testing` | `1.0.0` / `1.0.0` | Adds MCP protocol, transport, authorization, resource-poisoning, and generation-compatibility testing. |
| `ai-generated-code-review` | `1.0.0` / `1.0.0` | Adds AI/Agent code review for dependency authenticity, CI integrity, test effectiveness, and provenance evidence. |
| `structured-output-testing` | `1.0.0` / `1.0.0` | Adds JSON/schema evolution, streaming, and structured-result failure testing. |
| `skill-security-review` | `1.0.0` / `1.0.0` | Adds supply-chain security review for Skills, plugins, and MCP. |
| `ai-feature-release-workflow` | `1.0.0` / `1.0.0` | Adds staged handoffs from evaluation design through release gates, canary monitoring, and rollback. |

### Updated existing Skills

| Skill | Version (zh/en) | Update note |
| --- | --- | --- |
| `agent-failure-recovery-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds failure trajectories and missing-execution-evidence evaluation. |
| `agent-long-running-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds long-running traces, checkpoints, and missing-evidence checks. |
| `agent-loop-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds loop traces, stop conditions, and budget-evidence evaluation. |
| `agent-memory-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds memory traces and missing-execution-evidence checks. |
| `agent-permission-testing` | `1.0.0` → `1.0.1` / `1.0.0` → `1.0.1` | Adds a permission-trace fixture and missing-evidence evaluation. |
| `agent-tool-testing` | `1.0.0` → `1.0.1` / `1.0.0` → `1.0.1` | Adds MCP/schema handoff and missing-tool-evidence evaluation. |
| `ai-agent-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds Agent trajectory evaluation and missing-run-evidence checks. |
| `ai-assisted-testing` | `1.0.0` → `2.0.0` / `1.0.0` → `2.0.0` | Reworks the AI-assisted QA protocol with delegation, provenance, human gates, false-green, and cost evaluations. |
| `ai-feature-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds AI-feature trajectory fixtures and missing-run-evidence evaluation. |
| `ai-generated-test-review` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Strengthens provenance, assertion effectiveness, and trajectory-evidence review for generated tests. |
| `ai-safety-testing` | `1.0.0` → `1.0.1` / `1.0.0` → `1.0.1` | Adds a safety-trace validation fixture and missing-evidence cases. |
| `automation-roi-analysis` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds cost accounting for AI tokens, review, rework, and quality. |
| `ci-test-optimization` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds model/dataset identity, shard, cache, retry, and cumulative-cost constraints. |
| `code-review` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds review of AI-generated implementation test impact, CI integrity, and provenance evidence. |
| `discover-testing` | `1.3.0` → `1.4.0` / `1.3.0` → `1.4.0` | Adds AI-code, AI-release, and MCP routes plus the 176-entry capability snapshot. |
| `llm-consistency-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds model-migration trajectories and missing-evaluation-evidence checks. |
| `llm-evaluation-design` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds dataset hygiene, statistics, judge calibration, CI gates, and missing-evidence evaluation. |
| `llm-hallucination-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds trajectory and missing-evaluation-evidence boundary cases. |
| `llm-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds sampling, cost, domain boundaries, and missing-execution-evidence evaluation. |
| `multi-agent-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds collaboration traces, attribution evidence, and missing-evaluation-evidence checks. |
| `production-verification` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds model-version, drift, refusal, feedback, cost, and rollback evidence. |
| `prompt-injection-testing` | `1.0.0` → `1.0.1` / `1.0.0` → `1.0.1` | Adds missing-evidence and MCP/resource-poisoning security evaluation. |
| `prompt-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds Prompt-version regression and missing-evaluation-evidence constraints. |
| `quality-gate-design` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds structured traces and `NOT_RUN`/`UNKNOWN` evaluation gates. |
| `quality-productivity-metrics` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds denominator rules for AI calls, tokens, review, rework, and quality metrics. |
| `rag-quality-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds grounding, citation, and retrieval-trajectory evidence evaluation. |
| `rag-retrieval-testing` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds index migration, hybrid retrieval, reranking, freshness, and rebuild evaluation. |
| `requirement-quality-review` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds evidence boundaries and review cases for AI-generated specifications. |
| `test-data-generation` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds AI evaluation dataset provenance, license, leakage, and contamination checks. |
| `test-report-review` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds consistency checks across AI model, Prompt, dataset, judge versions, and run ID. |
| `test-reporting` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Adds AI evaluation version, run, sampling, cost, and execution-state fields. |
| `pr-quality-review` | `1.0.0` → `1.1.0` / `1.0.0` → `1.1.0` | Strengthens test-impact, effectiveness, and evidence-boundary review for Agent PRs. |
| `release-testing-workflow` | `1.1.0` → `1.2.0` / `1.1.0` → `1.2.0` | Adds the handoff contract from AI evaluation gates into release stages. |

### Iteration B/C Gap Closure

| Skill | Version (zh/en) | Update note |
| --- | --- | --- |
| `agent-tool-testing` | `1.0.1` → `1.0.2` / `1.0.1` → `1.0.2` | Adds `ATT-##`, MCP responsibility handoff, tool-description poisoning, and schema-evolution cases. |
| `ai-agent-testing` | `1.1.0` → `1.1.1` / `1.1.0` → `1.1.1` | Adds a no-skill baseline, bilingual paired-comparison protocol, and missing-evidence case. |
| `ai-safety-testing` | `1.0.1` → `1.0.2` / `1.0.1` → `1.0.2` | Adds an authorized red-team program, benign controls, over-refusal, and retest case. |
| `discover-testing` | `1.4.0` → `1.4.1` / `1.4.0` → `1.4.1` | Adds structured-output and supply-chain routes, updates the AI-domain count, and tests the multimodal capability gap. |
| `llm-consistency-testing` | `1.1.0` → `1.1.1` / `1.1.0` → `1.1.1` | Adds two-version/dual-run migration, re-baselining, deprecation, and rollback gates. |
| `llm-evaluation-design` | `1.1.0` → `1.1.1` / `1.1.0` → `1.1.1` | Clarifies dataset hygiene, stratified samples, confidence requirements, judge calibration, and CI blocking. |
| `llm-testing` | `1.1.0` → `1.1.1` / `1.1.0` → `1.1.1` | Adds domain-oracle boundaries, stratified sampling, cost budgets, and latency-evidence cases. |
| `prompt-injection-testing` | `1.0.1` → `1.0.2` / `1.0.1` → `1.0.2` | Extends RAG/MCP/UI injection surfaces, exfiltration channels, and post-refusal side-effect assertions. |
| `quality-gate-design` | `1.1.0` → `1.1.1` / `1.1.0` → `1.1.1` | Adds AI-evaluation sample, judge, flake, and cost gates plus a missing-evidence blocking case. |
