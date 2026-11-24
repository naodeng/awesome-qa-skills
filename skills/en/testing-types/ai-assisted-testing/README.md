# AI-Assisted Testing

## Skill Overview

Use AI to assist requirements analysis, test design, data preparation, script drafts, defect summaries, or report preparation while tracking human review, adopted versions, execution evidence, and cost. AI output is a draft by default; a human must confirm business oracles, assertions, privacy, high-risk tradeoffs, and release acceptance.

## How to Use

1. Open `SKILL.md` in this folder and confirm this skill fits your task.
2. In your AI tool, call `@skill ai-assisted-testing`, then provide scope, risks, data-use constraints, and the expected deliverable.
3. Review `AIA-##` findings and provenance; without real run evidence, keep the result `NOT_RUN` or `BLOCKED`.
4. If you need a specific output format (table, checklist, report), include it directly in your request.

## One-Click Install Script

Run from the repository root:

### macOS / Linux

```bash
bash ./scripts/install-skills-mac.sh --tool codex --lang en --skill ai-assisted-testing
```

### Windows PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang en -Skill ai-assisted-testing
```
