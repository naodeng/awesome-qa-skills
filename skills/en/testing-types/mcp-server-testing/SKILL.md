---
name: mcp-server-testing
description: Use this skill when designing or reviewing versioned tests for Model Context Protocol servers, including discovery, tools, transports, authorization, and safe side-effect boundaries; triggers include MCP server testing and MCP 服务端测试.
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

# MCP Server Testing

## When to use

- Plan or review tests for an MCP server's protocol behavior, tool contracts, transports, authorization, or error handling.
- Check a declared MCP revision and compatibility boundary instead of assuming a floating latest version.
- Prepare isolated validation for tool side effects, schemas, and server security properties.

## How to use

1. Read [prompts/mcp-server-testing.md](prompts/mcp-server-testing.md) as the complete execution contract.
2. Extract the target protocol revision, SDK/server version, transports, capabilities, tool contracts, authorization model, environment, and evidence. Mark missing inputs as assumptions or open questions.
3. Read [references/mcp-spec-2026-07-28.md](references/mcp-spec-2026-07-28.md) when the target is revision 2026-07-28; for a different declared revision, obtain its matching official specification before asserting protocol requirements.
4. Produce prioritized positive, negative, boundary, and compatibility cases with observable oracles, safe setup, evidence, and stop conditions.
5. Report plans and fixture comparisons separately from tests actually executed.

## Scope and constraints

- Focus on MCP server protocol and server behavior. A host/client user experience, model quality, and general application security need their own scope unless explicitly requested.
- Protocol conformance does not define every business tool effect; derive effects from the target tool contract and use isolated data.
- Do not use real credentials or invoke production/destructive tools without explicit authorization and an isolated safe environment.
- A server's self-reported identity, successful initialization on an older protocol, or installed SDK version alone does not prove which behavior was exercised.

## Load references when needed

- Read `references/mcp-spec-2026-07-28.md` for pinned protocol requirements and official source links.
- Read the matching eval case when reproducing a package's intended coverage; cases are synthetic and do not prove runtime behavior.

## Pre-delivery checks

- [ ] Protocol revision, transport, feature, and compatibility target are explicit.
- [ ] Allowed behavior has a valid control beside denial and malformed-input cases.
- [ ] Tool side effects, identity, authorization, and retry expectations have observable oracles.
- [ ] Missing runtime evidence remains NOT_RUN or UNKNOWN; no production result is invented.
