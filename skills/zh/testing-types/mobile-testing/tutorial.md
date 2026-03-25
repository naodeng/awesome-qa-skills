# 移动测试教程

## 📚 学习目标

完成本教程后，你将能够：
- 理解移动测试的核心概念和挑战
- 使用 Appium 编写移动自动化测试
- 测试 Android 和 iOS 应用
- 实现跨平台测试策略
- 处理移动特有的测试场景

## 🎯 前置要求

- 了解移动应用基础知识
- 基本的编程能力（JavaScript/Python/Java）
- 安装 Android Studio 或 Xcode
- 了解自动化测试概念

## 📖 教程内容

### 第1步：移动测试基础（15分钟）

#### 1.1 移动测试类型

**功能测试：**
- ✅ UI 测试
- ✅ 功能流程测试
- ✅ 兼容性测试

**非功能测试：**
- 📱 性能测试
- 🔋 电池消耗测试
- 📶 网络测试
- 💾 内存泄漏测试

**特殊场景：**
- 📞 中断测试（来电、短信）
- 🔄 屏幕旋转测试
- 🌐 多语言测试
- 🔐 安全测试

#### 1.2 移动测试挑战

```
🎯 设备碎片化
   - 不同的屏幕尺寸
   - 不同的操作系统版本
   - 不同的硬件配置

🔄 频繁的系统更新
   - iOS/Android 版本更新
   - 设备驱动更新

📱 真机 vs 模拟器
   - 真机测试更准确但成本高
   - 模拟器快速但可能不准确

🌐 网络环境
   - WiFi、4G、5G
   - 弱网、断网场景
```

### 第2步：环境搭建（30分钟）

#### 2.1 安装 Appium

```bash
# 安装 Node.js (v16+)
# 然后安装 Appium
npm install -g appium

# 安装 Appium Doctor（检查环境）
npm install -g appium-doctor

# 检查环境
appium-doctor --android
appium-doctor --ios
```

#### 2.2 Android 环境配置

**安装 Android Studio：**
1. 下载并安装 [Android Studio](https://developer.android.com/studio)
2. 安装 Android SDK
3. 配置环境变量：

```bash
# 添加到 ~/.bash_profile 或 ~/.zshrc
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

**安装 Appium UiAutomator2 Driver：**
```bash
appium driver install uiautomator2
```

#### 2.3 iOS 环境配置（仅 macOS）

**安装 Xcode：**
1. 从 App Store 安装 Xcode
2. 安装命令行工具：
```bash
xcode-select --install
```

**安装依赖：**
```bash
# 安装 Carthage
brew install carthage

# 安装 ios-deploy
npm install -g ios-deploy

# 安装 Appium XCUITest Driver
appium driver install xcuitest
```

#### 2.4 启动 Appium Server

```bash
# 启动 Appium
appium

# 或指定端口
appium -p 4723
```

### 第3步：第一个 Android 测试（25分钟）

#### 3.1 创建测试项目

```bash
mkdir mobile-testing
cd mobile-testing
npm init -y
npm install --save-dev webdriverio @wdio/cli
```

#### 3.2 配置 WebDriverIO

创建 `wdio.conf.js`：

```javascript
exports.config = {
  runner: 'local',
  port: 4723,
  specs: ['./test/specs/**/*.js'],
  maxInstances: 1,
  
  capabilities: [{
    platformName: 'Android',
    'appium:deviceName': 'Android Emulator',
    'appium:platformVersion': '13.0',
    'appium:app': '/path/to/your/app.apk',
    'appium:automationName': 'UiAutomator2',
    'appium:newCommandTimeout': 240,
  }],
  
  logLevel: 'info',
  bail: 0,
  waitforTimeout: 10000,
  connectionRetryTimeout: 120000,
  connectionRetryCount: 3,
  
  framework: 'mocha',
  mochaOpts: {
    ui: 'bdd',
    timeout: 60000
  },
};
```

#### 3.3 编写测试用例

创建 `test/specs/login.spec.js`：

```javascript
describe('登录功能测试', () => {
  it('应该成功登录', async () => {
    // 等待登录页面加载
    const usernameField = await $('~username');
    await usernameField.waitForDisplayed({ timeout: 5000 });
    
    // 输入用户名
    await usernameField.setValue('testuser');
    
    // 输入密码
    const passwordField = await $('~password');
    await passwordField.setValue('password123');
    
    // 点击登录按钮
    const loginButton = await $('~loginButton');
    await loginButton.click();
    
    // 验证登录成功
    const welcomeMessage = await $('~welcomeMessage');
    await welcomeMessage.waitForDisplayed({ timeout: 5000 });
    
    const text = await welcomeMessage.getText();
    expect(text).toContain('欢迎');
  });
  
  it('应该显示错误信息当凭证无效', async () => {
    const usernameField = await $('~username');
    await usernameField.setValue('invalid');
    
    const passwordField = await $('~password');
    await passwordField.setValue('wrong');
    
    const loginButton = await $('~loginButton');
    await loginButton.click();
    
    const errorMessage = await $('~errorMessage');
    await errorMessage.waitForDisplayed({ timeout: 5000 });
    
    const text = await errorMessage.getText();
    expect(text).toContain('用户名或密码错误');
  });
});
```

#### 3.4 运行测试

```bash
npx wdio run wdio.conf.js
```

### 第4步：iOS 测试（20分钟）

#### 4.1 配置 iOS 测试

更新 `wdio.conf.js` 添加 iOS 配置：

```javascript
capabilities: [{
  platformName: 'iOS',
  'appium:deviceName': 'iPhone 14',
  'appium:platformVersion': '16.0',
  'appium:app': '/path/to/your/app.app',
  'appium:automationName': 'XCUITest',
  'appium:newCommandTimeout': 240,
  'appium:udid': 'auto', // 或指定设备 UDID
}]
```

#### 4.2 iOS 特定测试

创建 `test/specs/ios-specific.spec.js`：

```javascript
describe('iOS 特定功能测试', () => {
  it('应该处理 iOS 权限弹窗', async () => {
    // 等待权限弹窗
    const allowButton = await $('//XCUIElementTypeButton[@name="允许"]');
    
    if (await allowButton.isDisplayed()) {
      await allowButton.click();
    }
  });
  
  it('应该测试滑动手势', async () => {
    const element = await $('~scrollView');
    
    // 向上滑动
    await element.touchAction([
      { action: 'press', x: 200, y: 400 },
      { action: 'wait', ms: 100 },
      { action: 'moveTo', x: 200, y: 100 },
      { action: 'release' }
    ]);
  });
});
```

### 第5步：Page Object 模式（30分钟）

#### 5.1 创建 Page Object

创建 `pageobjects/LoginPage.js`：

```javascript
class LoginPage {
  // 定位器
  get usernameField() { return $('~username'); }
  get passwordField() { return $('~password'); }
  get loginButton() { return $('~loginButton'); }
  get errorMessage() { return $('~errorMessage'); }
  
  // 页面操作
  async login(username, password) {
    await this.usernameField.setValue(username);
    await this.passwordField.setValue(password);
    await this.loginButton.click();
  }
  
  async getErrorMessage() {
    await this.errorMessage.waitForDisplayed({ timeout: 5000 });
    return await this.errorMessage.getText();
  }
  
  async isLoginButtonEnabled() {
    return await this.loginButton.isEnabled();
  }
}

module.exports = new LoginPage();
```

创建 `pageobjects/HomePage.js`：

```javascript
class HomePage {
  get welcomeMessage() { return $('~welcomeMessage'); }
  get menuButton() { return $('~menuButton'); }
  get logoutButton() { return $('~logoutButton'); }
  
  async getWelcomeText() {
    await this.welcomeMessage.waitForDisplayed({ timeout: 5000 });
    return await this.welcomeMessage.getText();
  }
  
  async logout() {
    await this.menuButton.click();
    await this.logoutButton.click();
  }
  
  async isDisplayed() {
    return await this.welcomeMessage.isDisplayed();
  }
}

module.exports = new HomePage();
```

#### 5.2 使用 Page Objects

创建 `test/specs/login-pom.spec.js`：

```javascript
const LoginPage = require('../pageobjects/LoginPage');
const HomePage = require('../pageobjects/HomePage');

describe('使用 POM 的登录测试', () => {
  it('应该成功登录', async () => {
    await LoginPage.login('testuser', 'password123');
    
    const welcomeText = await HomePage.getWelcomeText();
    expect(welcomeText).toContain('欢迎');
  });
  
  it('应该显示错误信息', async () => {
    await LoginPage.login('invalid', 'wrong');
    
    const error = await LoginPage.getErrorMessage();
    expect(error).toContain('错误');
  });
  
  it('应该成功登出', async () => {
    await LoginPage.login('testuser', 'password123');
    await HomePage.logout();
    
    const isLoginButtonEnabled = await LoginPage.isLoginButtonEnabled();
    expect(isLoginButtonEnabled).toBe(true);
  });
});
```

### 第6步：高级测试场景（35分钟）

#### 6.1 手势操作

```javascript
describe('手势测试', () => {
  it('应该支持滑动', async () => {
    const element = await $('~scrollView');
    
    // 向上滑动
    await element.touchAction([
      { action: 'press', x: 200, y: 400 },
      { action: 'wait', ms: 100 },
      { action: 'moveTo', x: 200, y: 100 },
      { action: 'release' }
    ]);
  });
  
  it('应该支持长按', async () => {
    const element = await $('~longPressElement');
    await element.touchAction([
      { action: 'longPress', x: 100, y: 100 },
      { action: 'release' }
    ]);
  });
  
  it('应该支持双击', async () => {
    const element = await $('~doubleTapElement');
    await element.doubleClick();
  });
  
  it('应该支持缩放', async () => {
    const element = await $('~zoomableImage');
    
    // 放大
    await driver.execute('mobile: pinch', {
      element: element.elementId,
      scale: 2.0,
      velocity: 1.0
    });
  });
});
```

#### 6.2 中断测试

```javascript
describe('中断场景测试', () => {
  it('应该处理来电中断', async () => {
    // 模拟来电
    await driver.execute('mobile: shell', {
      command: 'am',
      args: ['start', '-a', 'android.intent.action.CALL', '-d', 'tel:1234567890']
    });
    
    // 等待并处理来电
    await driver.pause(2000);
    
    // 返回应用
    await driver.activateApp('com.example.app');
    
    // 验证应用状态
    const element = await $('~mainScreen');
    expect(await element.isDisplayed()).toBe(true);
  });
  
  it('应该处理屏幕旋转', async () => {
    // 旋转到横屏
    await driver.setOrientation('LANDSCAPE');
    await driver.pause(1000);
    
    // 验证布局
    const element = await $('~landscapeElement');
    expect(await element.isDisplayed()).toBe(true);
    
    // 旋转回竖屏
    await driver.setOrientation('PORTRAIT');
  });
  
  it('应该处理应用切换', async () => {
    // 切换到后台
    await driver.background(5);
    
    // 验证应用恢复
    const element = await $('~mainScreen');
    expect(await element.isDisplayed()).toBe(true);
  });
});
```

#### 6.3 网络测试

```javascript
describe('网络场景测试', () => {
  it('应该在弱网环境下工作', async () => {
    // 设置网络为 3G
    await driver.setNetworkConnection(4); // 4 = 3G
    
    // 执行操作
    const button = await $('~loadButton');
    await button.click();
    
    // 验证加载指示器
    const loader = await $('~loadingIndicator');
    expect(await loader.isDisplayed()).toBe(true);
    
    // 恢复网络
    await driver.setNetworkConnection(6); // 6 = WiFi
  });
  
  it('应该处理离线场景', async () => {
    // 关闭网络
    await driver.setNetworkConnection(0);
    
    // 验证离线提示
    const offlineMessage = await $('~offlineMessage');
    expect(await offlineMessage.isDisplayed()).toBe(true);
    
    // 恢复网络
    await driver.setNetworkConnection(6);
  });
});
```

#### 6.4 性能测试

```javascript
describe('性能测试', () => {
  it('应该快速启动', async () => {
    const startTime = Date.now();
    
    await driver.activateApp('com.example.app');
    
    const splashScreen = await $('~splashScreen');
    await splashScreen.waitForDisplayed({ timeout: 5000 });
    
    const launchTime = Date.now() - startTime;
    expect(launchTime).toBeLessThan(3000); // 3秒内启动
  });
  
  it('应该流畅滚动', async () => {
    const scrollView = await $('~scrollView');
    
    const startTime = Date.now();
    
    // 执行滚动
    for (let i = 0; i < 10; i++) {
      await scrollView.touchAction([
        { action: 'press', x: 200, y: 400 },
        { action: 'moveTo', x: 200, y: 100 },
        { action: 'release' }
      ]);
    }
    
    const scrollTime = Date.now() - startTime;
    const fps = 10000 / scrollTime; // 计算 FPS
    
    expect(fps).toBeGreaterThan(30); // 至少 30 FPS
  });
});
```

### 第7步：跨平台测试（20分钟）

#### 7.1 创建跨平台配置

创建 `wdio.android.conf.js`：

```javascript
const baseConfig = require('./wdio.conf.js').config;

exports.config = {
  ...baseConfig,
  capabilities: [{
    platformName: 'Android',
    'appium:deviceName': 'Android Emulator',
    'appium:platformVersion': '13.0',
    'appium:app': './apps/android/app.apk',
    'appium:automationName': 'UiAutomator2',
  }],
};
```

创建 `wdio.ios.conf.js`：

```javascript
const baseConfig = require('./wdio.conf.js').config;

exports.config = {
  ...baseConfig,
  capabilities: [{
    platformName: 'iOS',
    'appium:deviceName': 'iPhone 14',
    'appium:platformVersion': '16.0',
    'appium:app': './apps/ios/app.app',
    'appium:automationName': 'XCUITest',
  }],
};
```

#### 7.2 平台特定代码

创建 `utils/platform-helper.js`：

```javascript
class PlatformHelper {
  static isAndroid() {
    return driver.isAndroid;
  }
  
  static isIOS() {
    return driver.isIOS;
  }
  
  static async getElement(androidSelector, iosSelector) {
    if (this.isAndroid()) {
      return await $(androidSelector);
    } else {
      return await $(iosSelector);
    }
  }
  
  static async scrollToElement(element) {
    if (this.isAndroid()) {
      await driver.execute('mobile: scrollGesture', {
        elementId: element.elementId,
        direction: 'down',
        percent: 1.0
      });
    } else {
      await driver.execute('mobile: scroll', {
        direction: 'down'
      });
    }
  }
}

module.exports = PlatformHelper;
```

使用平台助手：

```javascript
const PlatformHelper = require('../utils/platform-helper');

describe('跨平台测试', () => {
  it('应该在两个平台上工作', async () => {
    const button = await PlatformHelper.getElement(
      '~androidButton',
      '~iosButton'
    );
    
    await button.click();
    
    // 验证结果
    const result = await $('~result');
    expect(await result.isDisplayed()).toBe(true);
  });
});
```

### 第8步：CI/CD 集成（15分钟）

#### 8.1 GitHub Actions 配置

创建 `.github/workflows/mobile-test.yml`：

```yaml
name: Mobile Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  android-test:
    runs-on: macos-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Setup Java
        uses: actions/setup-java@v3
        with:
          distribution: 'temurin'
          java-version: '11'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Install Appium
        run: |
          npm install -g appium
          appium driver install uiautomator2
      
      - name: Start Appium
        run: appium &
      
      - name: Run Android Emulator
        uses: reactivecircus/android-emulator-runner@v2
        with:
          api-level: 29
          script: npx wdio run wdio.android.conf.js
      
      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: android-test-results
          path: test-results/
```

## 🎓 练习任务

### 初级练习
1. 为一个简单的登录页面编写测试
2. 测试基本的 UI 交互（点击、输入）
3. 验证文本和元素可见性

### 中级练习
1. 实现 Page Object 模式
2. 测试手势操作（滑动、长按）
3. 处理中断场景（来电、旋转）

### 高级练习
1. 实现跨平台测试框架
2. 添加性能测试
3. 集成到 CI/CD 流程

## 📚 延伸阅读

- [Appium 官方文档](http://appium.io/docs/en/about-appium/intro/)
- [WebDriverIO 文档](https://webdriver.io/)
- [移动测试最佳实践](https://appium.io/docs/en/about-appium/intro/)
- [Android 测试指南](https://developer.android.com/training/testing)
- [iOS 测试指南](https://developer.apple.com/documentation/xctest)

## 🔗 相关资源

- [Appium 示例代码](examples/)
- [移动测试 Skill](./SKILL.md)
- [快速开始指南](./quick-start.md)

## ❓ 常见问题

### Q: 真机测试还是模拟器测试？
A: 
- 开发阶段：使用模拟器快速迭代
- 发布前：在真机上进行完整测试
- 关键功能：必须在真机上测试

### Q: 如何处理不同屏幕尺寸？
A: 
- 使用相对定位而非绝对坐标
- 测试多种屏幕尺寸
- 使用响应式设计

### Q: 如何提高测试稳定性？
A: 
- 使用显式等待
- 添加重试机制
- 处理网络延迟
- 使用稳定的定位器

## 🎉 下一步

完成本教程后，你可以：
- 学习 [可访问性测试教程](references/local/testing-types-accessibility-testing-SKILL.md)
- 探索 [安全测试教程](references/local/testing-types-security-testing-SKILL.md)
- 查看 [性能测试教程](references/local/testing-types-performance-testing-tutorial.md)

---

*预计完成时间: 3-4 小时*  
*难度级别: 中级到高级*
