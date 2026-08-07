const { Builder, By, until } = require('selenium-webdriver');
const { expect } = require('chai');

describe('Selenium 等待策略测试', function() {
  this.timeout(30000);
  let driver;

  before(async function() {
    driver = await new Builder().forBrowser('chrome').build();
  });

  after(async function() {
    await driver.quit();
  });

  describe('显式等待 (Explicit Wait)', function() {
    it('应该等待元素出现', async function() {
      await driver.get('https://the-internet.herokuapp.com/dynamic_loading/1');
      
      // 点击开始按钮
      const startButton = await driver.findElement(By.css('#start button'));
      await startButton.click();
      
      // 显式等待元素出现
      const finishElement = await driver.wait(
        until.elementLocated(By.id('finish')),
        10000
      );
      
      // 等待元素可见
      await driver.wait(until.elementIsVisible(finishElement), 10000);
      
      const text = await finishElement.getText();
      expect(text).to.equal('Hello World!');
    });

    it('应该等待元素可点击', async function() {
      await driver.get('https://the-internet.herokuapp.com/dynamic_controls');
      
      // 点击移除按钮
      const removeButton = await driver.findElement(By.css('#checkbox-example button'));
      await removeButton.click();
      
      // 等待加载完成
      await driver.wait(
        until.elementLocated(By.css('#message')),
        10000
      );
      
      // 点击添加按钮
      const addButton = await driver.findElement(By.css('#checkbox-example button'));
      await addButton.click();
      
      // 等待复选框可点击
      const checkbox = await driver.wait(
        until.elementLocated(By.css('#checkbox')),
        10000
      );
      
      await driver.wait(until.elementIsEnabled(checkbox), 10000);
      
      const isEnabled = await checkbox.isEnabled();
      expect(isEnabled).to.be.true;
    });

    it('应该等待元素消失', async function() {
      await driver.get('https://the-internet.herokuapp.com/dynamic_loading/1');
      
      const startButton = await driver.findElement(By.css('#start button'));
      await startButton.click();
      
      // 等待加载指示器出现
      const loadingIndicator = await driver.findElement(By.id('loading'));
      await driver.wait(until.elementIsVisible(loadingIndicator), 5000);
      
      // 等待加载指示器消失
      await driver.wait(until.elementIsNotVisible(loadingIndicator), 10000);
      
      const isDisplayed = await loadingIndicator.isDisplayed();
      expect(isDisplayed).to.be.false;
    });

    it('应该等待文本出现', async function() {
      await driver.get('https://the-internet.herokuapp.com/dynamic_loading/2');
      
      const startButton = await driver.findElement(By.css('#start button'));
      await startButton.click();
      
      // 等待特定文本出现
      await driver.wait(
        until.elementTextIs(
          await driver.findElement(By.id('finish')),
          'Hello World!'
        ),
        10000
      );
      
      const finishElement = await driver.findElement(By.id('finish'));
      const text = await finishElement.getText();
      expect(text).to.equal('Hello World!');
    });
  });

  describe('隐式等待 (Implicit Wait)', function() {
    it('应该使用隐式等待查找元素', async function() {
      // 设置隐式等待
      await driver.manage().setTimeouts({ implicit: 10000 });
      
      await driver.get('https://the-internet.herokuapp.com/dynamic_loading/1');
      
      const startButton = await driver.findElement(By.css('#start button'));
      await startButton.click();
      
      // 隐式等待会自动等待元素出现
      const finishElement = await driver.findElement(By.id('finish'));
      
      // 但仍需要等待元素可见
      await driver.wait(until.elementIsVisible(finishElement), 10000);
      
      const text = await finishElement.getText();
      expect(text).to.equal('Hello World!');
      
      // 重置隐式等待
      await driver.manage().setTimeouts({ implicit: 0 });
    });
  });

  describe('流畅等待 (Fluent Wait)', function() {
    it('应该使用自定义条件等待', async function() {
      await driver.get('https://the-internet.herokuapp.com/dynamic_loading/1');
      
      const startButton = await driver.findElement(By.css('#start button'));
      await startButton.click();
      
      // 自定义等待条件
      const customCondition = async function() {
        try {
          const element = await driver.findElement(By.id('finish'));
          const isDisplayed = await element.isDisplayed();
          if (isDisplayed) {
            const text = await element.getText();
            return text === 'Hello World!';
          }
          return false;
        } catch (error) {
          return false;
        }
      };
      
      // 使用流畅等待
      await driver.wait(customCondition, 10000, '元素未在指定时间内出现');
      
      const finishElement = await driver.findElement(By.id('finish'));
      const text = await finishElement.getText();
      expect(text).to.equal('Hello World!');
    });

    it('应该等待元素属性变化', async function() {
      await driver.get('https://the-internet.herokuapp.com/dynamic_controls');
      
      // 点击启用按钮
      const enableButton = await driver.findElement(By.css('#input-example button'));
      await enableButton.click();
      
      // 等待输入框启用
      const inputField = await driver.findElement(By.css('#input-example input'));
      
      await driver.wait(async function() {
        return await inputField.isEnabled();
      }, 10000, '输入框未在指定时间内启用');
      
      const isEnabled = await inputField.isEnabled();
      expect(isEnabled).to.be.true;
    });
  });

  describe('等待策略组合', function() {
    it('应该组合使用多种等待策略', async function() {
      await driver.get('https://the-internet.herokuapp.com/dynamic_loading/2');
      
      // 1. 等待页面加载完成
      await driver.wait(
        until.elementLocated(By.css('#start button')),
        5000
      );
      
      // 2. 点击开始按钮
      const startButton = await driver.findElement(By.css('#start button'));
      await startButton.click();
      
      // 3. 等待加载指示器出现
      const loadingIndicator = await driver.wait(
        until.elementLocated(By.id('loading')),
        5000
      );
      
      // 4. 等待加载指示器消失
      await driver.wait(until.stalenessOf(loadingIndicator), 10000);
      
      // 5. 等待结果元素出现并可见
      const finishElement = await driver.wait(
        until.elementLocated(By.id('finish')),
        5000
      );
      
      await driver.wait(until.elementIsVisible(finishElement), 5000);
      
      // 6. 验证文本内容
      const text = await finishElement.getText();
      expect(text).to.equal('Hello World!');
    });
  });

  describe('超时处理', function() {
    it('应该在超时时抛出错误', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      try {
        // 尝试查找不存在的元素，设置短超时
        await driver.wait(
          until.elementLocated(By.id('non-existent-element')),
          1000
        );
        
        // 如果没有抛出错误，测试失败
        expect.fail('应该抛出超时错误');
      } catch (error) {
        expect(error.name).to.equal('TimeoutError');
      }
    });

    it('应该处理元素查找失败', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      try {
        const element = await driver.findElement(By.id('non-existent'));
        expect.fail('应该抛出 NoSuchElementError');
      } catch (error) {
        expect(error.name).to.equal('NoSuchElementError');
      }
    });
  });

  describe('页面加载等待', function() {
    it('应该等待页面完全加载', async function() {
      // 设置页面加载超时
      await driver.manage().setTimeouts({ pageLoad: 30000 });
      
      await driver.get('https://the-internet.herokuapp.com/');
      
      // 验证页面标题
      const title = await driver.getTitle();
      expect(title).to.include('The Internet');
    });

    it('应该等待 JavaScript 执行完成', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      // 等待 document.readyState 为 complete
      await driver.wait(async function() {
        const readyState = await driver.executeScript('return document.readyState');
        return readyState === 'complete';
      }, 10000);
      
      const readyState = await driver.executeScript('return document.readyState');
      expect(readyState).to.equal('complete');
    });
  });
});
