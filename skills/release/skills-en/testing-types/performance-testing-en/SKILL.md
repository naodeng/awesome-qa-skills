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

See: [examples/k6-load-testing/README.md](references/local/testing-types-performance-testing-examples-k6-load-testing-README.md)

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
