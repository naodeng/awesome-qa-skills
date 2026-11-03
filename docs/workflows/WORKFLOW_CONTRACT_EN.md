<div align="right"><a href="./WORKFLOW_CONTRACT.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# QA Workflow Contract v1.0

Start a new `workflow.yaml` from [`workflow.template.json`](../../resources/workflows/templates/workflow.template.json). The bilingual `pr-quality-review/workflow.yaml` is a complete example with stage dependencies, specialist Skill IDs, failure behavior, and permission policy.

`workflow.yaml`, `evidence.json`, and `run-state.json` are portable data contracts, not a workflow execution engine. The repository also provides an optional local state CLI to persist checkpoints, detect staleness, and record human approval. It does not schedule or execute Skills, and it cannot authenticate the identity supplied through `--approved-by`. Schemas live in [`resources/workflows/schemas/`](../../resources/workflows/schemas/), with examples beside them. A leaf workflow Skill depends only on prompts and references inside its own package; runtime use does not require the schema files.

To let the repository quality gate validate contracts without extra Python packages, `workflow.yaml` uses JSON syntax (JSON is a subset of YAML). The repository validator checks fields, step references, package-relative resources, bilingual parity, and examples. Consumers can apply a standard JSON Schema Draft 2020-12 validator for stricter validation.

## `workflow.yaml`

Each `skills/{zh,en}/testing-workflows/<slug>/workflow.yaml` records:

- `id`, semantic version, kind (sequential workflow, router, independent task set, or single task), and lifecycle state.
- Required/optional inputs, deliverables, stage order, and `depends_on` links.
- An output's `evidence_kind` marks its primary evidence type. Split composite reports into outputs by type, and preserve each claim's type in `evidence.json`.
- A stage may declare `skip_when`; every entry must give a checkable condition and reason. Without an explicit condition, the stage runs and cannot be silently skipped.
- Canonical Skill IDs used by a stage, optional package-local prompt paths, and behavior on failure or missing dependencies.
- Default permissions, side effects requiring explicit approval, handoff fields, and evidence-contract version.
- Checkpoints record the Workflow package fingerprint, user-input fingerprint, Commit SHA, stage state, evidence/artifact references, and idempotency keys. Any change invalidates prior results. The optional local CLI checks these values on `resume` and marks interrupted `RUNNING` stages `BLOCKED` for review; it never replays a stage. Actual Skill calls and trusted human authorization remain the host Runtime's responsibility.

Skill IDs are capability navigation, not automatic installation dependencies. If the host has not provided an installation inventory, availability remains `UNKNOWN`. A missing Skill must never be described as executed; the workflow must degrade, block, or request the minimum needed context according to its contract.

## `evidence.json`

Evidence is classified as `fact`, `inference`, `plan`, or `execution`. Each record carries a claim, status, source, producer version, and observation time; an inference also lists its basis. Execution evidence records execution type, scope, environment, and start/end times; test execution also requires a command and exit code. `static_analysis` proves only its static-check scope and cannot substantiate a passing `test_execution` claim.

`PASS`, `FAIL`, `BLOCKED`, and `UNKNOWN` apply only to the scope stated in the claim. Derive a workflow summary status from its evidence items using `FAIL > BLOCKED > UNKNOWN > PASS`; PASS requires at least one evidence item and every item to be PASS. No evidence means UNKNOWN. Missing sources, run records, or versions keep a claim UNKNOWN. A PASS past `valid_until` cannot be reused. A local workflow PASS does not authorize product release or risk acceptance.

## Recommended practices

- Route a single deliverable to an existing specialist Skill. Start a complete Workflow only when the user asks for a cross-stage outcome.
- Preserve source IDs, scope, input fingerprints, and unknowns at handoffs; do not turn an inference into a fact or a plan into an execution result.
- Link each conclusion to evidence and its status. `UNKNOWN`, `BLOCKED`, `STALE`, and missing evidence cannot roll up to PASS; reassess after evidence expires or inputs change.
- Separate analysis from external side effects. Writes, external publication, deletion, and final release approval require trusted human approval enforced by the Host.
- Validate the contract with repository checks first, then evaluate behavior with the target Agent and real project materials; record the two result types separately.

See the [complete PR Quality Review example](../../skills/en/testing-workflows/pr-quality-review/workflow.yaml) for stage dependencies and handoff fields. Chinese and English packages remain independently installable; this example link is for reading and is not a runtime dependency.

## `run-state.json` and recovery

The local CLI can persist `NOT_STARTED`, `RUNNING`, `COMPLETED`, `FAILED`, `BLOCKED`, or `STALE`. A checkpoint links the Workflow version and package fingerprint, input fingerprint, Commit SHA, stage state, evidence/artifact references, and idempotency keys. Before resuming, compare these values; any change marks the checkpoint `STALE` and requires re-evaluation. Duplicate stage starts are rejected. An interrupted stage becomes `BLOCKED` for review and is never replayed automatically. Repository writes, external writes, publishing, deletion, and final release approval require trusted explicit authorization from the host.

State transitions:

```text
NOT_STARTED → RUNNING → COMPLETED | FAILED | BLOCKED
Interrupted resume: RUNNING → BLOCKED (inspect side effects; no automatic replay)
Any non-terminal state → STALE (when input, Commit SHA, or Workflow package fingerprint changes)
```

Schema validation proves only that the record matches the contract. It does not prove a host persisted state, resumed execution, or ran a stage.

See [`WORKFLOW_STATE_RUNTIME_EN.md`](./WORKFLOW_STATE_RUNTIME_EN.md) for local state CLI commands, recovery limits, and approval-record examples.

## Validation

```bash
python3 scripts/validate_workflow_contracts.py --repo-root . --report /tmp/workflow-contract-report.json
python3 -m unittest scripts.tests.test_validate_workflow_contracts -v
```

`PASS` in this report means the contracts and examples validated. Skill-up `validate`/`run` are a separate layer: the former checks Eval configuration, while the latter executes model cases. Keep those evidence types separate.
