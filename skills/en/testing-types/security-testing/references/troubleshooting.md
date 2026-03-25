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

