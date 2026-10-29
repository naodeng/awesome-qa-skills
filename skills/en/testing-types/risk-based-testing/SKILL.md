---
name: risk-based-testing
description: Use this skill when you need to turn quality risks into prioritized test objectives, depth, methods, and scope tradeoffs; triggers include risk-based testing.
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

# Risk-Based Testing

Translate supplied quality risks, failure modes, and delivery constraints into evidence-backed test priority, level/method, depth, and scope tradeoffs. Produce `RBT-##` decisions. This is not a full test strategy; it does not replace risk analysis or regression selection, and it does not execute tests.

## When to Use

- Use it when business criticality, change surface, past defects, or failure modes must determine test order and depth.
- Use it when time, environment, or capacity is constrained and the tradeoffs between focus, sampling, and deferral must be explicit.
- Use it when risk evidence is incomplete but a bounded priority view with assumptions and triggers is useful.

Do not use it only to identify quality risks, write a complete test strategy, select an existing executable set, or announce release readiness.

## Output Format Options

- Use Markdown by default; when a table, CSV, or JSON is requested, preserve the same evidence, status, impact, owner, and validation fields.
- Do not present a structured format or static inventory as execution, pass, approval, or release evidence.

## How to Use

1. Read this Skill's primary prompt and provide the objective, scope, material, environment, and available evidence.
2. Follow the prompt's input audit and output contract; deliver a bounded first pass when information is incomplete.
3. Retain source, evidence status, impact, owner role, close condition, and validation method for every finding.

## Workflow

1. Read and follow `prompts/risk-based-testing.md`, starting with the six-part input audit.
2. Link risk source, failure mode, impact, likelihood/uncertainty, and detectability to a test objective.
3. Record priority, level/method, depth, scope tradeoff, and required evidence in `RBT-##` entries.
4. Define stop conditions, expansion triggers, residual risk, and Human decisions for constrained work.
5. Never turn unsupported numbers, risk grades, or test recommendations into facts or execution results.

## Domain Execution Essentials

1. Anchor qualitative risk in observable impact, exposure/occurrence evidence, detectability, and control gaps. Without a project numeric model do not invent score products; unknown likelihood remains uncertain.
2. Link each risk to objective, layer/platform, depth, data, minimum observable evidence, sourced duration, and residual risk. High risk needs falsifiable business assertions, not merely more cases.
3. Allocate the constrained window with mandatory protection/authority first. Expose deferrals, alternatives, owners, and Human risk acceptance; time shortage never automatically waives gates.
4. Retain benign/low-risk controls, selection reasons, and scope expansion triggers. Planned priority is no execution or risk-elimination evidence.

## Core Constraints

- `RBT-##` is a test-decision recommendation, not risk acceptance, a quality score, coverage proof, or release approval.
- Risk ratings need evidence and assumptions; without data, use qualitative levels and state uncertainty rather than pseudo-precise numbers.
- Do not generate a full test strategy or replace `quality-risk-analysis`, `test-strategy`, or regression-test selection.
- Do not select concrete existing test IDs, execute tests, or invent environments, thresholds, defects, or pass results.

## Reference Files

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- Always read `prompts/risk-based-testing.md` before producing an analysis.
- For regression, read `evals/eval.yaml` and its cases; configuration and recommendations do not prove that risks are controlled.
- For trigger checks, use `evals/trigger-prompts.csv` and `evals/local-rules.json`; missing selection trace is `BLOCKED`.

## Best Practices

- Prioritize high-impact gaps with a verifiable next action, using the smallest useful experiment or evidence request.
- Separate facts, evidence-backed inferences, recommendations, and Human decisions; never upgrade an assumption into a conclusion.

## Pre-delivery Check

- [ ] Recorded known facts, missing information, conflicts, stale information, out-of-scope items, and assumptions.
- [ ] Each `RBT-##` has risk source, test objective, level/method, depth, priority basis, and required evidence.
- [ ] Tradeoffs have impact, stop conditions, expansion triggers, and residual risk.
- [ ] Test recommendations, risk inference, execution evidence, and Human decisions are separate.
- [ ] A limited scope is not presented as full coverage, zero risk, or release approval.

## Common Pitfalls

- Listing risks without saying how they change test priority and depth.
- Using a risk score instead of evidence and tradeoff rationale.
- Turning a full strategy, regression set, or execution result into this Skill.
- Silently dropping a high-risk area under time pressure without an expansion trigger or residual-risk statement.
