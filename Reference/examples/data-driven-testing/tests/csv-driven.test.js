const { expect } = require('chai');
const fs = require('fs');
const csv = require('csv-parser');
const path = require('path');

describe('CSV 数据驱动测试', function() {
  this.timeout(30000);
  let testData = [];

  // 在所有测试前读取 CSV 数据
  before(function(done) {
    const csvPath = path.join(__dirname, '../data/test-data.csv');
    
    fs.createReadStream(csvPath)
      .pipe(csv())
      .on('data', (row) => {
        testData.push(row);
      })
      .on('end', () => {
        console.log(`已加载 ${testData.length} 条测试数据`);
        done();
      })
      .on('error', (error) => {
        done(error);
      });
  });

  describe('登录功能测试', function() {
    // 为每条数据生成一个测试用例
    testData.forEach((data, index) => {
      it(`测试 ${index + 1}: ${data.description}`, function() {
        console.log(`\n测试数据: ${JSON.stringify(data)}`);
        
        // 模拟登录逻辑
        const result = simulateLogin(data.username, data.password);
        
        // 验证结果
        expect(result).to.equal(data.expected);
      });
    });
  });

  describe('成功登录测试', function() {
    // 只测试预期成功的用例
    const successCases = testData.filter(data => data.expected === 'success');
    
    successCases.forEach((data) => {
      it(`应该成功登录: ${data.username}`, function() {
        const result = simulateLogin(data.username, data.password);
        expect(result).to.equal('success');
      });
    });
  });

  describe('失败登录测试', function() {
    // 只测试预期失败的用例
    const errorCases = testData.filter(data => data.expected.startsWith('error'));
    
    errorCases.forEach((data) => {
      it(`应该登录失败: ${data.description}`, function() {
        const result = simulateLogin(data.username, data.password);
        expect(result).to.equal(data.expected);
      });
    });
  });

  describe('边界值测试', function() {
    it('应该处理空用户名', function() {
      const emptyUsernameCases = testData.filter(
        data => data.username === '' || data.username === null
      );
      
      expect(emptyUsernameCases.length).to.be.greaterThan(0);
      
      emptyUsernameCases.forEach(data => {
        const result = simulateLogin(data.username, data.password);
        expect(result).to.include('error');
      });
    });

    it('应该处理空密码', function() {
      const emptyPasswordCases = testData.filter(
        data => data.password === '' || data.password === null
      );
      
      expect(emptyPasswordCases.length).to.be.greaterThan(0);
      
      emptyPasswordCases.forEach(data => {
        const result = simulateLogin(data.username, data.password);
        expect(result).to.include('error');
      });
    });
  });

  describe('数据统计', function() {
    it('应该统计测试数据分布', function() {
      const stats = {
        total: testData.length,
        success: testData.filter(d => d.expected === 'success').length,
        error_username: testData.filter(d => d.expected === 'error_username').length,
        error_password: testData.filter(d => d.expected === 'error_password').length,
        error_credentials: testData.filter(d => d.expected === 'error_credentials').length,
      };
      
      console.log('\n测试数据统计:');
      console.log(`总数: ${stats.total}`);
      console.log(`成功: ${stats.success}`);
      console.log(`用户名错误: ${stats.error_username}`);
      console.log(`密码错误: ${stats.error_password}`);
      console.log(`凭证错误: ${stats.error_credentials}`);
      
      expect(stats.total).to.be.greaterThan(0);
    });
  });
});

// 模拟登录函数
function simulateLogin(username, password) {
  // 验证用户名
  if (!username || username.trim() === '') {
    return 'error_username';
  }
  
  // 验证密码
  if (!password || password.trim() === '') {
    return 'error_password';
  }
  
  // 验证用户名格式
  if (username.includes(' ')) {
    return 'error_username';
  }
  
  // 验证用户名长度
  if (username.length > 20) {
    return 'error_username';
  }
  
  // 验证密码长度
  if (password.length < 6) {
    return 'error_password';
  }
  
  // 验证凭证
  const validCredentials = {
    'admin': 'admin123',
    'user1': 'user123',
    'user2': 'pass456',
    'test@example.com': 'test123'
  };
  
  if (validCredentials[username] === password) {
    return 'success';
  }
  
  return 'error_credentials';
}
