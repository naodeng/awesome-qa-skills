<div align="right"><a href="./skills-graph.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Skill Relationship Graph

This is a navigation aid, not an installation dependency. Physical packages remain under `skills/{zh|en}/`.

## Capability Landscape

```mermaid
flowchart LR
    D[Discovery and Requirements Analysis] --> S[Solution Design and Test Strategy]
    S --> P[Test Design and Preparation]
    P --> E[Test Execution and Analysis]
    E --> R[Release and Delivery]
    R --> O[Production Operations and Incident Response]
    O --> I[Retrospective and Continuous Improvement]

    C[Core QA Skills] --- D
    G[Engineering QA Skills] --- S
    G --- P
    G --- E
    Q[Production Quality Skills] --- R
    Q --- O
    A[AI Native QA Skills] --- D
    A --- P
    A --- E
    H[Skill Engineering\nCross-cutting governance] --- I
```

The evolution model is `Core QA Skills → Engineering QA Skills → Production Quality Skills → AI Native QA Skills`. Nodes show primary lifecycle placement, not a mandatory execution order.

## Recommended Compositions

| Scenario | Recommended composition | Outcome |
| --- | --- | --- |
| New-feature quality preparation | `requirements-analysis` → `test-strategy` → `test-case-writing` → `functional-testing` | Traceable test scope, cases, and execution conclusion |
| Change and regression decision | `change-impact-analysis` → `regression-scope-analysis` → `regression-test-selection` | Evidence-based regression scope and candidate test set |
| API delivery | `api-contract-testing` → `api-testing` → `test-reporting` | Contract compatibility, API coverage, and delivery report |
| Performance decision | `performance-workload-modeling` → `performance-testing` → `performance-result-analysis` → `capacity-planning-analysis` | Workload assumptions, result interpretation, and capacity risk |
| Production anomaly | `metrics-anomaly-analysis` → `distributed-trace-analysis` → `production-incident-analysis` → `root-cause-analysis` | Evidence timeline, testable hypotheses, and follow-up actions |
| AI feature validation | `ai-feature-testing` → `llm-evaluation-design` → `llm-testing` → `prompt-injection-testing` | Evaluation design, behavior evidence, and safety boundaries |
| Agent tool validation | `ai-agent-testing` → `agent-tool-testing` → `prompt-injection-testing` | State, tool side-effect, and injection-defense evidence |

Every composition is optional. Use `discover-testing` when the entry point or sequence is unclear.

## Boundaries

- `ai-assisted-testing` is **AI for QA** and can assist any stage; it is not a replacement for Testing for AI.
- Production Quality Skills analyze evidence and recommend actions; releases, rollbacks, waivers, and risk acceptance still require human approval.
- `skill-engineering` governs Skills; it is not a fifth QA lifecycle stage.

## Navigation

- [Complete index](skills-index.md)
- [Chinese roadmap](../governance/QA_SKILLS_EVOLUTION_ROADMAP.md)
- [English roadmap](../governance/QA_SKILLS_EVOLUTION_ROADMAP_EN.md)
