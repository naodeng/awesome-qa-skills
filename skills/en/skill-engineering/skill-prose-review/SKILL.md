---
name: skill-prose-review
description: Use this skill when reviewing the contract completeness of Skills, Prompts, metadata, or QA documentation; triggers include Skill prose review, Prompt review, and contract audit.
---

# Skill Prose Contract Review

## When to use

- Review a Skill, Prompt, metadata, example, or output format.
- Check whether prose is executable, independently installable, and verifiable.

## Workflow

1. Confirm scope and document role.
2. Trace trigger → input → rules → output → constraints → verification.
3. Report blockers, important suggestions, location, impact, and evidence.
4. List missing information and unverified claims.

## Constraints

- Do not invent behavior, tools, or facts.
- Do not report static reading as runtime validation.
- Do not rewrite files unless explicitly requested.

## On-demand loading

- Read `prompts/skill-prose-review.md` before producing the review.
- Use `evals/` for evaluation and report static and runtime evidence separately.

## Final checklist

- [ ] Scope and document role are explicit
- [ ] Input, output, constraints, and verification are covered
- [ ] Gaps and evidence levels are stated
- [ ] No unauthorized file changes
