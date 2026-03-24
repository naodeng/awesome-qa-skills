# Rest Assured Framework Specification

## 1. Directory Convention

- `scripts/parse_api_sources.py`: multi-format API source parser
- `scripts/generate_restassured_tests.py`: normalized endpoint -> Java test class
- `scripts/templates/restassured/`: runnable Maven test template
- `generated-tests/`: output Java tests generated from parsed endpoints

## 2. Test Layer Convention

- `smoke`: core endpoint availability
- `contract`: status code + response shape checks
- `business`: key API flows and state transitions
- `negative`: invalid params, auth failure, boundary inputs

## 3. Assertion Rules

- status code assertions are mandatory
- key response field assertions are mandatory
- latency checks on critical APIs are recommended
- negative tests should validate error payload structure

## 4. Data and Environment Rules

- use environment/properties for base URL and token
- never commit secrets in test sources
- use deterministic data or isolated test fixtures
- define cleanup strategy for mutable endpoints

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

- run smoke tests on each PR
- run full suite on main/nightly
- fail on P0 regression
- export surefire/junit XML for trend tracking
