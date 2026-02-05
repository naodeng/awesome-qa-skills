---
name: release-testing-workflow-en
description: Guides release testing from T-14 planning through Go/No-Go, deployment, and post-release. Covers functional, regression, performance, security, accessibility. Use when planning or executing release testing.
---

# Release Testing Workflow

**中文版：** 见技能 `release-testing-workflow`。

End-to-end release testing (1–2 weeks before release through post-release). Prompts: see [reference.md](reference.md) and this directory's **`prompts/`**.

## When to Use

- User mentions **release testing**, **Go/No-Go**, or **release readiness**
- Need timeline: T-14 planning → T-7 feature freeze → T-5–T-4 specialized testing → T-3 RC → T-2 quality assessment → T-1 Go/No-Go → T-day release → T+1–T+7 post-release
- **Trigger:** e.g. “How do we schedule pre-release testing?” or “Go/No-Go checklist”

## How to Use the Prompts

For each step: 1) Check [reference.md](reference.md) for the prompt file; 2) Open that file under this directory’s `prompts/`; 3) Combine the prompt with the current release context (scope, environment, gate criteria) and run with the AI.

## Common Pitfalls

- ❌ Adding features after T-7 → ✅ Feature freeze: only defect fixes; non-critical code freeze
- ❌ Releasing without Go/No-Go → ✅ Release only after gates pass, team alignment, and rollback readiness
- ❌ No post-release monitoring → ✅ T+1 intensive monitoring and fast response; follow incident procedures

## Best Practices

- T-14: use test strategy and requirements prompts for release plan and risk assessment
- T-2: use test reporting and test strategy for quality gates and known-issue assessment
- Before deploy: confirm rollback tested, communication plan and support brief ready
- **Principle:** When in doubt, delay release.

## Reference Files

- **[reference.md](reference.md)** — Step-to-prompt file mapping
- **prompts/** — English prompt files for this workflow (open the matching `.md` per step and use with context)

**Related:** daily-testing-workflow-en, sprint-testing-workflow-en.
