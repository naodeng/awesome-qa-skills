# Release Testing Workflow — Stage Handoff Map

Orchestration prompt: `prompts/release-testing-workflow.md` (T-windows, release gates, Go/No-Go, handoffs).  
For stage deep-dives, hand off to the matching **type skill** (skill names only—no relative-path links to other skill internals).

| Step / Phase | Handoff skill | Use |
|--------------|---------------|-----|
| T-14 Release planning | `test-strategy`, `requirements-analysis` | Plan, risk, test data |
| T-10–T-8 Prep | `automation-testing`, `test-strategy` | Environment, CI/CD, regression, data |
| T-7 Feature freeze | `test-case-writing`, `functional-testing`, `ai-assisted-testing` | Functional cases, regression, E2E |
| T-5–T-4 Specialized | `performance-testing`, `security-testing`, `accessibility-testing` | Performance, security, a11y, visual |
| T-3 RC | `manual-testing` | Final regression, exploratory |
| T-2, T-1 | `test-reporting` | Quality assessment, Go/No-Go, retro |
