---
name: discover-testing
description: Use this skill when you need to route a testing request to the right testing-type or testing-workflow skill quickly; triggers include testing skill discovery, skill routing, and test approach selection.
---

# Testing Skill Discovery

Use this gateway skill to choose the right testing skill before execution.

## When to Use

- User asks "which testing skill should I use"
- Request mixes multiple testing domains (e.g. functional + API + report)
- Need to map project phase to a concrete workflow skill

## How to Use

1. Identify request intent: type-specific testing vs phase workflow.
2. Use [reference.md](reference.md) to map to the best primary skill.
3. If needed, add one supporting skill for output/reporting.

## Target Audience

- QA engineers selecting the most suitable skill before execution
- Team leads standardizing skill selection across projects
- AI users who need consistent routing from requirement to test output

## Not Recommended For

- Direct execution requests where the target skill is already explicit
- Non-testing requests outside QA scope

## Critical Success Factors

- Choose one primary skill first, then add at most one supporting skill
- Match workflow skills to project phase and time constraints
- Keep deliverables traceable from requirement to report

## Reference Files

- [reference.md](reference.md) — Testing skill routing map

## Output Templates and Parsing Scripts

- Template directory: `output-templates/`
- Parser scripts directory: `scripts/`
- Convert scripts directory: `scripts/`

Examples:
```bash
python3 scripts/parse_json.py output-templates/template-json.json
python3 scripts/convert_to_markdown.py output-templates/template-json.json
python3 scripts/batch_convert_templates.py --skip-same
```
