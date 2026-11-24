# AI Feature Release Workflow Prompt

Connect evaluation design, release gating, staged rollout, monitoring, and rollback planning for an AI feature. Produce a versioned, reviewable evidence chain. This Workflow coordinates work; it does not implement an evaluation engine, execute production changes, or approve release.

## Inputs

Record the feature and change scope; current and candidate model/provider/version; prompt or agent version; dataset and rubric/judge versions; evaluation run IDs and raw-evidence locations; thresholds and sample plan; cost and flake budgets; target environment and rollout cohort; monitored metrics and sourced thresholds; rollback actions; owners and decision authority. Mark unavailable values `UNKNOWN`.

## Phase Contract

| Phase | Entry evidence | Required artifacts | Exit condition |
| --- | --- | --- | --- |
| Contract and risk | Feature goal, scope, owner | Evaluation objective, risk slices, dataset/judge identity, sampling plan, thresholds, privacy boundary | Criteria and source versions are reviewable; otherwise `BLOCKED` |
| Pre-release evaluation | Frozen candidate and versioned assets | Run ID, model/prompt/dataset/judge versions, configuration, sample counts, raw report reference, cost, failures and uncertainty | All required criteria have current evidence; otherwise `NOT_RUN`, `UNKNOWN`, `STALE`, or `BLOCKED` |
| Release gate | Evaluation evidence and release scope | Gate table, confidence/flake limits, exceptions, residual risks, human decision owner | Recommendation is evidence-backed; formal decision remains `PENDING` until approved by an authorized human |
| Canary or shadow | Approved rollout plan and production owner | Cohort, traffic share, observation window, sourced guardrail thresholds, isolation, stop conditions | Criteria for expand/hold/rollback and evidence collection are explicit |
| Monitor, rollback, closeout | Live monitoring owner and rollback path | Drift/quality/refusal/feedback/cost signals, alert owner, rollback record, post-release evaluation and follow-up | Continue, hold, rollback, or closeout is recorded with evidence; no missing signal is treated as healthy |

## State and Version Rules

- Use `PASS`, `FAIL`, `BLOCKED`, `NOT_RUN`, `UNKNOWN`, or `STALE` for evidence and gate state. A stage run may also be `SKIPPED` only with a reason.
- Use `PENDING`, `APPROVED`, or `REJECTED` for the human release decision. Only an authorized human may set `APPROVED`.
- A gate is `PASS` only when every required criterion has current, in-scope evidence. Missing run artifacts are `NOT_RUN` when non-execution is known; otherwise `UNKNOWN`. Missing required inputs or unsafe conditions are `BLOCKED`. Version mismatch is `STALE`.
- Re-evaluate affected gates when model, provider, model version, prompt, dataset, judge, serving configuration, or cohort changes.
- Preserve raw evaluation report references, hashes when available, timestamp, sample counts, uncertainty, and cost basis. Summaries do not replace raw evidence.

## Handoffs

Use `llm-evaluation-design` for dataset/judge/statistical protocol; `quality-gate-design` for threshold and block rules; `release-testing-workflow` for general T-window and release coordination; `production-verification` for controlled production observations. Do not require these as install-time dependencies or claim they ran unless there is evidence.

## Output

1. Feature and release scope, owners, and version map.
2. Phase board with entry evidence, owner, state, exit criteria, and handoff.
3. Evaluation gate table with `evaluation_gate_status`, thresholds, observed values, raw evidence, uncertainty, and cost.
4. Canary/shadow plan with `rollout_status`, cohort, window, guardrails, stop and rollback criteria.
5. Monitoring and closeout plan, including evidence gaps and next actions.
6. `human_release_decision` and authorized owner; leave `PENDING` when no approval record is supplied.

## Stop Rules

- Block rollout planning when scope, owner, or rollback authority is unknown and the gap changes risk.
- Do not recommend expansion when a required gate is failed, blocked, stale, or unrun.
- A missing or broken monitoring signal is not a pass; hold or stop according to the sourced guardrail.
- Never invent thresholds, run results, approval, or production health.
