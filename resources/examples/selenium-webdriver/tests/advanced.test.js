const { Builder, By, until, Actions } = require('selenium-webdriver');
const { expect } = require('chai');

describe('Selenium 高级操作测试', function() {
  this.timeout(30000);
  let driver;

  before(async function() {
    driver = await new Builder().forBrowser('chrome').build();
  });

  after(async function() {
    await driver.quit();
  });

  describe('鼠标操作', function() {
    it('应该执行鼠标悬停', async function() {
      await driver.get('https://the-internet.herokuapp.com/hovers');
      
      const figure = await driver.findElement(By.css('.figure'));
      const actions = driver.actions({ async: true });
      
      // 鼠标悬停
      await actions.move({ origin: figure }).perform();
      
      // 等待悬停内容出现
      const caption = await driver.findElement(By.css('.figcaption'));
      await driver.wait(until.elementIsVisible(caption), 5000);
      
      const isDisplayed = await caption.isDisplayed();
      expect(isDisplayed).to.be.true;
    });

    it('应该执行右键点击', async function() {
      await driver.get('https://the-internet.herokuapp.com/context_menu');
      
      const hotSpot = await driver.findElement(By.id('hot-spot'));
      const actions = driver.actions({ async: true });
      
      // 右键点击
      await actions.contextClick(hotSpot).perform();
      
      // 等待 alert 出现
      await driver.wait(until.alertIsPresent(), 5000);
      
      const alert = await driver.switchTo().alert();
      const text = await alert.getText();
      expect(text).to.include('context menu');
      
      await alert.accept();
    });

    it('应该执行双击', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      // 注意：这个网站没有双击示例，这里展示通用方法
      const element = await driver.findElement(By.css('h1'));
      const actions = driver.actions({ async: true });
      
      // 双击
      await actions.doubleClick(element).perform();
      
      // 验证双击效果（实际应用中会有具体的验证）
      const isDisplayed = await element.isDisplayed();
      expect(isDisplayed).to.be.true;
    });

    it('应该执行拖拽操作', async function() {
      await driver.get('https://the-internet.herokuapp.com/drag_and_drop');
      
      const columnA = await driver.findElement(By.id('column-a'));
      const columnB = await driver.findElement(By.id('column-b'));
      
      const actions = driver.actions({ async: true });
      
      // 拖拽（注意：HTML5 拖拽可能需要特殊处理）
      await actions.dragAndDrop(columnA, columnB).perform();
      
      // 等待动画完成
      await driver.sleep(1000);
    });

    it('应该执行鼠标移动到坐标', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      const actions = driver.actions({ async: true });
      
      // 移动到指定坐标
      await actions.move({ x: 100, y: 100 }).perform();
      
      // 验证鼠标移动（实际应用中会有具体的验证）
      expect(true).to.be.true;
    });
  });

  describe('窗口和标签页操作', function() {
    it('应该切换窗口', async function() {
      await driver.get('https://the-internet.herokuapp.com/windows');
      
      const originalWindow = await driver.getWindowHandle();
      
      // 点击打开新窗口
      const link = await driver.findElement(By.linkText('Click Here'));
      await link.click();
      
      // 等待新窗口出现
      await driver.wait(
        async () => (await driver.getAllWindowHandles()).length === 2,
        5000
      );
      
      // 获取所有窗口句柄
      const windows = await driver.getAllWindowHandles();
      
      // 切换到新窗口
      for (const window of windows) {
        if (window !== originalWindow) {
          await driver.switchTo().window(window);
          break;
        }
      }
      
      // 验证新窗口内容
      const heading = await driver.findElement(By.css('h3'));
      const text = await heading.getText();
      expect(text).to.equal('New Window');
      
      // 关闭新窗口
      await driver.close();
      
      // 切换回原窗口
      await driver.switchTo().window(originalWindow);
    });

    it('应该获取窗口大小和位置', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      // 获取窗口大小
      const size = await driver.manage().window().getRect();
      expect(size.width).to.be.greaterThan(0);
      expect(size.height).to.be.greaterThan(0);
      
      console.log('窗口大小:', size);
    });

    it('应该设置窗口大小', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      // 设置窗口大小
      await driver.manage().window().setRect({ width: 1024, height: 768 });
      
      const size = await driver.manage().window().getRect();
      expect(size.width).to.equal(1024);
      expect(size.height).to.equal(768);
    });

    it('应该最大化窗口', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      // 最大化窗口
      await driver.manage().window().maximize();
      
      const size = await driver.manage().window().getRect();
      expect(size.width).to.be.greaterThan(1000);
    });
  });

  describe('Frame 操作', function() {
    it('应该切换到 iframe', async function() {
      await driver.get('https://the-internet.herokuapp.com/iframe');
      
      // 切换到 iframe
      const iframe = await driver.findElement(By.id('mce_0_ifr'));
      await driver.switchTo().frame(iframe);
      
      // 在 iframe 中操作
      const editor = await driver.findElement(By.id('tinymce'));
      await editor.clear();
      await editor.sendKeys('Hello from Selenium!');
      
      const text = await editor.getText();
      expect(text).to.equal('Hello from Selenium!');
      
      // 切换回主文档
      await driver.switchTo().defaultContent();
    });

    it('应该通过索引切换 frame', async function() {
      await driver.get('https://the-internet.herokuapp.com/nested_frames');
      
      // 切换到顶部 frame
      await driver.switchTo().frame(0);
      
      // 切换到左侧 frame
      await driver.switchTo().frame(0);
      
      const body = await driver.findElement(By.tagName('body'));
      const text = await body.getText();
      expect(text).to.include('LEFT');
      
      // 切换回主文档
      await driver.switchTo().defaultContent();
    });

    it('应该在嵌套 frame 中导航', async function() {
      await driver.get('https://the-internet.herokuapp.com/nested_frames');
      
      // 切换到顶部 frame
      await driver.switchTo().frame('frame-top');
      
      // 切换到中间 frame
      await driver.switchTo().frame('frame-middle');
      
      const content = await driver.findElement(By.id('content'));
      const text = await content.getText();
      expect(text).to.include('MIDDLE');
      
      // 切换回主文档
      await driver.switchTo().defaultContent();
    });
  });

  describe('Alert 处理', function() {
    it('应该处理简单 alert', async function() {
      await driver.get('https://the-internet.herokuapp.com/javascript_alerts');
      
      // 触发 alert
      const button = await driver.findElement(By.css('button[onclick="jsAlert()"]'));
      await button.click();
      
      // 等待 alert 出现
      await driver.wait(until.alertIsPresent(), 5000);
      
      // 切换到 alert
      const alert = await driver.switchTo().alert();
      const text = await alert.getText();
      expect(text).to.include('I am a JS Alert');
      
      // 接受 alert
      await alert.accept();
      
      // 验证结果
      const result = await driver.findElement(By.id('result'));
      const resultText = await result.getText();
      expect(resultText).to.include('successfully');
    });

    it('应该处理 confirm 对话框', async function() {
      await driver.get('https://the-internet.herokuapp.com/javascript_alerts');
      
      // 触发 confirm
      const button = await driver.findElement(By.css('button[onclick="jsConfirm()"]'));
      await button.click();
      
      await driver.wait(until.alertIsPresent(), 5000);
      
      const alert = await driver.switchTo().alert();
      const text = await alert.getText();
      expect(text).to.include('I am a JS Confirm');
      
      // 点击确定
      await alert.accept();
      
      const result = await driver.findElement(By.id('result'));
      let resultText = await result.getText();
      expect(resultText).to.include('Ok');
      
      // 再次触发并取消
      await button.click();
      await driver.wait(until.alertIsPresent(), 5000);
      const alert2 = await driver.switchTo().alert();
      await alert2.dismiss();
      
      resultText = await result.getText();
      expect(resultText).to.include('Cancel');
    });

    it('应该处理 prompt 对话框', async function() {
      await driver.get('https://the-internet.herokuapp.com/javascript_alerts');
      
      // 触发 prompt
      const button = await driver.findElement(By.css('button[onclick="jsPrompt()"]'));
      await button.click();
      
      await driver.wait(until.alertIsPresent(), 5000);
      
      const alert = await driver.switchTo().alert();
      
      // 输入文本
      await alert.sendKeys('Hello Selenium');
      
      // 接受
      await alert.accept();
      
      // 验证结果
      const result = await driver.findElement(By.id('result'));
      const resultText = await result.getText();
      expect(resultText).to.include('Hello Selenium');
    });
  });

  describe('Cookie 操作', function() {
    it('应该添加 cookie', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      // 添加 cookie
      await driver.manage().addCookie({
        name: 'test_cookie',
        value: 'test_value'
      });
      
      // 获取 cookie
      const cookie = await driver.manage().getCookie('test_cookie');
      expect(cookie.value).to.equal('test_value');
    });

    it('应该获取所有 cookies', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      const cookies = await driver.manage().getCookies();
      expect(cookies).to.be.an('array');
    });

    it('应该删除 cookie', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      // 添加 cookie
      await driver.manage().addCookie({
        name: 'temp_cookie',
        value: 'temp_value'
      });
      
      // 删除 cookie
      await driver.manage().deleteCookie('temp_cookie');
      
      // 验证已删除
      const cookie = await driver.manage().getCookie('temp_cookie');
      expect(cookie).to.be.null;
    });

    it('应该删除所有 cookies', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      // 删除所有 cookies
      await driver.manage().deleteAllCookies();
      
      const cookies = await driver.manage().getCookies();
      expect(cookies).to.be.empty;
    });
  });

  describe('截图操作', function() {
    it('应该截取整个页面', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      // 截图
      const screenshot = await driver.takeScreenshot();
      expect(screenshot).to.be.a('string');
      expect(screenshot.length).to.be.greaterThan(0);
      
      // 可以保存截图
      // const fs = require('fs');
      // fs.writeFileSync('screenshot.png', screenshot, 'base64');
    });

    it('应该截取特定元素', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      const heading = await driver.findElement(By.css('h1'));
      const screenshot = await heading.takeScreenshot();
      
      expect(screenshot).to.be.a('string');
      expect(screenshot.length).to.be.greaterThan(0);
    });
  });

  describe('JavaScript 高级操作', function() {
    it('应该滚动到元素', async function() {
      await driver.get('https://the-internet.herokuapp.com/large');
      
      const table = await driver.findElement(By.id('large-table'));
      
      // 滚动到元素
      await driver.executeScript('arguments[0].scrollIntoView(true);', table);
      
      // 验证元素可见
      const isDisplayed = await table.isDisplayed();
      expect(isDisplayed).to.be.true;
    });

    it('应该高亮元素', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      const heading = await driver.findElement(By.css('h1'));
      
      // 高亮元素
      await driver.executeScript(`
        arguments[0].style.border = '3px solid red';
        arguments[0].style.backgroundColor = 'yellow';
      `, heading);
      
      await driver.sleep(1000);
      
      // 移除高亮
      await driver.executeScript(`
        arguments[0].style.border = '';
        arguments[0].style.backgroundColor = '';
      `, heading);
    });

    it('应该获取元素的计算样式', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      const heading = await driver.findElement(By.css('h1'));
      
      // 获取计算样式
      const fontSize = await driver.executeScript(`
        return window.getComputedStyle(arguments[0]).fontSize;
      `, heading);
      
      expect(fontSize).to.be.a('string');
      console.log('字体大小:', fontSize);
    });

    it('应该触发自定义事件', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      const element = await driver.findElement(By.css('h1'));
      
      // 触发自定义事件
      await driver.executeScript(`
        var event = new CustomEvent('customEvent', { detail: 'test' });
        arguments[0].dispatchEvent(event);
      `, element);
      
      // 验证事件触发（实际应用中会有具体的验证）
      expect(true).to.be.true;
    });
  });

  describe('性能监控', function() {
    it('应该获取页面加载时间', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      // 获取性能数据
      const timing = await driver.executeScript(`
        return window.performance.timing;
      `);
      
      const loadTime = timing.loadEventEnd - timing.navigationStart;
      console.log('页面加载时间:', loadTime, 'ms');
      
      expect(loadTime).to.be.greaterThan(0);
    });

    it('应该获取资源加载信息', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      // 获取资源加载信息
      const resources = await driver.executeScript(`
        return window.performance.getEntriesByType('resource');
      `);
      
      expect(resources).to.be.an('array');
      console.log('资源数量:', resources.length);
    });
  });
});
