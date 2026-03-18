---
name: test-case-reviewer-plus
description: Use this skill when you need to parse requirement docs, requirement analysis, technical docs, project plans, test strategy docs, test case docs, and other docs from Word/HTML/JSON/Markdown/Excel, then review test cases and output review results in Markdown/Word/JSON/Excel.
---

# Test-Case-Reviewer Plus

Enhanced test case review skill with multi-document and multi-format parsing.

## When to Use

- You need a test case review based on multiple project documents.
- Source docs include requirements, requirement analysis, technical docs, project plans, test strategy docs, test case docs, and other references.
- Inputs can be Word/HTML/JSON/Markdown/Excel files.
- You need output review results in Markdown/Word/JSON/Excel.

## How to Use

1. Prepare `--testcase` and at least one requirement file.
2. Optionally provide analysis, technical docs, project plan, test strategy, and other docs.
3. Run:
   ```bash
   python3 scripts/run_review.py \
     --requirement /path/to/req.docx \
     --analysis /path/to/analysis.md \
     --tech /path/to/tech.html \
     --plan /path/to/plan.xlsx \
     --strategy /path/to/strategy.md \
     --testcase /path/to/testcases.docx \
     --other /path/to/notes.json \
     --output-format markdown
   ```
4. Read generated review result file (default format is Markdown).

## Input Formats

- Word: `.docx`
- HTML: `.html`, `.htm`
- JSON: `.json`
- Markdown: `.md`, `.markdown`
- Excel: `.xlsx`, `.xlsm`

## Output Formats

- Markdown (default)
- Word `.docx`
- JSON
- Excel-friendly TSV

## Prompt

- [prompts/test-case-reviewer-plus.md](prompts/test-case-reviewer-plus.md)

## Templates

- `output-templates/template-markdown.md`
- `output-templates/template-word.docx`
- `output-templates/template-json.json`
- `output-templates/template-excel.tsv`

## Scripts

- `scripts/run_review.py`: main entry
- `scripts/common_parser.py`: parser implementations
- `scripts/common_formatter.py`: review output formatters
- `scripts/parse_word.py`
- `scripts/parse_html.py`
- `scripts/parse_json.py`
- `scripts/parse_markdown.py`
- `scripts/parse_excel.py`
