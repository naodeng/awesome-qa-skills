---
name: requirements-analysis-plus
description: Use this skill when you need to analyze requirement documents from Word, HTML, JSON, Markdown, or Excel files, select the correct parser automatically, and output a structured requirements analysis conclusion.
---

# Requirements Analysis Plus

Enhanced requirements analysis skill with multi-format document parsing and structured conclusion output.

## When to Use

- Requirement source is a file instead of plain text
- Requirement file can be Word/HTML/JSON/Markdown/Excel
- You need stable, repeatable parsing before analysis
- You want a structured conclusion with risks and ambiguities

## How to Use

1. Put requirement file in any accessible path.
2. Run:
   ```bash
   python3 scripts/run_analysis.py --input /path/to/requirement.docx
   ```
3. Read generated conclusion markdown (default beside source file).

## Supported Formats

- Word: `.docx`
- HTML: `.html`, `.htm`
- JSON: `.json`
- Markdown: `.md`, `.markdown`
- Excel: `.xlsx`, `.xlsm`

## Prompts

- [prompts/requirements-analysis-plus.md](prompts/requirements-analysis-plus.md)

## Scripts

- `scripts/run_analysis.py`: main entry, auto-select parser by file type
- `scripts/common_parser.py`: parser implementations
- `scripts/parse_word.py`
- `scripts/parse_html.py`
- `scripts/parse_json.py`
- `scripts/parse_markdown.py`
- `scripts/parse_excel.py`

## Output

The script outputs a markdown conclusion containing:

- Requirement summary
- Functional requirement points
- Non-functional requirement points
- Ambiguities and risk assumptions
- Suggested test focus and next actions
