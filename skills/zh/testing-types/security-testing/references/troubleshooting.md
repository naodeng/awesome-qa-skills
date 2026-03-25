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

