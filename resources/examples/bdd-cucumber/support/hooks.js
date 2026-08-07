const { Before, After, BeforeAll, AfterAll, Status } = require('@cucumber/cucumber');

/**
 * 所有测试前执行一次
 */
BeforeAll(async function() {
  console.log('\n========================================');
  console.log('开始 BDD 测试');
  console.log('========================================\n');
});

/**
 * 每个场景前执行
 */
Before(async function(scenario) {
  // 记录开始时间
  this.startTime = Date.now();
  
  // 重置状态
  if (this.reset) {
    this.reset();
  }
  
  console.log(`\n--- 开始场景: ${scenario.pickle.name} ---`);
  
  // 检查标签
  const tags = scenario.pickle.tags.map(tag => tag.name);
  console.log(`标签: ${tags.join(', ')}`);
  
  // 根据标签执行特定操作
  if (tags.includes('@skip')) {
    return 'skipped';
  }
});

/**
 * 每个场景后执行
 */
After(async function(scenario) {
  // 计算执行时间
  const duration = Date.now() - this.startTime;
  
  console.log(`\n场景执行时间: ${duration}ms`);
  console.log(`场景状态: ${scenario.result.status}`);
  
  // 如果场景失败，记录详细信息
  if (scenario.result.status === Status.FAILED) {
    console.log('\n❌ 场景失败');
    console.log('错误信息:', scenario.result.message);
    
    // 打印 World 状态用于调试
    if (this.debug) {
      this.debug();
    }
    
    // 如果有浏览器驱动，截图
    if (this.driver) {
      try {
        const screenshot = await this.driver.takeScreenshot();
        this.attach(screenshot, 'image/png');
        console.log('已保存失败截图');
      } catch (error) {
        console.log('截图失败:', error.message);
      }
    }
  } else if (scenario.result.status === Status.PASSED) {
    console.log('✅ 场景通过');
  }
  
  console.log(`--- 结束场景: ${scenario.pickle.name} ---\n`);
  
  // 清理资源
  if (this.driver) {
    // 不在这里关闭驱动，因为可能在多个场景间复用
    // await this.driver.quit();
  }
});

/**
 * 所有测试后执行一次
 */
AfterAll(async function() {
  console.log('\n========================================');
  console.log('BDD 测试完成');
  console.log('========================================\n');
  
  // 清理全局资源
  // 例如：关闭数据库连接、清理测试数据等
});

/**
 * 特定标签的钩子
 */

// @smoke 标签的场景前执行
Before({ tags: '@smoke' }, async function() {
  console.log('🔥 这是一个冒烟测试');
});

// @slow 标签的场景设置更长的超时时间
Before({ tags: '@slow' }, async function() {
  this.timeout = 60000; // 60 秒
  console.log('⏱️  设置较长的超时时间');
});

// @database 标签的场景前后执行数据库操作
Before({ tags: '@database' }, async function() {
  console.log('💾 准备数据库测试数据');
  // 这里可以设置数据库连接和测试数据
});

After({ tags: '@database' }, async function() {
  console.log('💾 清理数据库测试数据');
  // 这里可以清理测试数据
});

// @api 标签的场景前执行
Before({ tags: '@api' }, async function() {
  console.log('🌐 准备 API 测试');
  // 这里可以设置 API 客户端
});

// @security 标签的场景
Before({ tags: '@security' }, async function() {
  console.log('🔒 安全测试场景');
});

// @performance 标签的场景
Before({ tags: '@performance' }, async function() {
  console.log('⚡ 性能测试场景');
  this.performanceMetrics = {
    startTime: Date.now(),
    memoryUsage: process.memoryUsage()
  };
});

After({ tags: '@performance' }, async function() {
  if (this.performanceMetrics) {
    const duration = Date.now() - this.performanceMetrics.startTime;
    const memoryDiff = process.memoryUsage().heapUsed - this.performanceMetrics.memoryUsage.heapUsed;
    
    console.log(`\n性能指标:`);
    console.log(`  执行时间: ${duration}ms`);
    console.log(`  内存变化: ${(memoryDiff / 1024 / 1024).toFixed(2)}MB`);
  }
});
