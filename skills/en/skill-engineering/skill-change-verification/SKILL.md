---
name: skill-change-verification
description: Use this skill when selecting and reporting verification for Skill changes; triggers include Skill change verification, quality gates, and evidence levels.
license: PolyForm-Noncommercial-1.0.0
metadata:
  version: "1.0.0"
  compatibility: ""
  author: "Awesome QA Skills contributors"
  language: "en"
  category: "skill-engineering"
  source: "https://github.com/naodeng/awesome-qa-skills"
  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"
---

# Skill Change Verification

Use this Skill to select the smallest sufficient checks for a change and state exactly what the evidence supports.

## Workflow

1. Classify content, metadata/directory, script, Eval, and runtime impact.
2. Select static, structural, evaluation, runtime, and human-review evidence.
3. Record commands run, results, omitted checks, and reasons.
4. Report residual risks and claims that are and are not supported.

## Constraints

- `skill-up validate` is not runtime semantic validation.
- Mark undiscoverable commands as confirmation items; never guess.
- Cover the actual diff instead of hiding gaps behind a full-suite run.

Read `prompts/skill-change-verification.md` before producing a report.
