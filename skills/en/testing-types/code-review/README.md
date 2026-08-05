# Code Review

## Skill Overview

Risk-driven review of a PR / diff with severity-ranked findings and actionable fixes — catch logic, security, financial-loss, and maintainability defects before merge.

## How to Use

1. Open `SKILL.md` in this folder and confirm this skill fits your task.
2. In your AI tool, call `@skill code-review`, then add the diff, business goal, stack, and upstream/downstream context.
3. If you need a specific output format (table, checklist, report), include it directly in your request.

## One-Click Install Script

Run from the repository root:

### macOS / Linux

```bash
bash ./scripts/install-skills-mac.sh --tool codex --lang en --skill code-review
```

### Windows PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang en -Skill code-review
```
