---
name: security-testing-en
version: 2.0.0
last-updated: 2024-02-06
description: Design security test plans including OWASP Top 10, penetration testing, vulnerability scanning. Default output Markdown; can request Excel/CSV/JSON. Use for security testing.
category: testing-types
level: advanced
tags: [security, owasp, penetration, vulnerability, zap, burp-suite, sql-injection, xss]
dependencies: [api-testing-en]
recommended-with: [automation-testing-en, test-strategy-en, test-reporting-en]
context-aware: true
context-patterns:
  project-types: [api, web, mobile]
  test-types: [vulnerability-scan, penetration, authentication, authorization, encryption, injection]
  test-frameworks: [owasp-zap, burp-suite, nmap, metasploit]
  standards: [owasp-top-10, pci-dss, gdpr, hipaa]
output-formats: [markdown, excel, csv, json, html-report]
examples-count: 1
has-tutorial: false
has-troubleshooting: true
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

1. Open `prompts/security-testing_EN.md`, copy everything below the dashed line into the AI chat.
2. Append your specific input.
3. For Excel/CSV/JSON, append the request line from output-formats.md.

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

## Troubleshooting

### Common Issues

#### 1. ZAP Scan Timeout

**Problem**: Scan takes too long or times out

**Solution**:
```bash
# Increase timeout
zap-baseline.py -t http://example.com --timeout 300

# Limit scan depth
zap-baseline.py -t http://example.com -m 3
```

#### 2. Too Many False Positives

**Problem**: Scan results contain many false positives

**Solution**:
- Use custom scan policies
- Exclude known false positives
- Manually verify high-risk vulnerabilities
- Adjust scan levels

#### 3. Cannot Scan Authenticated Pages

**Problem**: ZAP cannot access pages after login

**Solution**:
```bash
# Configure authentication
zap-cli auth \
  --auth-mode form \
  --auth-url http://example.com/login \
  --auth-username user \
  --auth-password pass
```

#### 4. Docker Permission Issues

**Problem**: Cannot write report files

**Solution**:
```bash
# Use correct permissions
docker run -u $(id -u):$(id -g) \
  -v $(pwd):/zap/wrk/:rw \
  owasp/zap2docker-stable \
  zap-baseline.py -t http://example.com
```

#### 5. Certificate Verification Error

**Problem**: SSL certificate verification failed

**Solution**:
```bash
# Skip certificate verification (test environment only)
zap-baseline.py -t https://example.com --hook-script skip-cert-check.py
```

#### 6. Scan Blocked by WAF

**Problem**: Requests blocked by Web Application Firewall

**Solution**:
- Reduce scan speed
- Use random User-Agent
- Coordinate test time with security team
- Use whitelist IP

#### 7. Difficult to Interpret Report

**Problem**: Don't understand vulnerabilities in scan report

**Solution**:
- Consult OWASP documentation
- Manually verify vulnerabilities
- Consult security experts
- Reference CVE database

## Reference Files

- **prompts/security-testing_EN.md** — Security testing Standard-version prompt
- **output-formats.md** — Markdown / Excel / CSV / JSON request instructions
- **examples/owasp-zap-scan/** — Complete OWASP ZAP example
- **quick-start.md** — 5-minute quick start guide

**Related skills:** api-testing-en, automation-testing-en, test-strategy-en, test-reporting-en.
