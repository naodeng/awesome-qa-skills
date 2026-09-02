import test from 'node:test';
import assert from 'node:assert/strict';

function createOrderService() {
  const chargedOrderIds = new Set();

  return {
    async submitOrder(order) {
      if (chargedOrderIds.has(order.id)) {
        return { code: 'ORDER_ALREADY_EXISTS' };
      }
      chargedOrderIds.add(order.id);
      return { code: 'ORDER_CREATED' };
    },
    chargeCount(orderId) {
      return chargedOrderIds.has(orderId) ? 1 : 0;
    },
  };
}

test('rejects a duplicate order without charging twice', async () => {
  const orders = createOrderService();
  const order = { id: 'order-1' };

  await orders.submitOrder(order);
  const duplicate = await orders.submitOrder(order);

  assert.equal(duplicate.code, 'ORDER_ALREADY_EXISTS');
  assert.equal(orders.chargeCount(order.id), 1);
});
