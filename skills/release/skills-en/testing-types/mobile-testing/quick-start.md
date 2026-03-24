# 移动端测试快速上手指南

5 分钟快速掌握移动端测试技能。

## 📋 前置条件

- 了解移动应用基础
- 安装 Android SDK 或 Xcode
- 安装 Appium

## 🚀 快速开始

### 步骤 1：安装 Appium

```bash
# 安装 Appium
npm install -g appium

# 安装驱动
appium driver install uiautomator2  # Android
appium driver install xcuitest      # iOS

# 验证
appium --version
```

### 步骤 2：配置环境

```bash
# Android
export ANDROID_HOME=/path/to/android-sdk
export PATH=$PATH:$ANDROID_HOME/platform-tools

# 验证
adb version
adb devices
```

### 步骤 3：运行示例

```bash
cd skills/testing-types/mobile-testing/examples/appium-android
pip install -r requirements.txt
appium &
pytest
```

## 📝 核心概念

### 1. 测试类型

- **功能测试** - 验证功能正常
- **兼容性测试** - 不同设备和系统
- **性能测试** - 响应时间、内存
- **网络测试** - 弱网、断网
- **安全测试** - 数据安全

### 2. 元素定位

```python
# Resource ID（推荐）
(AppiumBy.ID, "com.example:id/button")

# Accessibility ID
(AppiumBy.ACCESSIBILITY_ID, "login_button")

# XPath（最后选择）
(AppiumBy.XPATH, "//android.widget.Button[@text='Login']")
```

### 3. 手势操作

```python
# 滑动
driver.swipe(start_x, start_y, end_x, end_y, 500)

# 点击
driver.tap([(x, y)])

# 长按
actions.click_and_hold(element).perform()
```

## 🎯 测试检查清单

- [ ] 功能测试
- [ ] 兼容性测试
- [ ] 性能测试
- [ ] 网络测试
- [ ] 安全测试
- [ ] 生命周期测试
- [ ] 权限测试

## ❓ 遇到问题？

1. 查看 [SKILL.md#故障排除](SKILL.md#故障排除)
2. 查看 [examples/appium-android/](examples/appium-android/)
3. 参考 [Appium 文档](http://appium.io/docs/)

---

**预计学习时间：** 5-10 分钟  
**难度级别：** 高级  
**最后更新：** 2026-02-06
