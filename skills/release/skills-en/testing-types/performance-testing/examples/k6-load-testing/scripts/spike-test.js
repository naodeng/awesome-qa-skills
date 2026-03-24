/**
 * 尖峰测试 - Spike Test
 * 
 * 目的：测试系统应对突发流量的能力
 * 场景：短时间内流量急剧增加
 */

import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '1m', target: 50 },    // 正常负载
    { duration: '30s', target: 500 },  // 突然增加到500（尖峰）
    { duration: '1m', target: 500 },   // 保持尖峰
    { duration: '30s', target: 50 },   // 快速降回正常
    { duration: '2m', target: 50 },    // 恢复
    { duration: '1m', target: 0 },     // 结束
  ],
  
  thresholds: {
    'http_req_duration': ['p(95)<1000'],
    'http_req_failed': ['rate<0.1'],  // 尖峰时允许10%错误率
  },
};

const BASE_URL = __ENV.BASE_URL || 'https://test.k6.io';

export default function () {
  const res = http.get(`${BASE_URL}/`);
  
  check(res, {
    '状态码是 200 或 503': (r) => r.status === 200 || r.status === 503,
  });

  sleep(0.5);  // 尖峰测试思考时间较短
}
