---
name: ai-assisted-testing
description: Use this skill when you want AI to draft, analyze, review, or prioritize ordinary QA work under human verification; triggers include AI-assisted testing and AI for QA.
license: PolyForm-Noncommercial-1.0.0
metadata:
  version: "2.0.0"
  compatibility: ""
  author: "Awesome QA Skills contributors"
  language: "en"
  category: "testing-types"
  source: "https://github.com/naodeng/awesome-qa-skills"
  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"
---

# AI-Assisted Testing

**Chinese version:** See the corresponding Chinese skill.

## When to Use

- Use AI to assist with requirements analysis, test design, data preparation, script drafts, defect summaries, or test reports.
- Separate AI drafts, human adoption, and real execution evidence while recording effort and quality outcomes.
- For testing an AI product itself, use the matching AI Native QA Skill.

## Workflow

1. Read `prompts/ai-assisted-testing.md` and identify the task, scope, risks, permitted data use, and deliverable.
2. Use the delegation matrix to state what AI may draft, what a human must decide, and which evidence is required.
3. Record the source snapshot, model and instruction versions, draft, review, adoption, and execution evidence for each AI artifact; mark missing values `UNKNOWN`.
4. Compare manual baseline and full AI-assisted effort for the same scope, complexity, and time window. Report defects, rework, and false greens separately.
5. Keep unreviewed artifacts `DRAFT` and unexecuted results `NOT_RUN` or `BLOCKED`.

## Core Constraints

- A human must confirm the business oracle, assertion validity, privacy, high-risk tradeoffs, and release acceptance. AI cannot make these decisions.
- For release approval, report `release_gate_status` and `human_release_decision`; until a human accepts the evidence, keep the decision `PENDING` and the gate below `PASS`. For productivity claims, report `productivity_claim_status`.
- `review_decision` uses only `ACCEPTED`, `DRAFT`, or `REJECTED`; execution state uses only `PASS`, `FAIL`, `BLOCKED`, `NOT_RUN`, `UNKNOWN`, or `STALE`.
- Without `model_version` or `run_id`, an AI-effect claim is `UNKNOWN`; without execution evidence, never report a pass.
- Never remove or weaken failing checks to manufacture a green result. Coverage and generation speed do not prove defect detection or productivity gains.
- Do not invent endpoints, fields, test results, token costs, or a manual baseline; report version conflicts as gaps.

## Progressive Disclosure

- Before producing output, follow `prompts/ai-assisted-testing.md` for delegation, provenance, output contract, and human gates.
- For artifact-by-stage ownership, read [references/ai-delegation-matrix.md](references/ai-delegation-matrix.md).
- For false greens, unsupported productivity claims, or unreviewed adoption, read [references/false-confidence-catalog.md](references/false-confidence-catalog.md).
- For per-item decisions and cost calculations, read [references/domain-decision-example.md](references/domain-decision-example.md).
- To compare an existing project example, read only the relevant material under `examples/`.
- When Excel, CSV, JSON, or Word is requested, read `output-formats.md`; format-conversion scripts and templates remain optional tools.
- For format conversion or helper checks, use existing tools under `scripts/`; for the shortest onboarding path, read `quick-start.md`.
- Use `evals/` to evaluate this Skill. If behavior evaluation needs a model or credentials, mark it `NOT_RUN` until authorized.

## Pre-delivery Checklist

- [ ] Facts, assumptions, gaps, and recommendations are distinct
- [ ] AI drafts have `AIA-##` IDs, provenance, and review status
- [ ] Human gates and real execution evidence are explicit
- [ ] Cost covers baseline, generation, review, rework, acceptance, and token-cost accounting
- [ ] No draft, static analysis, or coverage figure is presented as executed or accepted

## Common Pitfalls

- Claiming productivity gains from generation time alone.
- Treating all-green tests as quality evidence without reviewing assertions.
- Marking an unreviewed draft as adopted.
- Using an AI summary in place of raw execution records or source evidence.
