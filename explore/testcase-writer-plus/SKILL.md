---
name: testcase-writer-plus
description: Use this skill when you need to parse requirement documents and requirement analysis results from Word/HTML/JSON/Markdown/Excel, then generate test cases and output them in Markdown/Word/JSON/Excel formats.
---

# TestcaseWriter Plus

Enhanced test case writing skill for multi-format inputs and multi-format outputs.

## When to Use

- Requirement input is file-based and can come from different formats.
- Requirement analysis result is also file-based.
- You need stable parser selection before writing test cases.
- You need test cases in Markdown/Word/JSON/Excel.

## How to Use

1. Prepare requirement file and requirement-analysis file.
2. Run:
   ```bash
   python3 scripts/run_writer.py --requirement /path/to/req.docx --analysis /path/to/analysis.md
   ```
3. Read generated output file. Default output format is Markdown.

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

- [prompts/testcase-writer-plus.md](prompts/testcase-writer-plus.md)

## Templates

- `output-templates/template-markdown.md`
- `output-templates/template-word.docx`
- `output-templates/template-json.json`
- `output-templates/template-excel.tsv`

## Scripts

- `scripts/run_writer.py`: main entry
- `scripts/common_parser.py`: parser implementations
- `scripts/common_formatter.py`: output formatters
- `scripts/parse_word.py`
- `scripts/parse_html.py`
- `scripts/parse_json.py`
- `scripts/parse_markdown.py`
- `scripts/parse_excel.py`
