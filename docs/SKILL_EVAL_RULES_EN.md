# Local Skill Evaluation Rules

This repository includes a read-only local rule engine for JSONL traces produced by `codex exec --json` and artifacts produced by a Skill run. It never executes commands from a trace and never presents subjective model grading as deterministic evidence.

## Quick start

Capture a run with `codex exec --json`, then copy and adapt the [rule configuration example](examples/skill-eval.rules.json):

```bash
codex exec --json --approve-for-me \
  'Use the $setup-demo-app skill to create the project in this directory.' \
  > evals/artifacts/test-01.jsonl

python3 scripts/grade_skill_trace.py \
  --trace evals/artifacts/test-01.jsonl \
  --config /tmp/demo-skill.rules.json \
  --project-dir /tmp/setup-demo-app \
  --report evals/artifacts/test-01.rules.json
```

Prepare the configuration with:

```bash
cp docs/examples/skill-eval.rules.json /tmp/demo-skill.rules.json
```

To run a batch from the article-style prompt set, preview the commands first:

```bash
python3 scripts/run_skill_trace_eval.py \
  --prompts docs/examples/skill-eval.prompts.csv \
  --config docs/examples/skill-eval.rules.json \
  --project-root /tmp/demo-skill-projects \
  --output-dir /tmp/demo-skill-reports
```

Only add `--run` after confirming the isolated directories and commands; add `--approve-for-me` only when the project really needs writes. The runner passes `--skip-git-repo-check` for its isolated non-Git case directories. Each case gets its own directory, and the trace, stderr, and rule report are persisted separately. Existing case directories are rejected rather than reused.

Exit codes are: `0` when no rule is failed or evidence-blocked, `1` when at least one rule is `FAIL`, and `2` when there are no failures but at least one rule is `BLOCKED`. `BLOCKED` is not a pass; it means the trace or environment cannot prove the assertion.

## Twenty local rules

| ID | Check | Required configuration or evidence |
| --- | --- | --- |
| `TRIGGER-001` | Explicit request selects the Skill | `trigger_mode=explicit` and `skill.selection` |
| `TRIGGER-002` | Implicit task selects the Skill | `trigger_mode=implicit` and `skill.selection` |
| `TRIGGER-003` | Domain-context task selects the Skill | `trigger_mode=contextual` and `skill.selection` |
| `TRIGGER-004` | Negative control does not select the Skill | `trigger_mode=negative` and `selected=false` |
| `TRACE-001` | Trace is non-empty and has no malformed lines | Valid JSONL |
| `TRACE-002` | Every line is a typed JSON object | JSONL stdout |
| `TRACE-003` | Commands have started/completed lifecycles | `require_command_lifecycle=true` |
| `PROCESS-001` | Required commands appear | `required_commands` |
| `PROCESS-002` | Commands appear in the expected order | `command_order` |
| `PROCESS-003` | Required commands exit with code 0 | `required_commands` + `exit_code` |
| `OUTCOME-001` | Definition-of-done artifacts exist and contain markers | `required_artifacts` |
| `OUTCOME-002` | Build command succeeds | `build_command` |
| `ARTIFACT-001` | Exact file structure, forbidden paths, and content match | `expected_files` / `forbidden_files` / `content_checks` |
| `ARTIFACT-002` | Artifacts are persisted on disk | `persisted_paths` |
| `ENV-001` | Working-directory and path assumptions hold | `eval.environment` + `environment` |
| `ENV-002` | Local tools are available | `required_tools` |
| `RUNTIME-001` | Runtime smoke command succeeds | `smoke_command` |
| `SAFETY-001` | Command, repetition, token, and git-cleanliness limits hold | Limits or `clean_repo` |
| `PERMISSION-001` | No escalation or forbidden command occurs | `permissions` / `forbidden_commands` |
| `REPRO-001` | Comparison run has the same command behavior | `compare_trace` |

A non-trigger rule runs only when its corresponding assertion is configured. Unconfigured rules are reported as `N/A` and must not be interpreted as passes. A missing or invalid `trigger_mode` is reported as `BLOCKED` rather than being silently skipped.

## Configuration example

```json
{
  "skill": "setup-demo-app",
  "trigger_mode": "explicit",
  "should_trigger": true,
  "required_commands": ["npm install", "npm run build"],
  "command_order": ["npm install", "npm run build"],
  "required_artifacts": [
    {"path": "package.json", "contains": "demo-app"}
  ],
  "build_command": "npm run build",
  "smoke_command": "curl -fsS http://127.0.0.1:5173/",
  "expected_files": [
    "package.json",
    "src/components/Header.tsx",
    "src/components/Card.tsx"
  ],
  "content_checks": [
    {"path": "src/index.css", "contains": "tailwindcss"}
  ],
  "required_tools": ["node", "npm", "curl"],
  "max_commands": 20,
  "max_repeated_commands": 2,
  "max_total_tokens": 100000,
  "forbidden_commands": ["git reset --hard", "rm -rf /"],
  "permissions": {"max_escalations": 0},
  "require_command_lifecycle": true
}
```

Trigger rules require the eval adapter to write `skill.selection` evidence with a boolean selection field into the trace. The article documents `command_execution` events for command and artifact checks, but does not guarantee a Skill-selection event. When the selection event is missing or its `selected`/`invoked`/`triggered` field is invalid, the rule reports `BLOCKED` rather than inferring that the Skill was not triggered.

## Boundaries

The article also recommends a second read-only `codex exec --output-schema` run for style and convention grading. This local engine only checks whether that result can be parsed; semantic judgments about component style or layout should be labeled `MODEL_ASSESSMENT` and kept outside the twenty deterministic rules above.

Keep the rule configuration small and focused. The prompt set should cover explicit, implicit, contextual, and negative-control cases and grow from real failures; that is test-data governance and is not replaced by scoring one trace.

## Evidence package and regression cases

`scripts/run_skill_trace_eval.py` records `run_metadata` in the batch and each case result: `run_id`, `case_id`, Skill commit/content identity, Eval input hash, `skill-up` version, engine/provider/model, judge, and environment. A dirty Skill includes a content hash; unavailable tools or values are recorded as `unknown` and never guessed.

Each case also records an `evidence_state`: `PASS`, `FAIL`, `BLOCKED`, or dry-run `NOT_RUN`, plus an optional `failure_classification`: `SKILL_DEFECT`, `EVAL_DEFECT`, `INFRASTRUCTURE_DEFECT`, or `UNKNOWN`. A malformed trace is `FAIL`, not infrastructure-blocked; infrastructure blocking is reserved for runs with no trace evidence.

After a human confirms the root cause of a real failure, `scripts/add_skill_eval_regression_case.py` can create a `REGRESSION` candidate under the selected Skill's `evals/cases/` and register it in that Skill's `evals/eval.yaml`. The candidate lifecycle is `CANDIDATE` while its evidence state remains `NOT_RUN`; the script rejects unsafe IDs and existing files, does not edit `SKILL.md`, and does not promote a candidate into a stable gate automatically.

Version regression comparison uses `scripts/compare_skill_eval_runs.py previous.json current.json`. It compares existing reports only, checks comparability across Eval, variant, engine, model, judge, environment, and an ordered timezone-aware time window, and reports previous `PASS` to current `FAIL` as `REGRESSION_OBSERVED` only when the current case is explicitly classified as `SKILL_DEFECT`. `EVAL_DEFECT`, `INFRASTRUCTURE_DEFECT`, `UNKNOWN`, or missing classifications remain `INCONCLUSIVE`; missing comparable evidence remains `INSUFFICIENT_EVIDENCE`.

These fields complement the twenty local rules without changing their deterministic semantics. Evaluation states and claim boundaries are governed by [`SKILL_EVALUATION_CONTRACT_EN.md`](governance/SKILL_EVALUATION_CONTRACT_EN.md).
