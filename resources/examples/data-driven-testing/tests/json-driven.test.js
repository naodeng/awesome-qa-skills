const { expect } = require('chai');
const testData = require('../data/test-data.json');

describe('JSON 数据驱动测试', function() {
  this.timeout(30000);

  describe('登录功能测试', function() {
    testData.loginTests.forEach((data) => {
      it(`测试 ${data.id}: ${data.description}`, function() {
        console.log(`\n测试数据: ${JSON.stringify(data)}`);
        
        const result = simulateLogin(data.username, data.password);
        expect(result).to.equal(data.expected);
      });
    });
  });

  describe('搜索功能测试', function() {
    testData.searchTests.forEach((data) => {
      it(`${data.description}`, function() {
        const results = simulateSearch(data.keyword);
        
        if (data.expectedResults === 0) {
          expect(results).to.be.empty;
        } else {
          expect(results.length).to.be.at.least(1);
        }
      });
    });
  });

  describe('表单验证测试', function() {
    testData.formTests.forEach((data, index) => {
      it(`表单测试 ${index + 1}: ${data.name || '空名称'}`, function() {
        const result = validateForm(data);
        expect(result).to.equal(data.expected);
      });
    });
  });

  describe('API 测试', function() {
    testData.apiTests.forEach((data) => {
      it(`${data.method} ${data.endpoint}`, async function() {
        const response = await simulateApiCall(data.endpoint, data.method);
        
        expect(response.status).to.equal(data.expectedStatus);
        
        if (data.expectedFields.length > 0) {
          data.expectedFields.forEach(field => {
            expect(response.data).to.have.property(field);
          });
        }
      });
    });
  });

  describe('参数化测试', function() {
    // 使用数组直接定义测试数据
    const testCases = [
      { input: 'hello', expected: 'HELLO' },
      { input: 'world', expected: 'WORLD' },
      { input: 'Test123', expected: 'TEST123' },
      { input: '', expected: '' },
    ];

    testCases.forEach(({ input, expected }) => {
      it(`应该将 "${input}" 转换为 "${expected}"`, function() {
        const result = input.toUpperCase();
        expect(result).to.equal(expected);
      });
    });
  });

  describe('组合测试', function() {
    // 测试多个字段的组合
    const combinations = [
      { username: 'admin', password: 'admin123', rememberMe: true, expected: 'success' },
      { username: 'admin', password: 'admin123', rememberMe: false, expected: 'success' },
      { username: 'user1', password: 'user123', rememberMe: true, expected: 'success' },
      { username: 'user1', password: 'user123', rememberMe: false, expected: 'success' },
    ];

    combinations.forEach((data, index) => {
      it(`组合测试 ${index + 1}: ${data.username} (记住我: ${data.rememberMe})`, function() {
        const result = simulateLoginWithRememberMe(
          data.username,
          data.password,
          data.rememberMe
        );
        expect(result.status).to.equal(data.expected);
        expect(result.rememberMe).to.equal(data.rememberMe);
      });
    });
  });

  describe('嵌套数据测试', function() {
    // 测试嵌套的 JSON 数据
    const nestedData = {
      users: [
        {
          name: 'Admin',
          roles: ['admin', 'user'],
          permissions: {
            read: true,
            write: true,
            delete: true
          }
        },
        {
          name: 'User',
          roles: ['user'],
          permissions: {
            read: true,
            write: false,
            delete: false
          }
        }
      ]
    };

    nestedData.users.forEach((user) => {
      it(`应该验证 ${user.name} 的权限`, function() {
        expect(user.roles).to.be.an('array');
        expect(user.permissions).to.be.an('object');
        expect(user.permissions).to.have.property('read');
        expect(user.permissions).to.have.property('write');
        expect(user.permissions).to.have.property('delete');
      });
    });
  });

  describe('动态数据生成', function() {
    // 动态生成测试数据
    const generateTestData = (count) => {
      const data = [];
      for (let i = 1; i <= count; i++) {
        data.push({
          id: i,
          username: `user${i}`,
          email: `user${i}@example.com`,
          active: i % 2 === 0
        });
      }
      return data;
    };

    const dynamicData = generateTestData(5);

    dynamicData.forEach((user) => {
      it(`应该验证用户 ${user.username}`, function() {
        expect(user.id).to.be.a('number');
        expect(user.username).to.include('user');
        expect(user.email).to.include('@example.com');
        expect(user.active).to.be.a('boolean');
      });
    });
  });
});

// 辅助函数
function simulateLogin(username, password) {
  if (!username || username.trim() === '') {
    return 'error_username';
  }
  if (!password || password.trim() === '') {
    return 'error_password';
  }
  
  const validCredentials = {
    'admin': 'admin123',
    'user1': 'user123',
    'user2': 'pass456'
  };
  
  if (validCredentials[username] === password) {
    return 'success';
  }
  
  return 'error_credentials';
}

function simulateSearch(keyword) {
  if (!keyword || keyword.trim() === '') {
    return [];
  }
  
  const mockResults = {
    'selenium': Array(10).fill({ title: 'Selenium Result' }),
    'playwright': Array(5).fill({ title: 'Playwright Result' }),
  };
  
  return mockResults[keyword.toLowerCase()] || [];
}

function validateForm(data) {
  if (!data.name || data.name.trim() === '') {
    return 'error_name';
  }
  
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(data.email)) {
    return 'error_email';
  }
  
  if (data.age < 18 || data.age > 100) {
    return 'error_age';
  }
  
  return 'success';
}

async function simulateApiCall(endpoint, method) {
  // 模拟 API 响应
  const mockResponses = {
    '/api/users': {
      status: 200,
      data: [
        { id: 1, name: 'User 1', email: 'user1@example.com' },
        { id: 2, name: 'User 2', email: 'user2@example.com' }
      ]
    },
    '/api/users/1': {
      status: 200,
      data: { id: 1, name: 'User 1', email: 'user1@example.com', phone: '123456789' }
    },
    '/api/users/999': {
      status: 404,
      data: { error: 'User not found' }
    }
  };
  
  return mockResponses[endpoint] || { status: 404, data: {} };
}

function simulateLoginWithRememberMe(username, password, rememberMe) {
  const loginResult = simulateLogin(username, password);
  
  return {
    status: loginResult,
    rememberMe: rememberMe,
    token: loginResult === 'success' ? 'mock-token-123' : null
  };
}
