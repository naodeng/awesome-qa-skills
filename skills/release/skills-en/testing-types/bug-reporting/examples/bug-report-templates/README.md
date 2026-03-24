# Bug Report 模板和示例集

这是一个完整的缺陷报告模板和真实示例集合，帮助你编写高质量的缺陷报告。

## 📋 项目概述

- **模板数量**: 5 个（Markdown、Jira、GitHub、Excel、简化版）
- **示例数量**: 10+ 个真实场景
- **格式支持**: Markdown、Jira、GitHub Issues、Excel、JSON
- **工具脚本**: 自动化报告生成和验证

## 🎯 包含内容

### 1. 模板文件

- `template-standard.md` - 标准 Markdown 模板
- `template-jira.md` - Jira 格式模板
- `template-github.md` - GitHub Issues 模板
- `template-simple.md` - 简化版模板（快速报告）
- `template-detailed.md` - 详细版模板（复杂问题）

### 2. 真实示例

#### 功能缺陷
- `example-login-failure.md` - 登录失败
- `example-payment-error.md` - 支付错误
- `example-data-loss.md` - 数据丢失

#### 界面问题
- `example-ui-layout.md` - 布局错误
- `example-responsive.md` - 响应式问题
- `example-accessibility.md` - 可访问性问题

#### 性能问题
- `example-slow-loading.md` - 加载缓慢
- `example-memory-leak.md` - 内存泄漏

#### 兼容性问题
- `example-browser-compat.md` - 浏览器兼容性
- `example-mobile-issue.md` - 移动端问题

### 3. 最佳实践

- `best-practices.md` - 缺陷报告最佳实践
- `anti-patterns.md` - 常见错误和反模式
- `checklist.md` - 提交前检查清单

### 4. 工具脚本

- `generate-report.sh` - 自动生成报告
- `validate-report.sh` - 验证报告完整性
- `convert-format.sh` - 格式转换工具

## 🚀 快速开始

### 使用模板

```bash
# 复制标准模板
cp template-standard.md my-bug-report.md

# 编辑模板
vim my-bug-report.md

# 验证报告
./validate-report.sh my-bug-report.md
```

### 查看示例

```bash
# 查看登录失败示例
cat examples/example-login-failure.md

# 查看所有示例
ls examples/
```

### 生成报告

```bash
# 交互式生成报告
./generate-report.sh

# 指定格式生成
./generate-report.sh --format jira

# 从现有信息生成
./generate-report.sh --input bug-info.txt --output bug-report.md
```

## 📖 模板说明

### 标准模板结构

```markdown
# [模块] 问题简述

## 基本信息
- Bug ID: 
- 报告人:
- 报告日期:
- 严重程度:
- 优先级:

## 问题描述
简短描述问题

## 复现步骤
1. 步骤一
2. 步骤二
3. 步骤三

## 预期结果
应该发生什么

## 实际结果
实际发生了什么

## 环境信息
- 操作系统:
- 浏览器/应用:
- 版本:
- 测试环境:

## 影响范围
- 影响用户:
- 发生频率:
- 业务影响:

## 附件
- 截图
- 日志
- 视频

## 变通方案
如果有临时解决方法

## 相关信息
- 相关 Bug:
- 相关需求:
```

## 🎨 示例展示

### 示例 1：登录失败（功能缺陷）

```markdown
# [登录] 使用特殊字符密码无法登录

## 基本信息
- Bug ID: BUG-2024-001
- 报告人: 张三
- 报告日期: 2024-02-06
- 严重程度: High
- 优先级: P1

## 问题描述
当用户密码包含特殊字符（@、#、$、%）时，点击登录按钮无响应，
无法完成登录流程。

## 复现步骤
1. 打开登录页面 https://example.com/login
2. 输入邮箱：test@example.com
3. 输入密码：Test@123（包含 @ 符号）
4. 点击"登录"按钮
5. 观察页面响应

## 预期结果
- 系统验证用户名和密码
- 登录成功后跳转到首页
- 显示欢迎消息

## 实际结果
- 点击登录按钮后无任何响应
- 页面停留在登录页面
- 控制台显示错误：`Error: Invalid character in password field`
- 没有任何用户提示

## 环境信息
- 操作系统: macOS 13.5
- 浏览器: Chrome 120.0.6099.109
- 应用版本: v2.3.1
- 测试环境: Staging (https://staging.example.com)
- 网络: WiFi
- 屏幕分辨率: 1920x1080

## 影响范围
- **影响用户**: 所有使用特殊字符密码的用户
- **用户比例**: 约 15%（根据密码策略要求）
- **发生频率**: 100%（每次使用特殊字符密码都会出现）
- **业务影响**: 
  - 用户无法登录系统
  - 可能导致用户流失
  - 影响新用户注册（密码策略要求特殊字符）

## 附件
- 截图: login-error.png（显示登录页面和控制台错误）
- 视频: login-reproduction.mp4（完整复现过程）
- 控制台日志: console-log.txt
- 网络请求: network-log.har

## 变通方案
暂无。用户必须修改密码为不包含特殊字符才能登录。

## 技术细节
```javascript
// 控制台错误堆栈
Error: Invalid character in password field
    at validatePassword (auth.js:45)
    at handleLogin (login.js:123)
    at HTMLButtonElement.<anonymous> (login.js:89)
```

## 相关信息
- 相关需求: REQ-2024-AUTH-001（密码策略）
- 类似问题: BUG-2023-456（注册页面相同问题，已修复）
- 文档: 密码策略文档 v2.0
```

### 示例 2：界面布局问题

```markdown
# [首页] 移动端导航菜单显示异常

## 基本信息
- Bug ID: BUG-2024-002
- 报告人: 李四
- 报告日期: 2024-02-06
- 严重程度: Medium
- 优先级: P2

## 问题描述
在 iPhone 12 上，点击导航菜单图标后，菜单展开但无法关闭，
遮挡页面内容，影响用户操作。

## 复现步骤
1. 使用 iPhone 12 打开应用首页
2. 点击左上角的菜单图标（三条横线）
3. 观察菜单展开动画
4. 尝试以下操作关闭菜单：
   - 点击菜单图标
   - 点击页面其他区域
   - 滑动页面
5. 观察菜单状态

## 预期结果
- 点击菜单图标，菜单应该收起
- 点击页面其他区域，菜单应该收起
- 菜单收起后，页面恢复正常显示

## 实际结果
- 菜单保持展开状态
- 无法通过任何操作关闭菜单
- 菜单遮挡页面内容，无法点击下方元素
- 只能通过刷新页面解决

## 环境信息
- 设备: iPhone 12
- 操作系统: iOS 17.2
- 浏览器: Safari 17.2
- 屏幕尺寸: 390x844
- 应用版本: v2.3.1
- 测试环境: Production

## 影响范围
- **影响用户**: 所有 iPhone 12 用户
- **用户比例**: 约 8%（iPhone 12 用户占比）
- **发生频率**: 100%（每次打开菜单都会出现）
- **业务影响**: 
  - 影响移动端用户体验
  - 用户需要刷新页面才能继续操作
  - 可能导致用户放弃使用

## 附件
- 视频: menu-bug.mp4（展示问题复现过程）
- 截图: menu-stuck.png（菜单卡住状态）
- 截图: menu-overlay.png（菜单遮挡内容）

## 变通方案
用户可以刷新页面来关闭菜单，但会丢失当前页面状态。

## 技术细节
- 可能原因：iOS Safari 的触摸事件处理问题
- 相关代码：navigation.js 第 156-178 行
- CSS 类：.mobile-menu-open

## 相关信息
- 相关问题: BUG-2024-003（iPad 上也有类似问题）
- 测试设备: 已在 iPhone 11、13 上测试，问题相同
```

## 🔧 工具脚本使用

### 1. 生成报告脚本

```bash
#!/bin/bash
# generate-report.sh

echo "=== Bug Report Generator ==="
echo ""

# 收集基本信息
read -p "Bug 标题: " title
read -p "模块名称: " module
read -p "严重程度 (Critical/High/Medium/Low): " severity
read -p "报告人: " reporter

# 生成报告
cat > "bug-report-$(date +%Y%m%d-%H%M%S).md" << EOF
# [$module] $title

## 基本信息
- Bug ID: 待分配
- 报告人: $reporter
- 报告日期: $(date +%Y-%m-%d)
- 严重程度: $severity
- 优先级: 待评估

## 问题描述
[请描述问题]

## 复现步骤
1. [步骤一]
2. [步骤二]
3. [步骤三]

## 预期结果
[应该发生什么]

## 实际结果
[实际发生了什么]

## 环境信息
- 操作系统: 
- 浏览器/应用: 
- 版本: 
- 测试环境: 

## 影响范围
- 影响用户: 
- 发生频率: 
- 业务影响: 

## 附件
- [ ] 截图
- [ ] 视频
- [ ] 日志文件

## 变通方案
[如果有临时解决方法]

## 相关信息
- 相关 Bug: 
- 相关需求: 
EOF

echo ""
echo "✅ 报告已生成！"
```

### 2. 验证报告脚本

```bash
#!/bin/bash
# validate-report.sh

file=$1

if [ -z "$file" ]; then
    echo "用法: ./validate-report.sh <report-file>"
    exit 1
fi

echo "=== 验证缺陷报告 ==="
echo "文件: $file"
echo ""

# 检查必需字段
required_fields=(
    "问题描述"
    "复现步骤"
    "预期结果"
    "实际结果"
    "环境信息"
)

missing=0

for field in "${required_fields[@]}"; do
    if ! grep -q "$field" "$file"; then
        echo "❌ 缺少: $field"
        missing=$((missing + 1))
    else
        echo "✅ 包含: $field"
    fi
done

echo ""

if [ $missing -eq 0 ]; then
    echo "🎉 验证通过！报告包含所有必需字段。"
    exit 0
else
    echo "⚠️  验证失败！缺少 $missing 个必需字段。"
    exit 1
fi
```

## 📚 最佳实践总结

### DO（应该做）

✅ 使用清晰的标题格式：`[模块] 简短描述`
✅ 提供详细的复现步骤
✅ 包含完整的环境信息
✅ 添加截图和视频
✅ 说明影响范围和业务影响
✅ 保持客观、专业的语气
✅ 一个报告只报告一个问题

### DON'T（不应该做）

❌ 使用模糊的标题："有个 bug"
❌ 省略复现步骤
❌ 忘记环境信息
❌ 只说"不工作"而不说明具体表现
❌ 使用情绪化的语言
❌ 在一个报告中混合多个问题
❌ 提交前不检查报告质量

## 🔗 相关资源

- [完整 SKILL 文档](../../SKILL.md)
- [快速上手指南](../../quick-start.md)
- [常见问题 FAQ](../../references/local/FAQ.md)
- [贡献指南](../../references/local/CONTRIBUTING.md)

## 📄 许可证

MIT License

---

**需要帮助？** 查看 [故障排除](../../SKILL.md#故障排除--troubleshooting) 或提交 Issue
