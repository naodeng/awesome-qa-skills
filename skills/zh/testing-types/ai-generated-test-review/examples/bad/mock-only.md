# 反例：只验证 mock

可直接运行：[mock-only.test.mjs](mock-only.test.mjs)。执行 `node --test mock-only.test.mjs`；它会通过，但故意不验证真实下单逻辑。

该测试没有验证保存内容、业务结果或错误路径；即使错误订单被保存也可能通过。
