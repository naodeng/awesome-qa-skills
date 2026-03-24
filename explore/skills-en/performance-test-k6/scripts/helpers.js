import http from 'k6/http';
import { check, sleep } from 'k6';
import { common } from './config.js';

export function get(path, tags = {}) {
  const res = http.get(`${common.baseURL}${path}`, {
    headers: common.defaultHeaders,
    tags,
  });
  return res;
}

export function post(path, body, tags = {}) {
  const res = http.post(`${common.baseURL}${path}`, JSON.stringify(body), {
    headers: common.defaultHeaders,
    tags,
  });
  return res;
}

export function assertOk(res, extraChecks = {}) {
  check(
    res,
    {
      'status is 200/201/204': (r) => [200, 201, 204].includes(r.status),
      ...extraChecks,
    }
  );
}

export function think(minSec = 0.5, maxSec = 1.5) {
  const span = Math.max(maxSec - minSec, 0);
  sleep(minSec + Math.random() * span);
}
