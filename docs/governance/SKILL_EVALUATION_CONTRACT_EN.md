<div align="right"><a href="./SKILL_EVALUATION_CONTRACT.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# Skill Evaluation Contract

This contract defines what evaluation results prove so that static checks, model behavior, and release conclusions are not conflated.

## Evidence states

| State | Meaning | Supported claim |
| --- | --- | --- |
| `PASS` | The configured assertion has evidence and passed | The assertion passed in this run |
| `FAIL` | Evidence exists and the assertion failed | Record the failure; do not auto-attribute it to the Skill |
| `BLOCKED` | Required trace, tool, permission, or environment evidence is missing | No conclusion for that assertion |
| `NOT_RUN` | This evaluation layer was not executed | Do not claim it was verified |
| `NOT_SCORED` | No valid Quality Score evidence exists | Do not claim a score |
| `UNASSESSED` | The dimension is outside the current assessment | Keep it unassessed |
| `INSUFFICIENT_EVIDENCE` | Execution evidence exists but cannot support a strong conclusion | Report only a limited conclusion |

`BLOCKED`, `NOT_RUN`, `UNASSESSED`, and `INSUFFICIENT_EVIDENCE` are not passes.

## Evidence levels

1. `Static`: files, frontmatter, format, and local scripts.
2. `Structural`: bilingual parity, independent installation, indexes, and Eval shape.
3. `Evaluation`: `skill-up validate` or an actual `skill-up run`.
4. `Runtime`: real Skill, tools, target, and artifact execution.
5. `Human review`: semantics, terminology, risk, and judge calibration.

Lower-level evidence cannot be promoted automatically to a higher-level claim. For example, `skill-up validate` is not runtime semantic validation, and Project `Done` is not release approval.

## Run metadata

Meaningful runs record at least:

```text
run_id, case_id, variant, skill_version, eval_version,
skill_up_version, engine, provider, requested_model, observed_model,
judge_type, judge_model, environment, timestamp
```

Unknown values are written as `unknown`, never guessed. Reports retain the Eval definition, case results, traces, judge results, artifact paths, limitations, and failure classification; unnecessary secrets are not copied.

## Failure classification

| Classification | Typical evidence | Action |
| --- | --- | --- |
| `SKILL_DEFECT` | Input, contract, and environment are valid but Skill behavior violates the requirement | Fix the Skill and rerun affected cases |
| `EVAL_DEFECT` | Prompt, expectation, judge, or fixture does not match the contract | Fix the Eval; do not blame the Skill |
| `INFRASTRUCTURE_DEFECT` | Runner, provider, permission, dependency, or target environment failed | Fix the environment or mark blocked |
| `UNKNOWN` | Evidence cannot support reliable attribution | Keep the limitation; do not force a diagnosis |

The local runner can record a classification but never guesses attribution from one failure.

## Judge contract

Choose `rule_based` for deterministic assertions, `script` for executable artifacts, and `agent_judge` only when semantic judgment is required. Before an Agent Judge becomes governance-critical, calibrate it with known-good, known-bad, and borderline examples and record variance.

## Trigger and regression

Expected selection belongs to the case; observed selection requires a `skill.selection` trace. Missing selection evidence is `BLOCKED`. A benchmark (with Skill vs without Skill) and a Version Regression (previous vs current) answer different questions and must not be merged.

A strong regression claim requires comparable Skill commit, Eval dataset, engine/model, judge, environment, and time window. A single semantic failure is an observation unless the contract explicitly permits a stronger claim.

## Standard report

```markdown
# Skill Evaluation Report
## Scope
## Run Metadata
## Configuration
## Evaluation Coverage
## Summary
## Case Results
## Trigger Evidence
## Process Evidence
## Outcome / Artifact Evidence
## Semantic Evidence
## Benchmark / Regression Findings
## Flaky / Blocked / Infrastructure Errors
## Eval Validity Findings
## Limitations
## Recommended Actions
```

Quality Score remains governed by [`QUALITY_SCORE_EVAL_CONTRACT_EN.md`](./QUALITY_SCORE_EVAL_CONTRACT_EN.md); this contract adds no scoring system.
