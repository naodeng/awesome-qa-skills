/**
 * API 性能测试
 * 
 * 目的：测试 REST API 的性能表现
 * 场景：模拟真实的 API 调用场景
 */

import http from 'k6/http';
import { check, group, sleep } from 'k6';
import { Rate } from 'k6/metrics';

const errorRate = new Rate('api_errors');

export const options = {
  vus: 50,
  duration: '5m',
  
  thresholds: {
    'http_req_duration{api:users}': ['p(95)<300'],
    'http_req_duration{api:posts}': ['p(95)<400'],
    'http_req_duration{api:comments}': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
    'api_errors': ['rate<0.05'],
  },
};

const BASE_URL = 'https://jsonplaceholder.typicode.com';

export default function () {
  // 用户 API 测试
  group('用户 API', function () {
    // 获取用户列表
    const listRes = http.get(`${BASE_URL}/users`, {
      tags: { api: 'users', operation: 'list' },
    });
    
    check(listRes, {
      '获取用户列表成功': (r) => r.status === 200,
      '返回数据是数组': (r) => Array.isArray(r.json()),
      '用户列表不为空': (r) => r.json().length > 0,
    }) || errorRate.add(1);

    sleep(1);

    // 获取单个用户
    const userId = Math.floor(Math.random() * 10) + 1;
    const userRes = http.get(`${BASE_URL}/users/${userId}`, {
      tags: { api: 'users', operation: 'get' },
    });
    
    check(userRes, {
      '获取用户详情成功': (r) => r.status === 200,
      '用户有 ID': (r) => r.json('id') !== undefined,
      '用户有名称': (r) => r.json('name') !== undefined,
    }) || errorRate.add(1);

    sleep(1);
  });

  // 文章 API 测试
  group('文章 API', function () {
    // 获取文章列表
    const postsRes = http.get(`${BASE_URL}/posts`, {
      tags: { api: 'posts', operation: 'list' },
    });
    
    check(postsRes, {
      '获取文章列表成功': (r) => r.status === 200,
      '文章列表不为空': (r) => r.json().length > 0,
    }) || errorRate.add(1);

    sleep(1);

    // 创建文章
    const createRes = http.post(
      `${BASE_URL}/posts`,
      JSON.stringify({
        title: `Test Post ${Date.now()}`,
        body: 'This is a test post for performance testing',
        userId: 1,
      }),
      {
        headers: { 'Content-Type': 'application/json' },
        tags: { api: 'posts', operation: 'create' },
      }
    );
    
    check(createRes, {
      '创建文章成功': (r) => r.status === 201,
      '返回文章 ID': (r) => r.json('id') !== undefined,
    }) || errorRate.add(1);

    const postId = createRes.json('id');
    sleep(1);

    // 更新文章
    const updateRes = http.put(
      `${BASE_URL}/posts/${postId}`,
      JSON.stringify({
        id: postId,
        title: 'Updated Test Post',
        body: 'This post has been updated',
        userId: 1,
      }),
      {
        headers: { 'Content-Type': 'application/json' },
        tags: { api: 'posts', operation: 'update' },
      }
    );
    
    check(updateRes, {
      '更新文章成功': (r) => r.status === 200,
    }) || errorRate.add(1);

    sleep(1);

    // 删除文章
    const deleteRes = http.del(`${BASE_URL}/posts/${postId}`, {
      tags: { api: 'posts', operation: 'delete' },
    });
    
    check(deleteRes, {
      '删除文章成功': (r) => r.status === 200,
    }) || errorRate.add(1);

    sleep(1);
  });

  // 评论 API 测试
  group('评论 API', function () {
    const postId = Math.floor(Math.random() * 100) + 1;
    
    const commentsRes = http.get(`${BASE_URL}/posts/${postId}/comments`, {
      tags: { api: 'comments', operation: 'list' },
    });
    
    check(commentsRes, {
      '获取评论列表成功': (r) => r.status === 200,
      '评论是数组': (r) => Array.isArray(r.json()),
    }) || errorRate.add(1);

    sleep(1);
  });
}

export function handleSummary(data) {
  return {
    'reports/api-test-summary.json': JSON.stringify(data, null, 2),
  };
}
