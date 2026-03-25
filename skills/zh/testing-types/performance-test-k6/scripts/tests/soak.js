import { assertOk, get, think } from '../helpers.js';
import { tags, thresholds } from '../config.js';

export const options = {
  scenarios: {
    soak_test: {
      executor: 'constant-vus',
      vus: 60,
      duration: '30m',
      tags: tags('soak', 'homepage'),
    },
  },
  thresholds: {
    ...thresholds,
    http_req_failed: ['rate<0.02'],
    http_req_duration: ['p(95)<900', 'p(99)<1800'],
  },
};

export default function () {
  const res = get('/');
  assertOk(res);
  think(0.5, 1.2);
}
