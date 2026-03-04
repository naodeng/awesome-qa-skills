---
name: performance-testing
description: Use this skill when you need to design performance testing for load, stress, spike, endurance, or capacity objectives; triggers include 性能测试 and performance testing.
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

1. 打开本目录 `prompts/` 下对应提示词文件，复制虚线以下内容。
2. 附加你的需求与上下文（业务流程、环境、约束、验收标准）。
3. 若需非 Markdown 输出，在末尾追加 `output-formats.md` 中的请求句。

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

## 常见误区 | Common Pitfalls

- ❌ 压测模型脱离真实业务流量 → ✅ 基于生产行为构建场景与负载配比
- ❌ 只看平均响应时间 → ✅ 同时关注 p95/p99、错误率、吞吐与资源饱和
- ❌ 跳过基线与预热阶段 → ✅ 先基线、后预热、再分阶段加压
- ❌ 只看测试结果不看系统指标 → ✅ 关联 CPU/内存/IO/下游依赖做瓶颈定位

## 故障排除

详细排障步骤已迁移到 [references/troubleshooting.md](references/troubleshooting.md)。
按需加载该文件，避免主技能文档过长。
## 参考文件

- **prompts/performance-testing.md** — 性能测试 Standard-version 提示词
- **output-formats.md** — Markdown / Excel / CSV / JSON 请求说明
- **examples/k6-load-testing/** — K6 完整示例
- **quick-start.md** — 5 分钟快速上手指南
