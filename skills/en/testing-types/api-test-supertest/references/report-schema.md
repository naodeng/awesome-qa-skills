# Unified API Test Report Schema

Use these fields for all generated API test reports:

- `run_id`: unique run identifier
- `tool`: `supertest` / `pytest` / `bruno` / `restassured`
- `env`: environment name (staging/prod-like)
- `case_id`: stable case identifier
- `api_name`: human-readable endpoint name
- `method`: HTTP method
- `path`: endpoint path
- `status`: `pass` / `fail` / `skip`
- `status_code`: actual HTTP status code
- `expected_status_code`: expected status code or range
- `latency_ms`: measured request latency
- `error_rate`: optional aggregated failure rate per run
- `assertions_total`: total assertions
- `assertions_passed`: passed assertions
- `message`: failure or debug message
- `timestamp`: ISO8601 UTC timestamp

Recommended rule:
- P0 failures should fail CI pipelines.
