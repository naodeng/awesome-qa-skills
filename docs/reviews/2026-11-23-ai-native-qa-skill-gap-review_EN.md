<div align="right"><a href="./2026-11-23-ai-native-qa-skill-gap-review.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Repository-wide Skill Gap Review for AI-Native QA

**Review date: 2026-11-23**
**Review-time baseline:** 171 logical Skills in `skills/zh` and `skills/en` (342 directories), focused on AI-native QA, AI for QA, and AI-native engineering quality.
**Recommendations in this report:** 4 new Skills, 1 conditional Workflow, 15 existing Skills to enhance, and 3 P0 blockers to fix. This is the gap review's direct recommendation count; the combined A–D implementation scope is reconciled at the end.
**Evidence boundary:** static file inspection, `grep` counts, the repository quality gate and unit tests, plus dated external public snapshots. No AI-related Skill was run, no model was called, and this is not a behavioral evaluation, business acceptance, or release approval.

## Summary

1. **The repository does not lack volume; it lacks three kinds of depth.** Testing for AI already has 18 specialists, but AI for QA has only 2 entries; AI-native engineering quality (AI-generated code, agent PRs, Skill/plugin supply chains) is essentially absent; protocol, cost, and trace evidence have no owner.
2. **AI for QA is structurally thin.** `ai-assisted-testing` has a 64-line Prompt with only four generic domain steps, while `prompt-testing` has 116 lines and 8 eval cases. Yet `ai-assisted-testing` is the router's default exit for AI-assisted tasks.
3. **Testing for AI is broad in scenarios but shallow in evidence.** Of the 20 AI-related Prompts, 5 have no domain-operation section and 8 have no stable `XX-##` finding contract. Most eval cases check headings or status codes, not trajectories or behavior.
4. **The workflow layer has no AI loop.** The only AI composition route, `ai-feature-validation`, stops at evaluation planning; there is no eval gate, canary, production monitoring, or rollback. The Bugfix-verification and AI-code-verification routes proposed in the 2026-10-16 review are still missing.
5. **The review-time baseline worktree was red.** `bash scripts/check_skills_quality.sh` failed at `[3/11]` with `stale_governance_inventory=zh,en`; the `discover-testing` capability inventory listed 169 IDs, and its unit test failed because `test-case-importer` and `test-case-retrieval` were missing. Implementation status is recorded at the end of this document.

## Method and evidence boundary

- Read every Skill's frontmatter, main Prompt, `evals/`, and optional `references/`; counted Prompt lines, domain-operation sections, finding contracts, and cases.
- Used `grep` to check coverage of MCP, structured output, token cost, TTFT, context compaction, model migration, multimodal, and online evaluation in both language trees.
- Ran `bash scripts/check_skills_quality.sh` and `python3 -m unittest scripts.tests.test_review_standalone_helpers.StandaloneHelperTests.test_router_snapshot_is_complete_and_availability_is_unknown`; recorded results without fixing them.
- Cross-checked `docs/catalog/`, `docs/governance/`, `docs/SKILL_MATCHING_REGISTER.md`, and earlier reviews so that completed or `MERGE`-decided capabilities are not re-proposed.
- External sources only explain "why now"; they are not evidence of this repository's behavior, effectiveness, or market size. Links and snapshot dates are at the end.

## Current state: 20 AI-related Skills

The two capability domains are D15 (AI for QA) and D16 (AI / LLM / Agent quality). the governance registry currently has only 2 Skills under D15 and 18 under D16. That ratio shows the investment went into "testing AI", not into "using AI for QA" and "quality control when AI participates in engineering".

| Skill | Domain | Existing evidence | Main gap |
| --- | --- | --- | --- |
| `ai-assisted-testing` | D15 | 64-line Prompt, 4 generic domain steps, 1 provenance line, 1 ROI line | No delegation matrix, AI-draft acceptance protocol, false-confidence list, or cost accounting |
| `ai-generated-test-review` | D15 | Layered references, 7 cases, domain execution points | Covers test code only, not AI-generated requirements/plans/reports |
| `ai-feature-testing` | D16 | 4 domain steps, slicing and rubric | No streaming, multimodal, cost, or production loop |
| `llm-testing` | D16 | Generic skeleton and coverage list | No domain steps, no `XX-##`, blurred boundary with feature/prompt/eval |
| `prompt-testing` | D16 | `PRT-##`, 8 cases, regression mode | No domain steps; no model/provider migration semantics |
| `llm-evaluation-design` | D16 | Metrics/data/scoring checklist | No dataset hygiene, statistics, or judge-calibration detail |
| `llm-hallucination-testing` | D16 | Domain steps and `LHT-##` | Handoff to RAG grounding could be sharper |
| `llm-consistency-testing` | D16 | Domain steps and `LCT-##` | No migration, deprecation deadline, shadow/canary |
| `rag-quality-testing` | D16 | Domain steps and `RAGQ-##` | No attribution of answer changes to retrieval changes |
| `rag-retrieval-testing` | D16 | Domain steps and `RAGT-##` | No embedding/index migration, hybrid search, reranker |
| `ai-agent-testing` | D16 | Generic skeleton and coverage list | No `XX-##`; no trace-evidence mode |
| `agent-tool-testing` | D16 | Generic skeleton and 10 coverage items | No domain steps, no MCP, no schema evolution |
| `agent-loop-testing` | D16 | Domain steps and `ALT-##` | Weak linkage to timeout/budget/cancellation |
| `agent-memory-testing` | D16 | Domain steps and `AMT-##` | No context assembly or compaction fidelity |
| `agent-permission-testing` | D16 | Domain steps and `AGP-##` | No MCP token passthrough or confused deputy |
| `agent-failure-recovery-testing` | D16 | Domain steps and `AFR-##` | Handoff between recovery evidence and incident triage needs work |
| `agent-long-running-testing` | D16 | Domain steps and `ALR-##` | No long-task cost or token budget |
| `multi-agent-testing` | D16 | Domain steps and `MAT-##` | No cross-agent trace merge and attribution |
| `ai-safety-testing` | D16 | Domain steps, `AIS-##`, policy matrix | No red-team program, over-refusal calibration, disclosure |
| `prompt-injection-testing` | D16 | Complete coverage list | No domain steps; no MCP/resource/tool-description poisoning or exfiltration channels |

**Confirmed strengths:** the 11 AI packages added in the 2026 v3-v4 batch already have domain-operation sections plus `XX-##` contracts, including the agent family, both RAG packages, hallucination, and consistency. The repository has proven it can go deep in a domain; the gap is back-filling the same standard into the 9 existing AI packages and the new capability areas.

## Four gap areas

### A. AI for QA: one thin entry

Today D15 has only `ai-assisted-testing` and `ai-generated-test-review`. The first gives generic advice on using AI; the second reviews AI-generated test code only. Missing is an operating protocol for AI as a QA collaborator.

- **No delegation matrix.** Nothing says which of requirements analysis, case generation, data preparation, failure triage, and reporting AI may draft, and what humans must decide.
- **No AI-draft acceptance.** There is no executable field chain of input snapshot → model/Prompt version → draft → human review → adopted version → evidence; one provenance sentence is not auditable.
- **No false-confidence catalog.** No list of "all-green but weak assertions", "AI rewrote the test to remove the failure", or "cited an API/field that does not exist".
- **No cost/benefit accounting.** One line says to measure human baseline hours; there is no token cost, review effort, or rework rate.
- **No acceptance for AI-generated non-test artifacts.** Requirements, test plans, bug reports, and release notes drafted by AI have no review rules.

Decision: do not add a generic "AI QA" Skill. Rewrite `ai-assisted-testing` as v2. Register "non-test artifact review" as an optional mode of `ai-generated-test-review` first, and only split later if artifacts and evidence diverge.

### B. Testing for AI: many scenarios, few hard edges

Covered: AI features, LLM behavior, prompts, evaluation design, hallucination, consistency, RAG answer and retrieval quality, 8 agent specialists, safety, and injection. The real blanks are:

| Gap | Current evidence | Why it matters now |
| --- | --- | --- |
| **MCP protocol and security** | `MCP` / `Model Context Protocol` has **0 hits** in Skills across both language trees | MCP 2026-07-28 removed protocol-level sessions and the `initialize` handshake, added `server/discover`, MRTR, `subscriptions/listen`, and OAuth 2.1 with `iss` validation; tool-description/resource poisoning, token passthrough, and confused deputy become their own test surface. `agent-tool-testing` covers only agent-side tool selection and side effects. |
| **Structured output** | `structured output` has **0 hits** in Skill Markdown; `prompt-testing` has only a "format" item | JSON mode, schema validation, invalid-JSON recovery, partial streaming output, and schema evolution are high-frequency product failures; `api-schema-validation` covers HTTP contracts only. |
| **Cost and latency** | `TTFT`, `token cost`, `cache hit` have **0 hits**; `llm-testing` has one "cost/latency" line | Context growth, retry amplification, cached-input pricing, and time to first token decide whether an AI feature can ship; generic performance Skills address infrastructure load. |
| **Trace evidence** | `OTel`/`GenAI` semantic conventions have **0 hits**; `ai-agent-testing` checks run/step ID order but does not parse traces | Final-answer-only evaluation misses wrong tool choice, wrong order, and useless retries; the trajectory is the primary Agent evidence. |
| **Judge calibration** | `LLM-as-judge` appears in one rule line of `llm-evaluation-design` | Position/verbosity/self-preference bias, inter-rater agreement, and judge versioning determine whether eval conclusions are credible. |
| **Model migration** | `deprecation`/`deprecat` has **0 hits** in AI Skills | Retirement windows range from weeks to months, and unpinned aliases drift silently; migration needs re-baselining, dual-run, and capability plus cost regression. |
| **Context assembly** | `context compaction`/`lost in the middle` has **0 hits** | Truncation, compaction, ordering, and cache misses often look like "model capability problems". |
| **Production AI quality** | Generic `production-verification` has no drift/online eval/guardrail rate | Post-release judgment still needs drift, refusal rates, feedback signals, and cost anomalies. |
| **Red team** | `red team` has **0 hits** in AI safety Skills | Security testing is planned coverage, but there is no attack-surface organization, attack library, disclosure flow, or over-refusal calibration. |
| **Multimodal/voice** | `multimodal`/`voice`/`OCR`/`vision` have **0 hits** | Vision and speech inputs are shipping, but cross-modal consistency and speech quality acceptance are absent. |

Decision: do not add an "all-purpose LLM testing" package. Cover the five directions — protocol, evidence, cost, migration, production — with only MCP and structured output as standalone packages; everything else should be a mode of an existing Skill.

### C. AI-native engineering quality: tests are covered, code and assets are not

- `ai-generated-test-review` already asks whether tests still pass after the implementation is broken. No Skill asks whether Agent-written production code is trustworthy.
- `code-review` covers general code risks (logic, concurrency, money loss, contracts) but not AI-code high-frequency problems: fictitious dependencies/APIs, silent fallbacks, over-broad diffs, changing only tests to go green, and generation provenance.
- There is no agent-PR contract: intent/scope/evidence/ownership, CI-integrity diff, untrusted input entering workflows.
- There is no supply-chain review for third-party Skills, plugins, or MCP servers: untrusted instructions, bundled scripts, tool permissions, data exfiltration, version, and provenance.
- When AI drafts requirements or designs, `requirement-quality-review` has no "AI-generated spec" mode (fictitious scope, missing constraints, non-verifiable wording).
- `quality-productivity-metrics` and `automation-roi-analysis` have no AI cost denominator (tokens, review hours, rework rate, false-green rate).

Decision: add `ai-generated-code-review` and `skill-security-review`; cover the rest through modes and fields on existing Skills, without new directories.

### D. Workflow and routing: no AI loop, and currently red

- **No AI-native workflow.** Among 14 workflows, none covers "AI feature from eval design to release gate and production monitoring"; `ai-feature-validation` only routes to `ai-feature-testing` + `llm-testing` and stops at evaluation planning.
- **Missing verification routes.** The 2026-10-16 review proposed `bugfix-verification` and `ai-code-verification`, but `discover-testing/reference.md` still has only 8 routes, neither included.
- **Router coverage of AI is thin.** Only 5 of 20 AI Skills are named in the routing Prompt (`ai-agent-testing`, `ai-assisted-testing`, `ai-feature-testing`, `llm-testing`, `prompt-testing`); `llm-evaluation-design`, RAG, safety, injection, and 6 agent specialists never reach the selection table.
- **Stale snapshot.** `references/skill-capability-inventory.json` still has 169 IDs and lacks `test-case-importer` and `test-case-retrieval`; its unit test fails.
- **Quality gate is red.** `bash scripts/check_skills_quality.sh` exits 1 at Step 3 because the generated governance inventory is stale.
- **Report fields are insufficient.** `test-reporting` and `test-report-review` have no model, Prompt, dataset, judge, run ID, or token-cost fields, so AI evidence cannot be audited downstream.
- **Eval coverage is text-heavy.** Most of the 4–8 cases in AI packages check headings, status codes, and "must contain"; there are no trace fixtures, no no-skill baseline, and no "block when evidence is missing" behavior assertion.

## Proposed new Skills

Only 4 standalone packages are recommended, plus 1 conditional. The common rationale is that an adjacent Skill's **inputs, outputs, and evidence model** cannot contain the capability — not that the name sounds new.

| Candidate | Priority | Decision | Owns | Does not own |
| --- | --- | --- | --- | --- |
| `mcp-server-testing` | P0 | NEW | MCP 2026-07-28 stateless protocol, `server/discover`, stdio/Streamable HTTP, MRTR, `subscriptions/listen`, OAuth 2.1 with `iss`/audience, tool-schema integrity, description/resource poisoning, dual-era compatibility | Agent-side tool selection and side effects (`agent-tool-testing`); HTTP API contracts (`api-contract-testing`); generic injection behavior (`prompt-injection-testing`) |
| `ai-generated-code-review` | P0 | NEW | Review Agent-written production code: intent/scope/evidence/ownership, CI-integrity diff, fictitious dependencies/APIs, silent fallbacks, copy/paste, missing tests, generation provenance, stop rules | AI-written tests (`ai-generated-test-review`); general code risk (`code-review`); the full PR flow (`pr-quality-review`) |
| `structured-output-testing` | P1 | NEW | JSON/schema conformance, invalid-JSON recovery, partial streaming output, schema evolution, tool-argument structure, refusal and repair loops | HTTP API schema (`api-schema-validation`); Prompt behavior regression (`prompt-testing`) |
| `skill-security-review` | P1 | NEW (`skill-engineering`) | Third-party Skill/plugin/MCP supply chain: untrusted instructions, bundled script execution, tool permissions, data exfiltration, provenance and integrity, install-time risk | Own-package contract quality (`skill-quality-review`); product runtime safety (`ai-safety-testing`) |
| `ai-feature-release-workflow` | P2 | Conditional NEW (define the stage contract first) | AI eval asset chain (dataset/judge/eval run) → gate → canary/shadow → production monitoring → rollback, with a reviewable evidence pack | Rewriting `release-testing-workflow`'s general gate; implementing an eval engine or CI runner |

### Why these four

- **MCP is the only protocol with 0 repository hits that is already an integration surface.** The 2026-07-28 revision changes sessions, initialization, and subscriptions; the existing "tool-call contract" cannot cover version negotiation, transport, authorization, or poisoning. None of `agent-tool-testing`'s 10 coverage items is protocol-level.
- **AI-generated code and AI-generated tests carry different risks.** `code-review` does not check dependency reality or generation provenance, and `ai-generated-test-review` explicitly reviews tests only. Nobody owns "does the implementation actually meet the acceptance criteria, and did it cheat CI".
- **Structured output is a high-frequency failure surface, not a Prompt detail.** Product JSON mode, function-call arguments, partial streaming, and schema evolution each have their own failure modes; folding them into `prompt-testing` would mix regression with structural validation.
- **Skill/plugin/MCP supply chains are a new AI-native attack surface.** This repository itself distributes executable instructions and its CI already scans plugins, yet `skill-engineering` has quality, evaluation, prose, and change verification but no security review.
- **A workflow is added only when the stage handoff can be defined.** The earlier `ai-native-quality-workflow` was decided `MERGE` because it lacked an end-to-end stage/input/output contract; this time require stages, artifacts, exit states, and an evidence list before creating a directory.

## Existing Skills to enhance (no new directories)

| Target | Priority | Change | Acceptance |
| --- | --- | --- | --- |
| `discover-testing` | P0 | Regenerate the 169→171 capability snapshot; add an AI sub-domain routing table (eval design vs LLM behavior vs Prompt vs RAG vs agent family); add routes `bugfix-verification`, `ai-code-verification`, `ai-eval-gate` | Unit test passes; AI specialist hit rate is checkable; each route gives exactly one primary and at most one optional |
| `ai-assisted-testing` | P0 | Rewrite as v2: artifact-based delegation matrix, AI-draft acceptance protocol, provenance fields, false-confidence/false-green catalog, token/review/rework cost, human gates | Evals cover complete input, insufficient input, and high-risk/unauthorized scope; the Prompt is no longer four generic lines |
| `test-reporting` + `test-report-review` | P0 | Add AI evidence fields: model/Prompt/dataset/judge versions, run ID, token cost, evaluator identity, execution state | Report review can locate version mismatch and unexecuted evidence |
| `agent-tool-testing` | P1 | Add domain steps and `ATT-##`; MCP handoff, schema evolution, tool-description poisoning, idempotency keys, side-effect levels | Clear boundary with `mcp-server-testing`, no duplicated coverage |
| `prompt-injection-testing` | P1 | Add domain steps; extend indirect injection to RAG, tool descriptions, MCP resources, UI content; exfiltration channels, defense in depth, multi-turn persistence | Every coverage item has an observable assertion and evidence requirement |
| `llm-evaluation-design` | P1 | Add dataset hygiene (contamination/leakage/labeling), sample size and confidence, judge-calibration handoff, CI thresholds, domain steps | Produces an executable evaluation protocol, not a metric checklist |
| `llm-testing` | P1 | Clarify the boundary with feature/prompt/eval; add domain steps, sampling and budget, trajectory and cost | Stops being an ambiguous "does everything" entry |
| `ai-safety-testing` | P1 | Add a red-team program mode: attack-surface organization, attack library, over-refusal calibration, disclosure and escalation | Safety conclusions separate "no known failure" from "passed" |
| `ai-agent-testing` | P1 | Add a trace-evidence mode: span model, step attribution, pass^k, failure localization; handoff to `distributed-trace-analysis` | No behavioral claim without trace evidence |
| `quality-gate-design` | P1 | Add an AI eval gate mode: sample size/confidence, flake budget, judge version, cost budget, evidence provenance | A gate can block "green but evidence-poor" |
| `release-testing-workflow` | P1 | Add AI feature gate handoff: eval regression, guardrails, canary/shadow, rollback, production metrics | No AI details hardcoded into the general release flow |
| AI package `evals/` | P1 | Add trace fixtures, no-skill baseline, evidence-missing blocking, cross-language comparison; reduce heading-only assertions | At least one case refuses to pass when evidence is missing |
| `llm-consistency-testing` | P2 | Add a model/provider migration mode: re-baselining, deprecation deadline, dual-run, capability + cost regression | A migration conclusion binds both versions |
| `production-verification` | P2 | Add an AI production mode: online eval, drift, guardrail block rate, refusal/feedback, cost anomaly | Does not turn one-shot verification into continuous monitoring |
| `rag-retrieval-testing` | P2 | Add embedding/index migration, hybrid search, reranker, rebuild and freshness | Answer impact of retrieval changes is attributable |
| `test-data-generation` | P2 | Add synthetic eval sets, licensing and PII, contamination control | Dataset source and limits are traceable |
| `ci-test-optimization` | P2 | Add eval job cost/sharding/caching/rerun strategy | LLM calls are not treated as unit tests |
| `code-review` + `pr-quality-review` | P2 | Add agent-PR signals: scope drift, CI integrity, dependency reality, untrusted input; handoff to `ai-generated-code-review` | The general PR flow can spot an AI-generated over-broad diff |
| `requirement-quality-review` | P2 | Add an AI-generated spec mode: fictitious scope, missing constraints, non-verifiable wording | "Looks like a requirement" is not testable |
| `quality-productivity-metrics` + `automation-roi-analysis` | P2 | Add AI cost denominators and false-green/rework metrics | Generation speed does not substitute for delivery value |

## Explicitly not adding, or deferring

- **No "AI testing overview"**: `llm-testing` is already the entry; another package creates a second router.
- **No separate `prompt-regression` directory**: the current `prompt-testing` mode already carries baseline, candidate, dataset identity, and `PRT-##`.
- **No new Eval Engine/Runner/leaderboard**: `skill-up` is the single general eval engine; promptfoo/DeepEval fits only as a thin adapter later, preserving raw reports and cost boundaries.
- **No multimodal Skill yet**: speech/vision acceptance has no unified consistency standard (ITU-T P.808 covers speech quality only; multimodal agents are still evolving). Trigger: the target product truly has image/speech input and reviewable acceptance samples.
- **No standalone context-engineering package**: merge into `agent-memory-testing` and `prompt-testing` first; split when assembly/compaction/caching produce their own artifacts and evidence model.
- **No Prompt release-management package**: merge into `prompt-testing` regression and the `quality-gate-design` AI gate mode.
- **No "AI quality perspective" role**: `multi-role-quality-synthesis` and the five existing perspectives can carry it; AI findings should come from specialists to avoid role sprawl.
- **No plugin-specific Skills** (e.g., QA workbench board/radar operations): host behavior is not a leaf Skill; reuse evidence status fields but do not hardcode plugin paths into Skills.

## Iteration plan and acceptance

### Iteration A (P0, one short iteration): clear the red lights, then fix the AI-for-QA spine

1. Regenerate the governance inventory and `skill-capability-inventory.json`; fix the router unit test and the quality gate.
2. Upgrade `discover-testing`: AI sub-domain routing table plus `bugfix-verification` / `ai-code-verification` / `ai-eval-gate` routes.
3. Rewrite `ai-assisted-testing` v2 and land AI evidence fields in `test-reporting` / `test-report-review`.
4. Sync README, index, composition, registry, and roadmap counts (README/index say 171; the roadmap still says 169/338).

**Acceptance:** `bash scripts/check_skills_quality.sh` exits 0; the router unit test passes; each new route has one positive and one "insufficient information does not pass" case.

### Iteration B (P1, one to two iterations): protocol and generated code

1. Add `mcp-server-testing` and `ai-generated-code-review` (bilingual, `agents/openai.yaml`, three eval classes, index and README markers).
2. Upgrade `agent-tool-testing`, `prompt-injection-testing`, `llm-evaluation-design`, and `llm-testing`.
3. Add trace fixtures and "block when evidence is missing" cases to AI packages.

**Acceptance:** both new packages install independently when copied; MCP cases cover version negotiation, transport, authorization, poisoning, and dual-era; AI code review has at least one "all tests green but implementation wrong" case.

### Iteration C (P1/P2, one to two iterations): evaluation credibility and the release loop

1. Add `structured-output-testing` and `skill-security-review`.
2. Upgrade `quality-gate-design`, `release-testing-workflow`, `ai-safety-testing`, `ai-agent-testing`, `llm-consistency-testing`, and `production-verification`.
3. Decide whether `ai-feature-release-workflow` is mature enough for a package; if not, extend the `ai-feature-validation` route first.

**Acceptance:** the eval gate distinguishes "passed", "insufficient evidence", and "not run"; migration mode binds two versions; supply-chain review has a threat model and blocking rules.

### Iteration D (P2/watch): data, CI, multimodal, metrics

Schedule `rag-retrieval-testing`, `test-data-generation`, `ci-test-optimization`, `code-review`/`pr-quality-review`, `requirement-quality-review`, and `quality-productivity-metrics` based on real project feedback. Keep multimodal on watch and open it only when the trigger is met.

## Relationship to hosts such as the QA workbench

- Skills in this repository must stay host-agnostic; the QA workbench, Codex, Claude Code, and Cursor are callers.
- A workbench's board, gates, and project sessions can consume this repository's state vocabulary (`PASS`/`FAIL`/`BLOCKED`/`NOT_RUN`/`UNKNOWN`/`STALE`) and evidence-pack fields, but must not write workbench paths, project IDs, or database schemas into leaf Skills.
- If automation needs to chain stages, prefer a host-side adapter or a copyable workflow recipe over stuffing multi-step orchestration into `discover-testing`'s "one primary Skill" contract.
- Project-scoped AI sessions are a good place to give each Skill a stable working directory and evidence location; that is a host responsibility, not an install dependency.

## External observations (2026-11-23 snapshot)

These explain "why now" only; the repository has not validated them:

- **MCP 2026-07-28** removes protocol-level sessions and the `initialize` handshake, adds `server/discover`, MRTR, and `subscriptions/listen`, and deprecates sampling/roots/logging/DCR. The test surface therefore expands from "tool arguments" to protocol, transport, authorization, and generational compatibility. [MCP changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog)
- **MCP security best practices** name token passthrough, confused deputy, SSRF, and state-handle binding; these can be turned into executable cases. [MCP security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)
- **OpenTelemetry GenAI semantic conventions** remain in Development and have moved out of the core repository; agent, tool, and `load_skill` spans can be an optional evidence layer, but must be version-pinned and content capture off by default. [semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai)
- **LLM-as-judge cannot be assumed trustworthy**: MT-Bench reports ~80% agreement with human preference while naming position, verbosity, and self-enhancement bias; JudgeBench shows strong judges may be only slightly better than random on objective hard pairs. Calibration should use inter-rater agreement and bias probes, not a single score. [MT-Bench](https://arxiv.org/abs/2306.05685) · [JudgeBench](https://arxiv.org/abs/2410.12784)
- **Model retirement is routine**: official notice windows range from weeks to months, and unpinned aliases drift silently; migration needs representative requests on both models with output, latency, and cost comparison. [OpenAI deprecations](https://developers.openai.com/api/docs/deprecations) · [Anthropic model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- **AI-generated code has quantifiable specific risks**: early Copilot research found about 40% of security-relevant generated snippets vulnerable; assistant users were more likely to overestimate their code's security; about 19.7% of generated package names were fictitious, enabling "slopsquatting". [Pearce et al.](https://cacm.acm.org/research-highlights/asleep-at-the-keyboard-assessing-the-security-of-github-copilots-code-contributions/) · [Perry et al.](https://arxiv.org/abs/2211.03622) · [USENIX 2025](https://par.nsf.gov/biblio/10686032/media/xml)
- **Agent PR review now has concrete checks**: CI gaming (deleted/skipped tests, lowered coverage), code-reuse blindness, "hallucinated correctness", untrusted input in workflows, and a "request a smaller PR above 5 unrelated files" stop rule. [GitHub Blog](https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/)
- **Agent evaluation is moving from final answers to trajectories**: LangSmith distinguishes final response, trajectory, and single step; DeepEval offers trajectory metrics; τ-bench's `pass^k` exposes "capable but unstable". [LangSmith](https://docs.langchain.com/langsmith/evaluate-complex-agent) · [DeepEval](https://deepeval.com/docs/metrics-introduction) · [τ-bench](https://arxiv.org/abs/2406.12045)
- **Speech/multimodal still lacks a unified acceptance standard**: ITU-T P.808 covers crowdsourced speech quality, and voice-agent metrics are still evolving; this supports "watch, do not split a package yet". [ITU-T P.808](https://www.itu.int/rec/T-REC-P.808-202106-I/en)

## Main sources

- Repository: [README](../../README_EN.md), [Skills index](../catalog/skills-index_EN.md), [evolution roadmap](../governance/QA_SKILLS_EVOLUTION_ROADMAP_EN.md), [governance roadmap](../governance/SKILL_GOVERNANCE_ROADMAP_EN.md), [matching register](../SKILL_MATCHING_REGISTER_EN.md)
- Earlier reviews: [AI-Native QA opportunities (2026-10-16)](./2026-10-16-ai-native-qa-development-landscape_EN.md), [GitHub adjacent projects (2026-10-25)](./2026-10-25-github-qa-skills-iteration-research_EN.md)
- Key files: [`ai-assisted-testing`](../../skills/en/testing-types/ai-assisted-testing/), [`agent-tool-testing`](../../skills/en/testing-types/agent-tool-testing/), [`llm-evaluation-design`](../../skills/en/testing-types/llm-evaluation-design/), [`discover-testing` routing reference](../../skills/en/testing-workflows/discover-testing/reference.md), [quality gate script](../../scripts/check_skills_quality.sh)
- External links are in the previous section; all external content is a public snapshot dated 2026-11-23 and was not independently re-tested.

## Iteration A (P0) Status Snapshot (2026-11-23)

This is a historical snapshot from the standalone Iteration A acceptance. Its 171-entry router snapshot and 171-Skill CLI discovery count predate the later B–D work and do not represent the current directory total. It records repository changes and checks, not a Skill behavior evaluation, business acceptance, or release approval.

| Item | Status | Evidence / remaining work |
| --- | --- | --- |
| A1 quality gate and router snapshot | **Complete** | Final `check_skills_quality.sh` PASS (414 tests); bilingual router snapshot has 171 entries and generated inventories/matrices are current. |
| A2 routing and AI subdomains | **Complete within the execution-plan scope** | Added `bugfix-verification` and `ai-eval-gate`; prompts cover 20 AI Skills and include four bilingual routing Evals; Composition has 10 routes and 16 target Skills. The `ai-code-verification` route proposed by this gap review was not implemented in this iteration and remains a follow-up. |
| A3 `ai-assisted-testing` v2 | **Complete** | Bilingual version 2.0.0 with delegation matrix, provenance chain, false-confidence catalog, cost fields, human gates, and six Eval cases per language. |
| A4 AI reporting evidence | **Complete** | Bilingual `test-reporting` and `test-report-review` version 1.1.0; report review adds check 8 for AI version/run consistency; each Skill has one new bilingual Eval. |
| Final read-only review | **Complete** | Strengthened bilingual Evals: false-green requires `release_gate_status: BLOCKED` / `human_release_decision: PENDING`; unsupported productivity requires `productivity_claim_status: UNSUPPORTED`; bugfix routing requires `verification_state: NOT_RUN`. These are literal field assertions and cannot detect renamed fields or contradictory prose; the corresponding Prompts define each field as the sole source of its conclusion. |
| AI behavior evaluation | **NOT_RUN** | No real-model evaluation was run; this iteration made no model calls, used no credentials, and incurred no model-evaluation cost. Static Eval YAML validation is not behavior evaluation. |
| Commit and release | **Not performed** | No commit or push was made; both remain subject to later authorization. |

Iteration A snapshot verification: `bash scripts/check_skills_quality.sh` PASS (414 tests); `SKILLS_CLI_PACKAGE="$PWD" bash scripts/check_skills_cli_compatibility.sh` PASS (`skills@1.7.0` discovered 171 Skills from the local checkout at that time and completed an isolated English `functional-testing` install smoke); `bash scripts/validate_skill_evals.sh` PASS (352 OK / 0 fail at that time); bilingual documentation check PASS (0 findings).

## Full Iteration Scope Reconciliation (2026-11-23)

This section combines the gap review with the A–D iteration scope supplied by the user. It reconciles the recommendations above with the Eval requirements for 20 AI Skills and avoids counting the same Skill twice.

- **Add 4 standalone Skills:** `mcp-server-testing`, `ai-generated-code-review`, `structured-output-testing`, and `skill-security-review`. There is also **1 conditional Workflow:** `ai-feature-release-workflow`. Its phase inputs/outputs, exit states, and evidence handoffs are now defined, so it is included for creation.
- **Modify 33 existing logical Skills:** 18 explicit Iteration B–D targets; 4 Iteration A items (`discover-testing`, `ai-assisted-testing`, `test-reporting`, and `test-report-review`); and 11 additional Skills from the 20-AI-Skill Eval audit not covered by those targets. The 20 Eval requirements are included in this count; do not add another 20.
- “Logical Skill” counts canonical names. The 33 existing bilingual updates map to 66 language directories. The 4 new Skills plus 1 Workflow map to 10 new language directories, for 38 canonical packages and 76 bilingual directories affected.
- `ai-code-verification` is a route in `discover-testing`, not a new Skill. Multimodal remains under observation until a target product has image/voice input and reviewable acceptance samples.
- After catalog synchronization, the repository should have 176 Skills per language (15 workflows, 155 testing types, 6 Skill Engineering), or 352 bilingual directories total.

### Final A–D Plan Closeout (2026-11-23)

- **Scope implemented:** 4 new standalone Skills, 1 conditional Workflow, and 33 existing logical Skills; 38 canonical packages / 76 bilingual directories total. Iteration A's `ai-code-verification` route, `ai-eval-gate`, and reporting evidence are implemented. Iteration B/C protocol, generated-code, structured-output, security, Eval-gate, release-loop, and migration items are implemented. Iteration D's RAG, test-data, CI, code-review, requirements-review, productivity-metric, and ROI items are included in their corresponding Skills.
- **Evaluation assets:** Added 12 bilingual Eval case pairs for B/C and the 20-AI-Skill evidence audit, covering MCP poisoning and dual-era compatibility, ATT/MCP handoff, structured-output evolution, judge/sample/CI gates, red-team testing, model migration, and trajectory/no-skill/bilingual comparison. Comparison runs remain `NOT_RUN`; no model output or behavioral evidence was fabricated.
- **Versioning:** New Skills start at `1.0.0`; 9 existing Skills modified in this follow-up received patch bumps, with reasons recorded in both language version histories.
- **Capability boundary:** Multimodal remains under observation and has no standalone Skill; its documented trigger conditions are not met.
- **Verification:** `bash scripts/check_skills_quality.sh` PASS (352 directories, 362 skill-up validations, 415 tests); `SKILLS_CLI_PACKAGE="$PWD" bash scripts/check_skills_cli_compatibility.sh` PASS (pinned `skills@1.7.0` discovered 176 Skills and completed an isolated English install smoke); `git diff --check` PASS. Static validation is not real-model behavioral evaluation.
- **Delivery:** All repository-level A–D plan items are implemented and committed to PR #50; the PR remains open and unmerged. PR CI must be read against the final commit.

**Not run / risk:** Real-model Evals, the no-skill baseline, and Chinese/English behavioral comparisons are `NOT_RUN` (the original D2 default scope); runtime behavior is therefore not claimed as passed. A multimodal Skill remains conditional on its trigger.
