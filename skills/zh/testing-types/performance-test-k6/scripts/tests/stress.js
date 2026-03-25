import { assertOk, get, think } from '../helpers.js';
import { tags, thresholds } from '../config.js';

export const options = {
  scenarios: {
    stress_test: {
      executor: 'ramping-vus',
      startVUs: 10,
      stages: [
        { duration: '2m', target: 100 },
        { duration: '3m', target: 200 },
        { duration: '3m', target: 300 },
        { duration: '2m', target: 0 },
      ],
      gracefulRampDown: '20s',
      tags: tags('stress', 'homepage'),
    },
  },
  thresholds: {
    ...thresholds,
    http_req_failed: ['rate<0.03'],
  },
};

export default function () {
  const res = get('/');
  assertOk(res);
  think(0.2, 0.8);
}
