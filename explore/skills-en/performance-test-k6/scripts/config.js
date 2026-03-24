import { SharedArray } from 'k6/data';

const target = __ENV.BASE_URL || 'https://test.k6.io';
const envName = __ENV.ENV || 'staging';

export const common = {
  baseURL: target,
  env: envName,
  defaultHeaders: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
  },
};

export const thresholds = {
  http_req_failed: ['rate<0.01'],
  http_req_duration: ['p(95)<800', 'p(99)<1500'],
};

export const samplePayloads = new SharedArray('sample-payloads', () => [
  { skuId: 'SKU-1001', userTier: 'PLUS' },
  { skuId: 'SKU-1002', userTier: 'NORMAL' },
  { skuId: 'SKU-1003', userTier: 'PLUS' },
]);

export function tags(testType, module) {
  return {
    test_type: testType,
    module,
    env: common.env,
  };
}
