import { assertOk, get, post, think } from '../helpers.js';
import { samplePayloads, tags, thresholds } from '../config.js';

export const options = {
  scenarios: {
    api_smoke: {
      executor: 'per-vu-iterations',
      vus: 10,
      iterations: 20,
      maxDuration: '3m',
      tags: tags('smoke', 'api'),
    },
  },
  thresholds,
};

export default function () {
  const probe = get('/');
  assertOk(probe);

  const payload = samplePayloads[Math.floor(Math.random() * samplePayloads.length)];
  const res = post('/api/login/', payload);
  assertOk(res, {
    'api response under 1s': (r) => r.timings.duration < 1000,
  });

  think(0.2, 0.6);
}
