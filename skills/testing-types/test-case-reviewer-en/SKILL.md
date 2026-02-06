---
name: test-case-reviewer-en
description: Review test cases from multiple dimensions; output review report, missing scenarios, and improvement suggestions. Default output Markdown; can request Excel, CSV, or JSON. Use for test case review.
---

# Test Case Reviewer (English)

**中文版：** See skill `test-case-reviewer`.

Prompt: this directory's `prompts/test-case-reviewer_EN.md`.

## When to Use

- User mentions "test case review", "test case reviewer"
- Need to review existing test cases for quality, missing scenarios, and improvements
- **Trigger:** e.g. "Review the following test cases" or "Identify gaps and risks in these cases"

## Output Format Options

**Markdown** by default. For **Excel / CSV / JSON**, add at the **end** of your request; see **[output-formats.md](output-formats.md)**.

## How to Use

1. Open `prompts/test-case-reviewer_EN.md`, copy everything below the dashed line into the AI chat.
2. Append the test cases to review.
3. For Excel/CSV/JSON, append the request from output-formats.md.

## Reference Files

- **prompts/test-case-reviewer_EN.md** — Test case reviewer Standard-version prompt
- **output-formats.md** — Markdown / Excel / CSV / JSON request instructions
