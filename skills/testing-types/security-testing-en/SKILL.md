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
