# Test Reporting

## Skill Overview

Summarize test scope, quality status, risks, defects, and next steps. When a report includes AI-effect or model-evaluation claims, record model, prompt, dataset, judge, run, sampling, token cost, evaluator, and execution state; without a model version or run ID, keep the AI-effect conclusion `UNKNOWN`.

## How to Use

1. Open `SKILL.md` in this folder and confirm this skill fits your task.
2. In your AI tool, call `@skill test-reporting`, then add your real project context and goal.
3. If you need a specific output format (table, checklist, report), include it directly in your request.

## One-Click Install Script

Run from the repository root:

### macOS / Linux

```bash
bash ./scripts/install-skills-mac.sh --tool codex --lang en --skill test-reporting
```

### Windows PowerShell

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang en -Skill test-reporting
```
