<div align="right"><a href="./PHASE_0_PROMPT_BASELINE_SOURCES.md">中文</a></div>

# Phase 0 Prompt Baseline Source Register

## Pinned source

Phase 0 candidate capabilities use the adjacent `naodeng/awesome-qa-prompt` repository as a
read-only reference. This review is pinned to `develop` commit
`554178fe9b93d851ec01388597ceb7996d22bd1c` at
`https://github.com/naodeng/awesome-qa-prompt`.

These files are content-quality and topic-coverage baselines, not a runtime dependency of
`awesome-qa-skills`. Skill packages must not copy `Standard-version/`, framework variants, or
cross-repository relative links; this register records source locations and match evidence only.

## Six evidence fields

| Field | Baseline evidence location |
| --- | --- |
| name | Bilingual `README.md` title and the Prompt role/title |
| purpose | `README.md` usage statement and the Prompt purpose comment |
| inputs | `必要输入` / `Required inputs` in `Standard-version/*.md` |
| outputs | `执行指令` / `Execution instructions` in `Standard-version/*.md` |
| decision_logic | `分析方法` / `分析与设计方法`, focused scope, and degradation rules |
| workflow_role | The stage boundary in `QA_SKILLS_EVOLUTION_ROADMAP_EN.md` and the baseline's focused output role |

## Candidate mapping

Paths below are relative to the pinned commit; `zh` and `en` directories are paired.

| Candidate | Current target | Conclusion | Prompt Baseline | Adaptation boundary |
| --- | --- | --- | --- | --- |
| `requirement-change-impact-analysis` | `change-impact-analysis` | MATCH | `testing-types/{zh,en}/change-impact-analysis/` | Direct and indirect change impact; not requirement-gap analysis |
| `test-impact-analysis` | `change-impact-analysis`, `pr-test-impact-analysis` | MERGE | `change-impact-analysis/` + `pr-risk-analysis/` | Combine change impact and PR test impact; risk is not an execution result |
| `code-change-risk-analysis` | `pr-test-impact-analysis` | MERGE | `testing-types/{zh,en}/pr-risk-analysis/` | PR/Diff risk, critical paths, and test impact; not full code review |
| `workload-modeling` | `performance-workload-modeling` | MATCH | `testing-types/{zh,en}/workload-model-design/` | Workload sources, transaction mix, arrival/concurrency, and growth assumptions |
| `capacity-planning` | `capacity-planning-analysis` | MATCH | `testing-types/{zh,en}/capacity-planning-analysis/` | Capacity needs, resource constraints, and growth assumptions; no invented metrics |
| `regression-scope-selection` | `regression-scope-analysis`, `regression-test-selection` | MERGE | `regression-scope-analysis/` + `regression-test-selection/` | Define scope first, then select an execution set from known assets |
| `ai-test-case-review` | `ai-generated-test-review` | MATCH | `testing-types/{zh,en}/ai-generated-test-review/` | Review AI-generated cases using supplied requirements and technical material |
| `ai-log-analysis` | `log-analysis` | ENHANCE | `testing-types/{zh,en}/log-analysis/` | Log events, timelines, errors, and correlated evidence |
| `ai-root-cause-analysis` | `root-cause-analysis` | ENHANCE | `testing-types/{zh,en}/root-cause-analysis/` | Evidence, cause hypotheses, and validation paths; no unverified root-cause claims |
| `quality-risk-identification` | `quality-risk-analysis` | MATCH | `testing-types/{zh,en}/quality-risk-analysis/` | Quality risks, impact, evidence, and mitigation options |
| `ai-test-data-generation` | `test-data-generation` | ENHANCE | `testing-types/{zh,en}/test-data-generation/` | Test goals, constraints, privacy, and traceable data plans |
| `llm-output-quality-testing` | `llm-testing` | ENHANCE | `testing-types/{zh,en}/llm-output-quality-evaluation/` | Output-quality dimensions, scoring, and evidence; not executed evaluation results |
| `llm-evaluation` | `llm-evaluation-design` | MATCH | `ai-evaluation-design/` + `llm-output-quality-evaluation/` | Evaluation goals, datasets, metrics, decision rules, and reproducibility |

## Limitations

These sources support a structured review of candidate name, purpose, inputs, outputs, decision
logic, and Workflow role. They do not provide project-specific business requirements, Issue/PR
constraints, model execution results, or real quality scores. Candidate `decision_state` therefore
uses `REVIEWED_WITH_LIMITATION`; Quality Score and Eval execution remain `NOT_SCORED` / `NOT_RUN`,
and Prompt semantic equivalence and runtime effectiveness remain `UNASSESSED`.
