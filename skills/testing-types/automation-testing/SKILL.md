---
name: automation-testing
description: Use this skill when you need to design automation testing approaches using patterns like POM, data-driven testing, or BDD; triggers include 自动化测试 and automation testing.
---

# 自动化测试（中文版）

**英文版：** 见技能 `automation-testing-en`。

提示词见本目录 `prompts/automation-testing.md`。

## 何时使用

- 用户提到「自动化测试」「automation-testing」
- 需要基于 Standard-version 执行该类测试或产出对应交付物
- **触发示例：**「根据以下内容生成/设计/编写…」

## 输出格式选项

默认 **Markdown**。若需 **Excel / CSV / JSON**，请在需求**末尾**说明，详见 **[output-formats.md](output-formats.md)**。

## 如何使用

1. 打开本目录 `prompts/` 下对应提示词文件，复制虚线以下内容。
2. 附加你的需求与上下文（业务流程、环境、约束、验收标准）。
3. 若需非 Markdown 输出，在末尾追加 `output-formats.md` 中的请求句。

## 代码示例

### 1. Selenium + Page Object Model (Python)

完整的 POM 设计模式实现，包含登录、产品管理等功能测试。

**位置：** `examples/selenium-pom-python/`

**包含内容：**
- 完整的 Page Object Model 架构
- 基础页面类（BasePage）
- 登录页面、首页页面对象
- 15+ 个测试用例
- Pytest 配置和 fixtures
- 自动截图功能
- HTML 测试报告

**快速开始：**
```bash
cd examples/selenium-pom-python
pip install -r requirements.txt
pytest
```

**测试覆盖：**
- 登录功能（有效/无效凭证、锁定用户）
- 产品列表显示
- 购物车操作（添加/移除商品）
- 产品排序功能
- 参数化测试

详见：[examples/selenium-pom-python/README.md](examples/selenium-pom-python/README.md)

## 最佳实践

### 自动化测试设计原则

1. **测试金字塔**
   - 单元测试（70%）：快速、稳定、低成本
   - 集成测试（20%）：测试模块间交互
   - UI 测试（10%）：端到端业务流程

2. **Page Object Model (POM)**
   - 页面元素和操作封装在页面类中
   - 测试用例只关注业务逻辑
   - 提高代码复用和可维护性

3. **等待策略**
   - 避免使用固定等待（time.sleep）
   - 使用显式等待（WebDriverWait）
   - 合理设置隐式等待时间

4. **测试数据管理**
   - 使用配置文件管理测试数据
   - 使用 fixtures 提供测试数据
   - 测试后清理数据

5. **测试独立性**
   - 每个测试应该独立运行
   - 不依赖其他测试的执行顺序
   - 使用 setup/teardown 管理测试环境

### 工具选择建议

| 工具 | 适用场景 | 优势 |
|------|---------|------|
| Selenium | Web UI 自动化 | 跨浏览器、多语言支持 |
| Playwright | 现代 Web 应用 | 快速、稳定、多浏览器 |
| Cypress | 前端开发者 | 易用、实时重载、调试友好 |
| Appium | 移动应用 | 跨平台、原生/混合应用 |
| Robot Framework | 关键字驱动 | 易读、非技术人员友好 |

### POM 设计模式最佳实践

```python
# ✅ 好的实践
class LoginPage(BasePage):
    # 元素定位器作为类常量
    USERNAME_INPUT = (By.ID, "username")
    
    def login(self, username, password):
        # 方法返回 self 支持链式调用
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

# ❌ 不好的实践
class LoginPage:
    def login(self, username, password):
        # 硬编码定位器
        driver.find_element(By.ID, "username").send_keys(username)
        # 在页面类中写断言
        assert driver.find_element(By.ID, "welcome").is_displayed()
```

## 常见误区 | Common Pitfalls

- ❌ 先自动化不稳定或未收敛的需求 → ✅ 优先自动化稳定且高价值的核心流程
- ❌ 大量使用脆弱定位器 → ✅ 使用稳定定位策略并统一定位规范
- ❌ 在各用例重复环境准备逻辑 → ✅ 抽离公共 setup/teardown 与夹具
- ❌ 忽略不稳定用例治理 → ✅ 记录 flaky 模式并先修复根因再扩覆盖

## 故障排除

详细排障步骤已迁移到 [references/troubleshooting.md](references/troubleshooting.md)。
按需加载该文件，避免主技能文档过长。
## 参考文件

- **prompts/automation-testing.md** — 自动化测试 Standard-version 提示词
- **output-formats.md** — Markdown / Excel / CSV / JSON 请求说明
- **examples/selenium-pom-python/** — Selenium + POM 完整示例
- **quick-start.md** — 5 分钟快速上手指南

## 目标受众

- 在真实项目中执行该测试域工作的 QA 与开发人员
- 需要结构化、可复用测试交付物的测试负责人
- 需要快速生成可落地测试产出的 AI 使用者

## 不适用场景

- 无测试范围上下文的纯线上应急处置
- 需要法律/合规最终裁定但缺少专家复核的决策
- 缺少最小输入（范围、环境、期望行为）的请求

## 关键成功因素

- 先明确范围、环境与验收标准，再生成测试内容
- 生成结果必须结合真实系统约束做二次校验
- 保持产物可追踪（需求 -> 测试点 -> 缺陷 -> 决策）

## 输出模板与解析脚本

- 模板目录：`output-templates/`
  - `template-word.md`（Word 友好结构）
  - `template-excel.tsv`（Excel 可直接粘贴）
  - `template-xmind.md`（XMind 结构化大纲）
  - `template-json.json`
  - `template-csv.csv`
  - `template-markdown.md`
- 解析脚本目录：`scripts/`
  - 解析通用：`parse_output_formats.py`
  - 解析按格式：`parse_word.py`、`parse_excel.py`、`parse_xmind.py`、`parse_json.py`、`parse_csv.py`、`parse_markdown.py`
  - 转换通用：`convert_output_formats.py`
  - 转换按格式：`convert_to_word.py`、`convert_to_excel.py`、`convert_to_xmind.py`、`convert_to_json.py`、`convert_to_csv.py`、`convert_to_markdown.py`
  - 批量转换：`batch_convert_templates.py`（批量输出到 `artifacts/`）

示例：
```bash
python3 scripts/parse_json.py output-templates/template-json.json
python3 scripts/parse_markdown.py output-templates/template-markdown.md
python3 scripts/convert_to_json.py output-templates/template-markdown.md
python3 scripts/convert_output_formats.py output-templates/template-json.json --to csv
python3 scripts/batch_convert_templates.py --skip-same
```
