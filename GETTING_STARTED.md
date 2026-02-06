# 开始使用 Awesome QA Skills

欢迎使用 Awesome QA Skills！本指南将帮助你快速上手。

---

## 🚀 快速开始

### 1. 选择你需要的 Skill

我们已经完成了 5 个核心 skills 的优化：

| Skill | 用途 | 难度 | 快速开始 |
|-------|------|------|---------|
| [functional-testing](skills/testing-types/functional-testing/) | Web 功能测试 | 初级 | [5分钟上手](skills/testing-types/functional-testing/quick-start.md) |
| [api-testing](skills/testing-types/api-testing/) | API 接口测试 | 中级 | [5分钟上手](skills/testing-types/api-testing/quick-start.md) |
| [automation-testing](skills/testing-types/automation-testing/) | UI 自动化测试 | 中级 | [5分钟上手](skills/testing-types/automation-testing/quick-start.md) |
| [performance-testing](skills/testing-types/performance-testing/) | 性能压力测试 | 高级 | [5分钟上手](skills/testing-types/performance-testing/quick-start.md) |
| [security-testing](skills/testing-types/security-testing/) | 安全漏洞测试 | 高级 | [5分钟上手](skills/testing-types/security-testing/quick-start.md) |

### 2. 运行代码示例

每个 skill 都包含可直接运行的完整示例：

```bash
# Functional Testing (Playwright)
cd skills/testing-types/functional-testing/examples/playwright-login
npm install
npm test

# API Testing (Postman + Newman)
cd skills/testing-types/api-testing/examples/postman-rest-api
npm install -g newman
./newman-run.sh

# Automation Testing (Selenium + Python)
cd skills/testing-types/automation-testing/examples/selenium-pom-python
pip install -r requirements.txt
pytest

# Performance Testing (K6)
cd skills/testing-types/performance-testing/examples/k6-load-testing
./run-tests.sh load

# Security Testing (OWASP ZAP)
cd skills/testing-types/security-testing/examples/owasp-zap-scan
./run-scan.sh baseline https://example.com
```

### 3. 使用 AI 提示词

每个 skill 都有专门的 AI 提示词，帮助你快速生成测试用例：

1. 打开 `skills/testing-types/{skill-name}/prompts/{skill-name}.md`
2. 复制虚线以下的内容到 AI 对话
3. 附加你的具体需求
4. AI 将生成完整的测试用例

---

## 📚 文档结构

每个 skill 包含以下文档：

```
skill-name/
├── SKILL.md                    # 主文档（完整说明）
├── quick-start.md              # 快速上手（5分钟）
├── output-formats.md           # 输出格式说明
├── prompts/                    # AI 提示词
│   └── {skill-name}.md
└── examples/                   # 代码示例
    └── example-name/
        ├── README.md           # 详细说明
        ├── 代码文件
        ├── 配置文件
        └── 运行脚本
```

---

## 🛠️ 工具脚本

我们提供了 5 个自动化工具脚本：

### 1. 生成新的 Skill

```bash
./tools/skill-generator.sh
```

### 2. 检查质量

```bash
# 检查单个 skill
./tools/quality-check.sh skills/testing-types/functional-testing

# 检查所有 skills
./tools/quality-check.sh skills
```

### 3. 检查中英文同步

```bash
./tools/sync-check.sh
```

### 4. 运行优化助手

```bash
./tools/run-optimization.sh
```

### 5. 检测项目上下文

```bash
./tools/context-detector.sh
```

---

## 📖 学习路径

### 初学者

1. 从 **functional-testing** 开始
2. 阅读 quick-start.md
3. 运行示例代码
4. 尝试修改和扩展

### 中级用户

1. 学习 **api-testing** 和 **automation-testing**
2. 理解最佳实践
3. 创建自己的测试项目
4. 集成到 CI/CD

### 高级用户

1. 掌握 **performance-testing** 和 **security-testing**
2. 优化测试策略
3. 建立测试框架
4. 贡献到社区

---

## 🎯 常见场景

### 场景 1：Web 应用测试

```bash
# 1. 功能测试
cd skills/testing-types/functional-testing/examples/playwright-login
npm test

# 2. 自动化测试
cd skills/testing-types/automation-testing/examples/selenium-pom-python
pytest

# 3. 性能测试
cd skills/testing-types/performance-testing/examples/k6-load-testing
./run-tests.sh load

# 4. 安全测试
cd skills/testing-types/security-testing/examples/owasp-zap-scan
./run-scan.sh baseline https://your-app.com
```

### 场景 2：API 测试

```bash
# 1. API 功能测试
cd skills/testing-types/api-testing/examples/postman-rest-api
./newman-run.sh

# 2. API 性能测试
cd skills/testing-types/performance-testing/examples/k6-load-testing
./run-tests.sh api

# 3. API 安全测试
cd skills/testing-types/security-testing/examples/owasp-zap-scan
./run-scan.sh api swagger.json https://api.example.com
```

### 场景 3：CI/CD 集成

```yaml
# GitHub Actions 示例
name: Test Suite

on: [push, pull_request]

jobs:
  functional-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Functional Tests
        run: |
          cd skills/testing-types/functional-testing/examples/playwright-login
          npm install
          npm test

  api-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run API Tests
        run: |
          cd skills/testing-types/api-testing/examples/postman-rest-api
          npm install -g newman
          ./newman-run.sh
```

---

## ❓ 常见问题

### Q1: 如何选择合适的测试类型？

**A**: 根据你的需求选择：
- **功能测试**: 验证功能是否正常
- **API 测试**: 测试接口是否符合规范
- **自动化测试**: 回归测试和持续集成
- **性能测试**: 验证系统性能和容量
- **安全测试**: 发现安全漏洞

### Q2: 示例代码可以直接用于生产吗？

**A**: 示例代码是学习和参考用途，生产使用需要：
- 根据实际情况调整
- 添加更多测试用例
- 完善错误处理
- 添加日志和监控

### Q3: 如何贡献代码？

**A**: 请查看 [CONTRIBUTING.md](CONTRIBUTING.md)

### Q4: 遇到问题怎么办？

**A**: 
1. 查看 skill 的故障排除章节
2. 查看 [FAQ.md](FAQ.md)
3. 提交 Issue
4. 联系维护者

### Q5: 如何获取更多帮助？

**A**:
- 📖 阅读完整文档
- 💬 加入社区讨论
- 📧 发送邮件咨询
- 🐛 提交 Issue

---

## 📊 项目统计

- ✅ **5** 个完整的 skills
- ✅ **63+** 个测试用例
- ✅ **14,700+** 行代码和文档
- ✅ **5** 个自动化工具
- ✅ **100%** 可运行示例

---

## 🎓 推荐资源

### 官方文档
- [Playwright 文档](https://playwright.dev/)
- [Selenium 文档](https://www.selenium.dev/)
- [K6 文档](https://k6.io/docs/)
- [OWASP ZAP 文档](https://www.zaproxy.org/docs/)

### 学习资源
- [测试金字塔](https://martinfowler.com/articles/practical-test-pyramid.html)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [性能测试最佳实践](https://k6.io/docs/testing-guides/)

### 社区
- GitHub Discussions
- Stack Overflow
- Reddit r/QualityAssurance

---

## 🚀 下一步

1. ✅ 选择一个 skill 开始学习
2. ✅ 运行示例代码
3. ✅ 阅读完整文档
4. ✅ 创建自己的测试项目
5. ✅ 分享你的经验

---

## 📞 获取帮助

- 📖 [完整文档](FINAL_SUMMARY.md)
- 📋 [执行摘要](EXECUTIVE_SUMMARY.md)
- 🔧 [执行指南](EXECUTION_GUIDE.md)
- ❓ [常见问题](FAQ.md)
- 🤝 [贡献指南](CONTRIBUTING.md)

---

**祝你测试愉快！** 🎉

---

*最后更新: 2026-02-06*
