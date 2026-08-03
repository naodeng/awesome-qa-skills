# Desensitized load profile fixture

- Endpoint: `GET ${BASE_URL}/orders/{id}`
- Auth: `Authorization: Bearer ${API_TOKEN}` (placeholder only)
- Observed peak (assumed): 200 RPS
- Promo peak (assumed): 800 RPS
- Candidate SLO (assumed): P95 < 300ms, error rate < 0.1%
