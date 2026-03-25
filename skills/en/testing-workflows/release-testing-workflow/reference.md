# Release Testing Workflow — Step → Prompt

Use files in **this directory's `prompts/`** for each step. Mapping below.

| Step / Phase | Prompt files | Use |
|--------------|--------------|-----|
| T-14 Release planning | test-strategy.md, requirements-analysis.md | Plan, risk, test data |
| T-10–T-8 Prep | automation-testing.md, test-strategy.md | Environment, CI/CD, regression, data |
| T-7 Feature freeze | test-case-writing.md, functional-testing.md, ai-assisted-testing.md | Functional cases, regression, E2E |
| T-5–T-4 Specialized | performance-testing.md, security-testing.md, accessibility-testing.md | Performance, security, a11y, visual |
| T-3 RC | manual-testing.md | Final regression, exploratory |
| T-2, T-1 | test-reporting.md | Quality assessment, Go/No-Go, retro |
