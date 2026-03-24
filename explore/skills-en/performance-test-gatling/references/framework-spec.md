# Gatling Framework Specification

## 1. Directory Convention

- `scripts/simulations/BaseSimulation.scala`: shared protocol, feeders, helper chains
- `scripts/simulations/*Simulation.scala`: scenario-specific simulation entries
- `reports/`: generated Gatling results and post-processed summaries
- `scripts/tools/`: summary/comparison helpers

## 2. Simulation Naming Convention

- `LoadSimulation.scala`: expected business load verification
- `StressSimulation.scala`: upper-limit and breaking-point exploration
- `SpikeSimulation.scala`: sudden traffic burst and recovery validation
- `SoakSimulation.scala`: long-run stability validation
- `ApiSmokeSimulation.scala`: low-cost API perf smoke

## 3. Workload Modeling Rules

- Start with baseline (single-digit users)
- Increase in phases with clear ramp profile
- Include realistic pause/think time for user behavior tests
- Split core and secondary flows with weighted scenarios when needed

## 4. Assertion Rules

Minimum recommended gates:
- successful requests percentage
- failed requests percentage
- p95/p99 response-time threshold
- optional throughput floor and business-specific checks

## 5. Reporting Requirements

Each test run should produce:
- test metadata (env, base URL, simulation class, timestamp, build/commit)
- injection profile used
- key latency percentiles and failure rate
- pass/fail conclusion
- bottleneck hints

## 6. CI/CD Integration Guidance

- Keep smoke/load-lite for PR checks
- Schedule stress/spike/soak in nightly or release pipelines
- fail pipeline only on hard assertions
- archive reports for trend comparison

## 7. Test Scope Baseline

Aligned with project performance-testing prompt:
- performance types: load, stress, spike, capacity/volume, endurance
- domains: web/API/database/resource
- metrics: latency, throughput, errors, concurrency, saturation
