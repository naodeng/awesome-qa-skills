/**
 * Web 操作关键字库
 * 提供常用的 Web 自动化操作关键字
 */

class WebKeywords {
  constructor(driver) {
    this.driver = driver;
    this.By = require('selenium-webdriver').By;
    this.until = require('selenium-webdriver').until;
  }

  /**
   * 导航到指定 URL
   */
  async navigateTo(url) {
    try {
      await this.driver.get(url);
      return { 
        status: 'pass', 
        message: `成功导航到: ${url}` 
      };
    } catch (error) {
      return { 
        status: 'fail', 
        message: `导航失败: ${url}`,
        error: error.message 
      };
    }
  }

  /**
   * 点击元素
   */
  async clickElement(selector) {
    try {
      const element = await this.driver.findElement(this.By.css(selector));
      await element.click();
      return { 
        status: 'pass', 
        message: `成功点击元素: ${selector}` 
      };
    } catch (error) {
      return { 
        status: 'fail', 
        message: `点击元素失败: ${selector}`,
        error: error.message 
      };
    }
  }

  /**
   * 输入文本
   */
  async inputText(selector, text) {
    try {
      const element = await this.driver.findElement(this.By.css(selector));
      await element.sendKeys(text);
      return { 
        status: 'pass', 
        message: `成功输入文本到 ${selector}: "${text}"` 
      };
    } catch (error) {
      return { 
        status: 'fail', 
        message: `输入文本失败: ${selector}`,
        error: error.message 
      };
    }
  }

  /**
   * 清空文本
   */
  async clearText(selector) {
    try {
      const element = await this.driver.findElement(this.By.css(selector));
      await element.clear();
      return { 
        status: 'pass', 
        message: `成功清空文本: ${selector}` 
      };
    } catch (error) {
      return { 
        status: 'fail', 
        message: `清空文本失败: ${selector}`,
        error: error.message 
      };
    }
  }

  /**
   * 验证文本
   */
  async verifyText(selector, expectedText) {
    try {
      const element = await this.driver.findElement(this.By.css(selector));
      const actualText = await element.getText();
      
      if (actualText.includes(expectedText)) {
        return { 
          status: 'pass', 
          message: `文本验证通过: "${expectedText}"` 
        };
      } else {
        return { 
          status: 'fail', 
          message: `文本验证失败: 期望包含 "${expectedText}", 实际为 "${actualText}"` 
        };
      }
    } catch (error) {
      return { 
        status: 'fail', 
        message: `文本验证失败: ${selector}`,
        error: error.message 
      };
    }
  }

  /**
   * 验证元素可见
   */
  async verifyElementVisible(selector) {
    try {
      const element = await this.driver.findElement(this.By.css(selector));
      const isDisplayed = await element.isDisplayed();
      
      if (isDisplayed) {
        return { 
          status: 'pass', 
          message: `元素可见: ${selector}` 
        };
      } else {
        return { 
          status: 'fail', 
          message: `元素不可见: ${selector}` 
        };
      }
    } catch (error) {
      return { 
        status: 'fail', 
        message: `验证元素可见失败: ${selector}`,
        error: error.message 
      };
    }
  }

  /**
   * 验证元素启用
   */
  async verifyElementEnabled(selector) {
    try {
      const element = await this.driver.findElement(this.By.css(selector));
      const isEnabled = await element.isEnabled();
      
      if (isEnabled) {
        return { 
          status: 'pass', 
          message: `元素已启用: ${selector}` 
        };
      } else {
        return { 
          status: 'fail', 
          message: `元素未启用: ${selector}` 
        };
      }
    } catch (error) {
      return { 
        status: 'fail', 
        message: `验证元素启用失败: ${selector}`,
        error: error.message 
      };
    }
  }

  /**
   * 验证 URL
   */
  async verifyUrl(expectedUrl) {
    try {
      const actualUrl = await this.driver.getCurrentUrl();
      
      if (actualUrl === expectedUrl || actualUrl.includes(expectedUrl)) {
        return { 
          status: 'pass', 
          message: `URL 验证通过: ${expectedUrl}` 
        };
      } else {
        return { 
          status: 'fail', 
          message: `URL 验证失败: 期望 "${expectedUrl}", 实际 "${actualUrl}"` 
        };
      }
    } catch (error) {
      return { 
        status: 'fail', 
        message: `URL 验证失败`,
        error: error.message 
      };
    }
  }

  /**
   * 等待元素
   */
  async waitForElement(selector, timeout = 5000) {
    try {
      await this.driver.wait(
        this.until.elementLocated(this.By.css(selector)),
        timeout
      );
      return { 
        status: 'pass', 
        message: `元素已出现: ${selector}` 
      };
    } catch (error) {
      return { 
        status: 'fail', 
        message: `等待元素超时: ${selector}`,
        error: error.message 
      };
    }
  }

  /**
   * 等待 URL
   */
  async waitForUrl(expectedUrl, timeout = 5000) {
    try {
      await this.driver.wait(
        this.until.urlContains(expectedUrl),
        timeout
      );
      return { 
        status: 'pass', 
        message: `URL 已变更: ${expectedUrl}` 
      };
    } catch (error) {
      return { 
        status: 'fail', 
        message: `等待 URL 超时: ${expectedUrl}`,
        error: error.message 
      };
    }
  }

  /**
   * 等待文本
   */
  async waitForText(selector, text, timeout = 5000) {
    try {
      await this.driver.wait(async () => {
        try {
          const element = await this.driver.findElement(this.By.css(selector));
          const actualText = await element.getText();
          return actualText.includes(text);
        } catch {
          return false;
        }
      }, timeout);
      
      return { 
        status: 'pass', 
        message: `文本已出现: "${text}"` 
      };
    } catch (error) {
      return { 
        status: 'fail', 
        message: `等待文本超时: "${text}"`,
        error: error.message 
      };
    }
  }

  /**
   * 选择下拉框
   */
  async selectDropdown(selector, value) {
    try {
      const element = await this.driver.findElement(this.By.css(selector));
      await element.sendKeys(value);
      return { 
        status: 'pass', 
        message: `成功选择: ${value}` 
      };
    } catch (error) {
      return { 
        status: 'fail', 
        message: `选择下拉框失败: ${selector}`,
        error: error.message 
      };
    }
  }

  /**
   * 勾选复选框
   */
  async checkCheckbox(selector) {
    try {
      const element = await this.driver.findElement(this.By.css(selector));
      const isSelected = await element.isSelected();
      
      if (!isSelected) {
        await element.click();
      }
      
      return { 
        status: 'pass', 
        message: `成功勾选复选框: ${selector}` 
      };
    } catch (error) {
      return { 
        status: 'fail', 
        message: `勾选复选框失败: ${selector}`,
        error: error.message 
      };
    }
  }

  /**
   * 取消勾选复选框
   */
  async uncheckCheckbox(selector) {
    try {
      const element = await this.driver.findElement(this.By.css(selector));
      const isSelected = await element.isSelected();
      
      if (isSelected) {
        await element.click();
      }
      
      return { 
        status: 'pass', 
        message: `成功取消勾选复选框: ${selector}` 
      };
    } catch (error) {
      return { 
        status: 'fail', 
        message: `取消勾选复选框失败: ${selector}`,
        error: error.message 
      };
    }
  }

  /**
   * 验证 Cookie
   */
  async verifyCookie(cookieName) {
    try {
      const cookie = await this.driver.manage().getCookie(cookieName);
      
      if (cookie) {
        return { 
          status: 'pass', 
          message: `Cookie 存在: ${cookieName}` 
        };
      } else {
        return { 
          status: 'fail', 
          message: `Cookie 不存在: ${cookieName}` 
        };
      }
    } catch (error) {
      return { 
        status: 'fail', 
        message: `验证 Cookie 失败: ${cookieName}`,
        error: error.message 
      };
    }
  }

  /**
   * 截图
   */
  async takeScreenshot(filename) {
    try {
      const screenshot = await this.driver.takeScreenshot();
      // 这里可以保存截图到文件
      return { 
        status: 'pass', 
        message: `截图成功: ${filename}`,
        screenshot: screenshot 
      };
    } catch (error) {
      return { 
        status: 'fail', 
        message: `截图失败: ${filename}`,
        error: error.message 
      };
    }
  }

  /**
   * 等待指定时间
   */
  async sleep(milliseconds) {
    try {
      await this.driver.sleep(milliseconds);
      return { 
        status: 'pass', 
        message: `等待 ${milliseconds}ms` 
      };
    } catch (error) {
      return { 
        status: 'fail', 
        message: `等待失败`,
        error: error.message 
      };
    }
  }

  /**
   * 刷新页面
   */
  async refresh() {
    try {
      await this.driver.navigate().refresh();
      return { 
        status: 'pass', 
        message: `页面已刷新` 
      };
    } catch (error) {
      return { 
        status: 'fail', 
        message: `刷新页面失败`,
        error: error.message 
      };
    }
  }

  /**
   * 后退
   */
  async goBack() {
    try {
      await this.driver.navigate().back();
      return { 
        status: 'pass', 
        message: `已后退` 
      };
    } catch (error) {
      return { 
        status: 'fail', 
        message: `后退失败`,
        error: error.message 
      };
    }
  }

  /**
   * 前进
   */
  async goForward() {
    try {
      await this.driver.navigate().forward();
      return { 
        status: 'pass', 
        message: `已前进` 
      };
    } catch (error) {
      return { 
        status: 'fail', 
        message: `前进失败`,
        error: error.message 
      };
    }
  }
}

module.exports = WebKeywords;
