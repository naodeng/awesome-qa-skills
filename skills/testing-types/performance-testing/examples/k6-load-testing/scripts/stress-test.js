/**
 * 压力测试 - Stress Test
 * 
 * 目的：找出系统的性能极限和瓶颈
 * 场景：逐步增加负载直到系统崩溃或性能严重下降
 */

import http from 'k6/http';
import { check, sleep } from 'k6';
import { Rate } from 'k6/metrics';

const errorRate = new Rate('errors');

export const options = {
  stages: [
    { duration: '2m', target: 50 },    // 预热
    { duration: '5m', target: 50 },    // 稳定在50
    { duration: '2m', target: 100 },   // 增加到100
    { duration: '5m', target: 100 },   
    { duration: '2m', target: 200 },   // 增加到200
    { duration: '5m', target: 200 },   
    { duration: '2m', target: 300 },   // 增加到300
    { duration: '5m', target: 300 },   
    { duration: '2m', target: 400 },   // 增加到400（极限）
    { duration: '5m', target: 400 },   
    { duration: '10m', target: 0 },    // 恢复
  ],
  
  thresholds: {
    'http_req_duration': ['p(99)<1500'],  // 99%请求<1500ms
    'http_req_failed': ['rate<0.05'],     // 错误率<5%
  },
};

const BASE_URL = __ENV.BASE_URL || 'https://test.k6.io';

export default function () {
  const res = http.get(`${BASE_URL}/`);
  
  check(res, {
    '状态码是 200': (r) => r.status === 200,
    '响应时间 < 1000ms': (r) => r.timings.duration < 1000,
  }) || errorRate.add(1);

  sleep(1);
}
