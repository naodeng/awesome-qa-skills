# 性能测试教程

## 📚 学习目标

完成本教程后，你将能够：
- 理解性能测试的核心概念和指标
- 使用 K6 编写负载测试脚本
- 分析性能测试结果
- 识别性能瓶颈
- 实施性能优化建议

## 🎯 前置要求

- 了解 HTTP 协议基础
- 基本的 JavaScript 知识
- 理解 API 测试概念
- 安装 K6 工具

## 📖 教程内容

### 第1步：性能测试基础（15分钟）

#### 1.1 什么是性能测试？

性能测试是评估系统在特定工作负载下的响应时间、吞吐量、资源利用率等指标的过程。

**性能测试类型：**
- 🔄 **负载测试** - 测试系统在预期负载下的表现
- 📈 **压力测试** - 测试系统的极限和崩溃点
- 🎯 **峰值测试** - 测试系统处理突发流量的能力
- ⏱️ **耐久测试** - 测试系统长时间运行的稳定性
- 📊 **容量测试** - 确定系统能支持的最大用户数

#### 1.2 关键性能指标

```
📊 响应时间 (Response Time)
   - 平均响应时间
   - 95th/99th 百分位响应时间
   - 最大/最小响应时间

🚀 吞吐量 (Throughput)
   - 每秒请求数 (RPS)
   - 每秒事务数 (TPS)

❌ 错误率 (Error Rate)
   - HTTP 错误数量
   - 超时数量

💻 资源利用率
   - CPU 使用率
   - 内存使用率
   - 网络带宽
```

### 第2步：安装和配置 K6（10分钟）

#### 2.1 安装 K6

**macOS:**
```bash
brew install k6
```

**Linux:**
```bash
sudo gpg -k
sudo gpg --no-default-keyring --keyring /usr/share/keyrings/k6-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D69
echo "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main" | sudo tee /etc/apt/sources.list.d/k6.list
sudo apt-get update
sudo apt-get install k6
```

**Windows:**
```powershell
choco install k6
```

#### 2.2 验证安装

```bash
k6 version
```

### 第3步：编写第一个性能测试（20分钟）

#### 3.1 简单的负载测试

创建 `load-test.js`：

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

// 测试配置
export const options = {
  vus: 10,        // 10 个虚拟用户
  duration: '30s', // 持续 30 秒
};

// 测试场景
export default function () {
  // 发送 HTTP 请求
  const response = http.get('https://test-api.k6.io/public/crocodiles/');
  
  // 验证响应
  check(response, {
    '状态码是 200': (r) => r.status === 200,
    '响应时间 < 500ms': (r) => r.timings.duration < 500,
  });
  
  // 模拟用户思考时间
  sleep(1);
}
```

#### 3.2 运行测试

```bash
k6 run load-test.js
```

#### 3.3 理解测试结果

```
     ✓ 状态码是 200
     ✓ 响应时间 < 500ms

     checks.........................: 100.00% ✓ 600  ✗ 0
     data_received..................: 1.2 MB  40 kB/s
     data_sent......................: 24 kB   800 B/s
     http_req_blocked...............: avg=1.2ms   min=1µs    med=3µs    max=123ms  p(90)=5µs    p(95)=7µs
     http_req_connecting............: avg=524µs   min=0s     med=0s     max=52ms   p(90)=0s     p(95)=0s
     http_req_duration..............: avg=145ms   min=102ms  med=142ms  max=234ms  p(90)=167ms  p(95)=178ms
     http_req_receiving.............: avg=128µs   min=49µs   med=113µs  max=1.2ms  p(90)=182µs  p(95)=221µs
     http_req_sending...............: avg=43µs    min=13µs   med=38µs   max=218µs  p(90)=66µs   p(95)=80µs
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s     max=0s     p(90)=0s     p(95)=0s
     http_req_waiting...............: avg=144ms   min=102ms  med=141ms  max=233ms  p(90)=166ms  p(95)=177ms
     http_reqs......................: 300     10/s
     iteration_duration.............: avg=1.14s   min=1.1s   med=1.14s  max=1.33s  p(90)=1.16s  p(95)=1.18s
     iterations.....................: 300     10/s
     vus............................: 10      min=10 max=10
     vus_max........................: 10      min=10 max=10
```

### 第4步：高级负载场景（30分钟）

#### 4.1 阶梯式负载测试

创建 `ramp-up-test.js`：

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '1m', target: 20 },   // 1分钟内增加到 20 用户
    { duration: '3m', target: 20 },   // 保持 20 用户 3 分钟
    { duration: '1m', target: 50 },   // 1分钟内增加到 50 用户
    { duration: '3m', target: 50 },   // 保持 50 用户 3 分钟
    { duration: '1m', target: 0 },    // 1分钟内降到 0 用户
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% 的请求应在 500ms 内完成
    http_req_failed: ['rate<0.01'],   // 错误率应低于 1%
  },
};

export default function () {
  const response = http.get('https://test-api.k6.io/public/crocodiles/');
  
  check(response, {
    '状态码是 200': (r) => r.status === 200,
  });
  
  sleep(1);
}
```

#### 4.2 压力测试

创建 `stress-test.js`：

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '2m', target: 100 },  // 快速增加到 100 用户
    { duration: '5m', target: 100 },  // 保持 100 用户
    { duration: '2m', target: 200 },  // 增加到 200 用户
    { duration: '5m', target: 200 },  // 保持 200 用户
    { duration: '2m', target: 300 },  // 增加到 300 用户
    { duration: '5m', target: 300 },  // 保持 300 用户
    { duration: '10m', target: 0 },   // 逐渐降到 0
  ],
};

export default function () {
  const response = http.get('https://test-api.k6.io/');
  check(response, { '状态码是 200': (r) => r.status === 200 });
  sleep(1);
}
```

#### 4.3 峰值测试

创建 `spike-test.js`：

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '10s', target: 100 },  // 快速增加到 100 用户
    { duration: '1m', target: 100 },   // 保持 100 用户
    { duration: '10s', target: 1400 }, // 突然增加到 1400 用户（峰值）
    { duration: '3m', target: 1400 },  // 保持峰值
    { duration: '10s', target: 100 },  // 快速降回 100 用户
    { duration: '3m', target: 100 },   // 恢复正常
    { duration: '10s', target: 0 },    // 降到 0
  ],
};

export default function () {
  const response = http.get('https://test-api.k6.io/');
  check(response, { '状态码是 200': (r) => r.status === 200 });
  sleep(1);
}
```

### 第5步：真实场景测试（35分钟）

#### 5.1 用户登录场景

创建 `user-flow-test.js`：

```javascript
import http from 'k6/http';
import { check, group, sleep } from 'k6';

export const options = {
  vus: 50,
  duration: '5m',
  thresholds: {
    'http_req_duration{scenario:login}': ['p(95)<1000'],
    'http_req_duration{scenario:browse}': ['p(95)<500'],
  },
};

export default function () {
  const baseUrl = 'https://test-api.k6.io';
  
  // 场景1: 用户登录
  group('用户登录', function () {
    const loginRes = http.post(`${baseUrl}/auth/token/login/`, {
      username: 'test_user',
      password: 'test_password',
    }, {
      tags: { scenario: 'login' },
    });
    
    check(loginRes, {
      '登录成功': (r) => r.status === 200,
      '返回 token': (r) => r.json('access') !== undefined,
    });
    
    const authToken = loginRes.json('access');
    
    // 场景2: 浏览内容
    group('浏览内容', function () {
      const headers = {
        'Authorization': `Bearer ${authToken}`,
      };
      
      const listRes = http.get(`${baseUrl}/my/crocodiles/`, {
        headers,
        tags: { scenario: 'browse' },
      });
      
      check(listRes, {
        '获取列表成功': (r) => r.status === 200,
        '列表不为空': (r) => r.json().length > 0,
      });
      
      sleep(2);
      
      // 场景3: 查看详情
      const detailRes = http.get(`${baseUrl}/my/crocodiles/1/`, {
        headers,
        tags: { scenario: 'browse' },
      });
      
      check(detailRes, {
        '获取详情成功': (r) => r.status === 200,
      });
    });
  });
  
  sleep(3);
}
```

#### 5.2 电商购物场景

创建 `ecommerce-test.js`：

```javascript
import http from 'k6/http';
import { check, group, sleep } from 'k6';
import { randomIntBetween } from 'https://jslib.k6.io/k6-utils/1.2.0/index.js';

export const options = {
  stages: [
    { duration: '2m', target: 100 },
    { duration: '5m', target: 100 },
    { duration: '2m', target: 0 },
  ],
};

export default function () {
  const baseUrl = 'https://test-api.k6.io';
  
  // 1. 访问首页
  group('访问首页', function () {
    const res = http.get(`${baseUrl}/`);
    check(res, { '首页加载成功': (r) => r.status === 200 });
    sleep(randomIntBetween(2, 5));
  });
  
  // 2. 搜索商品
  group('搜索商品', function () {
    const res = http.get(`${baseUrl}/public/crocodiles/`);
    check(res, { '搜索成功': (r) => r.status === 200 });
    sleep(randomIntBetween(1, 3));
  });
  
  // 3. 查看商品详情
  group('查看商品详情', function () {
    const productId = randomIntBetween(1, 10);
    const res = http.get(`${baseUrl}/public/crocodiles/${productId}/`);
    check(res, { '详情加载成功': (r) => r.status === 200 });
    sleep(randomIntBetween(3, 7));
  });
  
  // 4. 添加到购物车
  group('添加到购物车', function () {
    const res = http.post(`${baseUrl}/my/crocodiles/`, {
      name: 'Test Product',
      sex: 'M',
      date_of_birth: '2020-01-01',
    });
    check(res, { '添加成功': (r) => r.status === 201 });
    sleep(1);
  });
  
  sleep(randomIntBetween(1, 3));
}
```

### 第6步：数据驱动测试（20分钟）

#### 6.1 使用 CSV 文件

创建 `users.csv`：

```csv
username,password
user1,pass1
user2,pass2
user3,pass3
```

创建 `data-driven-test.js`：

```javascript
import http from 'k6/http';
import { check } from 'k6';
import { SharedArray } from 'k6/data';
import papaparse from 'https://jslib.k6.io/papaparse/5.1.1/index.js';

// 加载 CSV 数据
const csvData = new SharedArray('users', function () {
  return papaparse.parse(open('./users.csv'), { header: true }).data;
});

export const options = {
  vus: csvData.length,
  iterations: csvData.length,
};

export default function () {
  const user = csvData[__VU - 1];
  
  const response = http.post('https://test-api.k6.io/auth/token/login/', {
    username: user.username,
    password: user.password,
  });
  
  check(response, {
    [`${user.username} 登录成功`]: (r) => r.status === 200,
  });
}
```

#### 6.2 使用 JSON 文件

创建 `test-data.json`：

```json
{
  "users": [
    { "username": "admin", "password": "admin123", "role": "admin" },
    { "username": "user1", "password": "user123", "role": "user" }
  ],
  "products": [
    { "id": 1, "name": "Product 1", "price": 100 },
    { "id": 2, "name": "Product 2", "price": 200 }
  ]
}
```

使用 JSON 数据：

```javascript
import { SharedArray } from 'k6/data';

const testData = JSON.parse(open('./test-data.json'));

export default function () {
  const user = testData.users[__VU % testData.users.length];
  // 使用用户数据进行测试
}
```

### 第7步：结果分析和报告（15分钟）

#### 7.1 生成 HTML 报告

```bash
# 运行测试并生成 JSON 输出
k6 run --out json=results.json load-test.js

# 使用 k6-reporter 生成 HTML 报告
npm install -g k6-to-junit
k6-to-junit results.json > report.xml
```

#### 7.2 集成 Grafana

```bash
# 使用 InfluxDB 和 Grafana
k6 run --out influxdb=http://localhost:8086/k6 load-test.js
```

#### 7.3 自定义指标

```javascript
import { Trend, Counter } from 'k6/metrics';

const myTrend = new Trend('my_custom_metric');
const myCounter = new Counter('my_custom_counter');

export default function () {
  const start = Date.now();
  
  // 执行操作
  http.get('https://test-api.k6.io/');
  
  const duration = Date.now() - start;
  myTrend.add(duration);
  myCounter.add(1);
}
```

### 第8步：性能优化建议（10分钟）

#### 8.1 识别性能瓶颈

**常见瓶颈：**
- 🐌 数据库查询慢
- 🔄 API 响应时间长
- 💾 内存泄漏
- 🌐 网络延迟
- 🔒 资源竞争

#### 8.2 优化策略

```javascript
// 1. 使用连接池
export const options = {
  batch: 10,           // 批量请求
  batchPerHost: 5,     // 每个主机的批量请求数
};

// 2. 优化等待时间
sleep(randomIntBetween(1, 3)); // 随机等待时间

// 3. 使用缓存
const cachedData = http.get('https://test-api.k6.io/', {
  headers: { 'Cache-Control': 'max-age=3600' },
});

// 4. 减少不必要的请求
if (response.status === 200) {
  // 只在成功时继续
}
```

## 🎓 练习任务

### 初级练习
1. 为一个简单的 API 编写负载测试
2. 测试不同并发用户数下的性能
3. 生成性能测试报告

### 中级练习
1. 实现完整的用户场景测试
2. 使用数据驱动测试
3. 设置性能阈值和告警

### 高级练习
1. 实现复杂的电商场景测试
2. 集成 Grafana 实时监控
3. 进行性能瓶颈分析和优化

## 📚 延伸阅读

- [K6 官方文档](https://k6.io/docs/)
- [性能测试最佳实践](https://k6.io/docs/testing-guides/test-types/)
- [性能优化指南](https://web.dev/performance/)
- [负载测试策略](https://martinfowler.com/articles/practical-test-pyramid.html)

## 🔗 相关资源

- [K6 示例代码](examples/)
- [性能测试 Skill](./SKILL.md)
- [快速开始指南](./quick-start.md)

## ❓ 常见问题

### Q: 需要多少虚拟用户？
A: 根据预期的并发用户数和业务场景确定。通常从小规模开始，逐步增加。

### Q: 如何确定性能基准？
A: 
- 分析历史数据
- 参考行业标准
- 根据业务需求设定 SLA

### Q: 测试应该运行多久？
A: 
- 负载测试：5-30 分钟
- 压力测试：30-60 分钟
- 耐久测试：数小时到数天

## 🎉 下一步

完成本教程后，你可以：
- 学习 [安全测试教程](references/local/testing-types-security-testing-SKILL.md)
- 探索 [移动测试教程](references/local/testing-types-mobile-testing-tutorial.md)
- 查看 [可访问性测试教程](references/local/testing-types-accessibility-testing-SKILL.md)

---

*预计完成时间: 2-3 小时*  
*难度级别: 中级*
