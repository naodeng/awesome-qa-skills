import { assertOk, get, think } from '../helpers.js';
import { tags, thresholds } from '../config.js';

export const options = {
  scenarios: {
    spike_test: {
      executor: 'ramping-vus',
      startVUs: 10,
      stages: [
        { duration: '1m', target: 20 },
        { duration: '30s', target: 250 },
        { duration: '2m', target: 250 },
        { duration: '30s', target: 20 },
        { duration: '2m', target: 20 },
      ],
      gracefulRampDown: '10s',
      tags: tags('spike', 'homepage'),
    },
  },
  thresholds: {
    ...thresholds,
    http_req_failed: ['rate<0.05'],
  },
};

export default function () {
  const res = get('/');
  assertOk(res);
  think(0.1, 0.3);
}
