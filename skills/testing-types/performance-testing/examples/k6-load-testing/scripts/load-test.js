/**
 * 负载测试 - Load Test
 * 
 * 目的：评估系统在预期负载下的性能表现
 * 场景：模拟正常业务量，验证系统是否满足性能要求
 */

import http from 'k6/http';
import { check, sleep, group } from 'k6';
import { Rate, Trend } from 'k6/metrics';

// 自定义指标
const errorRate = new Rate('errors');
const customTrend = new Trend('custom_duration');

// 测试配置
export const options = {
  stages: [
    { duration: '2m', target: 50 },   // 预热：2分钟内增加到50个用户
    { duration: '5m', target: 50 },   // 稳定：保持50个用户5分钟
    { duration: '2m', target: 100 },  // 增加：2分钟内增加到100个用户
    { duration: '5m', target: 100 },  // 稳定：保持100个用户5分钟
    { duration: '2m', target: 0 },    // 降温：2分钟内降到0
  ],
  
  // 性能阈值
  thresholds: {
    'http_req_duration': ['p(95)<500', 'p(99)<1000'],  // 95%请求<500ms, 99%<1000ms
    'http_req_failed': ['rate<0.01'],                   // 错误率<1%
    'errors': ['rate<0.1'],                             // 自定义错误率<10%
    'checks': ['rate>0.95'],                            // 检查通过率>95%
  },
};

const BASE_URL = __ENV.BASE_URL || 'https://test.k6.io';

// 设置函数 - 在测试开始前执行一次
export function setup() {
  console.log('开始负载测试...');
  console.log(`目标 URL: ${BASE_URL}`);
  return { startTime: new Date().toISOString() };
}

// 主测试函数
export default function (data) {
  // 测试首页
  group('首页访问', function () {
    const homeRes = http.get(`${BASE_URL}/`);
    
    const homeCheck = check(homeRes, {
      '首页状态码是 200': (r) => r.status === 200,
      '首页响应时间 < 500ms': (r) => r.timings.duration < 500,
      '首页包含标题': (r) => r.body.includes('Collection of simple web-pages'),
    });
    
    if (!homeCheck) {
      errorRate.add(1);
    }
    
    customTrend.add(homeRes.timings.duration);
  });

  sleep(1);

  // 测试联系页面
  group('联系页面', function () {
    const contactRes = http.get(`${BASE_URL}/contacts.php`);
    
    check(contactRes, {
      '联系页面状态码是 200': (r) => r.status === 200,
      '联系页面响应时间 < 500ms': (r) => r.timings.duration < 500,
    }) || errorRate.add(1);
  });

  sleep(1);

  // 测试新闻页面
  group('新闻页面', function () {
    const newsRes = http.get(`${BASE_URL}/news.php`);
    
    check(newsRes, {
      '新闻页面状态码是 200': (r) => r.status === 200,
    }) || errorRate.add(1);
  });

  sleep(Math.random() * 2 + 1);  // 随机思考时间 1-3 秒
}

// 清理函数 - 在测试结束后执行一次
export function teardown(data) {
  console.log('负载测试完成！');
  console.log(`开始时间: ${data.startTime}`);
  console.log(`结束时间: ${new Date().toISOString()}`);
}
