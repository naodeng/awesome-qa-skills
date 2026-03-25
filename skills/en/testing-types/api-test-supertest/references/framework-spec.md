# Supertest Framework Specification

## 1. Directory Convention

- `scripts/parse_api_sources.py`: multi-format API source parser
- `scripts/generate_supertest_tests.py`: normalized endpoint -> Jest/Supertest tests
- `scripts/templates/supertest/`: runnable Node.js test template
- `generated-tests/`: output test files generated from parsed endpoints

## 2. Test Layer Convention

- `smoke`: core endpoint availability
- `contract`: status code + schema/shape checks
- `business`: key API flows and state transitions
- `negative`: invalid params, auth failure, boundary inputs

## 3. Assertion Rules

- status code assertions are mandatory
- response shape assertions for key fields are mandatory
- latency thresholds for critical endpoints are recommended
- error payload assertions for 4xx/5xx are required in negative tests

## 4. Data and Environment Rules

- use environment variables for base URL and token
- never commit secrets in test files
- use deterministic test data or isolated seed fixtures
- ensure cleanup strategy for mutable endpoints

## 5. Parsing Scope Rules

Supported parser inputs:
- curl
- Postman collections
- Swagger/OpenAPI (including v3)
- Bruno
- OpenCollection
- Insomnia
- WSDL
- ZIP containing any supported format

Parser output must be normalized endpoint JSON with:
- method
- path
- source format
- optional base URL, headers, query/body hints

## 6. CI Guidance

- run smoke tests on every PR
- run full suite on main/nightly
- fail on P0 regression
- export JUnit and coverage artifacts when possible
