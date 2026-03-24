# Gatling Setup and CI Guide

## 1. Local Setup

### macOS (Homebrew)
```bash
brew install gatling
gatling --help
```

### Linux (manual)
1. Download Gatling bundle from the official site.
2. Unzip and add `bin/gatling` to `PATH`.
3. Verify:
```bash
gatling --help
```

## 2. Running Simulations

```bash
cd scripts
./run-tests.sh load
./run-tests.sh stress
./run-tests.sh spike
./run-tests.sh soak
./run-tests.sh smoke
```

If `gatling` is not in PATH:
```bash
GATLING_BIN=/opt/gatling/bin/gatling ./run-tests.sh load
```

## 3. CI Strategy

- PR pipeline:
  - run `smoke` or light `load`
  - fail fast on hard assertions
- Nightly / release pipeline:
  - run `stress`, `spike`, `soak`
  - archive full HTML reports and JSON stats

## 4. Artifact Recommendation

- Keep raw Gatling output per run
- Extract metrics into summary JSON
- Track trend deltas against last stable baseline
