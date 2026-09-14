# Local Skill Evaluation Rules

This repository includes a read-only local rule engine for JSONL traces produced by `codex exec --json` and artifacts produced by a Skill run. It never executes commands from a trace and never presents subjective model grading as deterministic evidence.

## Quick start

Capture a run with `codex exec --json`, then copy and adapt the [rule configuration example](examples/skill-eval.rules.json):

```bash
codex exec --json --full-auto \
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

Only add `--run` after confirming the isolated directories and commands; add `--full-auto` only when the project really needs writes. Each case gets its own directory, and the trace, stderr, and rule report are persisted separately. Existing case directories are rejected rather than reused.

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

A rule runs only when its corresponding assertion is configured. Unconfigured rules are reported as `N/A` and must not be interpreted as passes.

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

Trigger rules require the eval adapter to write selection evidence into the trace. The article documents `command_execution` events for command and artifact checks, but does not guarantee a Skill-selection event. When `skill.selection` is missing, the rule reports `BLOCKED` rather than inferring that the Skill was not triggered.

## Boundaries

The article also recommends a second read-only `codex exec --output-schema` run for style and convention grading. This local engine only checks whether that result can be parsed; semantic judgments about component style or layout should be labeled `MODEL_ASSESSMENT` and kept outside the twenty deterministic rules above.

Keep the rule configuration small and focused. The prompt set should cover explicit, implicit, contextual, and negative-control cases and grow from real failures; that is test-data governance and is not replaced by scoring one trace.
