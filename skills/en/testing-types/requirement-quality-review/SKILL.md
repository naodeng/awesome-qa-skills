---
name: requirement-quality-review
description: Use this skill when a requirement, acceptance-criteria set, or change brief needs an evidence-bounded quality review before design or testing; triggers include requirement quality review, requirements quality gate, and requirement completeness review.
---

# Requirement Quality Review

Review requirement completeness, clarity, verifiability, feasibility, scope, and evidence quality from a QA and delivery perspective. Produce traceable gaps, risks, and next actions; this is a quality overview and routing entry point, not a release approval or numeric scorer.

## When to Use

- Before test design, technical design, or planning when requirement quality is uncertain.
- When acceptance criteria look complete but exception paths, constraints, actors, or decision conditions may be missing.
- When a requirement needs routing to ambiguity, consistency, conflict, or traceability analysis.

Do not use it to write test cases, execute tests, approve a release, or assign a quality score from unsupported material.

## Output Format Options

- Use Markdown by default; when a table, CSV, or JSON is requested, preserve the same evidence, status, impact, owner, and validation fields.
- Do not present a structured format or static inventory as execution, pass, approval, or release evidence.

## How to Use

1. Read this Skill's primary prompt and provide the objective, scope, material, environment, and available evidence.
2. Follow the prompt's input audit and output contract; deliver a bounded first pass when information is incomplete.
3. Retain source, evidence status, impact, owner role, close condition, and validation method for every finding.

## Workflow

1. Read and follow `prompts/requirement-quality-review.md`; it defines the audit, quality dimensions, and output order.
2. Inventory supplied requirements, stories, acceptance criteria, change notes, constraints, versions, and evidence. Separate known, missing, conflicting, stale, and out-of-scope information.
3. Rank findings by delivery, quality, and testability impact. Retain source, evidence, status, priority, owner role, and a closeable next action for each finding.
4. Suggest specialist routing by Skill name only. Do not read or link another Skill's internal files and do not turn routing into an installation dependency.
5. With incomplete input, return a minimum usable draft and 3–5 high-value open questions. State a blocker when a safe judgment is impossible.

## Core Constraints

- Keep direct source facts, evidence-backed inferences, recommendations, and Human decisions separate.
- Do not invent business rules, fields, endpoints, thresholds, SLAs, environments, owners, root causes, execution results, or approvals.
- Do not output a universal numeric quality score or infer Go/No-Go from one requirement.
- Use `RQ-##` finding IDs and distinguish `missing`, `ambiguous`, `untestable`, `conflict`, and `unassessed`.
- Every P0/P1 finding needs impact, a suggested owner role, a decision question, and a validation method.

## Reference Files

- Always read `prompts/requirement-quality-review.md` before producing an assessment.
- Use `evals/eval.yaml` and `evals/cases/` to regress this Skill; Eval files constrain structure and behavior but do not prove runtime quality.
- To check discovery behavior, run `scripts/run_skill_trace_eval.py` with `evals/trigger-prompts.csv` and `evals/local-rules.json`; missing `skill.selection` evidence is `BLOCKED`, not a trigger pass.
- This is a repository-root development check; a standalone Skill package does not include the repository runner and does not depend on it at runtime.

## Best Practices

- Prioritize high-impact gaps with a verifiable next action, using the smallest useful experiment or evidence request.
- Separate facts, evidence-backed inferences, recommendations, and Human decisions; never upgrade an assumption into a conclusion.

## Pre-delivery Checklist

- [ ] Scope, known facts, missing information, conflicts/staleness, and assumptions are explicit
- [ ] Completeness, clarity, verifiability, feasibility, scope, and evidence quality are assessed separately
- [ ] Findings include source, status, impact, priority, question, owner role, action, and validation method
- [ ] Specialist suggestions, static checks, and document mappings are not presented as execution or approval evidence
- [ ] High-priority questions are assignable and closeable; unsupported areas remain `UNASSESSED`

## Common Pitfalls

- Treating “readable” as “verifiable.”
- Restating the requirement without identifying delivery or testing blockers.
- Filling in absent rules from common practice or hiding missing evidence behind a score.
- Making the final product, engineering, or release decision for a Human.
