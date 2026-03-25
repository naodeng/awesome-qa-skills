/**
 * Cypress 高级 API Mocking 示例
 * 
 * 功能：
 * - 拦截和模拟 API 请求
 * - 动态响应
 * - 延迟和错误模拟
 * - 请求验证
 */

describe('高级 API Mocking', () => {
  beforeEach(() => {
    cy.visit('https://example.cypress.io/commands/network-requests')
  })

  it('应该拦截并模拟 GET 请求', () => {
    // 拦截 GET 请求并返回模拟数据
    cy.intercept('GET', '/users', {
      statusCode: 200,
      body: [
        { id: 1, name: 'John Doe', email: 'john@example.com' },
        { id: 2, name: 'Jane Smith', email: 'jane@example.com' }
      ]
    }).as('getUsers')

    // 触发请求
    cy.get('.network-btn').click()

    // 等待请求完成
    cy.wait('@getUsers').then((interception) => {
      expect(interception.response.statusCode).to.equal(200)
      expect(interception.response.body).to.have.length(2)
    })
  })

  it('应该拦截并模拟 POST 请求', () => {
    // 拦截 POST 请求
    cy.intercept('POST', '/users', {
      statusCode: 201,
      body: {
        id: 3,
        name: 'New User',
        email: 'newuser@example.com',
        createdAt: new Date().toISOString()
      }
    }).as('createUser')

    // 模拟表单提交
    cy.get('.network-post').click()

    // 验证请求
    cy.wait('@createUser').then((interception) => {
      expect(interception.response.statusCode).to.equal(201)
      expect(interception.response.body).to.have.property('id')
    })
  })

  it('应该模拟 API 延迟', () => {
    // 模拟慢速网络
    cy.intercept('GET', '/users', (req) => {
      req.reply({
        statusCode: 200,
        body: [{ id: 1, name: 'John Doe' }],
        delay: 2000 // 延迟 2 秒
      })
    }).as('slowRequest')

    cy.get('.network-btn').click()

    // 验证加载状态
    cy.get('.loading-spinner').should('be.visible')

    cy.wait('@slowRequest')

    // 验证加载完成
    cy.get('.loading-spinner').should('not.exist')
  })

  it('应该模拟 API 错误', () => {
    // 模拟 500 错误
    cy.intercept('GET', '/users', {
      statusCode: 500,
      body: {
        error: 'Internal Server Error',
        message: 'Something went wrong'
      }
    }).as('serverError')

    cy.get('.network-btn').click()

    cy.wait('@serverError')

    // 验证错误消息显示
    cy.get('.error-message')
      .should('be.visible')
      .and('contain', 'Something went wrong')
  })

  it('应该模拟网络超时', () => {
    // 模拟请求超时
    cy.intercept('GET', '/users', (req) => {
      req.reply({
        forceNetworkError: true
      })
    }).as('networkError')

    cy.get('.network-btn').click()

    cy.wait('@networkError')

    // 验证超时错误处理
    cy.get('.error-message')
      .should('be.visible')
      .and('contain', 'Network Error')
  })

  it('应该验证请求参数', () => {
    cy.intercept('GET', '/users*', (req) => {
      // 验证查询参数
      expect(req.query).to.have.property('page')
      expect(req.query).to.have.property('limit')

      req.reply({
        statusCode: 200,
        body: {
          data: [],
          page: parseInt(req.query.page),
          limit: parseInt(req.query.limit)
        }
      })
    }).as('getUsersWithParams')

    // 触发带参数的请求
    cy.get('.network-btn').click()

    cy.wait('@getUsersWithParams').then((interception) => {
      expect(interception.request.query.page).to.exist
      expect(interception.request.query.limit).to.exist
    })
  })

  it('应该验证请求头', () => {
    cy.intercept('GET', '/users', (req) => {
      // 验证请求头
      expect(req.headers).to.have.property('authorization')
      expect(req.headers['content-type']).to.include('application/json')

      req.reply({
        statusCode: 200,
        body: []
      })
    }).as('authenticatedRequest')

    cy.get('.network-btn').click()

    cy.wait('@authenticatedRequest')
  })

  it('应该修改请求数据', () => {
    cy.intercept('POST', '/users', (req) => {
      // 修改请求体
      req.body.timestamp = new Date().toISOString()
      req.body.source = 'cypress-test'

      req.reply({
        statusCode: 201,
        body: req.body
      })
    }).as('modifiedRequest')

    cy.get('.network-post').click()

    cy.wait('@modifiedRequest').then((interception) => {
      expect(interception.request.body).to.have.property('timestamp')
      expect(interception.request.body).to.have.property('source')
    })
  })

  it('应该模拟分页响应', () => {
    let page = 1

    cy.intercept('GET', '/users*', (req) => {
      const currentPage = parseInt(req.query.page) || 1
      const limit = parseInt(req.query.limit) || 10

      req.reply({
        statusCode: 200,
        body: {
          data: Array.from({ length: limit }, (_, i) => ({
            id: (currentPage - 1) * limit + i + 1,
            name: `User ${(currentPage - 1) * limit + i + 1}`
          })),
          pagination: {
            page: currentPage,
            limit: limit,
            total: 100,
            hasNext: currentPage * limit < 100
          }
        }
      })
    }).as('paginatedRequest')

    // 第一页
    cy.get('.network-btn').click()
    cy.wait('@paginatedRequest')

    // 第二页
    cy.get('.next-page-btn').click()
    cy.wait('@paginatedRequest')
  })

  it('应该模拟条件响应', () => {
    cy.intercept('GET', '/users/*', (req) => {
      const userId = req.url.split('/').pop()

      if (userId === '1') {
        req.reply({
          statusCode: 200,
          body: { id: 1, name: 'Admin User', role: 'admin' }
        })
      } else if (userId === '999') {
        req.reply({
          statusCode: 404,
          body: { error: 'User not found' }
        })
      } else {
        req.reply({
          statusCode: 200,
          body: { id: userId, name: 'Regular User', role: 'user' }
        })
      }
    }).as('conditionalResponse')

    // 测试不同的用户ID
    cy.visit('/user/1')
    cy.wait('@conditionalResponse')
    cy.contains('Admin User')

    cy.visit('/user/999')
    cy.wait('@conditionalResponse')
    cy.contains('User not found')
  })

  it('应该模拟文件上传', () => {
    cy.intercept('POST', '/upload', (req) => {
      // 验证文件上传
      expect(req.headers['content-type']).to.include('multipart/form-data')

      req.reply({
        statusCode: 200,
        body: {
          success: true,
          fileId: 'file-123',
          url: 'https://example.com/files/file-123'
        }
      })
    }).as('fileUpload')

    // 模拟文件上传
    cy.get('input[type="file"]').selectFile('cypress/fixtures/example.json')
    cy.get('.upload-btn').click()

    cy.wait('@fileUpload').then((interception) => {
      expect(interception.response.body.success).to.be.true
    })
  })

  it('应该模拟 WebSocket 连接', () => {
    // 注意：Cypress 对 WebSocket 的支持有限
    // 可以拦截初始的 HTTP 升级请求
    cy.intercept('GET', '/ws', {
      statusCode: 101,
      headers: {
        'Upgrade': 'websocket',
        'Connection': 'Upgrade'
      }
    }).as('wsUpgrade')

    cy.visit('/chat')
    cy.wait('@wsUpgrade')
  })

  it('应该模拟多个并发请求', () => {
    // 拦截多个不同的 API
    cy.intercept('GET', '/users', { fixture: 'users.json' }).as('getUsers')
    cy.intercept('GET', '/posts', { fixture: 'posts.json' }).as('getPosts')
    cy.intercept('GET', '/comments', { fixture: 'comments.json' }).as('getComments')

    cy.visit('/dashboard')

    // 等待所有请求完成
    cy.wait(['@getUsers', '@getPosts', '@getComments'])

    // 验证所有数据都已加载
    cy.get('.users-list').should('be.visible')
    cy.get('.posts-list').should('be.visible')
    cy.get('.comments-list').should('be.visible')
  })

  it('应该使用 fixture 文件', () => {
    // 使用 fixture 文件作为响应
    cy.intercept('GET', '/users', { fixture: 'users.json' }).as('getUsers')

    cy.get('.network-btn').click()

    cy.wait('@getUsers').then((interception) => {
      expect(interception.response.body).to.be.an('array')
    })
  })

  it('应该动态生成响应数据', () => {
    cy.intercept('GET', '/users', (req) => {
      // 动态生成数据
      const users = Array.from({ length: 10 }, (_, i) => ({
        id: i + 1,
        name: `User ${i + 1}`,
        email: `user${i + 1}@example.com`,
        createdAt: new Date(Date.now() - i * 86400000).toISOString()
      }))

      req.reply({
        statusCode: 200,
        body: users
      })
    }).as('dynamicUsers')

    cy.get('.network-btn').click()

    cy.wait('@dynamicUsers').then((interception) => {
      expect(interception.response.body).to.have.length(10)
    })
  })

  it('应该测试重试逻辑', () => {
    let attemptCount = 0

    cy.intercept('GET', '/users', (req) => {
      attemptCount++

      if (attemptCount < 3) {
        // 前两次请求失败
        req.reply({
          statusCode: 500,
          body: { error: 'Server Error' }
        })
      } else {
        // 第三次请求成功
        req.reply({
          statusCode: 200,
          body: [{ id: 1, name: 'John Doe' }]
        })
      }
    }).as('retryRequest')

    cy.get('.network-btn').click()

    // 等待多次请求
    cy.wait('@retryRequest')
    cy.wait('@retryRequest')
    cy.wait('@retryRequest')

    // 验证最终成功
    cy.get('.success-message').should('be.visible')
  })

  it('应该模拟 GraphQL 请求', () => {
    cy.intercept('POST', '/graphql', (req) => {
      // 检查 GraphQL 查询
      if (req.body.query.includes('getUser')) {
        req.reply({
          statusCode: 200,
          body: {
            data: {
              user: {
                id: '1',
                name: 'John Doe',
                email: 'john@example.com'
              }
            }
          }
        })
      } else if (req.body.query.includes('getPosts')) {
        req.reply({
          statusCode: 200,
          body: {
            data: {
              posts: [
                { id: '1', title: 'Post 1', content: 'Content 1' },
                { id: '2', title: 'Post 2', content: 'Content 2' }
              ]
            }
          }
        })
      }
    }).as('graphqlRequest')

    cy.visit('/graphql-page')
    cy.wait('@graphqlRequest')
  })
})

describe('API Mocking 最佳实践', () => {
  it('应该使用别名管理多个拦截', () => {
    cy.intercept('GET', '/users', { fixture: 'users.json' }).as('getUsers')
    cy.intercept('POST', '/users', { statusCode: 201 }).as('createUser')
    cy.intercept('PUT', '/users/*', { statusCode: 200 }).as('updateUser')
    cy.intercept('DELETE', '/users/*', { statusCode: 204 }).as('deleteUser')

    // 使用别名等待特定请求
    cy.get('.create-btn').click()
    cy.wait('@createUser')

    cy.get('.update-btn').click()
    cy.wait('@updateUser')
  })

  it('应该清理拦截器', () => {
    // 设置拦截器
    cy.intercept('GET', '/users', { fixture: 'users.json' }).as('getUsers')

    cy.visit('/users')
    cy.wait('@getUsers')

    // 在某些情况下，可能需要移除拦截器
    // Cypress 会在每个测试后自动清理
  })

  it('应该使用环境变量控制 mocking', () => {
    const useMock = Cypress.env('USE_MOCK_API') !== false

    if (useMock) {
      cy.intercept('GET', '/users', { fixture: 'users.json' }).as('getUsers')
    }

    cy.visit('/users')

    if (useMock) {
      cy.wait('@getUsers')
    }
  })
})
