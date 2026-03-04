---
name: performance-testing-en
description: Use this skill when you need to design performance testing for load, stress, spike, endurance, or capacity objectives; triggers include performance testing and load testing.
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

1. Open the relevant file in this directory's `prompts/` and copy the content below the dashed line.
2. Append your requirements and context (business flow, environment, constraints, acceptance criteria).
3. If you need non-Markdown output, append the request sentence from `output-formats.md` at the end.

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

## Common Pitfalls

- ❌ Using unrealistic traffic models → ✅ Build scenarios from production-like behavior and workload mix
- ❌ Looking only at average latency → ✅ Track p95/p99, error rate, throughput, and saturation together
- ❌ Skipping baseline and warm-up phases → ✅ Establish baseline, warm-up, then apply staged load
- ❌ Ignoring bottleneck evidence → ✅ Correlate app metrics with CPU, memory, I/O, and downstream services

## Troubleshooting

Detailed troubleshooting steps were moved to [references/troubleshooting.md](references/troubleshooting.md).
Load it on demand to keep the main skill concise.
## Reference Files

- **prompts/performance-testing_EN.md** — Performance testing Standard-version prompt
- **output-formats.md** — Markdown / Excel / CSV / JSON request instructions
- **examples/k6-load-testing/** — Complete K6 example
- **quick-start.md** — 5-minute quick start guide

**Related skills:** api-testing-en, automation-testing-en, test-strategy-en, test-reporting-en.
