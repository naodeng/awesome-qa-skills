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

## Registry linkage

Candidate name, target, conclusion, and adaptation boundary are maintained only in
`docs/governance/skill-governance-registry.yaml`; the Registry is the single source of truth.
This file defines only the pinned Prompt Baseline commit and the evidence-location rules, so it
does not become a second candidate decision table.

Each Registry `candidate_source` lists the relevant Baseline `README.md` and
`Standard-version/*.md` paths directly. Each six-field `evidence` value lists concrete files and
sections on both the candidate-Baseline and current-Target sides. Paths below are relative to the
pinned commit; `zh` and `en` directories are paired.

## Limitations

These sources support a structured review of candidate name, purpose, inputs, outputs, decision
logic, and Workflow role. They do not provide project-specific business requirements, Issue/PR
constraints, model execution results, or real quality scores. Candidate `decision_state` therefore
uses `REVIEWED_WITH_LIMITATION`; Quality Score and Eval execution remain `NOT_SCORED` / `NOT_RUN`,
and Prompt semantic equivalence and runtime effectiveness remain `UNASSESSED`.
