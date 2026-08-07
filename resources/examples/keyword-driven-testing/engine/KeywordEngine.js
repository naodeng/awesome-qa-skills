/**
 * 关键字执行引擎
 * 负责解析和执行测试用例中的关键字
 */

const { Builder } = require('selenium-webdriver');
const WebKeywords = require('../keywords/WebKeywords');

class KeywordEngine {
  constructor(options = {}) {
    this.driver = null;
    this.keywords = null;
    this.results = [];
    this.currentTestCase = null;
    this.options = {
      browser: options.browser || 'chrome',
      headless: options.headless !== false,
      timeout: options.timeout || 30000,
      ...options
    };
  }

  /**
   * 初始化驱动和关键字库
   */
  async initialize() {
    console.log('初始化测试环境...');
    
    // 创建 WebDriver
    this.driver = await new Builder()
      .forBrowser(this.options.browser)
      .build();
    
    // 设置超时
    await this.driver.manage().setTimeouts({
      implicit: this.options.timeout,
      pageLoad: this.options.timeout,
      script: this.options.timeout
    });
    
    // 初始化关键字库
    this.keywords = new WebKeywords(this.driver);
    
    console.log('测试环境初始化完成');
  }

  /**
   * 清理资源
   */
  async cleanup() {
    console.log('清理测试环境...');
    
    if (this.driver) {
      await this.driver.quit();
    }
    
    console.log('测试环境清理完成');
  }

  /**
   * 运行测试套件
   */
  async runTestSuite(testSuite) {
    const startTime = Date.now();
    
    console.log(`\n========================================`);
    console.log(`测试套件: ${testSuite.testSuite}`);
    console.log(`描述: ${testSuite.description || '无'}`);
    console.log(`========================================\n`);
    
    try {
      await this.initialize();
      
      const suiteResults = {
        name: testSuite.testSuite,
        description: testSuite.description,
        parameters: testSuite.parameters,
        testCases: [],
        summary: {
          total: testSuite.testCases.length,
          passed: 0,
          failed: 0,
          skipped: 0
        },
        startTime: new Date().toISOString(),
        duration: 0
      };
      
      // 执行每个测试用例
      for (const testCase of testSuite.testCases) {
        const result = await this.runTestCase(testCase, testSuite.parameters);
        suiteResults.testCases.push(result);
        
        if (result.status === 'pass') {
          suiteResults.summary.passed++;
        } else if (result.status === 'fail') {
          suiteResults.summary.failed++;
        } else {
          suiteResults.summary.skipped++;
        }
      }
      
      suiteResults.duration = Date.now() - startTime;
      suiteResults.endTime = new Date().toISOString();
      
      this.printSummary(suiteResults);
      
      return suiteResults;
      
    } catch (error) {
      console.error('测试套件执行失败:', error);
      throw error;
    } finally {
      await this.cleanup();
    }
  }

  /**
   * 运行单个测试用例
   */
  async runTestCase(testCase, globalParameters = {}) {
    const startTime = Date.now();
    this.currentTestCase = testCase;
    
    console.log(`\n--- 测试用例: ${testCase.id} - ${testCase.name} ---`);
    console.log(`优先级: ${testCase.priority || 'medium'}`);
    console.log(`标签: ${testCase.tags ? testCase.tags.join(', ') : '无'}\n`);
    
    const result = {
      id: testCase.id,
      name: testCase.name,
      priority: testCase.priority,
      tags: testCase.tags,
      steps: [],
      status: 'pass',
      startTime: new Date().toISOString(),
      duration: 0,
      error: null
    };
    
    try {
      // 执行每个步骤
      for (let i = 0; i < testCase.steps.length; i++) {
        const step = testCase.steps[i];
        const stepNumber = i + 1;
        
        console.log(`步骤 ${stepNumber}: ${step.keyword}(${step.args.join(', ')})`);
        if (step.description) {
          console.log(`  描述: ${step.description}`);
        }
        
        const stepResult = await this.executeStep(step, globalParameters);
        result.steps.push({
          number: stepNumber,
          keyword: step.keyword,
          args: step.args,
          description: step.description,
          ...stepResult
        });
        
        console.log(`  结果: ${stepResult.status} - ${stepResult.message}`);
        
        // 如果步骤失败，标记测试用例失败并停止执行
        if (stepResult.status === 'fail') {
          result.status = 'fail';
          result.error = stepResult.message;
          console.log(`\n❌ 测试用例失败: ${testCase.name}`);
          break;
        }
      }
      
      if (result.status === 'pass') {
        console.log(`\n✅ 测试用例通过: ${testCase.name}`);
      }
      
    } catch (error) {
      result.status = 'fail';
      result.error = error.message;
      console.error(`\n❌ 测试用例异常: ${testCase.name}`, error);
    }
    
    result.duration = Date.now() - startTime;
    result.endTime = new Date().toISOString();
    
    return result;
  }

  /**
   * 执行单个步骤
   */
  async executeStep(step, globalParameters = {}) {
    try {
      // 替换参数
      const args = this.replaceParameters(step.args, globalParameters);
      
      // 获取关键字方法
      const keyword = this.keywords[step.keyword];
      
      if (!keyword) {
        return {
          status: 'fail',
          message: `关键字不存在: ${step.keyword}`
        };
      }
      
      // 执行关键字
      const result = await keyword.apply(this.keywords, args);
      
      return result;
      
    } catch (error) {
      return {
        status: 'fail',
        message: `执行关键字失败: ${step.keyword}`,
        error: error.message
      };
    }
  }

  /**
   * 替换参数中的变量
   */
  replaceParameters(args, parameters) {
    return args.map(arg => {
      if (typeof arg === 'string' && arg.includes('${')) {
        // 替换 ${variable} 格式的变量
        return arg.replace(/\$\{([^}]+)\}/g, (match, key) => {
          return parameters[key] || match;
        });
      }
      return arg;
    });
  }

  /**
   * 打印测试摘要
   */
  printSummary(results) {
    console.log(`\n========================================`);
    console.log(`测试摘要`);
    console.log(`========================================`);
    console.log(`测试套件: ${results.name}`);
    console.log(`执行时间: ${results.startTime}`);
    console.log(`总耗时: ${(results.duration / 1000).toFixed(2)}s`);
    console.log(`\n测试用例统计:`);
    console.log(`  总数: ${results.summary.total}`);
    console.log(`  通过: ${results.summary.passed} ✅`);
    console.log(`  失败: ${results.summary.failed} ❌`);
    console.log(`  跳过: ${results.summary.skipped} ⏭️`);
    console.log(`\n通过率: ${((results.summary.passed / results.summary.total) * 100).toFixed(2)}%`);
    console.log(`========================================\n`);
    
    // 打印失败的测试用例
    if (results.summary.failed > 0) {
      console.log(`失败的测试用例:`);
      results.testCases
        .filter(tc => tc.status === 'fail')
        .forEach(tc => {
          console.log(`  ❌ ${tc.id} - ${tc.name}`);
          console.log(`     错误: ${tc.error}`);
        });
      console.log('');
    }
  }
}

module.exports = KeywordEngine;
