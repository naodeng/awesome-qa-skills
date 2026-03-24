# Bruno Framework Specification

## 1. Directory Convention

- `scripts/parse_api_sources.py`: multi-format API source parser
- `scripts/generate_bruno_requests.py`: normalized endpoint -> Bruno requests
- `scripts/templates/bruno/`: runnable Bruno baseline collection
- `generated-bruno/`: generated collection output

## 2. Test Layer Convention

- `smoke`: core endpoint availability
- `contract`: status code + response shape checks
- `business`: key API flow and state transition checks
- `negative`: invalid params, auth failure, boundary inputs

## 3. Assertion Rules

- status code checks are mandatory
- response-time checks for critical endpoints are recommended
- negative tests must validate error structure
- use environment-scoped variables for auth and host

## 4. Data and Environment Rules

- use `{{baseUrl}}` and token variables
- never commit secrets into collection files
- keep test data deterministic or seed-controlled
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

- run smoke collection on each PR
- run full collection on main/nightly
- fail on P0 regressions
- export machine-readable reports for trend tracking
