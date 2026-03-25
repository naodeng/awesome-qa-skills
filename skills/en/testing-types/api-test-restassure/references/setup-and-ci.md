# Setup and CI Guide

## Local

```bash
cd scripts/templates/restassured
mvn -q test
```

## One-Click Flow

```bash
cd scripts
./run.sh ../examples
```

## CI Recommendation

- PR: run smoke/generated subset
- main/nightly: run full suite
- archive surefire reports

## CI Template

- `examples/ci/github-actions-restassure.yml`
- `examples/ci/Jenkinsfile.restassure`

## Report Schema

- `references/report-schema.md`
