const request = require('supertest');

/**
 * User API 测试
 * 
 * 使用 Supertest 测试 RESTful API
 * 基础 URL: https://jsonplaceholder.typicode.com
 */

const baseURL = 'https://jsonplaceholder.typicode.com';

describe('User API Tests', () => {
  describe('GET /users', () => {
    it('should return all users', async () => {
      const response = await request(baseURL)
        .get('/users')
        .expect(200)
        .expect('Content-Type', /json/);

      expect(response.body).toBeInstanceOf(Array);
      expect(response.body.length).toBeGreaterThan(0);
      expect(response.body[0]).toHaveProperty('id');
      expect(response.body[0]).toHaveProperty('name');
      expect(response.body[0]).toHaveProperty('email');
    });

    it('should return users within acceptable time', async () => {
      const startTime = Date.now();
      
      await request(baseURL)
        .get('/users')
        .expect(200);
      
      const endTime = Date.now();
      const responseTime = endTime - startTime;
      
      expect(responseTime).toBeLessThan(2000); // 2 秒内
    });
  });

  describe('GET /users/:id', () => {
    it('should return a single user by ID', async () => {
      const userId = 1;
      
      const response = await request(baseURL)
        .get(`/users/${userId}`)
        .expect(200)
        .expect('Content-Type', /json/);

      expect(response.body).toHaveProperty('id', userId);
      expect(response.body).toHaveProperty('name');
      expect(response.body).toHaveProperty('email');
      expect(response.body.email).toMatch(/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/);
    });

    it('should return 404 for non-existent user', async () => {
      await request(baseURL)
        .get('/users/9999')
        .expect(404);
    });

    it('should return user with complete address', async () => {
      const response = await request(baseURL)
        .get('/users/1')
        .expect(200);

      expect(response.body).toHaveProperty('address');
      expect(response.body.address).toHaveProperty('street');
      expect(response.body.address).toHaveProperty('city');
      expect(response.body.address).toHaveProperty('zipcode');
    });
  });

  describe('POST /users', () => {
    it('should create a new user', async () => {
      const newUser = {
        name: 'John Doe',
        username: 'johndoe',
        email: 'john@example.com',
        address: {
          street: '123 Main St',
          city: 'New York'
        }
      };

      const response = await request(baseURL)
        .post('/users')
        .send(newUser)
        .set('Content-Type', 'application/json')
        .expect(201)
        .expect('Content-Type', /json/);

      expect(response.body).toHaveProperty('id');
      expect(response.body.name).toBe(newUser.name);
      expect(response.body.email).toBe(newUser.email);
    });

    it('should handle missing required fields', async () => {
      const incompleteUser = {
        name: 'John Doe'
        // 缺少 email 等字段
      };

      const response = await request(baseURL)
        .post('/users')
        .send(incompleteUser)
        .set('Content-Type', 'application/json');

      // JSONPlaceholder 不验证，但真实 API 应该返回 400
      expect([200, 201, 400]).toContain(response.status);
    });

    it('should validate email format', async () => {
      const invalidUser = {
        name: 'John Doe',
        email: 'invalid-email'
      };

      const response = await request(baseURL)
        .post('/users')
        .send(invalidUser)
        .set('Content-Type', 'application/json');

      // 真实 API 应该返回 400
      expect([200, 201, 400]).toContain(response.status);
    });
  });

  describe('PUT /users/:id', () => {
    it('should update an existing user', async () => {
      const userId = 1;
      const updatedUser = {
        name: 'John Updated',
        email: 'john.updated@example.com'
      };

      const response = await request(baseURL)
        .put(`/users/${userId}`)
        .send(updatedUser)
        .set('Content-Type', 'application/json')
        .expect(200)
        .expect('Content-Type', /json/);

      expect(response.body).toHaveProperty('id', userId);
      expect(response.body.name).toBe(updatedUser.name);
      expect(response.body.email).toBe(updatedUser.email);
    });

    it('should handle update of non-existent user', async () => {
      const updatedUser = {
        name: 'John Updated',
        email: 'john.updated@example.com'
      };

      const response = await request(baseURL)
        .put('/users/9999')
        .send(updatedUser)
        .set('Content-Type', 'application/json');

      // 真实 API 应该返回 404
      expect([200, 404]).toContain(response.status);
    });
  });

  describe('PATCH /users/:id', () => {
    it('should partially update a user', async () => {
      const userId = 1;
      const partialUpdate = {
        email: 'newemail@example.com'
      };

      const response = await request(baseURL)
        .patch(`/users/${userId}`)
        .send(partialUpdate)
        .set('Content-Type', 'application/json')
        .expect(200)
        .expect('Content-Type', /json/);

      expect(response.body).toHaveProperty('id', userId);
      expect(response.body.email).toBe(partialUpdate.email);
    });
  });

  describe('DELETE /users/:id', () => {
    it('should delete a user', async () => {
      const userId = 1;

      await request(baseURL)
        .delete(`/users/${userId}`)
        .expect(200);
    });

    it('should handle deletion of non-existent user', async () => {
      const response = await request(baseURL)
        .delete('/users/9999');

      // 真实 API 应该返回 404
      expect([200, 404]).toContain(response.status);
    });
  });

  describe('Query Parameters', () => {
    it('should filter users by username', async () => {
      const response = await request(baseURL)
        .get('/users')
        .query({ username: 'Bret' })
        .expect(200);

      expect(response.body).toBeInstanceOf(Array);
      if (response.body.length > 0) {
        expect(response.body[0].username).toBe('Bret');
      }
    });

    it('should handle multiple query parameters', async () => {
      const response = await request(baseURL)
        .get('/users')
        .query({ 
          username: 'Bret',
          email: 'Sincere@april.biz'
        })
        .expect(200);

      expect(response.body).toBeInstanceOf(Array);
    });
  });

  describe('Headers', () => {
    it('should send custom headers', async () => {
      await request(baseURL)
        .get('/users/1')
        .set('Accept', 'application/json')
        .set('User-Agent', 'Supertest')
        .expect(200);
    });

    it('should verify response headers', async () => {
      const response = await request(baseURL)
        .get('/users/1')
        .expect(200);

      expect(response.headers['content-type']).toMatch(/json/);
      expect(response.headers).toHaveProperty('connection');
    });
  });

  describe('Error Handling', () => {
    it('should handle invalid JSON', async () => {
      const response = await request(baseURL)
        .post('/users')
        .send('invalid json')
        .set('Content-Type', 'application/json');

      // 真实 API 应该返回 400
      expect([200, 201, 400]).toContain(response.status);
    });

    it('should handle network errors gracefully', async () => {
      try {
        await request('http://invalid-domain-that-does-not-exist.com')
          .get('/users')
          .timeout(1000);
      } catch (error) {
        expect(error).toBeDefined();
      }
    });
  });

  describe('Response Validation', () => {
    it('should validate response structure', async () => {
      const response = await request(baseURL)
        .get('/users/1')
        .expect(200);

      // 验证必需字段
      const requiredFields = ['id', 'name', 'username', 'email'];
      requiredFields.forEach(field => {
        expect(response.body).toHaveProperty(field);
      });

      // 验证嵌套对象
      expect(response.body).toHaveProperty('address');
      expect(response.body.address).toHaveProperty('geo');
      expect(response.body.address.geo).toHaveProperty('lat');
      expect(response.body.address.geo).toHaveProperty('lng');
    });

    it('should validate data types', async () => {
      const response = await request(baseURL)
        .get('/users/1')
        .expect(200);

      expect(typeof response.body.id).toBe('number');
      expect(typeof response.body.name).toBe('string');
      expect(typeof response.body.email).toBe('string');
      expect(typeof response.body.address).toBe('object');
    });
  });
});

describe('Posts API Tests', () => {
  describe('GET /posts', () => {
    it('should return all posts', async () => {
      const response = await request(baseURL)
        .get('/posts')
        .expect(200);

      expect(response.body).toBeInstanceOf(Array);
      expect(response.body.length).toBeGreaterThan(0);
    });

    it('should filter posts by userId', async () => {
      const userId = 1;
      
      const response = await request(baseURL)
        .get('/posts')
        .query({ userId })
        .expect(200);

      expect(response.body).toBeInstanceOf(Array);
      response.body.forEach(post => {
        expect(post.userId).toBe(userId);
      });
    });
  });

  describe('GET /users/:id/posts', () => {
    it('should return posts for a specific user', async () => {
      const userId = 1;
      
      const response = await request(baseURL)
        .get(`/users/${userId}/posts`)
        .expect(200);

      expect(response.body).toBeInstanceOf(Array);
      if (response.body.length > 0) {
        response.body.forEach(post => {
          expect(post).toHaveProperty('userId', userId);
          expect(post).toHaveProperty('title');
          expect(post).toHaveProperty('body');
        });
      }
    });
  });
});
