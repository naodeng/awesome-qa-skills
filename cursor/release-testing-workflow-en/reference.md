# Release Testing Workflow — Step → Prompt

Use files in **this directory's `prompts/`** for each step. Mapping below.

| Step / Phase | Prompt files | Use |
|--------------|--------------|-----|
| T-14 Release planning | test-strategy_EN.md, requirements-analysis_EN.md | Plan, risk, test data |
| T-10–T-8 Prep | automation-testing_EN.md, test-strategy_EN.md | Environment, CI/CD, regression, data |
| T-7 Feature freeze | test-case-writing_EN.md, functional-testing_EN.md, ai-assisted-testing_EN.md | Functional cases, regression, E2E |
| T-5–T-4 Specialized | performance-testing_EN.md, security-testing_EN.md, accessibility-testing_EN.md | Performance, security, a11y, visual |
| T-3 RC | manual-testing_EN.md | Final regression, exploratory |
| T-2, T-1 | test-reporting_EN.md | Quality assessment, Go/No-Go, retro |
