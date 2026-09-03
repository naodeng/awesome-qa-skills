# Technical Summary

- The campaign service calls inventory and order services.
- Redis caches eligibility and a message queue creates orders asynchronously.
- Core APIs: `/api/seckill/join` and `/api/seckill/status`.
