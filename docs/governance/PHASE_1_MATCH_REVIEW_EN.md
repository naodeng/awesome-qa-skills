<div align="right"><a href="./PHASE_1_MATCH_REVIEW.md">中文</a></div>

# v1.6 Phase 1 Project-Context Match Review

This record connects the four v1.6 Project #4 Match Review cards to one real project context. It is bounded project evidence, not proof of semantic equivalence, production behavior, model effectiveness, or business acceptance.

## Pinned scope and evidence

- Project: `Awesome QA Skills — Governance & Roadmap`, Project #4.
- Four cards: `capacity-planning`, `workload-modeling`, `requirement-change-impact-analysis`, and `quality-risk-identification`.
- Project context: [`naodeng/dsh-qa@6d650ca`](https://github.com/naodeng/dsh-qa/tree/6d650cae72be8fc582bc4f47d6ba48e3fc28157d).
- Requirements evidence: [`2026-09-15-requirements.md`](https://github.com/naodeng/dsh-qa/blob/6d650cae72be8fc582bc4f47d6ba48e3fc28157d/docs/quality-workbench/2026-09-15-requirements.md).
- Capacity evidence: [`2026-08-25-technical-design.md`](https://github.com/naodeng/dsh-qa/blob/6d650cae72be8fc582bc4f47d6ba48e3fc28157d/docs/quality-workbench/2026-08-25-technical-design.md) and [`server/quality/test-runner.js`](https://github.com/naodeng/dsh-qa/blob/6d650cae72be8fc582bc4f47d/server/quality/test-runner.js).
- Lifecycle evidence: [`test/e2e/dsh-panel-lifecycle.spec.js`](https://github.com/naodeng/dsh-qa/blob/6d650cae72be8fc582bc4f47d6ba48e3fc28157d/test/e2e/dsh-panel-lifecycle.spec.js).

The project material is supplied as input facts to the target Skill's bilingual Evals. The Evals do not need runtime access to dsh-qa, and an output of `MATCH` is not automatically promoted to an implementation change.

## Review results

| Candidate | Target Skill | Observed project contract | Conclusion | State and boundary | Eval evidence |
| --- | --- | --- | --- | --- | --- |
| `requirement-change-impact-analysis` | `change-impact-analysis` | Panel/Slot shell migration, preserved iframe/API boundary, MutationObserver lifecycle, and real-host checks require direct/transitive impact, rollback, and evidence-gap analysis. | `MATCH` | `REVIEWED_WITH_LIMITATION`; semantic state=`UNASSESSED`. | [`zh phase-1-project-context`](../../skills/zh/testing-types/change-impact-analysis/evals/cases/phase-1-project-context.yaml), [`en phase-1-project-context`](../../skills/en/testing-types/change-impact-analysis/evals/cases/phase-1-project-context.yaml) |
| `workload-modeling` | `performance-workload-modeling` | One running test per project, two globally, `MAX_ACTIVE_PREVIEWS=20`, queue/running/terminal states, and capacity-exceeded behavior require transaction, arrival-rate, and concurrency modeling. | `MATCH` | `REVIEWED_WITH_LIMITATION`; semantic state=`UNASSESSED`. | [`zh phase-1-project-context`](../../skills/zh/testing-types/performance-workload-modeling/evals/cases/phase-1-project-context.yaml), [`en phase-1-project-context`](../../skills/en/testing-types/performance-workload-modeling/evals/cases/phase-1-project-context.yaml) |
| `capacity-planning` | `capacity-planning-analysis` | Run and preview limits, reserved slots, queueing, and `QUALITY_RUN_CAPACITY_EXCEEDED` require connecting throughput, resources, SLOs, degradation, and scaling lead time. | `MATCH` | `REVIEWED_WITH_LIMITATION`; semantic state=`UNASSESSED`. | [`zh phase-1-project-context`](../../skills/zh/testing-types/capacity-planning-analysis/evals/cases/phase-1-project-context.yaml), [`en phase-1-project-context`](../../skills/en/testing-types/capacity-planning-analysis/evals/cases/phase-1-project-context.yaml) |
| `quality-risk-identification` | `quality-risk-analysis` | Panel/Slot lifecycle, iframe/API boundary, run-capacity limits, and E2E lifecycle coverage require failure modes, likelihood, impact, detectability, controls, and residual risk. | `MATCH` | `REVIEWED_WITH_LIMITATION`; semantic state=`UNASSESSED`. | [`zh phase-1-project-context`](../../skills/zh/testing-types/quality-risk-analysis/evals/cases/phase-1-project-context.yaml), [`en phase-1-project-context`](../../skills/en/testing-types/quality-risk-analysis/evals/cases/phase-1-project-context.yaml) |

## Decision boundaries

- All four records continue to reuse existing bilingual target Skills; no duplicate directory was created and no canonical name was changed.
- `MATCH` means that the project context aligns with the existing target capability surface. It does not prove Prompt semantic equivalence.
- Project documents, source code, and Eval outputs are static, project-context, and evaluation evidence. They do not replace real-model comparison, external-target execution, production observation, human approval, or business acceptance.
- A target Skill's `eval_execution`, `quality_score`, and production/business states are not promoted by this record. Without corresponding evidence they remain `NOT_RUN`, `NOT_SCORED`, or `UNASSESSED`.
- If future evidence finds a difference, open an enhancement/implementation card against the existing target Skill; do not create a parallel directory based on this Match Review.

## Reproduction

```bash
python3 scripts/generate_skill_governance_matrix.py --check
python3 scripts/check_docs_bilingual.py --repo-root .
skill-up validate skills/zh/testing-types/change-impact-analysis/evals/eval.yaml
skill-up validate skills/en/testing-types/change-impact-analysis/evals/eval.yaml
```

The project-context case is registered in each of the eight bilingual target `eval.yaml` files. Real-model replay, production capacity, and business acceptance require separate authorization and evidence.

As of 2026-09-22, the historical replay for all eight new project-context cases ended in `PASS`; the existing three-case regressions for all four target Skills also passed in both languages, for 32/32 historical final case outcomes. That 32/32 record corresponds to the configuration before the domain-fact assertions were strengthened in this review. After the fix, new project-context cases retain a dedicated `720s` per-case budget, while existing regression cases keep the `180s` suite default so unrelated model cost is not expanded; the first fresh Phase 1 replay ended in `ERROR` after reaching the `720s` case timeout, so current strict-assertion model evidence is recorded as `INSUFFICIENT_EVIDENCE`, not as a Skill failure. The bilingual requirements-analysis boundary and semantic cases passed fresh in this review. These results prove only the target output contract and bounded model replay for pinned inputs; they do not prove semantic equivalence, production behavior, or business acceptance.
