---
name: security-requirement-review
description: Use this skill when you need evidence-bounded security-requirement-review analysis and validation preparation; triggers include 安全需求审查 and security-requirement-review.
license: PolyForm-Noncommercial-1.0.0
metadata:
  version: "1.0.0"
  compatibility: ""
  author: "Awesome QA Skills contributors"
  language: "en"
  category: "testing-types"
  source: "https://github.com/naodeng/awesome-qa-skills"
  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"
---

# Security-Requirement Review

## When to Use

- Use this Skill when the work needs evidence-bounded analysis of security objectives, testability, trace links, acceptance conditions, and evidence gaps.
- Use it when input is incomplete but a reviewable draft with assumptions and gaps is still useful.
- Use it when static security evidence must remain separate from planned validation and completed execution.

## Output Format Options

- Default to Markdown organized by security risk, evidence, and priority.
- If the user asks for a table, CSV, JSON, or ticket format, preserve the same finding fields and evidence states.
- Confirm the schema, enum values, and required fields before feeding the output to automation.

## How to Use

1. Read prompts/security-requirement-review.md and follow its input audit, coverage checklist, and output contract.
2. Extract scope, environment, version, roles, data, dependencies, constraints, and available evidence.
3. Model security objectives, testability, trace links, acceptance conditions, and evidence gaps with reviewable scenarios, separating known facts, inferences, and candidate validation.
4. Record impact, priority, owner role, close condition, and validation method for each item.
5. With incomplete input, deliver a bounded draft; do not turn a risk assumption into a confirmed vulnerability or security pass.

## Reference Files

- Read prompts/security-requirement-review.md for every invocation.
- Read evals/eval.yaml and matching evals/cases/ when evaluating the Skill.
- Read references/, examples/, scripts/, or output-formats.md only when the directory exists and the task needs it.

## Domain Execution Essentials

- Map asset→threat actor/path→security obligation→control→verifiable acceptance, retaining scope, sources and project-supplied standard/version; do not select an unsupplied compliance baseline.
- Deliver obligation/acceptance/evidence mappings and testability gaps; drafted requirements remain proposals rather than approved obligations.
- When deriving domain candidates, read and follow [prompts/security-requirement-review.md](prompts/security-requirement-review.md) for the domain procedure and oracle; retain valid controls, evidence gaps, and validation actions for each item.

## Core Constraints

- Analyze only security objectives, testability, trace links, acceptance conditions, and evidence gaps; do not log in, call real APIs, or read credentials.
- Do not invent vulnerabilities, exploit success, remediation completion, scan coverage, or security-pass claims.
- Mark unsupported evidence as pending, blocked, or unassessed and provide an isolated validation method.
- Leave risk acceptance, exception authorization, and release judgment to a Human.

## Delivery Self-Check

- [ ] Complete the known, missing, conflicting, stale, out_of_scope, and assumptions audit.
- [ ] Cover the security requirement, triggers, expected concerns, and evidence state.
- [ ] Separate facts, inferences, recommendations, gaps, and Human decisions.
- [ ] Do not turn static findings or a dry-run into a real exploit, absence-of-vulnerability, or release-approval claim.

## Common Pitfalls

- Treating broad security review or API contract checking as a complete substitute for Security-Requirement Review.
- Listing attack names without applicability, evidence, expected results, or close conditions.
- Declaring a system secure with incomplete input, or reading real credentials for completeness.

## Best Practices

- Start with high-impact, hard-to-detect, permission-sensitive, or data-sensitive paths.
- Use redacted material, least privilege, isolated environments, and reversible validation suggestions.
- Make each security conclusion reviewable by another engineer from its source and boundary.
