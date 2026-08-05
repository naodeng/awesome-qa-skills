# Code Review - 5-Minute Quick Start

## Minimum Input

Paste this to the AI (mark anything unknown):

```text
Use code-review for this change.
Business goal:
Change scope / diff:
Tech stack:
Upstream/downstream deps:
Known risks or team norms:
```

## Expected Output Shape

1. Change summary + overall risk rating  
2. P0 / P1 / P2 list (with location + fix guidance)  
3. Testability and observability  
4. Recommended fix order  
5. Residual risks and gaps  

## Severity Cheat Sheet

| Level | Meaning | Examples |
| --- | --- | --- |
| P0 | Block merge | Financial loss, severe security, main-path breakage |
| P1 | Fix this iteration | Likely race, clear perf issue, missing core logs |
| P2 | Optional / debt | Non-core smells, minor readability |

## Pre-submit Self-check

- [ ] No naming/indent noise dump  
- [ ] P0/P1 have impact rationale and location  
- [ ] Every finding has an executable fix direction  
- [ ] Assumptions and gaps are marked  
