# Example: Payment Callback Missing Idempotency

## Input (redacted)

**Business goal**: On successful payment callback, move the order from Pending Payment to Paid.

**Stack**: Java / Spring; order state in MySQL.

**Diff sketch**:

```java
// OrderPaymentController.java
@PostMapping("/callback/pay")
public void onPaySuccess(@RequestBody PayCallback req) {
    orderService.markPaid(req.getOrderId());
    // no idempotency key / no state guard
}
```

## Expected Review Focus (sketch)

### 1. Change Summary and Overall Assessment

- Business goal: payment callback drives order state change
- Overall risk: **High** (callbacks may retry; duplicate side effects possible)

### 2. Findings

#### [P0 - Blocker]

- File and location: `OrderPaymentController.java` (callback entry)
- Category: idempotency / financial-loss risk
- Risk: channel retries may re-enter `markPaid` and downstream side effects (coupons, ledger), causing bad state or duplicate fulfillment
- Fix: idempotency on `orderId + paymentId`; allow only `PENDING -> PAID`; put side effects behind the same dedupe/transaction boundary

#### [P1] / [P2]

- Add as needed for missing signature verification, tracing, failure/retry semantics

### 5. Residual Risks and Gaps

- Assumption: `markPaid` itself is not idempotent (implementation not provided)
- Need: full `orderService.markPaid`, any existing dedupe table, callback signature checks
