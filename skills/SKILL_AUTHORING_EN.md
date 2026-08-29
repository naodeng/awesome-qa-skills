<div align="right"><a href="./SKILL_AUTHORING.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Skill Authoring Guide

This guide adapts skill-up and Agent Skills practices to this QA Skill repository. Skills must be measurable, reproducible, independently installable, and evolvable.

## Quality Goals

1. **Accurate triggering:** `description` loads the Skill for the right user intent.
2. **Efficient context:** `SKILL.md` contains only recurring constraints; depth loads on demand.
3. **Stable output:** the primary prompt defines minimum coverage, output order, and quality gates.
4. **Evaluability:** every Skill maintains skill-up regression cases.

## `SKILL.md`

Minimum frontmatter:

```yaml
---
name: skill-name
description: Use this skill when ...; triggers include 中文触发词 and English triggers.
---
```

- `name` uses lowercase letters, digits, and hyphens and matches the directory and `agents/openai.yaml` key.
- `description` uses `Use this skill when...`, states what and when, includes trigger phrases, and stays below 1024 characters.
- Write for user intent rather than internal implementation.
- Test neighboring negative intents so descriptions do not over-trigger.

Recommended body:

1. When to use
2. Execution flow
3. Core constraints
4. Progressive disclosure
5. Pre-delivery checklist
6. Domain-specific pitfalls

Keep `SKILL.md` under roughly 500 lines and usually much shorter.

## Relationship to `prompts/`

- `prompts/` remains the complete execution specification.
- `SKILL.md` summarizes the recurring constraints and says exactly when to load prompts, references, examples, scripts, or format guidance.
- Move long examples, troubleshooting, and deep rules to progressive-disclosure files.
- Do not make `SKILL.md` an empty pointer to the prompt.

## Evaluations

Required structure:

```text
<skill>/
  SKILL.md
  prompts/
  evals/
    eval.yaml
    cases/
      basic-success.yaml
      edge-incomplete-input.yaml
      edge-risk-priority.yaml
```

- Start with three realistic cases: success, incomplete context, and scope/risk boundary.
- Prefer rule-based judges for stable structure assertions.
- Use script judges for executable artifacts and agent judges sparingly for semantic grading.
- Match the case language to the Skill language.
- Do not weaken reasonable assertions merely to pass the eval.
- Quote YAML titles containing colons.
- Incomplete-input cases should assert assumptions and open questions without becoming brittle about synonyms.

Scaffold and validate:

```bash
python3 scripts/scaffold_skill_evals.py --skill skills/en/testing-types/functional-testing
bash scripts/validate_skill_evals.sh
bash scripts/run_skill_eval.sh skills/en/testing-types/functional-testing/evals/eval.yaml \
  --include-case-name "basic-success"
```

Always write eval artifacts outside the Skill package, under `.skill-up-workspaces/`.

## Metadata

Every Skill includes `agents/openai.yaml`:

```yaml
version: 1
metadata:
  key: "skill-name"
interface:
  display_name: "..."
  short_description: "..."
  default_prompt: "Use the skill-name skill ..."
policy:
  allow_implicit_invocation: true
```

The metadata key, frontmatter name, and directory must match.

## Prohibited Patterns

- Real tokens, passwords, cookies, private keys, or personal data in examples.
- Markdown links from one Skill package to another Skill's internal files.
- Unnecessary copies of shared resources in many packages.
- Removing meaningful eval assertions to make tests green.
- Inventing APIs, fields, versions, metrics, evidence, or execution results.

## Completion

Run:

```bash
bash scripts/check_skills_quality.sh
```

The full gate validates directories, metadata, independence, integrity, snapshot hygiene, eval YAML, and bilingual documentation.
