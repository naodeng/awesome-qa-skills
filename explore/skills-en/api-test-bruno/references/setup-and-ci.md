# Setup and CI Guide

## Local

```bash
npm i -g @usebruno/cli
cd scripts
./run-tests.sh ./templates/bruno staging
```

## One-Click Flow

```bash
cd scripts
./run.sh ../examples
```

## CI Recommendation

- PR: run smoke subset
- main/nightly: run full generated collection
- archive json report output

## CI Template

- `examples/ci/github-actions-bruno.yml`
- `examples/ci/Jenkinsfile.bruno`

## Report Schema

- `references/report-schema.md`
