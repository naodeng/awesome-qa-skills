const { Builder, By, until, Key } = require('selenium-webdriver');
const { expect } = require('chai');

describe('Selenium 交互操作测试', function() {
  this.timeout(30000);
  let driver;

  before(async function() {
    driver = await new Builder().forBrowser('chrome').build();
  });

  after(async function() {
    await driver.quit();
  });

  describe('基本交互操作', function() {
    it('应该点击元素', async function() {
      await driver.get('https://the-internet.herokuapp.com/add_remove_elements/');
      
      const addButton = await driver.findElement(By.css('button[onclick="addElement()"]'));
      await addButton.click();
      
      const deleteButton = await driver.findElement(By.className('added-manually'));
      const isDisplayed = await deleteButton.isDisplayed();
      expect(isDisplayed).to.be.true;
    });

    it('应该输入文本', async function() {
      await driver.get('https://the-internet.herokuapp.com/login');
      
      const usernameField = await driver.findElement(By.id('username'));
      await usernameField.sendKeys('tomsmith');
      
      const value = await usernameField.getAttribute('value');
      expect(value).to.equal('tomsmith');
    });

    it('应该清空输入框', async function() {
      await driver.get('https://the-internet.herokuapp.com/login');
      
      const usernameField = await driver.findElement(By.id('username'));
      await usernameField.sendKeys('test');
      await usernameField.clear();
      
      const value = await usernameField.getAttribute('value');
      expect(value).to.equal('');
    });

    it('应该获取元素文本', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      const heading = await driver.findElement(By.css('h1'));
      const text = await heading.getText();
      expect(text).to.include('Welcome');
    });

    it('应该获取元素属性', async function() {
      await driver.get('https://the-internet.herokuapp.com/login');
      
      const usernameField = await driver.findElement(By.id('username'));
      const type = await usernameField.getAttribute('type');
      const name = await usernameField.getAttribute('name');
      
      expect(type).to.equal('text');
      expect(name).to.equal('username');
    });
  });

  describe('表单操作', function() {
    it('应该提交表单', async function() {
      await driver.get('https://the-internet.herokuapp.com/login');
      
      await driver.findElement(By.id('username')).sendKeys('tomsmith');
      await driver.findElement(By.id('password')).sendKeys('SuperSecretPassword!');
      
      const form = await driver.findElement(By.id('login'));
      await form.submit();
      
      await driver.wait(until.urlContains('/secure'), 5000);
      const url = await driver.getCurrentUrl();
      expect(url).to.include('/secure');
    });

    it('应该操作下拉选择框', async function() {
      await driver.get('https://the-internet.herokuapp.com/dropdown');
      
      const dropdown = await driver.findElement(By.id('dropdown'));
      
      // 选择选项1
      await dropdown.sendKeys('Option 1');
      
      // 验证选中的值
      const selectedOption = await dropdown.findElement(By.css('option:checked'));
      const text = await selectedOption.getText();
      expect(text).to.equal('Option 1');
    });

    it('应该操作复选框', async function() {
      await driver.get('https://the-internet.herokuapp.com/checkboxes');
      
      const checkboxes = await driver.findElements(By.css('input[type="checkbox"]'));
      const firstCheckbox = checkboxes[0];
      
      // 检查初始状态
      let isChecked = await firstCheckbox.isSelected();
      expect(isChecked).to.be.false;
      
      // 勾选复选框
      await firstCheckbox.click();
      
      // 验证已勾选
      isChecked = await firstCheckbox.isSelected();
      expect(isChecked).to.be.true;
    });

    it('应该操作单选按钮', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      // 注意：这个网站没有单选按钮示例，这里展示通用方法
      // 实际使用时替换为真实的单选按钮
      
      // const radio = await driver.findElement(By.css('input[type="radio"][value="option1"]'));
      // await radio.click();
      // const isSelected = await radio.isSelected();
      // expect(isSelected).to.be.true;
    });
  });

  describe('键盘操作', function() {
    it('应该发送特殊按键', async function() {
      await driver.get('https://the-internet.herokuapp.com/key_presses');
      
      const input = await driver.findElement(By.id('target'));
      
      // 发送 Enter 键
      await input.sendKeys(Key.ENTER);
      
      const result = await driver.findElement(By.id('result'));
      let text = await result.getText();
      expect(text).to.include('ENTER');
      
      // 发送 Tab 键
      await input.sendKeys(Key.TAB);
      text = await result.getText();
      expect(text).to.include('TAB');
      
      // 发送 Escape 键
      await input.sendKeys(Key.ESCAPE);
      text = await result.getText();
      expect(text).to.include('ESCAPE');
    });

    it('应该发送组合键', async function() {
      await driver.get('https://the-internet.herokuapp.com/key_presses');
      
      const input = await driver.findElement(By.id('target'));
      
      // 发送 Ctrl+A (全选)
      await input.sendKeys(Key.chord(Key.CONTROL, 'a'));
      
      // 发送 Ctrl+C (复制)
      await input.sendKeys(Key.chord(Key.CONTROL, 'c'));
    });

    it('应该模拟键盘输入', async function() {
      await driver.get('https://the-internet.herokuapp.com/login');
      
      const usernameField = await driver.findElement(By.id('username'));
      
      // 逐字符输入
      await usernameField.sendKeys('t', 'o', 'm', 's', 'm', 'i', 't', 'h');
      
      const value = await usernameField.getAttribute('value');
      expect(value).to.equal('tomsmith');
    });
  });

  describe('文件上传', function() {
    it('应该上传文件', async function() {
      await driver.get('https://the-internet.herokuapp.com/upload');
      
      const fileInput = await driver.findElement(By.id('file-upload'));
      
      // 注意：需要提供实际存在的文件路径
      // 这里使用相对路径示例
      const filePath = require('path').resolve(__dirname, '../package.json');
      await fileInput.sendKeys(filePath);
      
      const submitButton = await driver.findElement(By.id('file-submit'));
      await submitButton.click();
      
      await driver.wait(until.urlContains('/upload'), 5000);
      
      const uploadedFile = await driver.findElement(By.id('uploaded-files'));
      const text = await uploadedFile.getText();
      expect(text).to.include('package.json');
    });
  });

  describe('拖拽操作', function() {
    it('应该拖拽元素', async function() {
      await driver.get('https://the-internet.herokuapp.com/drag_and_drop');
      
      const columnA = await driver.findElement(By.id('column-a'));
      const columnB = await driver.findElement(By.id('column-b'));
      
      // 获取初始文本
      let textA = await columnA.getText();
      let textB = await columnB.getText();
      
      expect(textA).to.equal('A');
      expect(textB).to.equal('B');
      
      // 执行拖拽（使用 JavaScript 因为 HTML5 拖拽）
      await driver.executeScript(`
        function simulateDragDrop(sourceNode, destinationNode) {
          var EVENT_TYPES = {
            DRAG_END: 'dragend',
            DRAG_START: 'dragstart',
            DROP: 'drop'
          }
          
          function createCustomEvent(type) {
            var event = new CustomEvent("CustomEvent")
            event.initCustomEvent(type, true, true, null)
            event.dataTransfer = {
              data: {},
              setData: function(type, val) {
                this.data[type] = val
              },
              getData: function(type) {
                return this.data[type]
              }
            }
            return event
          }
          
          function dispatchEvent(node, type, event) {
            if (node.dispatchEvent) {
              return node.dispatchEvent(event)
            }
            if (node.fireEvent) {
              return node.fireEvent("on" + type, event)
            }
          }
          
          var event = createCustomEvent(EVENT_TYPES.DRAG_START)
          dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, event)
          
          var dropEvent = createCustomEvent(EVENT_TYPES.DROP)
          dropEvent.dataTransfer = event.dataTransfer
          dispatchEvent(destinationNode, EVENT_TYPES.DROP, dropEvent)
          
          var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END)
          dragEndEvent.dataTransfer = event.dataTransfer
          dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent)
        }
        
        simulateDragDrop(arguments[0], arguments[1]);
      `, columnA, columnB);
      
      // 等待动画完成
      await driver.sleep(1000);
      
      // 验证拖拽结果
      textA = await columnA.getText();
      textB = await columnB.getText();
      
      expect(textA).to.equal('B');
      expect(textB).to.equal('A');
    });
  });

  describe('元素状态检查', function() {
    it('应该检查元素是否显示', async function() {
      await driver.get('https://the-internet.herokuapp.com/dynamic_loading/1');
      
      const finishElement = await driver.findElement(By.id('finish'));
      let isDisplayed = await finishElement.isDisplayed();
      expect(isDisplayed).to.be.false;
      
      const startButton = await driver.findElement(By.css('#start button'));
      await startButton.click();
      
      await driver.wait(until.elementIsVisible(finishElement), 10000);
      isDisplayed = await finishElement.isDisplayed();
      expect(isDisplayed).to.be.true;
    });

    it('应该检查元素是否启用', async function() {
      await driver.get('https://the-internet.herokuapp.com/dynamic_controls');
      
      const input = await driver.findElement(By.css('#input-example input'));
      let isEnabled = await input.isEnabled();
      expect(isEnabled).to.be.false;
      
      const enableButton = await driver.findElement(By.css('#input-example button'));
      await enableButton.click();
      
      await driver.wait(until.elementIsEnabled(input), 10000);
      isEnabled = await input.isEnabled();
      expect(isEnabled).to.be.true;
    });

    it('应该检查元素是否选中', async function() {
      await driver.get('https://the-internet.herokuapp.com/checkboxes');
      
      const checkboxes = await driver.findElements(By.css('input[type="checkbox"]'));
      const firstCheckbox = checkboxes[0];
      
      let isSelected = await firstCheckbox.isSelected();
      expect(isSelected).to.be.false;
      
      await firstCheckbox.click();
      
      isSelected = await firstCheckbox.isSelected();
      expect(isSelected).to.be.true;
    });
  });

  describe('JavaScript 执行', function() {
    it('应该执行 JavaScript 代码', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      // 执行 JavaScript 获取页面标题
      const title = await driver.executeScript('return document.title;');
      expect(title).to.include('The Internet');
    });

    it('应该通过 JavaScript 操作元素', async function() {
      await driver.get('https://the-internet.herokuapp.com/login');
      
      const usernameField = await driver.findElement(By.id('username'));
      
      // 使用 JavaScript 设置值
      await driver.executeScript(
        'arguments[0].value = arguments[1];',
        usernameField,
        'tomsmith'
      );
      
      const value = await usernameField.getAttribute('value');
      expect(value).to.equal('tomsmith');
    });

    it('应该通过 JavaScript 滚动页面', async function() {
      await driver.get('https://the-internet.herokuapp.com/infinite_scroll');
      
      // 滚动到页面底部
      await driver.executeScript('window.scrollTo(0, document.body.scrollHeight);');
      
      // 等待新内容加载
      await driver.sleep(2000);
      
      // 验证滚动位置
      const scrollY = await driver.executeScript('return window.scrollY;');
      expect(scrollY).to.be.greaterThan(0);
    });

    it('应该通过 JavaScript 点击元素', async function() {
      await driver.get('https://the-internet.herokuapp.com/add_remove_elements/');
      
      const addButton = await driver.findElement(By.css('button[onclick="addElement()"]'));
      
      // 使用 JavaScript 点击
      await driver.executeScript('arguments[0].click();', addButton);
      
      const deleteButton = await driver.findElement(By.className('added-manually'));
      const isDisplayed = await deleteButton.isDisplayed();
      expect(isDisplayed).to.be.true;
    });
  });

  describe('导航操作', function() {
    it('应该前进和后退', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      const url1 = await driver.getCurrentUrl();
      
      await driver.get('https://the-internet.herokuapp.com/login');
      const url2 = await driver.getCurrentUrl();
      
      // 后退
      await driver.navigate().back();
      const currentUrl = await driver.getCurrentUrl();
      expect(currentUrl).to.equal(url1);
      
      // 前进
      await driver.navigate().forward();
      const forwardUrl = await driver.getCurrentUrl();
      expect(forwardUrl).to.equal(url2);
    });

    it('应该刷新页面', async function() {
      await driver.get('https://the-internet.herokuapp.com/');
      
      // 刷新页面
      await driver.navigate().refresh();
      
      const title = await driver.getTitle();
      expect(title).to.include('The Internet');
    });
  });
});
