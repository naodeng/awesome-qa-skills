# Setup and CI Guide

## Local

```bash
cd scripts/templates/pytest
pip install -r requirements.txt
pytest -q
```

## One-Click Flow

```bash
cd scripts
./run.sh ../examples
```

## CI Recommendation

- PR: run smoke/generated subset
- main/nightly: run full suite
- export junit xml for trend tracking

## CI Template

- `examples/ci/github-actions-pytest.yml`
- `examples/ci/Jenkinsfile.pytest`

## Report Schema

- `references/report-schema.md`
