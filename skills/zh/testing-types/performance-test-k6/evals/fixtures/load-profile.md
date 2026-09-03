# 脱敏负载配置样例

- 接口：`GET ${BASE_URL}/orders/{id}`
- 认证：`Authorization: Bearer ${API_TOKEN}`（仅为占位符）
- 观察到的峰值（假设）：200 RPS
- 促销峰值（假设）：800 RPS
- 候选 SLO（假设）：P95 < 300 ms，错误率 < 0.1%
