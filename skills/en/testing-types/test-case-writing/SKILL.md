---
name: test-case-writing
description: Use this skill when you need to create high-quality test cases with normal, exception, and boundary scenarios; triggers include test case writing and test design.
---

# Test Case Writing (English)

**Chinese version：** See the corresponding Chinese skill.

## When to Use

- Need help with test case writing in a real project context.
- Need an output that can be used directly for execution, review, or follow-up.
- Need to merge scenario candidates from several roles into one traceable test suite without role-based duplication.

## Workflow

1. Read and follow the main prompt listed under Progressive disclosure (coverage, structure, quality bar).
2. Add only project context that changes the result: scope, environment, constraints, risks, dependencies, expected deliverable, and optional role scenario candidates with `source_role`.
3. Identify equivalent candidates by requirement trace, trigger, action, and observable outcome before generating one unified suite.
4. If input is incomplete, return a usable first draft and explicitly mark assumptions and gaps.
5. Default to Markdown; switch formats only when the user asks.

## Core Constraints

- Prioritize by risk / business impact — do not treat everything equally.
- Separate confirmed facts from current assumptions.
- Do not invent endpoints, fields, environments, or root causes the user did not provide.
- Keep output executable: concrete scenarios, clear priority, clear next steps.
- Do not generate suites per role. Equivalent candidates become one case that lists every contributing `source_role`, requirement/acceptance trace, and risk tag.
- Split cases only when differences in trigger, execution method, or observable outcome materially change execution; wording differences never justify duplicates.

## Routing Boundary with the Plus Skill

- This Skill remains the lightweight/default authoring path. It can consume already-formed role scenario candidates and unify them with source and requirement traceability.
- Choose `testcase-writer-plus` when the task requires conflict and provenance reconciliation across heterogeneous sources, a formal traceability matrix as a standalone deliverable, or higher coverage gates such as positive+negative+boundary coverage for high-risk paths plus data setup and cleanup. Do not switch merely for the base case fields or `Trace` already required here. Keep the two Skills independent; do not merge or rename them.

## Progressive Disclosure

- Before producing output, read and follow `prompts/test-case-writing.md` (minimum coverage, output structure, quality bar).
- When Excel/CSV/JSON/Word is requested: read `output-formats.md` and honor the format.
- When a ready-made template fits: use matching files under `output-templates/`.
- For deep framework/troubleshoot/schema notes: read only the relevant file(s) under `references/`, do not load the whole directory.
- For format conversion or helper checks: prefer existing `scripts/` over reinventing.
- For evaluating/regressing this skill: use `evals/` with skill-up.

## Pre-delivery Checklist

- [ ] Followed the main prompt's output structure
- [ ] Minimum coverage focus: scope, case priority, preconditions, test data, steps, expected results, positive scenarios, negative scenarios, `source_role`, and requirement traceability ... (details in main prompt)
- [ ] Produced one unified suite; merged equivalent role candidates while retaining every contributing role
- [ ] Covered the minimum checklist, or explained omissions
- [ ] High-risk items have explicit priority
- [ ] Did not invent details the user did not provide
- [ ] Assumptions and gaps are marked

## Common Pitfalls

- Do not pretend completeness when scope/context is missing.
- Do not treat every item as equally important.
- Do not skip assumptions and information gaps.
- Do not copy the same scenario into Product, QA, UI/UX, or Technical suites, and do not drop minority sources during a merge.
- Do not dump generic theory unrelated to the current toolchain.
