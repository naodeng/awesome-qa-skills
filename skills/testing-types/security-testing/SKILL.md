---
name: security-testing
version: 2.0.0
description: 默认输出 Markdown，可请求 Excel/CSV/JSON。Use for 安全测试 or security-testing.
tags: [security, testing, owasp, zap, penetration-testing, vulnerability]
difficulty: advanced
last_updated: 2026-02-06
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

1. 打开本目录 `prompts/security-testing.md`，将虚线以下内容复制到 AI 对话。
2. 附加你的具体需求。
3. 若需 Excel/CSV/JSON，在末尾加上 output-formats.md 中的请求句。

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

## 故障排除

### 常见问题

#### 1. ZAP 扫描超时

**问题**: 扫描时间过长或超时

**解决方案**:
```bash
# 增加超时时间
zap-baseline.py -t http://example.com --timeout 300

# 限制扫描深度
zap-baseline.py -t http://example.com -m 3
```

#### 2. 误报过多

**问题**: 扫描结果包含大量误报

**解决方案**:
- 使用自定义扫描策略
- 排除已知的误报
- 手动验证高危漏洞
- 调整扫描级别

#### 3. 无法扫描需要认证的页面

**问题**: ZAP 无法访问登录后的页面

**解决方案**:
```bash
# 配置认证
zap-cli auth \
  --auth-mode form \
  --auth-url http://example.com/login \
  --auth-username user \
  --auth-password pass
```

#### 4. Docker 权限问题

**问题**: 报告文件无法写入

**解决方案**:
```bash
# 使用正确的权限
docker run -u $(id -u):$(id -g) \
  -v $(pwd):/zap/wrk/:rw \
  owasp/zap2docker-stable \
  zap-baseline.py -t http://example.com
```

#### 5. 证书验证错误

**问题**: SSL certificate verification failed

**解决方案**:
```bash
# 跳过证书验证（仅测试环境）
zap-baseline.py -t https://example.com --hook-script skip-cert-check.py
```

#### 6. 扫描被 WAF 拦截

**问题**: 请求被 Web 应用防火墙拦截

**解决方案**:
- 降低扫描速度
- 使用随机 User-Agent
- 与安全团队协调测试时间
- 使用白名单 IP

#### 7. 报告解读困难

**问题**: 不理解扫描报告中的漏洞

**解决方案**:
- 查阅 OWASP 文档
- 手动验证漏洞
- 咨询安全专家
- 参考 CVE 数据库

## 参考文件

- **prompts/security-testing.md** — 安全测试 Standard-version 提示词
- **output-formats.md** — Markdown / Excel / CSV / JSON 请求说明
- **examples/owasp-zap-scan/** — OWASP ZAP 完整示例
- **quick-start.md** — 5 分钟快速上手指南
