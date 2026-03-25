# Setup and CI Guide

## Local

```bash
cd scripts/templates/supertest
npm install
npm test
```

## One-Click Flow

```bash
cd scripts
./run.sh ../examples
```

## CI Recommendation

- PR: run smoke/generated subset
- main/nightly: run full suite
- archive junit or test summary output

## CI Template

- `examples/ci/github-actions-supertest.yml`
- `examples/ci/Jenkinsfile.supertest`

## Report Schema

- `references/report-schema.md`
