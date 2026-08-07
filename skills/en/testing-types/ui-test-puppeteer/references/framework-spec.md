# UI Test Puppeteer Framework Notes

## Primary Focus

- page automation
- Chrome DevTools Protocol use cases
- screenshots and PDFs
- network interception
- E2E framework fit boundaries

## Recommended Structure

- Start from business-critical flows or endpoints.
- Group tests by product capability and execution risk.
- Keep setup, data, assertions, and reporting visible in the plan.
- Prefer maintainable naming and reusable helpers over large scripts.

## Decision Rules

- Use this skill when UI Test Puppeteer is the chosen or likely tool.
- Use the generic parent testing skill when the tool is still undecided.
- Call out constraints that make another tool a better fit.
