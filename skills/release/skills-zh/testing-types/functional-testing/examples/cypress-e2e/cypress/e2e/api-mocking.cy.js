/**
 * API Mocking 测试示例
 * 
 * 演示如何使用 Cypress 拦截和模拟 API 请求
 */

describe('API Mocking 测试', () => {
  beforeEach(() => {
    cy.visit('/users')
  })

  it('应该成功加载用户列表', () => {
    // 拦截 API 请求并返回模拟数据
    cy.intercept('GET', '/api/users', {
      statusCode: 200,
      body: [
        { id: 1, name: 'John Doe', email: 'john@example.com' },
        { id: 2, name: 'Jane Smith', email: 'jane@example.com' },
        { id: 3, name: 'Bob Johnson', email: 'bob@example.com' }
      ]
    }).as('getUsers')
    
    // 等待 API 请求完成
    cy.wait('@getUsers')
    
    // 验证用户列表显示
    cy.get('[data-cy=user-list]').children().should('have.length', 3)
    cy.get('[data-cy=user-item]').first().should('contain', 'John Doe')
  })

  it('应该处理 API 错误', () => {
    // 模拟 API 错误
    cy.intercept('GET', '/api/users', {
      statusCode: 500,
      body: {
        error: 'Internal Server Error'
      }
    }).as('getUsersError')
    
    cy.wait('@getUsersError')
    
    // 验证错误信息显示
    cy.get('[data-cy=error-message]')
      .should('be.visible')
      .and('contain', 'Failed to load users')
  })

  it('应该处理网络超时', () => {
    // 模拟网络延迟
    cy.intercept('GET', '/api/users', (req) => {
      req.reply({
        delay: 5000, // 5秒延迟
        statusCode: 200,
        body: []
      })
    }).as('getUsersTimeout')
    
    // 验证加载指示器显示
    cy.get('[data-cy=loading-spinner]').should('be.visible')
    
    // 等待超时
    cy.wait('@getUsersTimeout', { timeout: 10000 })
    
    // 验证超时错误
    cy.get('[data-cy=timeout-message]')
      .should('contain', 'Request timeout')
  })

  it('应该成功创建新用户', () => {
    // 拦截 POST 请求
    cy.intercept('POST', '/api/users', {
      statusCode: 201,
      body: {
        id: 4,
        name: 'New User',
        email: 'newuser@example.com'
      }
    }).as('createUser')
    
    // 填写表单
    cy.get('[data-cy=name-input]').type('New User')
    cy.get('[data-cy=email-input]').type('newuser@example.com')
    cy.get('[data-cy=submit-button]').click()
    
    // 等待请求完成
    cy.wait('@createUser').its('request.body').should('deep.equal', {
      name: 'New User',
      email: 'newuser@example.com'
    })
    
    // 验证成功消息
    cy.get('[data-cy=success-message]')
      .should('contain', 'User created successfully')
  })

  it('应该处理验证错误', () => {
    // 模拟验证错误
    cy.intercept('POST', '/api/users', {
      statusCode: 400,
      body: {
        errors: {
          email: 'Email already exists'
        }
      }
    }).as('createUserError')
    
    cy.get('[data-cy=name-input]').type('Test User')
    cy.get('[data-cy=email-input]').type('existing@example.com')
    cy.get('[data-cy=submit-button]').click()
    
    cy.wait('@createUserError')
    
    // 验证错误消息
    cy.get('[data-cy=email-error]')
      .should('contain', 'Email already exists')
  })

  it('应该能够更新用户信息', () => {
    // 先加载用户列表
    cy.intercept('GET', '/api/users', {
      body: [
        { id: 1, name: 'John Doe', email: 'john@example.com' }
      ]
    }).as('getUsers')
    
    cy.wait('@getUsers')
    
    // 拦截 PUT 请求
    cy.intercept('PUT', '/api/users/1', {
      statusCode: 200,
      body: {
        id: 1,
        name: 'John Updated',
        email: 'john.updated@example.com'
      }
    }).as('updateUser')
    
    // 点击编辑按钮
    cy.get('[data-cy=edit-button]').first().click()
    
    // 修改信息
    cy.get('[data-cy=name-input]').clear().type('John Updated')
    cy.get('[data-cy=email-input]').clear().type('john.updated@example.com')
    cy.get('[data-cy=save-button]').click()
    
    cy.wait('@updateUser')
    
    // 验证更新成功
    cy.get('[data-cy=success-message]')
      .should('contain', 'User updated successfully')
  })

  it('应该能够删除用户', () => {
    // 先加载用户列表
    cy.intercept('GET', '/api/users', {
      body: [
        { id: 1, name: 'John Doe', email: 'john@example.com' }
      ]
    }).as('getUsers')
    
    cy.wait('@getUsers')
    
    // 拦截 DELETE 请求
    cy.intercept('DELETE', '/api/users/1', {
      statusCode: 204
    }).as('deleteUser')
    
    // 点击删除按钮
    cy.get('[data-cy=delete-button]').first().click()
    
    // 确认删除
    cy.get('[data-cy=confirm-delete]').click()
    
    cy.wait('@deleteUser')
    
    // 验证删除成功
    cy.get('[data-cy=success-message]')
      .should('contain', 'User deleted successfully')
  })

  it('应该能够搜索用户', () => {
    // 拦截搜索请求
    cy.intercept('GET', '/api/users?search=john', {
      statusCode: 200,
      body: [
        { id: 1, name: 'John Doe', email: 'john@example.com' }
      ]
    }).as('searchUsers')
    
    // 输入搜索关键词
    cy.get('[data-cy=search-input]').type('john')
    cy.get('[data-cy=search-button]').click()
    
    cy.wait('@searchUsers')
    
    // 验证搜索结果
    cy.get('[data-cy=user-list]').children().should('have.length', 1)
    cy.get('[data-cy=user-item]').should('contain', 'John Doe')
  })

  it('应该能够分页加载用户', () => {
    // 第一页
    cy.intercept('GET', '/api/users?page=1', {
      body: {
        data: [
          { id: 1, name: 'User 1', email: 'user1@example.com' },
          { id: 2, name: 'User 2', email: 'user2@example.com' }
        ],
        pagination: {
          currentPage: 1,
          totalPages: 3,
          totalItems: 6
        }
      }
    }).as('getPage1')
    
    cy.wait('@getPage1')
    
    // 第二页
    cy.intercept('GET', '/api/users?page=2', {
      body: {
        data: [
          { id: 3, name: 'User 3', email: 'user3@example.com' },
          { id: 4, name: 'User 4', email: 'user4@example.com' }
        ],
        pagination: {
          currentPage: 2,
          totalPages: 3,
          totalItems: 6
        }
      }
    }).as('getPage2')
    
    // 点击下一页
    cy.get('[data-cy=next-page]').click()
    cy.wait('@getPage2')
    
    // 验证第二页数据
    cy.get('[data-cy=user-list]').should('contain', 'User 3')
    cy.get('[data-cy=current-page]').should('contain', '2')
  })
})

describe('API 请求验证', () => {
  it('应该发送正确的请求头', () => {
    cy.intercept('GET', '/api/users', (req) => {
      // 验证请求头
      expect(req.headers).to.have.property('authorization')
      expect(req.headers['content-type']).to.include('application/json')
      
      req.reply({
        statusCode: 200,
        body: []
      })
    }).as('getUsers')
    
    cy.wait('@getUsers')
  })

  it('应该发送正确的请求体', () => {
    cy.intercept('POST', '/api/users', (req) => {
      // 验证请求体
      expect(req.body).to.have.property('name')
      expect(req.body).to.have.property('email')
      expect(req.body.email).to.match(/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/)
      
      req.reply({
        statusCode: 201,
        body: req.body
      })
    }).as('createUser')
    
    cy.get('[data-cy=name-input]').type('Test User')
    cy.get('[data-cy=email-input]').type('test@example.com')
    cy.get('[data-cy=submit-button]').click()
    
    cy.wait('@createUser')
  })
})
