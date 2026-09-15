---
name: session-security-testing
description: Use this skill when you need evidence-bounded session-security-testing analysis and validation preparation; triggers include 会话安全测试 and session-security-testing.
---

# Session-Security Testing

## When to Use

- Use this Skill when the work needs evidence-bounded analysis of session creation, fixation, expiry, revocation, concurrency, and cross-device boundaries.
- Use it when input is incomplete but a reviewable draft with assumptions and gaps is still useful.
- Use it when static security evidence must remain separate from planned validation and completed execution.

## Output Format Options

- Default to Markdown organized by security risk, evidence, and priority.
- If the user asks for a table, CSV, JSON, or ticket format, preserve the same finding fields and evidence states.
- Confirm the schema, enum values, and required fields before feeding the output to automation.

## How to Use

1. Read prompts/session-security-testing.md and follow its input audit, coverage checklist, and output contract.
2. Extract scope, environment, version, roles, data, dependencies, constraints, and available evidence.
3. Model session creation, fixation, expiry, revocation, concurrency, and cross-device boundaries with reviewable scenarios, separating known facts, inferences, and candidate validation.
4. Record impact, priority, owner role, close condition, and validation method for each item.
5. With incomplete input, deliver a bounded draft; do not turn a risk assumption into a confirmed vulnerability or security pass.

## Reference Files

- Read prompts/session-security-testing.md for every invocation.
- Read evals/eval.yaml and matching evals/cases/ when evaluating the Skill.
- Read references/, examples/, scripts/, or output-formats.md only when the directory exists and the task needs it.

## Core Constraints

- Analyze only session creation, fixation, expiry, revocation, concurrency, and cross-device boundaries; do not log in, call real APIs, or read credentials.
- Do not invent vulnerabilities, exploit success, remediation completion, scan coverage, or security-pass claims.
- Mark unsupported evidence as pending, blocked, or unassessed and provide an isolated validation method.
- Leave risk acceptance, exception authorization, and release judgment to a Human.

## Delivery Self-Check

- [ ] Complete the known, missing, conflicting, stale, out_of_scope, and assumptions audit.
- [ ] Cover the session security, triggers, expected concerns, and evidence state.
- [ ] Separate facts, inferences, recommendations, gaps, and Human decisions.
- [ ] Do not turn static findings or a dry-run into a real exploit, absence-of-vulnerability, or release-approval claim.

## Common Pitfalls

- Treating broad security review or API contract checking as a complete substitute for Session-Security Testing.
- Listing attack names without applicability, evidence, expected results, or close conditions.
- Declaring a system secure with incomplete input, or reading real credentials for completeness.

## Best Practices

- Start with high-impact, hard-to-detect, permission-sensitive, or data-sensitive paths.
- Use redacted material, least privilege, isolated environments, and reversible validation suggestions.
- Make each security conclusion reviewable by another engineer from its source and boundary.
