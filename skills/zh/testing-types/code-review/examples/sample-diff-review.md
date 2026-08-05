# 示例：支付回调缺少幂等保护

## 输入（脱敏）

**业务目标**：支付成功回调后把订单从「待支付」更新为「已支付」。

**技术栈**：Java / Spring；订单状态在 MySQL。

**Diff 摘要**（示意）：

```java
// OrderPaymentController.java
@PostMapping("/callback/pay")
public void onPaySuccess(@RequestBody PayCallback req) {
    orderService.markPaid(req.getOrderId());
    // 无幂等键 / 无状态校验
}
```

## 期望审查要点（示意）

### 1. 变更摘要与整体评估

- 业务目标理解：支付回调驱动订单状态变更
- 综合风险评级：**高**（回调可能重试，存在重复副作用风险）

### 2. 缺陷与风险清单

#### [P0 - 阻塞级]

- 问题文件与位置：`OrderPaymentController.java`（回调入口）
- 问题分类：幂等 / 资损隐患
- 风险描述：支付渠道重试回调时可能重复执行 `markPaid` 及后续副作用（发券、记账等），导致状态错乱或重复履约
- 修复方案：按 `orderId + paymentId` 做幂等；仅允许 `PENDING -> PAID` 状态机迁移；副作用放入幂等事务或去重表

#### [P1] / [P2]

- 视是否缺少回调验签、日志 Trace、失败重试语义等补充

### 5. 剩余风险与信息缺口

- 假设：`markPaid` 内部无幂等（用户未提供实现）
- 待补充：完整 `orderService.markPaid` 实现、是否已有去重表、回调验签逻辑
