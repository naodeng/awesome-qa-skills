# Technical Summary

- The architecture consists of gateway, campaign, inventory, and order services.
- Redis caches eligibility; a message queue creates orders asynchronously.
- The APIs are `/api/seckill/join` and `/api/seckill/status`.
