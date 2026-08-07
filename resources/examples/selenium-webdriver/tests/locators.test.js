const { Builder, By, until } = require('selenium-webdriver');
const { expect } = require('chai');

describe('Selenium 元素定位测试', function() {
  this.timeout(30000);
  let driver;

  before(async function() {
    driver = await new Builder().forBrowser('chrome').build();
  });

  after(async function() {
    await driver.quit();
  });

  describe('基本定位方法', function() {
    beforeEach(async function() {
      await driver.get('https://the-internet.herokuapp.com/login');
    });

    it('应该通过 ID 定位元素', async function() {
      // ID 定位是最快最可靠的方法
      const usernameField = await driver.findElement(By.id('username'));
      await usernameField.sendKeys('tomsmith');
      
      const value = await usernameField.getAttribute('value');
      expect(value).to.equal('tomsmith');
    });

    it('应该通过 Name 定位元素', async function() {
      const usernameField = await driver.findElement(By.name('username'));
      await usernameField.sendKeys('tomsmith');
      
      const value = await usernameField.getAttribute('value');
      expect(value).to.equal('tomsmith');
    });

    it('应该通过 Class Name 定位元素', async function() {
      const loginButton = await driver.findElement(By.className('radius'));
      const tagName = await loginButton.getTagName();
      expect(tagName).to.equal('button');
    });

    it('应该通过 Tag Name 定位元素', async function() {
      const buttons = await driver.findElements(By.tagName('button'));
      expect(buttons.length).to.be.greaterThan(0);
    });

    it('应该通过 Link Text 定位链接', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      const link = await driver.findElement(By.linkText('Form Authentication'));
      await link.click();
      
      const url = await driver.getCurrentUrl();
      expect(url).to.include('/login');
    });

    it('应该通过 Partial Link Text 定位链接', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      const link = await driver.findElement(By.partialLinkText('Form Auth'));
      await link.click();
      
      const url = await driver.getCurrentUrl();
      expect(url).to.include('/login');
    });
  });

  describe('CSS Selector 定位', function() {
    beforeEach(async function() {
      await driver.get('https://the-internet.herokuapp.com/login');
    });

    it('应该通过 CSS ID 选择器定位', async function() {
      const element = await driver.findElement(By.css('#username'));
      const id = await element.getAttribute('id');
      expect(id).to.equal('username');
    });

    it('应该通过 CSS Class 选择器定位', async function() {
      const element = await driver.findElement(By.css('.radius'));
      const className = await element.getAttribute('class');
      expect(className).to.include('radius');
    });

    it('应该通过 CSS 属性选择器定位', async function() {
      const element = await driver.findElement(By.css('input[name="username"]'));
      const name = await element.getAttribute('name');
      expect(name).to.equal('username');
    });

    it('应该通过 CSS 组合选择器定位', async function() {
      const element = await driver.findElement(By.css('form#login input[type="text"]'));
      const type = await element.getAttribute('type');
      expect(type).to.equal('text');
    });

    it('应该通过 CSS 伪类选择器定位', async function() {
      const firstInput = await driver.findElement(By.css('input:first-of-type'));
      const id = await firstInput.getAttribute('id');
      expect(id).to.equal('username');
    });

    it('应该通过 CSS 子元素选择器定位', async function() {
      const button = await driver.findElement(By.css('form > button'));
      const tagName = await button.getTagName();
      expect(tagName).to.equal('button');
    });
  });

  describe('XPath 定位', function() {
    beforeEach(async function() {
      await driver.get('https://the-internet.herokuapp.com/login');
    });

    it('应该通过绝对 XPath 定位', async function() {
      // 不推荐使用绝对路径，容易失效
      const element = await driver.findElement(
        By.xpath('/html/body/div[2]/div/div/form/div[1]/div/input')
      );
      const id = await element.getAttribute('id');
      expect(id).to.equal('username');
    });

    it('应该通过相对 XPath 定位', async function() {
      // 推荐使用相对路径
      const element = await driver.findElement(By.xpath('//input[@id="username"]'));
      const id = await element.getAttribute('id');
      expect(id).to.equal('username');
    });

    it('应该通过 XPath 文本定位', async function() {
      const button = await driver.findElement(By.xpath('//button[contains(text(), "Login")]'));
      const text = await button.getText();
      expect(text).to.include('Login');
    });

    it('应该通过 XPath 属性定位', async function() {
      const element = await driver.findElement(By.xpath('//input[@name="username"]'));
      const name = await element.getAttribute('name');
      expect(name).to.equal('username');
    });

    it('应该通过 XPath 多条件定位', async function() {
      const element = await driver.findElement(
        By.xpath('//input[@type="text" and @name="username"]')
      );
      const type = await element.getAttribute('type');
      expect(type).to.equal('text');
    });

    it('应该通过 XPath 父子关系定位', async function() {
      const element = await driver.findElement(
        By.xpath('//form[@id="login"]//input[@type="text"]')
      );
      const id = await element.getAttribute('id');
      expect(id).to.equal('username');
    });

    it('应该通过 XPath 索引定位', async function() {
      const firstInput = await driver.findElement(By.xpath('(//input)[1]'));
      const id = await firstInput.getAttribute('id');
      expect(id).to.equal('username');
    });

    it('应该通过 XPath contains 函数定位', async function() {
      const element = await driver.findElement(
        By.xpath('//input[contains(@id, "user")]')
      );
      const id = await element.getAttribute('id');
      expect(id).to.equal('username');
    });

    it('应该通过 XPath starts-with 函数定位', async function() {
      const element = await driver.findElement(
        By.xpath('//input[starts-with(@id, "user")]')
      );
      const id = await element.getAttribute('id');
      expect(id).to.equal('username');
    });
  });

  describe('查找多个元素', function() {
    it('应该查找所有匹配的元素', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      const links = await driver.findElements(By.tagName('a'));
      expect(links.length).to.be.greaterThan(0);
      
      // 遍历所有链接
      for (const link of links) {
        const text = await link.getText();
        console.log('链接文本:', text);
      }
    });

    it('应该通过 CSS 选择器查找多个元素', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      const listItems = await driver.findElements(By.css('ul li'));
      expect(listItems.length).to.be.greaterThan(0);
    });

    it('应该通过 XPath 查找多个元素', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      const links = await driver.findElements(By.xpath('//a'));
      expect(links.length).to.be.greaterThan(0);
    });
  });

  describe('嵌套元素查找', function() {
    it('应该在父元素中查找子元素', async function() {
      await driver.get('https://the-internet.herokuapp.com/login');
      
      // 先找到表单
      const form = await driver.findElement(By.id('login'));
      
      // 在表单中查找输入框
      const usernameField = await form.findElement(By.id('username'));
      await usernameField.sendKeys('tomsmith');
      
      const value = await usernameField.getAttribute('value');
      expect(value).to.equal('tomsmith');
    });

    it('应该在父元素中查找多个子元素', async function() {
      await driver.get('https://the-internet.herokuapp.com/login');
      
      const form = await driver.findElement(By.id('login'));
      const inputs = await form.findElements(By.tagName('input'));
      
      expect(inputs.length).to.equal(2); // username 和 password
    });
  });

  describe('动态元素定位', function() {
    it('应该定位动态 ID 的元素', async function() {
      await driver.get('https://the-internet.herokuapp.com/dynamic_controls');
      
      // 使用部分匹配定位动态 ID
      const checkbox = await driver.findElement(By.css('input[type="checkbox"]'));
      const isDisplayed = await checkbox.isDisplayed();
      expect(isDisplayed).to.be.true;
    });

    it('应该使用 XPath 定位动态元素', async function() {
      await driver.get('https://the-internet.herokuapp.com/dynamic_controls');
      
      // 使用 contains 函数匹配部分属性
      const button = await driver.findElement(
        By.xpath('//button[contains(text(), "Remove")]')
      );
      const text = await button.getText();
      expect(text).to.include('Remove');
    });
  });

  describe('定位策略最佳实践', function() {
    it('应该优先使用 ID 定位', async function() {
      await driver.get('https://the-internet.herokuapp.com/login');
      
      // ID 是最快最可靠的定位方式
      const start = Date.now();
      const element = await driver.findElement(By.id('username'));
      const duration = Date.now() - start;
      
      console.log('ID 定位耗时:', duration, 'ms');
      expect(await element.isDisplayed()).to.be.true;
    });

    it('应该使用稳定的定位器', async function() {
      await driver.get('https://the-internet.herokuapp.com/login');
      
      // ✅ 好的定位器：使用稳定的属性
      const goodLocator = await driver.findElement(By.id('username'));
      
      // ❌ 不好的定位器：使用索引或绝对路径
      // const badLocator = await driver.findElement(By.xpath('/html/body/div[2]/div/div/form/div[1]/div/input'));
      
      expect(await goodLocator.isDisplayed()).to.be.true;
    });

    it('应该使用有意义的定位器', async function() {
      await driver.get('https://the-internet.herokuapp.com/login');
      
      // ✅ 清晰的定位器
      const usernameField = await driver.findElement(By.css('input[name="username"]'));
      const loginButton = await driver.findElement(By.css('button[type="submit"]'));
      
      expect(await usernameField.isDisplayed()).to.be.true;
      expect(await loginButton.isDisplayed()).to.be.true;
    });
  });
});
