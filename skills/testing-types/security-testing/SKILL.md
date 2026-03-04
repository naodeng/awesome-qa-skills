---
name: security-testing
description: Use this skill when you need to design security testing around OWASP risks, vulnerability scanning, and penetration scenarios; triggers include 安全测试 and security testing.
---

# 安全测试（中文版）

**英文版：** 见技能 `security-testing-en`。

提示词见本目录 `prompts/security-testing.md`。

## 何时使用

- 用户提到「安全测试」「security-testing」
- 需要基于 Standard-version 执行该类测试或产出对应交付物
- **触发示例：**「根据以下内容生成/设计/编写…」

## 输出格式选项

默认 **Markdown**。若需 **Excel / CSV / JSON**，请在需求**末尾**说明，详见 **[output-formats.md](output-formats.md)**。

## 如何使用

1. 打开本目录 `prompts/` 下对应提示词文件，复制虚线以下内容。
2. 附加你的需求与上下文（业务流程、环境、约束、验收标准）。
3. 若需非 Markdown 输出，在末尾追加 `output-formats.md` 中的请求句。

## 代码示例

### 1. OWASP ZAP 安全扫描

完整的 OWASP ZAP 安全测试示例，包含基线扫描、完整扫描和 API 扫描。

**位置：** `examples/owasp-zap-scan/`

**包含内容：**
- 基线扫描脚本（快速扫描）
- 完整扫描脚本（深度扫描）
- API 扫描脚本
- 自动化运行脚本
- 详细的 README 文档

**快速开始：**
```bash
cd examples/owasp-zap-scan
./run-scan.sh baseline https://example.com
```

**测试覆盖：**
- SQL 注入检测
- XSS 漏洞检测
- CSRF 漏洞检测
- 安全配置检查
- API 安全测试

详见：[examples/owasp-zap-scan/README.md](examples/owasp-zap-scan/README.md)

## 最佳实践

### 安全测试原则

1. **OWASP Top 10**
   - 注入攻击
   - 失效的身份认证
   - 敏感数据泄露
   - XML 外部实体 (XXE)
   - 失效的访问控制
   - 安全配置错误
   - 跨站脚本 (XSS)
   - 不安全的反序列化
   - 使用含有已知漏洞的组件
   - 不足的日志记录和监控

2. **测试阶段**
   - 开发阶段：静态代码分析
   - 测试阶段：动态安全测试
   - 发布前：渗透测试
   - 生产环境：持续监控

3. **测试方法**
   - 黑盒测试：不了解内部实现
   - 白盒测试：完全了解内部实现
   - 灰盒测试：部分了解内部实现

### 工具选择建议

| 工具 | 适用场景 | 优势 |
|------|---------|------|
| OWASP ZAP | Web 应用安全 | 开源、易用、自动化 |
| Burp Suite | 渗透测试 | 功能强大、专业 |
| Nmap | 网络扫描 | 端口扫描、服务识别 |
| SQLMap | SQL 注入 | 自动化注入测试 |
| Nikto | Web 服务器 | 快速漏洞扫描 |

## 常见误区 | Common Pitfalls

- ❌ 只跑工具不做威胁建模 → ✅ 先识别资产、攻击面与风险优先级
- ❌ 把扫描结果当最终结论 → ✅ 做漏洞分级、可利用性验证并过滤误报
- ❌ 漏测认证鉴权绕过场景 → ✅ 增加越权、会话劫持、权限边界测试
- ❌ 只在发版前做一次安全测试 → ✅ 在 CI 与发布门禁中持续执行安全检查

## 故障排除

详细排障步骤已迁移到 [references/troubleshooting.md](references/troubleshooting.md)。
按需加载该文件，避免主技能文档过长。
## 参考文件

- **prompts/security-testing.md** — 安全测试 Standard-version 提示词
- **output-formats.md** — Markdown / Excel / CSV / JSON 请求说明
- **examples/owasp-zap-scan/** — OWASP ZAP 完整示例
- **quick-start.md** — 5 分钟快速上手指南
