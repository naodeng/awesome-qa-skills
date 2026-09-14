---
name: database-design-quality-review
description: Use this skill when an ERD, DDL, ORM schema, or migration plan needs an evidence-bounded database design review before implementation; triggers include database design review, migration readiness review, and schema quality audit.
---

# Database Design Quality Review

Review ERDs, DDL, ORM schemas, data ownership, lifecycle, query constraints, transaction/concurrency, migration compatibility, and recovery design before implementation or migration. It produces `DB-##` findings and validation preparation; it does not connect to a real database or approve launch.

## When to Use

- Use it to check model integrity, constraints, indexes, lifecycle/privacy, and data ownership.
- Use it to identify transaction, concurrency, migration rollback, backup/recovery, and performance risks.
- Use it when DDL or migration material is incomplete but a bounded design review is needed.

Do not use it to execute migrations, connect to production, benchmark queries, or infer business rules from table names.

## Output Format Options

- Use Markdown by default; when a table, CSV, or JSON is requested, preserve the same evidence, status, impact, owner, and validation fields.
- Do not present a structured format or static inventory as execution, pass, approval, or release evidence.

## How to Use

1. Read this Skill's primary prompt and provide the objective, scope, material, environment, and available evidence.
2. Follow the prompt's input audit and output contract; deliver a bounded first pass when information is incomplete.
3. Retain source, evidence status, impact, owner role, close condition, and validation method for every finding.

## Workflow

1. Read `prompts/database-design-quality-review.md` and audit objective, version, database scope, and evidence.
2. Classify input as `known`, `missing`, `conflicting`, `stale`, `out_of_scope`, and `assumptions`.
3. Build coverage by object, constraints, indexes, transaction/concurrency, lifecycle, migration, and recovery; bind evidence to `DB-##` findings.
4. Separate facts, evidence-backed inferences, recommendations, and Human decisions with impact, owner, close condition, and validation.
5. Without execution identity, time, environment, and raw results, do not write that a database operation succeeded.

## Core Constraints

- Do not connect, write, migrate, or query a real database; do not run benchmarks or recovery drills.
- Do not infer business rules, thresholds, retention periods, or privacy classes from table or field names.
- Each `DB-##` includes object, source/evidence, constraints/indexes, transaction/concurrency, migration rollback, impact, owner, and validation method.
- All examples use redacted data; mark absent evidence `missing`, `unverified`, `unexecuted`, or `unassessed`.

## Reference Files

- Always read `prompts/database-design-quality-review.md` before producing a review.
- For regression, read `evals/eval.yaml` and its cases; static design checks do not prove database behavior.
- For trigger checks, use `evals/trigger-prompts.csv` and `evals/local-rules.json`; missing selection trace is `BLOCKED`.

## Best Practices

- Prioritize high-impact gaps with a verifiable next action, using the smallest useful experiment or evidence request.
- Separate facts, evidence-backed inferences, recommendations, and Human decisions; never upgrade an assumption into a conclusion.

## Delivery Checklist

- [ ] Audit objects, version, ownership, scope, and evidence.
- [ ] Cover model, constraints, indexes, lifecycle/privacy, transactions, concurrency, migrations, performance, recovery, and test readiness.
- [ ] Give every `DB-##` minimum evidence, impact, owner, action, and validation.
- [ ] Use redacted examples and do not connect to a real database.
- [ ] Do not present DDL presence or static checks as migration success or launch approval.

## Common Pitfalls

- Checking tables and fields without constraints, lifecycle, rollback, or recovery.
- Treating an index as proof that query performance was verified.
- Treating a parseable migration as backward compatibility and rollback proof.
