---
name: mobile-testing
version: 2.0.0
description: 设计移动端（iOS/Android）测试方案与用例，覆盖功能、兼容性、性能、网络、安全等。默认输出 Markdown，可请求 Excel/CSV/JSON。Use for 移动端测试 or mobile testing.
tags: [mobile, testing, appium, android, ios, automation]
difficulty: advanced
last_updated: 2026-02-06
---

# 移动端测试（中文版）

**英文版：** 见技能 `mobile-testing-en`。

提示词见本目录 `prompts/mobile-testing.md`。

## 何时使用

- 用户提到「移动端测试」「mobile testing」「APP 测试」「iOS/Android 测试」
- 需要设计或执行移动端测试方案与用例（设备矩阵、系统版本、网络、生命周期等）
- **触发示例：**「根据以下需求设计移动端测试方案」「输出移动端测试用例」

## 输出格式选项

默认 **Markdown**。若需 **Excel / CSV / JSON**，请在需求**末尾**说明，详见 **[output-formats.md](output-formats.md)**。

## 如何使用

1. 打开本目录 `prompts/mobile-testing.md`，将虚线以下内容复制到 AI 对话。
2. 附加移动应用需求、平台特性或测试目标。
3. 若需 Excel/CSV/JSON，在末尾加上 output-formats.md 中的请求句。

## 代码示例

### 1. Appium Android 自动化测试

完整的 Appium + Python Android 测试示例。

**位置：** `examples/appium-android/`

**包含内容：**
- Page Object Model 架构
- 登录和导航测试
- 手势操作示例
- Pytest 配置

**快速开始：**
```bash
cd examples/appium-android
pip install -r requirements.txt
appium &
pytest
```

详见：[examples/appium-android/README.md](examples/appium-android/README.md)

## 最佳实践

### 移动测试策略

1. **设备覆盖**
   - 主流设备型号
   - 不同屏幕尺寸
   - 不同系统版本

2. **测试类型**
   - 功能测试
   - 兼容性测试
   - 性能测试
   - 网络测试
   - 安全测试

3. **自动化策略**
   - 核心流程自动化
   - 回归测试自动化
   - 手工测试补充

## 故障排除

### 常见问题

#### 1. Appium 连接失败

**解决方案**:
```bash
appium --version
adb devices
pkill -f appium && appium
```

#### 2. 元素定位失败

**解决方案**:
- 使用 Appium Inspector
- 增加等待时间
- 检查定位器

#### 3. 应用安装失败

**解决方案**:
```bash
adb install app.apk
adb uninstall com.example.app
```

## 参考文件

- **prompts/mobile-testing.md** — 移动端测试 Standard-version 提示词
- **output-formats.md** — Markdown / Excel / CSV / JSON 请求说明
- **examples/appium-android/** — Appium Android 完整示例
- **quick-start.md** — 5 分钟快速上手指南
