# K6 Framework Specification

## 1. Directory Convention

- `scripts/config.js`: shared configuration and thresholds
- `scripts/helpers.js`: shared request wrappers, checks, and tags
- `scripts/tests/*.js`: scenario-specific k6 entry scripts
- `reports/`: generated outputs (summary json/html)

## 2. Script Naming Convention

- `load.js`: expected business load verification
- `stress.js`: upper-limit and breaking-point exploration
- `spike.js`: sudden traffic burst and recovery validation
- `soak.js`: long-run stability validation
- `api-smoke.js`: low-cost API availability/perf smoke

## 3. Workload Modeling Rules

- Start with baseline (single-digit VUs)
- Increase in phases (ramp-up, hold, ramp-down)
- Use realistic think time when simulating user behavior
- Separate core flow and secondary flow ratios with weighted scenarios if needed

## 4. Threshold Rules

Minimum recommended gates:
- `http_req_duration`: p95 and p99 limits
- `http_req_failed`: error-rate ceiling
- throughput floor if SLO requires it (`http_reqs` rate)
- custom trend/rate metrics for business latency and success ratio

## 5. Reporting Requirements

Each test run should produce:
- command and test metadata (env, target URL, commit/tag)
- stages and thresholds used
- key latency percentiles and error rate
- pass/fail conclusion
- suspected bottleneck hints

## 6. CI/CD Integration Guidance

- Keep test durations bounded for PR checks (smoke/load-lite)
- Run stress/spike/soak in scheduled pipelines
- fail pipeline on hard thresholds only
- archive artifacts for trend comparison

## 7. Test Scope Baseline

Aligned with project performance-testing prompt:
- performance types: load, stress, spike, capacity/volume, endurance
- domains: web/API/database/resource
- metrics: latency, throughput, errors, concurrency, resource saturation
