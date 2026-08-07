# WebdriverIO UI Testing Framework Notes

## Primary Focus

- wdio configuration
- services
- runner behavior
- Page Object structure
- capabilities and reporters

## Recommended Structure

- Start from business-critical flows or endpoints.
- Group tests by product capability and execution risk.
- Keep setup, data, assertions, and reporting visible in the plan.
- Prefer maintainable naming and reusable helpers over large scripts.

## Decision Rules

- Use this skill when WebdriverIO is the chosen or likely tool.
- Use the generic parent testing skill when the tool is still undecided.
- Call out constraints that make another tool a better fit.
