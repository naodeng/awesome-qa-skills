# Gatling Report Interpretation Guide

This guide standardizes how to interpret Gatling result artifacts.

## 1. Required Metrics

- global success/failed request rate
- response time p95 and p99
- request throughput (req/s)
- scenario-level assertion outcomes
- optional custom business success ratio

## 2. Default Pass/Fail Baseline

- latency gate:
  - p95 <= 800ms
  - p99 <= 1500ms
- error gate:
  - failed requests < 1%
- stability gate:
  - no sustained degradation in soak run
- recovery gate:
  - spike run should recover near baseline after burst

Use scenario-specific assertions where intentionally relaxed (for stress/spike exploration).

## 3. Recommended Output Sections

1. Test metadata:
- simulation, env, base URL, timestamp, build/commit

2. Workload profile:
- users, ramp pattern, hold duration, scenario mix

3. Key results:
- p95, p99, failed %, throughput, assertion summary

4. Verdict:
- pass/fail against assertions and threshold rationale

5. Bottleneck hints:
- app CPU saturation, DB contention, cache miss surge, dependency timeout

## 4. Trend Comparison Rules

- Compare same simulation + same env + same profile first.
- Regression candidate when:
  - p95 increased > 15%, or
  - failed % increased > 0.5 percentage point
- Always correlate with infra/app metrics before root-cause conclusion.
