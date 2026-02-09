/**
 * 测试数据生成器
 * 用于动态生成各种类型的测试数据
 */

class DataGenerator {
  /**
   * 生成随机字符串
   */
  static randomString(length = 10) {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let result = '';
    for (let i = 0; i < length; i++) {
      result += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return result;
  }

  /**
   * 生成随机数字
   */
  static randomNumber(min = 0, max = 100) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  /**
   * 生成随机邮箱
   */
  static randomEmail() {
    const username = this.randomString(8).toLowerCase();
    const domains = ['example.com', 'test.com', 'demo.com'];
    const domain = domains[Math.floor(Math.random() * domains.length)];
    return `${username}@${domain}`;
  }

  /**
   * 生成随机电话号码
   */
  static randomPhone() {
    return `1${this.randomNumber(3, 9)}${this.randomNumber(10000000, 99999999)}`;
  }

  /**
   * 生成登录测试数据
   */
  static generateLoginData(options = {}) {
    const {
      count = 10,
      includeValid = true,
      includeInvalid = true,
      includeEdgeCases = true
    } = options;

    const data = [];

    // 有效数据
    if (includeValid) {
      for (let i = 1; i <= Math.floor(count / 3); i++) {
        data.push({
          username: `user${i}`,
          password: `pass${i}123`,
          expected: 'success',
          description: `有效用户 ${i}`
        });
      }
    }

    // 无效数据
    if (includeInvalid) {
      data.push({
        username: this.randomString(8),
        password: this.randomString(8),
        expected: 'error_credentials',
        description: '无效的凭证'
      });
    }

    // 边界值
    if (includeEdgeCases) {
      data.push(
        {
          username: '',
          password: 'password',
          expected: 'error_username',
          description: '空用户名'
        },
        {
          username: 'username',
          password: '',
          expected: 'error_password',
          description: '空密码'
        },
        {
          username: this.randomString(100),
          password: 'password',
          expected: 'error_username',
          description: '用户名过长'
        },
        {
          username: 'user',
          password: '12',
          expected: 'error_password',
          description: '密码过短'
        }
      );
    }

    return data;
  }

  /**
   * 生成表单测试数据
   */
  static generateFormData(options = {}) {
    const { count = 10 } = options;
    const data = [];

    for (let i = 1; i <= count; i++) {
      data.push({
        name: `测试用户${i}`,
        email: this.randomEmail(),
        age: this.randomNumber(18, 65),
        phone: this.randomPhone(),
        address: `测试地址${i}`,
        city: ['北京', '上海', '广州', '深圳'][i % 4],
        country: '中国'
      });
    }

    return data;
  }

  /**
   * 生成 API 测试数据
   */
  static generateApiTestData(options = {}) {
    const { endpoints = [], methods = ['GET', 'POST', 'PUT', 'DELETE'] } = options;

    const data = [];

    endpoints.forEach(endpoint => {
      methods.forEach(method => {
        data.push({
          endpoint,
          method,
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${this.randomString(32)}`
          },
          body: method !== 'GET' ? {
            id: this.randomNumber(1, 1000),
            name: this.randomString(10),
            email: this.randomEmail()
          } : null
        });
      });
    });

    return data;
  }

  /**
   * 生成搜索测试数据
   */
  static generateSearchData(options = {}) {
    const { count = 10 } = options;
    const data = [];

    const keywords = [
      'selenium', 'playwright', 'cypress', 'webdriver',
      'testing', 'automation', 'qa', 'test'
    ];

    for (let i = 0; i < count; i++) {
      const keyword = keywords[i % keywords.length];
      data.push({
        keyword,
        expectedResults: this.randomNumber(1, 100),
        filters: {
          category: ['技术', '工具', '框架'][i % 3],
          sortBy: ['relevance', 'date', 'popularity'][i % 3]
        }
      });
    }

    return data;
  }

  /**
   * 生成边界值测试数据
   */
  static generateBoundaryData(field, type = 'string') {
    const data = [];

    switch (type) {
      case 'string':
        data.push(
          { [field]: '', description: '空字符串' },
          { [field]: ' ', description: '单个空格' },
          { [field]: '   ', description: '多个空格' },
          { [field]: 'a', description: '单个字符' },
          { [field]: this.randomString(10), description: '正常长度' },
          { [field]: this.randomString(100), description: '较长字符串' },
          { [field]: this.randomString(1000), description: '超长字符串' },
          { [field]: '特殊字符!@#$%^&*()', description: '特殊字符' },
          { [field]: '<script>alert("xss")</script>', description: 'XSS 攻击' },
          { [field]: "'; DROP TABLE users; --", description: 'SQL 注入' }
        );
        break;

      case 'number':
        data.push(
          { [field]: 0, description: '零' },
          { [field]: -1, description: '负数' },
          { [field]: 1, description: '最小正数' },
          { [field]: 100, description: '正常数值' },
          { [field]: Number.MAX_SAFE_INTEGER, description: '最大安全整数' },
          { [field]: Number.MIN_SAFE_INTEGER, description: '最小安全整数' },
          { [field]: 3.14, description: '小数' },
          { [field]: NaN, description: 'NaN' },
          { [field]: Infinity, description: '无穷大' }
        );
        break;

      case 'email':
        data.push(
          { [field]: 'valid@example.com', description: '有效邮箱' },
          { [field]: 'invalid', description: '无效格式' },
          { [field]: '@example.com', description: '缺少用户名' },
          { [field]: 'user@', description: '缺少域名' },
          { [field]: 'user@domain', description: '缺少顶级域名' },
          { [field]: 'user name@example.com', description: '包含空格' },
          { [field]: 'user@domain@example.com', description: '多个@符号' }
        );
        break;

      case 'phone':
        data.push(
          { [field]: '13800138000', description: '有效手机号' },
          { [field]: '1380013800', description: '位数不足' },
          { [field]: '138001380000', description: '位数过多' },
          { [field]: 'abcdefghijk', description: '非数字' },
          { [field]: '00000000000', description: '全零' }
        );
        break;
    }

    return data;
  }

  /**
   * 生成组合测试数据
   */
  static generateCombinationData(fields) {
    const combinations = [];
    
    function generateCombinations(current, remaining) {
      if (remaining.length === 0) {
        combinations.push({ ...current });
        return;
      }

      const [field, ...rest] = remaining;
      const [fieldName, values] = field;

      values.forEach(value => {
        generateCombinations(
          { ...current, [fieldName]: value },
          rest
        );
      });
    }

    generateCombinations({}, Object.entries(fields));
    return combinations;
  }

  /**
   * 生成性能测试数据
   */
  static generatePerformanceData(options = {}) {
    const { userCount = 100, duration = 60 } = options;
    const data = [];

    for (let i = 1; i <= userCount; i++) {
      data.push({
        userId: i,
        username: `user${i}`,
        startTime: Math.floor(Math.random() * duration),
        actions: this.randomNumber(5, 20),
        thinkTime: this.randomNumber(1, 5)
      });
    }

    return data;
  }

  /**
   * 导出为 CSV 格式
   */
  static toCSV(data) {
    if (data.length === 0) return '';

    const headers = Object.keys(data[0]);
    const rows = data.map(row => 
      headers.map(header => {
        const value = row[header];
        // 处理包含逗号或引号的值
        if (typeof value === 'string' && (value.includes(',') || value.includes('"'))) {
          return `"${value.replace(/"/g, '""')}"`;
        }
        return value;
      }).join(',')
    );

    return [headers.join(','), ...rows].join('\n');
  }

  /**
   * 导出为 JSON 格式
   */
  static toJSON(data, pretty = true) {
    return JSON.stringify(data, null, pretty ? 2 : 0);
  }
}

module.exports = DataGenerator;
