const request = require('supertest');
const app = require(process.env.SUPERTEST_APP || '../app');

describe('Generated API Tests', () => {
test('api_get_v1_users_page_1_1', async () => {
  const res = await request(app).get('/v1/users?page=1');
  expect([200, 201, 202, 204, 400, 401, 403, 404]).toContain(res.status);
});
test('api_post_v1_login_2', async () => {
  const res = await request(app).post('/v1/login').send({});
  expect([200, 201, 202, 204, 400, 401, 403, 404]).toContain(res.status);
});
test('api_get_v1_users_3', async () => {
  const res = await request(app).get('/v1/users');
  expect([200, 201, 202, 204, 400, 401, 403, 404]).toContain(res.status);
});
test('api_post_v1_users_4', async () => {
  const res = await request(app).post('/v1/users').send({});
  expect([200, 201, 202, 204, 400, 401, 403, 404]).toContain(res.status);
});
test('api_post_soap_getuser_5', async () => {
  const res = await request(app).post('/soap/GetUser').send({});
  expect([200, 201, 202, 204, 400, 401, 403, 404]).toContain(res.status);
});
test('api_post_soap_createuser_6', async () => {
  const res = await request(app).post('/soap/CreateUser').send({});
  expect([200, 201, 202, 204, 400, 401, 403, 404]).toContain(res.status);
});
test('api_get_v1_orders_7', async () => {
  const res = await request(app).get('/v1/orders');
  expect([200, 201, 202, 204, 400, 401, 403, 404]).toContain(res.status);
});
test('api_post_v1_orders_8', async () => {
  const res = await request(app).post('/v1/orders').send({});
  expect([200, 201, 202, 204, 400, 401, 403, 404]).toContain(res.status);
});
test('api_get_v1_products_9', async () => {
  const res = await request(app).get('/v1/products');
  expect([200, 201, 202, 204, 400, 401, 403, 404]).toContain(res.status);
});
test('api_post_v1_products_10', async () => {
  const res = await request(app).post('/v1/products').send({});
  expect([200, 201, 202, 204, 400, 401, 403, 404]).toContain(res.status);
});
test('api_get_v1_users_11', async () => {
  const res = await request(app).get('/v1/users');
  expect([200, 201, 202, 204, 400, 401, 403, 404]).toContain(res.status);
});
});
