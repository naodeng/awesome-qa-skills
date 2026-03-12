---
name: test-strategy-plus
description: Use this skill when you need to parse requirement documents, requirement analysis results, technical docs, project plans, and other documents from Word/HTML/JSON/Markdown/Excel, then generate a structured test strategy in Markdown/Word/JSON/Excel.
---

# Test Strategy Plus

Enhanced test strategy design skill with multi-document and multi-format parsing.

## When to Use

- You need a test strategy based on multiple document sources.
- Source docs may include requirement docs, requirement analysis result, technical docs, project plans, and other references.
- Inputs can be Word/HTML/JSON/Markdown/Excel files.
- You need output strategy in Markdown/Word/JSON/Excel.

## How to Use

1. Prepare at least one requirement file.
2. Optionally provide analysis, technical docs, project plan, and other docs.
3. Run:
   ```bash
   python3 scripts/run_strategy.py \
     --requirement /path/to/req.docx \
     --analysis /path/to/analysis.md \
     --tech /path/to/tech.html \
     --plan /path/to/plan.xlsx \
     --other /path/to/notes.json \
     --output-format markdown
   ```
4. Read generated strategy file (default format is Markdown).

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

- [prompts/test-strategy-plus.md](prompts/test-strategy-plus.md)

## Templates

- `output-templates/template-markdown.md`
- `output-templates/template-word.docx`
- `output-templates/template-json.json`
- `output-templates/template-excel.tsv`

## Scripts

- `scripts/run_strategy.py`: main entry
- `scripts/common_parser.py`: parser implementations
- `scripts/common_formatter.py`: strategy output formatters
- `scripts/parse_word.py`
- `scripts/parse_html.py`
- `scripts/parse_json.py`
- `scripts/parse_markdown.py`
- `scripts/parse_excel.py`
