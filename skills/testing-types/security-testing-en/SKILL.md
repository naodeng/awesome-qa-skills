---
name: security-testing-en
description: Use this skill when you need to design security testing around OWASP risks, vulnerability scanning, and penetration scenarios; triggers include security testing and vulnerability testing.
---

# Security Testing (English)

**中文版:** See skill `security-testing`.

Prompt: this directory's `prompts/security-testing_EN.md`.

## When to Use

- User mentions **security testing**, **security-testing**
- Need to execute this testing type or produce deliverables per Standard-version
- **Trigger examples:** "Generate/design/write security test plan for the following"

## Output Format Options

**Markdown** by default. For **Excel / CSV / JSON**, add at the **end** of your request; see **[output-formats.md](output-formats.md)**.

## How to Use

1. Open the relevant file in this directory's `prompts/` and copy the content below the dashed line.
2. Append your requirements and context (business flow, environment, constraints, acceptance criteria).
3. If you need non-Markdown output, append the request sentence from `output-formats.md` at the end.

## Code Examples

### 1. OWASP ZAP Security Scanning

Complete OWASP ZAP security testing example including baseline scan, full scan, and API scan.

**Location:** `../security-testing/examples/owasp-zap-scan/`

**Includes:**
- Baseline scan script (quick scan)
- Full scan script (deep scan)
- API scan script
- Automated run scripts
- Detailed README documentation

**Quick Start:**
```bash
cd examples/owasp-zap-scan
./run-scan.sh baseline https://example.com
```

**Test Coverage:**
- SQL injection detection
- XSS vulnerability detection
- CSRF vulnerability detection
- Security configuration check
- API security testing

See: [examples/owasp-zap-scan/README.md](../security-testing/examples/owasp-zap-scan/README.md)

## Best Practices

### Security Testing Principles

1. **OWASP Top 10**
   - Injection attacks
   - Broken authentication
   - Sensitive data exposure
   - XML External Entities (XXE)
   - Broken access control
   - Security misconfiguration
   - Cross-Site Scripting (XSS)
   - Insecure deserialization
   - Using components with known vulnerabilities
   - Insufficient logging and monitoring

2. **Testing Phases**
   - Development: Static code analysis
   - Testing: Dynamic security testing
   - Pre-release: Penetration testing
   - Production: Continuous monitoring

3. **Testing Methods**
   - Black box: No knowledge of internal implementation
   - White box: Full knowledge of internal implementation
   - Gray box: Partial knowledge of internal implementation

### Tool Selection Guide

| Tool | Use Case | Advantages |
|------|----------|------------|
| OWASP ZAP | Web application security | Open source, easy to use, automated |
| Burp Suite | Penetration testing | Powerful, professional |
| Nmap | Network scanning | Port scanning, service identification |
| SQLMap | SQL injection | Automated injection testing |
| Nikto | Web server | Quick vulnerability scanning |

## Common Pitfalls

- ❌ Running tools without threat context → ✅ Map tests to assets, attack surfaces, and risk priorities
- ❌ Treating scan output as final truth → ✅ Triage findings, verify exploitability, and reduce false positives
- ❌ Missing authz/authn abuse scenarios → ✅ Add broken access control and session abuse cases
- ❌ One-time testing before release only → ✅ Integrate recurring security checks in CI and release gates

## Troubleshooting

Detailed troubleshooting steps were moved to [references/troubleshooting.md](references/troubleshooting.md).
Load it on demand to keep the main skill concise.
## Reference Files

- **prompts/security-testing_EN.md** — Security testing Standard-version prompt
- **output-formats.md** — Markdown / Excel / CSV / JSON request instructions
- **examples/owasp-zap-scan/** — Complete OWASP ZAP example
- **quick-start.md** — 5-minute quick start guide

**Related skills:** api-testing-en, automation-testing-en, test-strategy-en, test-reporting-en.

## Target Audience

- QA engineers and developers executing this testing domain in real projects
- Team leads who need structured, reproducible testing outputs
- AI users who need fast, format-ready deliverables for execution and reporting

## Not Recommended For

- Pure production incident response without test scope/context
- Decisions requiring legal/compliance sign-off without expert review
- Requests lacking minimum inputs (scope, environment, expected behavior)

## Critical Success Factors

- Provide clear scope, environment, and acceptance criteria before generation
- Validate generated outputs against real system constraints before execution
- Keep artifacts traceable (requirements -> test points -> defects -> decisions)

## Output Templates and Parsing Scripts

- Template directory: `output-templates/`
  - `template-word.md` (Word-friendly structure)
  - `template-excel.tsv` (Excel paste-ready)
  - `template-xmind.md` (XMind-friendly outline)
  - `template-json.json`
  - `template-csv.csv`
  - `template-markdown.md`
- Parser scripts directory: `scripts/`
  - Parse (generic): `parse_output_formats.py`
  - Parse (per-format): `parse_word.py`, `parse_excel.py`, `parse_xmind.py`, `parse_json.py`, `parse_csv.py`, `parse_markdown.py`
  - Convert (generic): `convert_output_formats.py`
  - Convert (per-format): `convert_to_word.py`, `convert_to_excel.py`, `convert_to_xmind.py`, `convert_to_json.py`, `convert_to_csv.py`, `convert_to_markdown.py`
  - Batch convert: `batch_convert_templates.py` (outputs into `artifacts/`)

Examples:
```bash
python3 scripts/parse_json.py output-templates/template-json.json
python3 scripts/parse_markdown.py output-templates/template-markdown.md
python3 scripts/convert_to_json.py output-templates/template-markdown.md
python3 scripts/convert_output_formats.py output-templates/template-json.json --to csv
python3 scripts/batch_convert_templates.py --skip-same
```
