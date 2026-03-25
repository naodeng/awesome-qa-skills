# 安全测试快速上手指南

5 分钟快速掌握安全测试技能的使用方法。

## 📋 前置条件

- 了解基本的 Web 安全概念
- 熟悉 HTTP 协议
- 安装 Docker

## 🚀 快速开始

### 步骤 1：了解 OWASP Top 10

| 漏洞类型 | 风险 | 示例 |
|---------|------|------|
| 注入攻击 | 高 | SQL 注入、命令注入 |
| 失效的身份认证 | 高 | 弱密码、会话劫持 |
| 敏感数据泄露 | 高 | 未加密传输 |
| XML 外部实体 (XXE) | 中 | XML 解析漏洞 |
| 失效的访问控制 | 高 | 越权访问 |
| 安全配置错误 | 中 | 默认配置、目录列表 |
| 跨站脚本 (XSS) | 中 | 反射型、存储型 XSS |
| 不安全的反序列化 | 高 | 远程代码执行 |
| 使用含有已知漏洞的组件 | 中 | 过时的库 |
| 不足的日志记录和监控 | 低 | 无法追踪攻击 |

### 步骤 2：安装 OWASP ZAP

```bash
# 使用 Docker（推荐）
docker pull owasp/zap2docker-stable

# 或下载安装包
# macOS: brew install --cask owasp-zap
# Linux: sudo snap install zaproxy --classic
```

### 步骤 3：运行第一次扫描

```bash
# 进入示例目录
cd skills/testing-types/security-testing/examples/owasp-zap-scan

# 运行基线扫描
./run-scan.sh baseline https://test.k6.io

# 查看报告
open reports/baseline-scan-*.html
```

## 📝 核心概念

### 1. 扫描类型

#### 基线扫描 (Baseline Scan)
- **目的**: 快速识别常见安全问题
- **时间**: 5-10 分钟
- **适用**: CI/CD 集成

#### 完整扫描 (Full Scan)
- **目的**: 深度扫描，包含主动攻击
- **时间**: 30-60 分钟
- **适用**: 发布前安全审计

#### API 扫描 (API Scan)
- **目的**: 针对 REST API 的安全测试
- **时间**: 10-20 分钟
- **适用**: API 安全验证

### 2. 常见漏洞

#### SQL 注入
```sql
-- 恶意输入
1' OR '1'='1
1'; DROP TABLE users--
```

#### XSS (跨站脚本)
```html
<!-- 恶意脚本 -->
<script>alert('XSS')</script>
<img src=x onerror="alert('XSS')">
```

#### CSRF (跨站请求伪造)
```html
<!-- 恶意表单 -->
<form action="http://bank.com/transfer" method="POST">
  <input name="amount" value="1000">
  <input name="to" value="attacker">
</form>
```

### 3. 风险等级

| 级别 | 说明 | 处理 |
|------|------|------|
| High | 高危漏洞 | 立即修复 |
| Medium | 中危漏洞 | 尽快修复 |
| Low | 低危漏洞 | 计划修复 |
| Info | 信息提示 | 参考改进 |

## 🔧 常用命令

```bash
# 基线扫描
./run-scan.sh baseline https://example.com

# 完整扫描
./run-scan.sh full https://example.com

# API 扫描
./run-scan.sh api swagger.json https://api.example.com

# 使用 Docker 直接运行
docker run -t owasp/zap2docker-stable \
  zap-baseline.py -t https://example.com
```

## 🎯 安全测试检查清单

### 测试前
- [ ] 获得测试授权
- [ ] 准备测试环境
- [ ] 备份重要数据
- [ ] 通知相关团队

### 测试中
- [ ] SQL 注入测试
- [ ] XSS 测试
- [ ] CSRF 测试
- [ ] 认证测试
- [ ] 授权测试
- [ ] 会话管理测试
- [ ] 输入验证测试
- [ ] 错误处理测试

### 测试后
- [ ] 分析扫描报告
- [ ] 手动验证高危漏洞
- [ ] 生成测试报告
- [ ] 提交漏洞修复建议
- [ ] 跟踪修复进度

## ❓ 遇到问题？

1. **查看故障排除章节**：[SKILL.md#故障排除](SKILL.md#故障排除)
2. **查看示例代码**：[examples/owasp-zap-scan/](examples/owasp-zap-scan/)
3. **参考官方文档**：
   - [OWASP ZAP 文档](https://www.zaproxy.org/docs/)
   - [OWASP Top 10](https://owasp.org/www-project-top-ten/)

## 🎓 下一步

- ✅ 完成快速上手
- 📖 阅读完整的 [SKILL.md](SKILL.md)
- 🔨 运行示例项目
- 🚀 为你的项目进行安全测试
- 🤖 使用 AI 提示词生成测试用例
- 📚 学习进阶主题（渗透测试、代码审计）

---

**预计学习时间：** 5-10 分钟  
**难度级别：** 高级  
**最后更新：** 2026-02-06
