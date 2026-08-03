# Desensitized curl examples for API automation fixtures.
# Use placeholders only — never real tokens.

# Create order
curl -sS -X POST "${BASE_URL}/orders" \
  -H "Authorization: Bearer ${API_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"skuId":"SKU-1001","qty":1}'

# Payment callback
curl -sS -X POST "${BASE_URL}/payments/callback" \
  -H "Content-Type: application/json" \
  -d '{"orderId":"ORD-PLACEHOLDER","result":"SUCCESS"}'

# Get order
curl -sS "${BASE_URL}/orders/ORD-PLACEHOLDER" \
  -H "Authorization: Bearer ${API_TOKEN}"
