---
name: api-test-restassure
description: Use this skill when you need to parse multi-format API definitions and generate Rest Assured Java test classes; triggers include Rest Assured, RestAssured, and Java API automation.
---

# api-test-restassure (EN)

**Chinese version：** See the corresponding Chinese skill.

## When to Use

- Need API outputs that should land in REST Assured based automation.
- The project is Java-based or already uses REST Assured.

## Workflow

1. Read and follow the main prompt listed under Progressive disclosure (coverage, structure, quality bar).
2. Add only project context that changes the result: scope, environment, constraints, risks, dependencies, expected deliverable.
3. If input is incomplete, return a usable first draft and explicitly mark assumptions and gaps.
4. Default to Markdown; switch formats only when the user asks.

## Core Constraints

- Prioritize by risk / business impact — do not treat everything equally.
- Separate confirmed facts from current assumptions.
- Do not invent endpoints, fields, environments, or root causes the user did not provide.
- Use placeholders or env-var semantics for auth/secrets; never hardcode real credentials.
- Keep output executable: concrete scenarios, clear priority, clear next steps.

## Progressive Disclosure

- Before producing output, read and follow `prompts/api-test-restassure.md` (minimum coverage, output structure, quality bar).
- When a ready-made template fits: use matching files under `output-templates/`.
- When the user wants examples or alignment with existing assets: read relevant `examples/`.
- For deep framework/troubleshoot/schema notes: read only the relevant file(s) under `references/`, do not load the whole directory.
- For format conversion or helper checks: prefer existing `scripts/` over reinventing.
- For evaluating/regressing this skill: use `evals/` with skill-up.

## Pre-delivery Checklist

- [ ] Followed the main prompt's output structure
- [ ] Minimum coverage focus: suite structure, common setup, auth handling, priority endpoints, positive scenarios, negative and boundary scenarios, assertion focus, test data strategy, ... (details in main prompt)
- [ ] Covered the minimum checklist, or explained omissions
- [ ] High-risk items have explicit priority
- [ ] Did not invent details the user did not provide
- [ ] Assumptions and gaps are marked

## Common Pitfalls

- Do not pretend completeness when scope/context is missing.
- Do not treat every item as equally important.
- Do not skip assumptions and information gaps.
- Do not dump generic theory unrelated to the current toolchain.
