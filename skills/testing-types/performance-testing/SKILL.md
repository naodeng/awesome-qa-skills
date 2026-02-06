---
name: performance-testing
version: 2.0.0
description: 默认输出 Markdown，可请求 Excel/CSV/JSON。Use for 性能测试 or performance-testing.
tags: [performance, testing, load-testing, stress-testing, k6, jmeter]
difficulty: advanced
last_updated: 2026-02-06
---

# 性能测试（中文版）

**英文版：** 见技能 `performance-testing-en`。

提示词见本目录 `prompts/performance-testing.md`。

## 何时使用

- 用户提到「性能测试」「performance-testing」
- 需要基于 Standard-version 执行该类测试或产出对应交付物
- **触发示例：**「根据以下内容生成/设计/编写…」

## 输出格式选项

默认 **Markdown**。若需 **Excel / CSV / JSON**，请在需求**末尾**说明，详见 **[output-formats.md](output-formats.md)**。

## 如何使用

1. 打开本目录 `prompts/performance-testing.md`，将虚线以下内容复制到 AI 对话。
2. 附加你的具体需求。
3. 若需 Excel/CSV/JSON，在末尾加上 output-formats.md 中的请求句。

## 代码示例

### 1. K6 负载测试

完整的 K6 性能测试示例，包含负载测试、压力测试、尖峰测试和 API 测试。

**位置：** `examples/k6-load-testing/`

**包含内容：**
- 负载测试脚本（Load Test）
- 压力测试脚本（Stress Test）
- 尖峰测试脚本（Spike Test）
- API 性能测试脚本
- 自动化运行脚本
- 详细的 README 文档

**快速开始：**
```bash
cd examples/k6-load-testing
chmod +x run-tests.sh
./run-tests.sh load
```

**测试覆盖：**
- 负载测试（模拟正常业务量）
- 压力测试（找出性能极限）
- 尖峰测试（突发流量）
- API 性能测试（REST API）
- 自定义指标和阈值

详见：[examples/k6-load-testing/README.md](examples/k6-load-testing/README.md)

## 最佳实践

### 性能测试设计原则

1. **测试类型选择**
   - 负载测试：验证系统在预期负载下的性能
   - 压力测试：找出系统的性能极限
   - 尖峰测试：测试突发流量处理能力
   - 浸泡测试：验证长时间运行的稳定性

2. **测试场景设计**
   - 基于真实用户行为
   - 合理的思考时间（Think Time）
   - 逐步增加负载
   - 包含预热和降温阶段

3. **性能指标**
   - 响应时间（Response Time）
   - 吞吐量（Throughput/RPS）
   - 错误率（Error Rate）
   - 并发用户数（Concurrent Users）
   - 资源使用率（CPU、内存、网络）

4. **阈值设置**
   - 基于业务需求定义
   - 使用百分位数（p95、p99）
   - 设置合理的错误率
   - 监控趋势变化

### 工具选择建议

| 工具 | 适用场景 | 优势 |
|------|---------|------|
| K6 | 现代化性能测试 | 脚本化、易用、云原生 |
| JMeter | 传统性能测试 | 功能丰富、GUI、插件多 |
| Gatling | Scala/Java 项目 | 高性能、报告美观 |
| Locust | Python 项目 | 易学、分布式 |
| Artillery | Node.js 项目 | 配置简单、CI/CD 友好 |

## 故障排除

### 常见问题

#### 1. 连接超时

**问题：** `request timeout` 或 `connection timeout`

**解决方案：**
```javascript
// K6 示例
export const options = {
  timeout: '60s',  // 增加超时时间
};

// 或检查网络连接和服务器状态
```

#### 2. 内存不足

**问题：** K6 或 JMeter 占用内存过高

**解决方案：**
- 减少虚拟用户数
- 使用 SharedArray 共享数据（K6）
- 分布式测试
- 增加测试机器内存

#### 3. 证书验证错误

**问题：** SSL certificate verification failed

**解决方案：**
```javascript
// K6 示例
export const options = {
  insecureSkipTLSVerify: true,  // 跳过证书验证（仅测试环境）
};
```

#### 4. 速率限制

**问题：** 被服务器限流（429 Too Many Requests）

**解决方案：**
- 增加思考时间（sleep）
- 使用随机延迟
- 分阶段增加负载
- 与服务器团队协调测试时间

#### 5. 结果不稳定

**问题：** 每次测试结果差异很大

**解决方案：**
- 确保测试环境稳定
- 多次运行取平均值
- 检查网络状况
- 隔离其他干扰因素

#### 6. 无法达到目标负载

**问题：** 实际 RPS 远低于预期

**解决方案：**
- 检查客户端资源（CPU、网络）
- 使用分布式测试
- 优化测试脚本
- 减少不必要的等待时间

#### 7. 报告数据异常

**问题：** 性能指标异常高或异常低

**解决方案：**
- 检查测试脚本逻辑
- 验证阈值设置
- 查看详细日志
- 对比历史数据

## 参考文件

- **prompts/performance-testing.md** — 性能测试 Standard-version 提示词
- **output-formats.md** — Markdown / Excel / CSV / JSON 请求说明
- **examples/k6-load-testing/** — K6 完整示例
- **quick-start.md** — 5 分钟快速上手指南
