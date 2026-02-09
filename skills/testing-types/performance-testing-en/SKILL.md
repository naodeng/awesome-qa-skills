---
name: performance-testing-en
version: 2.0.0
last-updated: 2024-02-06
description: Design performance test plans including load, stress, capacity, stability testing. Default output Markdown; can request Excel/CSV/JSON. Use for performance testing.
category: testing-types
level: advanced
tags: [performance, load, stress, capacity, scalability, k6, jmeter, gatling]
dependencies: [automation-testing-en]
recommended-with: [api-testing-en, test-strategy-en, test-reporting-en]
context-aware: true
context-patterns:
  project-types: [api, web, mobile]
  test-types: [load, stress, spike, endurance, scalability, volume]
  test-frameworks: [k6, jmeter, gatling, locust, artillery]
  metrics: [response-time, throughput, error-rate, resource-usage]
output-formats: [markdown, excel, csv, json, html-report]
examples-count: 1
has-tutorial: false
has-troubleshooting: true
---

# Performance Testing (English)

**中文版:** See skill `performance-testing`.

Prompt: this directory's `prompts/performance-testing_EN.md`.

## When to Use

- User mentions **performance testing**, **performance-testing**
- Need to execute this testing type or produce deliverables per Standard-version
- **Trigger examples:** "Generate/design/write performance test plan for the following"

## Output Format Options

**Markdown** by default. For **Excel / CSV / JSON**, add at the **end** of your request; see **[output-formats.md](output-formats.md)**.

## How to Use

1. Open `prompts/performance-testing_EN.md`, copy everything below the dashed line into the AI chat.
2. Append your specific input.
3. For Excel/CSV/JSON, append the request line from output-formats.md.

## Code Examples

### 1. K6 Load Testing

Complete K6 performance testing example including load, stress, spike, and API testing.

**Location:** `../performance-testing/examples/k6-load-testing/`

**Includes:**
- Load test script
- Stress test script
- Spike test script
- API performance test script
- Automated run scripts
- Detailed README documentation

**Quick Start:**
```bash
cd examples/k6-load-testing
chmod +x run-tests.sh
./run-tests.sh load
```

**Test Coverage:**
- Load testing (simulate normal business volume)
- Stress testing (find performance limits)
- Spike testing (sudden traffic)
- API performance testing (REST API)
- Custom metrics and thresholds

See: [examples/k6-load-testing/README.md](../performance-testing/examples/k6-load-testing/README.md)

## Best Practices

### Performance Test Design Principles

1. **Test Type Selection**
   - Load testing: Verify system performance under expected load
   - Stress testing: Find system performance limits
   - Spike testing: Test sudden traffic handling capability
   - Soak testing: Verify long-term stability

2. **Test Scenario Design**
   - Based on real user behavior
   - Reasonable think time
   - Gradually increase load
   - Include warm-up and cool-down phases

3. **Performance Metrics**
   - Response Time
   - Throughput/RPS
   - Error Rate
   - Concurrent Users
   - Resource Usage (CPU, Memory, Network)

4. **Threshold Setting**
   - Define based on business requirements
   - Use percentiles (p95, p99)
   - Set reasonable error rates
   - Monitor trend changes

### Tool Selection Guide

| Tool | Use Case | Advantages |
|------|----------|------------|
| K6 | Modern performance testing | Scriptable, easy to use, cloud-native |
| JMeter | Traditional performance testing | Feature-rich, GUI, many plugins |
| Gatling | Scala/Java projects | High performance, beautiful reports |
| Locust | Python projects | Easy to learn, distributed |
| Artillery | Node.js projects | Simple configuration, CI/CD friendly |

## Troubleshooting

### Common Issues

#### 1. Connection Timeout

**Problem:** `request timeout` or `connection timeout`

**Solution:**
```javascript
// K6 example
export const options = {
  timeout: '60s',  // Increase timeout
};

// Or check network connection and server status
```

#### 2. Out of Memory

**Problem:** K6 or JMeter consuming too much memory

**Solution:**
- Reduce virtual users
- Use SharedArray to share data (K6)
- Distributed testing
- Increase test machine memory

#### 3. Certificate Verification Error

**Problem:** SSL certificate verification failed

**Solution:**
```javascript
// K6 example
export const options = {
  insecureSkipTLSVerify: true,  // Skip certificate verification (test environment only)
};
```

#### 4. Rate Limiting

**Problem:** Rate limited by server (429 Too Many Requests)

**Solution:**
- Increase think time (sleep)
- Use random delays
- Gradually increase load
- Coordinate test time with server team

#### 5. Unstable Results

**Problem:** Test results vary greatly each time

**Solution:**
- Ensure stable test environment
- Run multiple times and average
- Check network conditions
- Isolate other interference factors

#### 6. Cannot Reach Target Load

**Problem:** Actual RPS much lower than expected

**Solution:**
- Check client resources (CPU, network)
- Use distributed testing
- Optimize test scripts
- Reduce unnecessary wait times

#### 7. Abnormal Report Data

**Problem:** Performance metrics abnormally high or low

**Solution:**
- Check test script logic
- Verify threshold settings
- Review detailed logs
- Compare with historical data

## Reference Files

- **prompts/performance-testing_EN.md** — Performance testing Standard-version prompt
- **output-formats.md** — Markdown / Excel / CSV / JSON request instructions
- **examples/k6-load-testing/** — Complete K6 example
- **quick-start.md** — 5-minute quick start guide

**Related skills:** api-testing-en, automation-testing-en, test-strategy-en, test-reporting-en.
