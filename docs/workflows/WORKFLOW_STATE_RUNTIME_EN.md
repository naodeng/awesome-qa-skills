<div align="right"><a href="./WORKFLOW_STATE_RUNTIME.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Local Workflow Run State CLI

`scripts/workflow_run_state.py` is an optional local JSON ledger for Workflow contracts. It stores Run ID, Workflow package fingerprint, input fingerprint, Commit SHA, stage states, evidence references, checkpoints, and idempotency keys. It does not call an Agent, schedule Skills, or perform writes or releases.

## Create a Run and fingerprint inputs

`fingerprint` hashes selected file or directory contents together with the Commit SHA. `create` also records the Workflow package fingerprint, so local Workflow or prompt changes invalidate old Runs.

```bash
COMMIT_SHA="$(git rev-parse HEAD)"
python3 scripts/workflow_run_state.py fingerprint \
  --base-dir . \
  --input skills/en/testing-workflows/pr-quality-review \
  --input path/to/review-input.md \
  --commit-sha "$COMMIT_SHA"

python3 scripts/workflow_run_state.py create \
  --workflow-file skills/en/testing-workflows/pr-quality-review/workflow.yaml \
  --state-dir /tmp/qa-workflow-state \
  --input-fingerprint <SHA-256-from-the-previous-command> \
  --commit-sha "$COMMIT_SHA"
```

The state is a new standalone JSON file; keep its directory outside the Skill package. Creating the same Run ID twice fails.

## Stages and checkpoints

`start-stage` rechecks the input fingerprint, Commit SHA, and Workflow package. A stage cannot start before its dependencies complete, and a stage that was already started or finished cannot be started again in the same Run. Completing a stage requires at least one evidence reference. Failures, blocks, and skips must be recorded explicitly.

```bash
python3 scripts/workflow_run_state.py start-stage \
  --state-file /tmp/qa-workflow-state/pr-quality-review/<run-id>.json \
  --workflow-file skills/en/testing-workflows/pr-quality-review/workflow.yaml \
  --stage-id scope \
  --expected-input-fingerprint <SHA-256> \
  --expected-commit-sha "$COMMIT_SHA"

python3 scripts/workflow_run_state.py complete-stage \
  --state-file /tmp/qa-workflow-state/pr-quality-review/<run-id>.json \
  --stage-id scope \
  --evidence-ref evidence/scope-review.json \
  --checkpoint-ref checkpoints/scope.json
```

## Recovery and permissions

```bash
python3 scripts/workflow_run_state.py resume \
  --state-file /tmp/qa-workflow-state/pr-quality-review/<run-id>.json \
  --workflow-file skills/en/testing-workflows/pr-quality-review/workflow.yaml \
  --expected-input-fingerprint <current-SHA-256> \
  --expected-commit-sha "$(git rev-parse HEAD)"
```

- If an input, package, or Commit fingerprint changes, the Run and unfinished stages become `STALE`.
- If a process stops while a stage is `RUNNING`, `resume` changes that stage to `BLOCKED` so its side effects can be reviewed. The CLI never replays it automatically.
- `resume` reports whether the checkpoint still matches and which untouched stages are ready. It does not call a Skill or retry a stage.
- A stage with `permission: write` or `approval_required: true` requires `--confirm --approved-by <identifier>`. The state records the time, scope, and supplied identifier.
- `--approved-by` is an audit label, not an authenticated identity. External writes, deletion, publishing, and formal release approval still require trusted human confirmation enforced by the Agent Host; the local CLI is not a security authorization boundary.

See the [Workflow Contract](./WORKFLOW_CONTRACT_EN.md) and [Run State Schema](../../resources/workflows/schemas/run-state.schema.json) for field constraints. This is a Python standard-library script and adds no Skill installation dependency.

## Validation

```bash
python3 -m unittest scripts.tests.test_workflow_run_state -v
python3 scripts/validate_workflow_contracts.py --repo-root .
```
