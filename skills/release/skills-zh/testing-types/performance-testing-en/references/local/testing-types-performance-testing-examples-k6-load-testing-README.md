# Local Reference

This file is an in-skill formal reference migrated from `_external`.

Original file: `testing-types__performance-testing__examples__k6-load-testing__README.md`

---

# Snapshot Reference

This file is a localized snapshot for skill portability.

---
# K6 性能测试示例

这是一个使用 K6 进行性能测试的完整示例，包含负载测试、压力测试、浸泡测试等多种场景。

## 📋 项目结构

```
k6-load-testing/
├── README.md                    # 本文件
├── scripts/                     # 测试脚本
│   ├── load-test.js            # 负载测试
│   ├── stress-test.js          # 压力测试
│   ├── spike-test.js           # 尖峰测试
│   ├── soak-test.js            # 浸泡测试
│   └── api-test.js             # API 性能测试
├── config/                      # 配置文件
│   ├── thresholds.js           # 性能阈值
│   └── scenarios.js            # 测试场景
├── utils/                       # 工具函数
│   ├── helpers.js              # 辅助函数
│   └── data.js                 # 测试数据
├── reports/                     # 测试报告（自动生成）
└── run-tests.sh                # 运行脚本
```

## 🎯 测试类型说明

### 1. 负载测试 (Load Test)
评估系统在预期负载下的性能表现。

**场景**: 模拟正常业务量，验证系统是否满足性能要求。

### 2. 压力测试 (Stress Test)
找出系统的性能极限和瓶颈。

**场景**: 逐步增加负载直到系统崩溃或性能严重下降。

### 3. 尖峰测试 (Spike Test)
测试系统应对突发流量的能力。

**场景**: 短时间内流量急剧增加。

### 4. 浸泡测试 (Soak Test)
验证系统长时间运行的稳定性。

**场景**: 在正常负载下持续运行数小时或数天。

## 🚀 快速开始

### 1. 安装 K6

```bash
# macOS
brew install k6

# Linux
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D69
echo "deb https://dl.k6.io/deb stable main" | sudo tee /etc/apt/sources.list.d/k6.list
sudo apt-get update
sudo apt-get install k6

# Windows (使用 Chocolatey)
choco install k6
```


### 2. 运行测试

```bash
# 运行负载测试
k6 run scripts/load-test.js

# 运行压力测试
k6 run scripts/stress-test.js

# 运行尖峰测试
k6 run scripts/spike-test.js

# 运行浸泡测试
k6 run scripts/soak-test.js

# 使用自定义配置
k6 run --vus 100 --duration 5m scripts/load-test.js

# 生成 HTML 报告
k6 run --out json=reports/results.json scripts/load-test.js
```

### 3. 使用运行脚本

```bash
# 赋予执行权限
chmod +x run-tests.sh

# 运行所有测试
./run-tests.sh all

# 运行特定测试
./run-tests.sh load
./run-tests.sh stress
./run-tests.sh spike
./run-tests.sh soak
```

## 📝 代码示例

### 负载测试 (load-test.js)

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';
import { Rate } from 'k6/metrics';

// 自定义指标
const errorRate = new Rate('errors');

// 测试配置
export const options = {
  stages: [
    { duration: '2m', target: 100 },  // 2分钟内增加到100个用户
    { duration: '5m', target: 100 },  // 保持100个用户5分钟
    { duration: '2m', target: 200 },  // 2分钟内增加到200个用户
    { duration: '5m', target: 200 },  // 保持200个用户5分钟
    { duration: '2m', target: 0 },    // 2分钟内降到0
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],  // 95%的请求响应时间<500ms
    http_req_failed: ['rate<0.01'],    // 错误率<1%
    errors: ['rate<0.1'],              // 自定义错误率<10%
  },
};

export default function () {
  // 测试首页
  const homeRes = http.get('https://test.k6.io');
  
  check(homeRes, {
    '首页状态码是 200': (r) => r.status === 200,
    '首页响应时间 < 500ms': (r) => r.timings.duration < 500,
  }) || errorRate.add(1);

  sleep(1);

  // 测试登录
  const loginRes = http.post('https://test.k6.io/login', {
    username: 'test',
    password: 'test123',
  });

  check(loginRes, {
    '登录状态码是 200': (r) => r.status === 200,
    '登录成功': (r) => r.json('authenticated') === true,
  }) || errorRate.add(1);

  sleep(1);
}
```

### 压力测试 (stress-test.js)

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '2m', target: 100 },   // 预热
    { duration: '5m', target: 100 },   // 稳定
    { duration: '2m', target: 200 },   // 增加负载
    { duration: '5m', target: 200 },   
    { duration: '2m', target: 300 },   // 继续增加
    { duration: '5m', target: 300 },   
    { duration: '2m', target: 400 },   // 达到极限
    { duration: '5m', target: 400 },   
    { duration: '10m', target: 0 },    // 恢复
  ],
  thresholds: {
    http_req_duration: ['p(99)<1500'],
    http_req_failed: ['rate<0.05'],
  },
};

export default function () {
  const res = http.get('https://test.k6.io');
  check(res, { '状态码是 200': (r) => r.status === 200 });
  sleep(1);
}
```

### API 性能测试 (api-test.js)

```javascript
import http from 'k6/http';
import { check, group, sleep } from 'k6';

export const options = {
  vus: 50,
  duration: '5m',
  thresholds: {
    'http_req_duration{api:users}': ['p(95)<300'],
    'http_req_duration{api:posts}': ['p(95)<400'],
    'http_req_failed': ['rate<0.01'],
  },
};

const BASE_URL = 'https://jsonplaceholder.typicode.com';

export default function () {
  group('用户 API', function () {
    // 获取用户列表
    const listRes = http.get(`${BASE_URL}/users`, {
      tags: { api: 'users' },
    });
    
    check(listRes, {
      '获取用户列表成功': (r) => r.status === 200,
      '返回数据是数组': (r) => Array.isArray(r.json()),
    });

    sleep(1);

    // 获取单个用户
    const userId = Math.floor(Math.random() * 10) + 1;
    const userRes = http.get(`${BASE_URL}/users/${userId}`, {
      tags: { api: 'users' },
    });
    
    check(userRes, {
      '获取用户详情成功': (r) => r.status === 200,
      '用户有 ID': (r) => r.json('id') !== undefined,
    });

    sleep(1);
  });

  group('文章 API', function () {
    // 获取文章列表
    const postsRes = http.get(`${BASE_URL}/posts`, {
      tags: { api: 'posts' },
    });
    
    check(postsRes, {
      '获取文章列表成功': (r) => r.status === 200,
    });

    sleep(1);

    // 创建文章
    const createRes = http.post(
      `${BASE_URL}/posts`,
      JSON.stringify({
        title: 'Test Post',
        body: 'This is a test post',
        userId: 1,
      }),
      {
        headers: { 'Content-Type': 'application/json' },
        tags: { api: 'posts' },
      }
    );
    
    check(createRes, {
      '创建文章成功': (r) => r.status === 201,
    });

    sleep(1);
  });
}
```

## 📊 性能指标说明

### 核心指标

| 指标 | 说明 | 目标值 |
|------|------|--------|
| http_req_duration | 请求响应时间 | p(95) < 500ms |
| http_req_failed | 请求失败率 | < 1% |
| http_reqs | 每秒请求数 (RPS) | 根据需求 |
| vus | 虚拟用户数 | 根据场景 |
| iterations | 迭代次数 | 根据场景 |

### 百分位数 (Percentiles)

- **p(50)**: 中位数，50%的请求响应时间
- **p(90)**: 90%的请求响应时间
- **p(95)**: 95%的请求响应时间
- **p(99)**: 99%的请求响应时间


## 🔧 高级功能

### 1. 使用检查点 (Checks)

```javascript
import { check } from 'k6';

check(response, {
  '状态码是 200': (r) => r.status === 200,
  '响应时间 < 500ms': (r) => r.timings.duration < 500,
  '响应体包含关键字': (r) => r.body.includes('success'),
});
```

### 2. 自定义指标

```javascript
import { Counter, Gauge, Rate, Trend } from 'k6/metrics';

const myCounter = new Counter('my_counter');
const myGauge = new Gauge('my_gauge');
const myRate = new Rate('my_rate');
const myTrend = new Trend('my_trend');

export default function () {
  myCounter.add(1);
  myGauge.add(100);
  myRate.add(true);
  myTrend.add(response.timings.duration);
}
```

### 3. 场景配置

```javascript
export const options = {
  scenarios: {
    constant_load: {
      executor: 'constant-vus',
      vus: 100,
      duration: '5m',
    },
    ramping_load: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '2m', target: 100 },
        { duration: '5m', target: 100 },
        { duration: '2m', target: 0 },
      ],
    },
  },
};
```

### 4. 数据参数化

```javascript
import { SharedArray } from 'k6/data';
import papaparse from 'https://jslib.k6.io/papaparse/5.1.1/index.js';

const csvData = new SharedArray('users', function () {
  return papaparse.parse(open('./data/users.csv'), { header: true }).data;
});

export default function () {
  const user = csvData[Math.floor(Math.random() * csvData.length)];
  http.post('https://test.k6.io/login', {
    username: user.username,
    password: user.password,
  });
}
```

### 5. 环境变量

```javascript
const BASE_URL = __ENV.BASE_URL || 'https://test.k6.io';
const VUS = __ENV.VUS || 10;

export const options = {
  vus: VUS,
  duration: '5m',
};

export default function () {
  http.get(BASE_URL);
}
```

运行时传递环境变量：
```bash
k6 run -e BASE_URL=https://example.com -e VUS=100 script.js
```

## 📈 测试报告

### 控制台输出

```
     ✓ 首页状态码是 200
     ✓ 首页响应时间 < 500ms

     checks.........................: 100.00% ✓ 2000      ✗ 0
     data_received..................: 1.2 MB  40 kB/s
     data_sent......................: 180 kB  6.0 kB/s
     http_req_blocked...............: avg=1.2ms    min=1µs     med=3µs     max=150ms   p(90)=5µs     p(95)=7µs
     http_req_connecting............: avg=500µs    min=0s      med=0s      max=50ms    p(90)=0s      p(95)=0s
     http_req_duration..............: avg=250ms    min=100ms   med=230ms   max=800ms   p(90)=350ms   p(95)=400ms
     http_req_failed................: 0.00%   ✓ 0         ✗ 1000
     http_req_receiving.............: avg=1ms      min=50µs    med=800µs   max=50ms    p(90)=2ms     p(95)=3ms
     http_req_sending...............: avg=50µs     min=10µs    med=40µs    max=5ms     p(90)=80µs    p(95)=100µs
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s      p(90)=0s      p(95)=0s
     http_req_waiting...............: avg=249ms    min=99ms    med=229ms   max=799ms   p(90)=349ms   p(95)=399ms
     http_reqs......................: 1000    33.33/s
     iteration_duration.............: avg=1.25s    min=1.1s    med=1.23s   max=1.8s    p(90)=1.35s   p(95)=1.4s
     iterations.....................: 1000    33.33/s
     vus............................: 100     min=100     max=100
     vus_max........................: 100     min=100     max=100
```

### JSON 输出

```bash
k6 run --out json=reports/results.json script.js
```

### HTML 报告（使用 k6-reporter）

```bash
# 安装 k6-reporter
npm install -g k6-to-html

# 生成报告
k6 run --out json=results.json script.js
k6-to-html results.json --output reports/report.html
```

### 集成到 Grafana

```bash
# 使用 InfluxDB + Grafana
k6 run --out influxdb=http://localhost:8086/k6 script.js
```

## 🎯 最佳实践

### 1. 测试设计原则

- ✅ 从小规模开始，逐步增加负载
- ✅ 使用真实的用户行为模式
- ✅ 设置合理的思考时间（sleep）
- ✅ 定义明确的性能目标（thresholds）
- ✅ 监控系统资源（CPU、内存、网络）

### 2. 阈值设置

```javascript
export const options = {
  thresholds: {
    // 响应时间
    'http_req_duration': ['p(95)<500', 'p(99)<1000'],
    
    // 错误率
    'http_req_failed': ['rate<0.01'],
    
    // 特定 API 的阈值
    'http_req_duration{api:users}': ['p(95)<300'],
    
    // 检查通过率
    'checks': ['rate>0.95'],
  },
};
```

### 3. 场景设计

```javascript
export const options = {
  scenarios: {
    // 预热阶段
    warmup: {
      executor: 'constant-vus',
      vus: 10,
      duration: '1m',
      startTime: '0s',
    },
    // 负载测试
    load_test: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '2m', target: 100 },
        { duration: '5m', target: 100 },
        { duration: '2m', target: 0 },
      ],
      startTime: '1m',
    },
  },
};
```

### 4. 错误处理

```javascript
import { check } from 'k6';

export default function () {
  const res = http.get('https://test.k6.io');
  
  if (!check(res, { '状态码是 200': (r) => r.status === 200 })) {
    console.error(`请求失败: ${res.status} - ${res.body}`);
  }
}
```

## 🐛 常见问题

### 1. 连接超时

**问题**: `request timeout`

**解决方案**:
```javascript
export const options = {
  timeout: '60s',  // 增加超时时间
};
```

### 2. 内存不足

**问题**: K6 占用内存过高

**解决方案**:
- 减少虚拟用户数
- 使用 SharedArray 共享数据
- 避免在循环中创建大对象

### 3. 证书验证错误

**问题**: SSL certificate verification failed

**解决方案**:
```javascript
export const options = {
  insecureSkipTLSVerify: true,  // 跳过证书验证（仅测试环境）
};
```

### 4. 速率限制

**问题**: 被服务器限流

**解决方案**:
```javascript
import { sleep } from 'k6';

export default function () {
  http.get('https://test.k6.io');
  sleep(Math.random() * 2 + 1);  // 随机延迟 1-3 秒
}
```

## 📚 参考资源

- K6 官方文档 (https://k6.io/docs/)
- K6 示例库 (https://k6.io/docs/examples/)
- 性能测试最佳实践 (https://k6.io/docs/testing-guides/test-types/)
- K6 扩展 (https://k6.io/docs/extensions/)

## 🎓 学习路径

1. ✅ 运行基础负载测试
2. ✅ 理解性能指标
3. ✅ 设置性能阈值
4. ✅ 创建自定义场景
5. ✅ 使用数据参数化
6. ✅ 集成到 CI/CD
7. ✅ 分析和优化性能

---

**难度级别**: 中级  
**预计学习时间**: 30-60 分钟  
**最后更新**: 2026-02-06
