# Local Reference

This file is an in-skill formal reference migrated from `_external`.

Original file: `testing-types__security-testing__examples__owasp-zap-scan__README.md`

---

# Snapshot Reference

This file is a localized snapshot for skill portability.

---
# OWASP ZAP 安全测试示例

这是一个使用 OWASP ZAP (Zed Attack Proxy) 进行安全测试的完整示例。

## 📋 项目结构

```
owasp-zap-scan/
├── README.md                    # 本文件
├── scripts/                     # 测试脚本
│   ├── baseline-scan.sh        # 基线扫描
│   ├── full-scan.sh            # 完整扫描
│   ├── api-scan.sh             # API 扫描
│   └── spider-scan.sh          # 爬虫扫描
├── config/                      # 配置文件
│   ├── zap-config.conf         # ZAP 配置
│   └── scan-policy.policy      # 扫描策略
├── reports/                     # 测试报告（自动生成）
└── run-scan.sh                 # 运行脚本
```

## 🎯 安全测试类型

### 1. 基线扫描 (Baseline Scan)
快速扫描，识别常见的安全问题。

**适用场景**: CI/CD 集成、快速验证

### 2. 完整扫描 (Full Scan)
深度扫描，包含主动攻击测试。

**适用场景**: 发布前安全审计

### 3. API 扫描 (API Scan)
针对 REST API 的安全测试。

**适用场景**: API 安全验证

### 4. 爬虫扫描 (Spider Scan)
发现应用的所有页面和端点。

**适用场景**: 全面的安全评估

## 🚀 快速开始

### 1. 安装 OWASP ZAP

```bash
# macOS
brew install --cask owasp-zap

# Linux (Debian/Ubuntu)
sudo snap install zaproxy --classic

# Windows
# 下载安装包: https://www.zaproxy.org/download/

# Docker
docker pull owasp/zap2docker-stable
```

### 2. 运行基线扫描

```bash
# 使用脚本
./run-scan.sh baseline https://example.com

# 或直接使用 ZAP
zap-baseline.py -t https://example.com -r report.html
```

### 3. 查看报告

```bash
# HTML 报告
open reports/baseline-scan-*.html

# JSON 报告
cat reports/baseline-scan-*.json
```

## 📝 脚本示例

### 基线扫描脚本

```bash
#!/bin/bash
# baseline-scan.sh

TARGET_URL="$1"
REPORT_DIR="reports"

mkdir -p "$REPORT_DIR"

docker run -v $(pwd):/zap/wrk/:rw \
  -t owasp/zap2docker-stable \
  zap-baseline.py \
  -t "$TARGET_URL" \
  -r "baseline-scan-$(date +%Y%m%d-%H%M%S).html" \
  -J "baseline-scan-$(date +%Y%m%d-%H%M%S).json"
```


### 完整扫描脚本

```bash
#!/bin/bash
# full-scan.sh

TARGET_URL="$1"
REPORT_DIR="reports"

mkdir -p "$REPORT_DIR"

docker run -v $(pwd):/zap/wrk/:rw \
  -t owasp/zap2docker-stable \
  zap-full-scan.py \
  -t "$TARGET_URL" \
  -r "full-scan-$(date +%Y%m%d-%H%M%S).html" \
  -J "full-scan-$(date +%Y%m%d-%H%M%S).json"
```

### API 扫描脚本

```bash
#!/bin/bash
# api-scan.sh

API_DEFINITION="$1"  # OpenAPI/Swagger 文件
TARGET_URL="$2"
REPORT_DIR="reports"

mkdir -p "$REPORT_DIR"

docker run -v $(pwd):/zap/wrk/:rw \
  -t owasp/zap2docker-stable \
  zap-api-scan.py \
  -t "$API_DEFINITION" \
  -f openapi \
  -r "api-scan-$(date +%Y%m%d-%H%M%S).html" \
  -J "api-scan-$(date +%Y%m%d-%H%M%S).json"
```

## 🔍 常见安全漏洞检测

### 1. SQL 注入 (SQL Injection)

**测试方法**:
```bash
# 使用 ZAP 扫描
zap-cli quick-scan -s xss,sqli http://example.com

# 手动测试
curl "http://example.com/user?id=1' OR '1'='1"
```

**防护措施**:
- 使用参数化查询
- 输入验证和过滤
- 最小权限原则

### 2. 跨站脚本 (XSS)

**测试方法**:
```bash
# 测试反射型 XSS
curl "http://example.com/search?q=<script>alert('XSS')</script>"

# 测试存储型 XSS
# 在表单中提交恶意脚本
```

**防护措施**:
- 输出编码
- Content Security Policy (CSP)
- HttpOnly Cookie

### 3. 跨站请求伪造 (CSRF)

**测试方法**:
```html
<!-- 创建恶意页面 -->
<form action="http://example.com/transfer" method="POST">
  <input type="hidden" name="amount" value="1000">
  <input type="hidden" name="to" value="attacker">
</form>
<script>document.forms[0].submit();</script>
```

**防护措施**:
- CSRF Token
- SameSite Cookie
- 验证 Referer

### 4. 不安全的直接对象引用 (IDOR)

**测试方法**:
```bash
# 尝试访问其他用户的资源
curl http://example.com/api/users/1
curl http://example.com/api/users/2
curl http://example.com/api/users/3
```

**防护措施**:
- 访问控制检查
- 使用 UUID 而非递增 ID
- 权限验证

### 5. 安全配置错误

**检查项**:
- 默认凭证
- 目录列表
- 详细错误信息
- 不必要的服务
- 过时的组件

### 6. 敏感数据泄露

**检查项**:
- HTTPS 使用
- 敏感数据加密
- 密码存储
- API 密钥暴露

### 7. 缺少访问控制

**测试方法**:
```bash
# 未授权访问测试
curl http://example.com/admin
curl -H "Authorization: Bearer invalid_token" http://example.com/api/admin
```

## 📊 ZAP 扫描报告解读

### 风险等级

| 级别 | 说明 | 处理优先级 |
|------|------|-----------|
| High | 高危漏洞 | 立即修复 |
| Medium | 中危漏洞 | 尽快修复 |
| Low | 低危漏洞 | 计划修复 |
| Informational | 信息提示 | 参考改进 |

### 常见告警

#### SQL Injection
```
风险: High
描述: 应用可能存在 SQL 注入漏洞
URL: http://example.com/user?id=1
参数: id
攻击: 1' OR '1'='1
```

#### XSS (Reflected)
```
风险: High
描述: 应用存在反射型 XSS 漏洞
URL: http://example.com/search?q=test
参数: q
攻击: <script>alert('XSS')</script>
```

#### Missing Anti-CSRF Tokens
```
风险: Medium
描述: 表单缺少 CSRF 保护
URL: http://example.com/transfer
方法: POST
```

## 🔧 高级功能

### 1. 自定义扫描策略

创建 `scan-policy.policy`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<policy>
  <name>Custom Policy</name>
  <scanner>
    <id>40018</id>  <!-- SQL Injection -->
    <enabled>true</enabled>
    <level>HIGH</level>
  </scanner>
  <scanner>
    <id>40012</id>  <!-- XSS -->
    <enabled>true</enabled>
    <level>HIGH</level>
  </scanner>
</policy>
```

### 2. 认证扫描

```bash
# 使用认证信息
zap-cli quick-scan \
  --auth-mode form \
  --auth-url http://example.com/login \
  --auth-username admin \
  --auth-password secret \
  http://example.com
```

### 3. 排除特定 URL

```bash
# 排除登出和删除操作
zap-baseline.py \
  -t http://example.com \
  -x ".*logout.*" \
  -x ".*delete.*"
```

### 4. 集成到 CI/CD

#### GitHub Actions
```yaml
name: Security Scan

on: [push, pull_request]

jobs:
  zap_scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: ZAP Baseline Scan
        uses: zaproxy/action-baseline@v0.7.0
        with:
          target: 'https://example.com'
          rules_file_name: '.zap/rules.tsv'
          cmd_options: '-a'
```

#### GitLab CI
```yaml
zap_scan:
  image: owasp/zap2docker-stable
  script:
    - zap-baseline.py -t https://example.com -r report.html
  artifacts:
    paths:
      - report.html
    expire_in: 1 week
```

## 🎯 最佳实践

### 1. 扫描策略

- ✅ 开发阶段：每次提交运行基线扫描
- ✅ 测试阶段：每日运行完整扫描
- ✅ 发布前：运行深度扫描和手动测试
- ✅ 生产环境：定期运行被动扫描

### 2. 漏洞修复优先级

1. **立即修复** (High)
   - SQL 注入
   - XSS
   - 远程代码执行
   - 认证绕过

2. **尽快修复** (Medium)
   - CSRF
   - IDOR
   - 信息泄露
   - 安全配置错误

3. **计划修复** (Low)
   - 缺少安全头
   - Cookie 安全
   - 版本信息泄露

### 3. 安全测试检查清单

- [ ] SQL 注入测试
- [ ] XSS 测试（反射型、存储型、DOM型）
- [ ] CSRF 测试
- [ ] 认证和授权测试
- [ ] 会话管理测试
- [ ] 输入验证测试
- [ ] 错误处理测试
- [ ] 加密测试
- [ ] 业务逻辑测试
- [ ] API 安全测试

## 🐛 常见问题

### 1. ZAP 扫描超时

**问题**: 扫描时间过长或超时

**解决方案**:
```bash
# 增加超时时间
zap-baseline.py -t http://example.com --timeout 300

# 限制扫描深度
zap-baseline.py -t http://example.com -m 3
```

### 2. 误报过多

**问题**: 扫描结果包含大量误报

**解决方案**:
- 使用自定义扫描策略
- 排除已知的误报
- 手动验证高危漏洞

### 3. 无法扫描需要认证的页面

**问题**: ZAP 无法访问登录后的页面

**解决方案**:
```bash
# 配置认证
zap-cli --api-key <key> auth \
  --auth-mode form \
  --auth-url http://example.com/login \
  --auth-username user \
  --auth-password pass
```

### 4. Docker 权限问题

**问题**: 报告文件无法写入

**解决方案**:
```bash
# 使用正确的权限
docker run -u $(id -u):$(id -g) \
  -v $(pwd):/zap/wrk/:rw \
  owasp/zap2docker-stable \
  zap-baseline.py -t http://example.com
```

## 📚 参考资源

- OWASP ZAP 官方文档 (https://www.zaproxy.org/docs/)
- OWASP Top 10 (https://owasp.org/www-project-top-ten/)
- ZAP Docker 镜像 (https://www.zaproxy.org/docs/docker/)
- ZAP API 文档 (https://www.zaproxy.org/docs/api/)

## 🎓 学习路径

1. ✅ 了解常见安全漏洞（OWASP Top 10）
2. ✅ 安装和配置 ZAP
3. ✅ 运行基线扫描
4. ✅ 理解扫描报告
5. ✅ 手动验证漏洞
6. ✅ 集成到 CI/CD
7. ✅ 学习高级扫描技术

---

**难度级别**: 高级  
**预计学习时间**: 60-90 分钟  
**最后更新**: 2026-02-06
