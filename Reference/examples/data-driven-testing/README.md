# 数据驱动测试示例

这个示例展示了如何实现数据驱动测试（Data-Driven Testing），使用不同的数据源和测试框架。

## 📋 功能特性

- ✅ CSV 文件数据驱动
- ✅ JSON 文件数据驱动
- ✅ Excel 文件数据驱动
- ✅ 数据库数据驱动
- ✅ API 数据驱动
- ✅ 参数化测试
- ✅ 测试数据生成器

## 🚀 快速开始

### 安装依赖

```bash
npm install
```

### 运行测试

```bash
# 运行所有测试
npm test

# 运行特定测试
npm test -- --grep "CSV"
```

## 📁 项目结构

```
data-driven-testing/
├── tests/
│   ├── csv-driven.test.js       # CSV 数据驱动测试
│   ├── json-driven.test.js      # JSON 数据驱动测试
│   ├── excel-driven.test.js     # Excel 数据驱动测试
│   ├── database-driven.test.js  # 数据库数据驱动测试
│   └── api-driven.test.js       # API 数据驱动测试
├── data/
│   ├── test-data.csv            # CSV 测试数据
│   ├── test-data.json           # JSON 测试数据
│   ├── test-data.xlsx           # Excel 测试数据
│   └── test-data.sql            # SQL 测试数据
├── utils/
│   ├── csv-reader.js            # CSV 读取工具
│   ├── json-reader.js           # JSON 读取工具
│   ├── excel-reader.js          # Excel 读取工具
│   └── data-generator.js        # 数据生成器
├── package.json
└── README.md
```

## 📚 测试用例

### 1. CSV 数据驱动测试

使用 CSV 文件作为测试数据源：

```csv
username,password,expected
admin,admin123,success
user1,user123,success
,password,error_username
username,,error_password
invalid,wrong,error_credentials
```

### 2. JSON 数据驱动测试

使用 JSON 文件作为测试数据源：

```json
{
  "loginTests": [
    {
      "username": "admin",
      "password": "admin123",
      "expected": "success"
    },
    {
      "username": "user1",
      "password": "user123",
      "expected": "success"
    }
  ]
}
```

### 3. Excel 数据驱动测试

使用 Excel 文件作为测试数据源，支持多个工作表。

### 4. 数据库数据驱动测试

从数据库读取测试数据：

```sql
SELECT username, password, expected_result
FROM test_data
WHERE test_type = 'login';
```

### 5. API 数据驱动测试

从 API 获取测试数据：

```javascript
const testData = await fetch('https://api.example.com/test-data');
```

## 🔧 使用方法

### CSV 数据驱动

```javascript
const csv = require('csv-parser');
const fs = require('fs');

const testData = [];

fs.createReadStream('data/test-data.csv')
  .pipe(csv())
  .on('data', (row) => testData.push(row))
  .on('end', () => {
    testData.forEach(({ username, password, expected }) => {
      it(`测试: ${username}`, async () => {
        // 测试逻辑
      });
    });
  });
```

### JSON 数据驱动

```javascript
const testData = require('./data/test-data.json');

testData.loginTests.forEach(({ username, password, expected }) => {
  it(`测试: ${username}`, async () => {
    // 测试逻辑
  });
});
```

### 参数化测试

```javascript
const testCases = [
  ['admin', 'admin123', 'success'],
  ['user1', 'user123', 'success'],
  ['', 'password', 'error'],
];

testCases.forEach(([username, password, expected]) => {
  it(`测试: ${username}`, async () => {
    // 测试逻辑
  });
});
```

## 🎯 最佳实践

### 1. 数据分离

```javascript
// ✅ 推荐：数据与测试逻辑分离
const testData = require('./data/test-data.json');

testData.forEach(data => {
  it(`测试: ${data.scenario}`, async () => {
    await performTest(data);
  });
});

// ❌ 不推荐：数据硬编码在测试中
it('测试1', async () => {
  await login('admin', 'admin123');
});
```

### 2. 数据验证

```javascript
// 验证测试数据格式
function validateTestData(data) {
  if (!data.username || !data.password) {
    throw new Error('测试数据格式错误');
  }
  return true;
}

testData.forEach(data => {
  validateTestData(data);
  it(`测试: ${data.username}`, async () => {
    // 测试逻辑
  });
});
```

### 3. 数据生成

```javascript
// 使用数据生成器
const { generateTestData } = require('./utils/data-generator');

const testData = generateTestData({
  count: 100,
  type: 'login',
  includeEdgeCases: true
});
```

### 4. 数据清理

```javascript
describe('数据驱动测试', () => {
  before(async () => {
    // 准备测试数据
    await setupTestData();
  });

  after(async () => {
    // 清理测试数据
    await cleanupTestData();
  });

  testData.forEach(data => {
    it(`测试: ${data.scenario}`, async () => {
      // 测试逻辑
    });
  });
});
```

## 📊 数据源对比

| 数据源 | 优点 | 缺点 | 适用场景 |
|--------|------|------|----------|
| CSV | 简单易用，Excel 可编辑 | 不支持复杂结构 | 简单的表格数据 |
| JSON | 支持复杂结构，易于解析 | 不易手动编辑 | 复杂的测试数据 |
| Excel | 非技术人员友好 | 需要额外库支持 | 业务人员维护数据 |
| 数据库 | 支持大量数据，易于查询 | 需要数据库环境 | 大规模测试数据 |
| API | 动态数据，实时更新 | 依赖网络和 API | 集成测试场景 |

## 🐛 常见问题

### Q: 如何处理大量测试数据？

A:
1. 使用流式读取避免内存溢出
2. 分批执行测试
3. 使用数据库存储大量数据
4. 考虑使用测试数据采样

### Q: 如何维护测试数据？

A:
1. 使用版本控制管理数据文件
2. 定期审查和更新测试数据
3. 使用数据生成器自动生成数据
4. 建立数据维护流程

### Q: 如何处理敏感数据？

A:
1. 使用环境变量存储敏感信息
2. 加密敏感数据
3. 使用测试专用数据
4. 不要将敏感数据提交到版本控制

## 📚 相关资源

- [数据驱动测试最佳实践](https://martinfowler.com/bliki/DataDrivenTesting.html)
- [Mocha 参数化测试](https://mochajs.org/)
- [Jest 数据驱动测试](https://jestjs.io/docs/api#testeachtablename-fn-timeout)

## 📝 许可证

MIT License
