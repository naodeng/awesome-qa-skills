import { assertOk, get, think } from '../helpers.js';
import { tags, thresholds } from '../config.js';

export const options = {
  scenarios: {
    load_test: {
      executor: 'ramping-vus',
      startVUs: 5,
      stages: [
        { duration: '2m', target: 30 },
        { duration: '5m', target: 80 },
        { duration: '2m', target: 0 },
      ],
      gracefulRampDown: '30s',
      tags: tags('load', 'homepage'),
    },
  },
  thresholds,
};

export default function () {
  const res = get('/');
  assertOk(res, {
    'body has html': (r) => String(r.body || '').includes('<html'),
  });
  think();
}
