<div align="right"><a href="./SKILL_EVALUATION_PILOTS.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# Skill Evaluation Dual Pilot

This record binds the analysis and executable pilots to existing Skills; it does not create a second global case repository.

## Analysis Pilot

- Skill: `requirements-analysis`
- Focus: trigger behavior, requirement gaps, risk relevance, assumption control, and an `agent_judge` rubric.
- Existing configuration: `skills/{zh,en}/testing-types/requirements-analysis/evals/eval.yaml`.
- Minimum coverage: success, incomplete information, and risk priority; neighbor boundaries are recorded separately through adjacent Skills such as `testability-analysis`.
- Judge configuration: `edge-semantic-agent-judge` uses `agent_judge`; the basic cases retain `rule_based` checks.
- Current evidence: structure and `skill-up validate` are executable; real-model replay, judge calibration, and semantic effectiveness are `NOT_RUN`.

## Executable Pilot

- Skill: `ui-test-playwright`
- Focus: test-artifact structure, script executability, JavaScript syntax, test declaration discovery, and a `script` judge; browser/runtime smoke remains a separate layer.
- Existing configuration: `skills/{zh,en}/testing-types/ui-test-playwright/evals/eval.yaml`, with benchmark configuration enabled.
- Judge configuration: `basic-script-artifact` uses a `script` judge to extract a JavaScript code block, validate its syntax, and check Playwright test, navigation, and assertion declarations.
- Current evidence: configuration, artifact extraction, syntax, and declaration checks are verifiable; without an authorized target application and real model run, browser/runtime execution and benchmark results are `NOT_RUN`.

## Reproducible validation commands

```bash
skill-up validate skills/zh/testing-types/requirements-analysis/evals/eval.yaml
skill-up validate skills/en/testing-types/requirements-analysis/evals/eval.yaml
skill-up validate skills/zh/testing-types/ui-test-playwright/evals/eval.yaml
skill-up validate skills/en/testing-types/ui-test-playwright/evals/eval.yaml
```

When runtime evidence is requested, record run metadata, traces, judge type, target, limitations, and failure classification; `skill-up validate` is not a substitute for execution.
