---
name: requirement-ambiguity-analysis
description: Use this skill when requirement wording has unclear actors, references, scope, quantities, conditions, timing, states, or acceptance criteria; triggers include requirement ambiguity, unclear requirements, and ambiguity analysis.
---

# Requirement Ambiguity Analysis

Identify wording that cannot be uniquely understood or decided, preserve the statement and source, and explain which discriminator is missing and how a responsible role can close it. This diagnoses under-specification; it does not choose an interpretation.

## When to Use

- Requirement wording contains undefined terms such as “timely,” “fast,” “when necessary,” or “normal.”
- Actors, objects, scope, quantities, conditions, timing, states, or acceptance criteria have multiple plausible readings.
- You need to distinguish ordinary ambiguity from an explicit cross-source conflict.

Do not use it to make a final decision between mutually exclusive rules, execute tests, or fill in business rules from convention.

## Output Format Options

- Use Markdown by default; when a table, CSV, or JSON is requested, preserve the same evidence, status, impact, owner, and validation fields.
- Do not present a structured format or static inventory as execution, pass, approval, or release evidence.

## How to Use

1. Read this Skill's primary prompt and provide the objective, scope, material, environment, and available evidence.
2. Follow the prompt's input audit and output contract; deliver a bounded first pass when information is incomplete.
3. Retain source, evidence status, impact, owner role, close condition, and validation method for every finding.

## Workflow

1. Read and follow `prompts/requirement-ambiguity-analysis.md`.
2. Audit known, missing, conflicting, stale, out-of-scope, and assumed information.
3. Preserve each ambiguous statement, source, applicability, and missing discriminator. List possible readings without selecting one.
4. Rank delivery, quality, and testability impact; provide assignable, closeable questions and validation methods.
5. When material is explicitly mutually exclusive, mark it as conflict and suggest `requirement-conflict-detection` by Skill name only; do not link its internal files.

## Core Constraints

- Use `RA-##` finding IDs and distinguish `ambiguous`, `missing`, `untestable`, `conflict`, and `out_of_scope`.
- Do not fill in absent thresholds, actors, formats, time limits, states, or permissions from common practice.
- Retain source, statement, missing discriminator, possible readings, impact, priority, question, owner role, and validation method for each important finding.
- With incomplete input, return a minimum usable draft and explicitly list assumptions and 3–5 high-value questions.
- Do not decide the final interpretation for product, business, legal, or compliance roles.

## Reference Files

- Always read `prompts/requirement-ambiguity-analysis.md` before producing an analysis.
- Use `evals/eval.yaml` and `evals/cases/` to regress this Skill; structural or rule-based checks do not prove real-project effectiveness.
- To check discovery behavior, run `scripts/run_skill_trace_eval.py` with `evals/trigger-prompts.csv` and `evals/local-rules.json`; missing `skill.selection` evidence is `BLOCKED`, not a trigger pass.
- This is a repository-root development check; a standalone Skill package does not include the repository runner and does not depend on it at runtime.

## Best Practices

- Prioritize high-impact gaps with a verifiable next action, using the smallest useful experiment or evidence request.
- Separate facts, evidence-backed inferences, recommendations, and Human decisions; never upgrade an assumption into a conclusion.

## Pre-delivery Checklist

- [ ] The ambiguous phrase and source are quoted
- [ ] The missing decision discriminator is stated, not just “it is ambiguous”
- [ ] Possible readings and final decisions are separate
- [ ] P0/P1 items have owner role, close condition, and validation method
- [ ] Explicit conflicts are routed without silently choosing a side

## Common Pitfalls

- Treating industry convention as a requirement fact.
- Rewriting a sentence without explaining the impact of different readings.
- Combining rules from different versions or applicability scopes.
- Refusing to provide any useful draft because context is incomplete.
