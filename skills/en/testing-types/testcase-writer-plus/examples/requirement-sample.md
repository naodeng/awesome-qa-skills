# Flash-Sale Gift Campaign Requirements

## Business objective
- A user may claim a gift after completing a flash-sale order during the campaign window.

## Core rules
- A user must be a PLUS member and have spent at least 199 CNY in the last 30 days.
- Each user may claim one gift per campaign.
- Inventory deduction must stay consistent with order status.

## Exception rules
- Reserved inventory must be restored after a failed payment.
- The UI must prevent an ineligible user from ordering and explain why.

## Non-functional requirements
- The campaign peak load is 50,000 QPS.
- The eligibility API p95 response time is below 300 ms.
