import test from 'node:test';
import assert from 'node:assert/strict';

function createSpy(result) {
  const calls = [];
  return Object.assign(async (...args) => {
    calls.push(args);
    return result;
  }, { calls });
}

test('这个测试会通过，但没有验证真实下单逻辑', async () => {
  const create = createSpy({ id: 'order-1' });
  const orderService = { create };

  await orderService.create({ sku: 'book' });

  assert.equal(create.calls.length, 1);
});
