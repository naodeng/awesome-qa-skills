---
name: skill-quality-review
description: Use this skill when reviewing a complete Skill package for architecture, scope, triggers, independent installation, bilingual consistency, Eval readiness, and evidence boundaries; triggers include Skill quality review and package review.
---

# Skill Quality Review

## When to use

- Review a Skill at package level rather than only polishing prose.
- Check whether `SKILL.md`, the primary Prompt, metadata, examples, references, and `evals/` form one consistent contract.
- Assess whether a Skill can be copied or installed independently and which conclusions still lack runtime evidence.

## Workflow

1. Confirm the Skill, language, directory, and review goal; list information gaps before reviewing absent files.
2. Check architecture responsibility, scope/non-goals, triggers, input audit, output contract, progressive disclosure, and neighbor boundaries.
3. Check path, name, and semantic consistency across `SKILL.md`, the primary Prompt, `agents/openai.yaml`, examples/references, and `evals/`.
4. Check independent installation: relative resources still resolve when only this Skill directory is copied, with no hard dependency on another Skill's private files.
5. Report blocking issues, important suggestions, information gaps, and evidence boundaries; separate static findings from runtime/model conclusions.

## Constraints

- This is a static package review. Do not execute the business task or silently modify the Skill.
- Directory completeness, `skill-up validate`, CLI install smoke, and Project status cannot prove runtime behavior, model effectiveness, business acceptance, Quality Score, or release approval.
- Do not invent environments, dependencies, metrics, trigger observations, or execution facts. Use `UNASSESSED`, `NOT_RUN`, `BLOCKED`, or `INSUFFICIENT_EVIDENCE` when evidence is absent.
- Do not create a second Eval Engine, Judge, Benchmark, or Quality Score.

## Progressive disclosure

- Read `prompts/skill-quality-review.md` before producing the report; it is the output contract.
- Read the target Skill's `evals/` when behavior coverage matters, but do not call configuration validation runtime evidence.
- Read repository Evaluation Contract and local trace rules for deeper evidence when available. If a copied Skill does not contain them, preserve the limitation instead of creating filesystem coupling.

## Pre-delivery checklist

- [ ] Scope, document roles, and input gaps are explicit
- [ ] Triggers, inputs, outputs, constraints, independent installation, and Eval readiness were checked
- [ ] Blocking issues, suggestions, unassessed items, and evidence levels are traceable
- [ ] Static checks are not presented as runtime/model evidence
