---
name: api-testing
description: Use this skill when you need to design API test plans or cases for REST, GraphQL, or gRPC interfaces; triggers include API testing and API test cases.
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

# API Testing (English)

**Chinese version：** See the corresponding Chinese skill.

## When to Use

- Need an API test plan, API cases, or API risk analysis.
- The request involves REST, GraphQL, SOAP, gRPC, WebSocket, or mixed API behavior.

## Workflow

1. Read and follow the main prompt listed under Progressive disclosure (coverage, structure, quality bar).
2. Add only project context that changes the result: scope, environment, constraints, risks, dependencies, expected deliverable.
3. If input is incomplete, return a usable first draft and explicitly mark assumptions and gaps.
4. Default to Markdown; switch formats only when the user asks.

## Domain Execution Essentials

1. Branch only for confirmed protocols: REST method/status/schema/idempotency; GraphQL data+errors/null/field permissions; gRPC status/metadata/deadline/stream termination; WebSocket handshake/message IDs/order/reconnect; SOAP WSDL/namespaces/Fault. Do not require unused protocols.
2. Separate contract checks from cross-request business postconditions: create/update→read-back→permission view→repeat/downstream effects. Preserve request IDs, business keys, versions, and evidence.
3. Correct status with wrong persisted balance/state/relationships is a business failure. For asynchronous effects apply project consistency windows, never invented delays.
4. Prepare isolated namespaces/unique business keys, clean in reverse dependency order, and record residuals. Missing authority or real-effect constraints stay blocked.

## Core Constraints

- Prioritize by risk / business impact — do not treat everything equally.
- Separate confirmed facts from current assumptions.
- Do not invent endpoints, fields, environments, or root causes the user did not provide.
- Keep output executable: concrete scenarios, clear priority, clear next steps.

## Progressive Disclosure

- When calibrating domain outcomes, valid controls, or evidence gaps, read [references/domain-decision-example.md](references/domain-decision-example.md) for sanitized input, per-item oracles, and reproducible calculations.

- Before producing output, read and follow `prompts/api-testing.md` (minimum coverage, output structure, quality bar).
- When Excel/CSV/JSON/Word is requested: read `output-formats.md` and honor the format.
- When a ready-made template fits: use matching files under `output-templates/`.
- For deep framework/troubleshoot/schema notes: read only the relevant file(s) under `references/`, do not load the whole directory.
- For format conversion or helper checks: prefer existing `scripts/` over reinventing.
- For evaluating/regressing this skill: use `evals/` with skill-up.

## Pre-delivery Checklist

- [ ] Followed the main prompt's output structure
- [ ] Minimum coverage focus: endpoints or business flows in scope, priority and risk level, positive scenarios, negative scenarios, boundary scenarios, auth and permission checks, request and response validation, error handling, ... (details in main prompt)
- [ ] Covered the minimum checklist, or explained omissions
- [ ] High-risk items have explicit priority
- [ ] Did not invent details the user did not provide
- [ ] Assumptions and gaps are marked

## Common Pitfalls

- Do not pretend completeness when scope/context is missing.
- Do not treat every item as equally important.
- Do not skip assumptions and information gaps.
- Do not dump generic theory unrelated to the current toolchain.
