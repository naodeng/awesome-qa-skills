---
name: functional-testing-en
description: Design functional test plans and cases (business, UI, data, integration). Default output Markdown; can request Excel, CSV, or JSON. Use for functional testing.
---

# Functional Testing (English)

**中文版：** See skill `functional-testing`.

Prompt: this directory’s `prompts/functional-testing_EN.md`.

## When to Use

- User mentions **functional testing**, **functional test cases**, **functional test plan**
- Need to design functional test strategy, cases, or plan from requirements/specs
- **Trigger:** e.g. “Design functional test cases for the following requirements” or “Create a functional test plan”

## Output Format Options

This skill **defaults to Markdown** (Standard-version template). To get another format, add one of the following at the **end** of your request:

| Format | Description | How to request (example) |
|--------|-------------|--------------------------|
| **Markdown** | Default; good for reading and version control | No extra instruction |
| **Excel** | Tab-separated, paste into Excel | “Please output as tab-separated table for pasting into Excel” |
| **CSV** | Comma-separated, header row first | “Please output as CSV” |
| **JSON** | For tooling/parsing | “Please output as JSON” |

Details and examples: **[output-formats.md](output-formats.md)** in this directory.

## How to Use the Prompt

1. Open `prompts/functional-testing_EN.md`, copy everything below the dashed line into the AI chat.
2. Append your functional requirements or system spec.
3. If you want Excel/CSV/JSON, append the relevant line from output-formats.md.

## Reference Files

- **[prompts/functional-testing_EN.md](prompts/functional-testing_EN.md)** — Functional testing Standard-version prompt
- **[output-formats.md](output-formats.md)** — Markdown / Excel / CSV / JSON request instructions

**Related:** api-testing-en, test-case-writing-en, test-strategy-en.
