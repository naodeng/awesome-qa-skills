/**
 * 登录功能测试
 * 
 * 测试场景：
 * 1. 成功登录
 * 2. 登录失败 - 错误的用户名
 * 3. 登录失败 - 错误的密码
 * 4. 登录失败 - 空字段
 * 5. 记住我功能
 */

describe('登录功能测试', () => {
  beforeEach(() => {
    // 访问登录页面
    cy.visit('/login')
    
    // 清除 cookies 和 localStorage
    cy.clearCookies()
    cy.clearLocalStorage()
  })

  it('应该成功登录有效用户', () => {
    // 输入用户名和密码
    cy.get('[data-cy=username]').type('testuser')
    cy.get('[data-cy=password]').type('password123')
    
    // 点击登录按钮
    cy.get('[data-cy=login-button]').click()
    
    // 验证登录成功
    cy.url().should('include', '/dashboard')
    cy.get('[data-cy=welcome-message]').should('contain', 'Welcome, testuser')
    
    // 验证 token 已保存
    cy.window().its('localStorage.token').should('exist')
  })

  it('应该显示错误信息 - 无效的用户名', () => {
    cy.get('[data-cy=username]').type('invaliduser')
    cy.get('[data-cy=password]').type('password123')
    cy.get('[data-cy=login-button]').click()
    
    // 验证错误信息
    cy.get('[data-cy=error-message]')
      .should('be.visible')
      .and('contain', 'Invalid username or password')
    
    // 验证仍在登录页面
    cy.url().should('include', '/login')
  })

  it('应该显示错误信息 - 无效的密码', () => {
    cy.get('[data-cy=username]').type('testuser')
    cy.get('[data-cy=password]').type('wrongpassword')
    cy.get('[data-cy=login-button]').click()
    
    cy.get('[data-cy=error-message]')
      .should('be.visible')
      .and('contain', 'Invalid username or password')
  })

  it('应该显示验证错误 - 空用户名', () => {
    cy.get('[data-cy=password]').type('password123')
    cy.get('[data-cy=login-button]').click()
    
    cy.get('[data-cy=username]')
      .should('have.attr', 'aria-invalid', 'true')
    
    cy.get('[data-cy=username-error]')
      .should('contain', 'Username is required')
  })

  it('应该显示验证错误 - 空密码', () => {
    cy.get('[data-cy=username]').type('testuser')
    cy.get('[data-cy=login-button]').click()
    
    cy.get('[data-cy=password]')
      .should('have.attr', 'aria-invalid', 'true')
    
    cy.get('[data-cy=password-error]')
      .should('contain', 'Password is required')
  })

  it('应该正确处理"记住我"功能', () => {
    cy.get('[data-cy=username]').type('testuser')
    cy.get('[data-cy=password]').type('password123')
    cy.get('[data-cy=remember-me]').check()
    cy.get('[data-cy=login-button]').click()
    
    // 验证登录成功
    cy.url().should('include', '/dashboard')
    
    // 验证 cookie 已设置
    cy.getCookie('remember_token').should('exist')
  })

  it('应该能够切换密码可见性', () => {
    cy.get('[data-cy=password]').type('password123')
    
    // 默认密码应该被隐藏
    cy.get('[data-cy=password]').should('have.attr', 'type', 'password')
    
    // 点击显示密码按钮
    cy.get('[data-cy=toggle-password]').click()
    cy.get('[data-cy=password]').should('have.attr', 'type', 'text')
    
    // 再次点击隐藏密码
    cy.get('[data-cy=toggle-password]').click()
    cy.get('[data-cy=password]').should('have.attr', 'type', 'password')
  })

  it('应该能够导航到忘记密码页面', () => {
    cy.get('[data-cy=forgot-password-link]').click()
    cy.url().should('include', '/forgot-password')
  })

  it('应该能够导航到注册页面', () => {
    cy.get('[data-cy=signup-link]').click()
    cy.url().should('include', '/signup')
  })

  it('应该在多次失败后锁定账户', () => {
    // 尝试 5 次失败的登录
    for (let i = 0; i < 5; i++) {
      cy.get('[data-cy=username]').clear().type('testuser')
      cy.get('[data-cy=password]').clear().type('wrongpassword')
      cy.get('[data-cy=login-button]').click()
      cy.wait(500)
    }
    
    // 验证账户被锁定
    cy.get('[data-cy=error-message]')
      .should('contain', 'Account locked')
  })
})

describe('登录会话管理', () => {
  it('应该在会话过期后重定向到登录页', () => {
    // 先登录
    cy.visit('/login')
    cy.get('[data-cy=username]').type('testuser')
    cy.get('[data-cy=password]').type('password123')
    cy.get('[data-cy=login-button]').click()
    
    // 验证登录成功
    cy.url().should('include', '/dashboard')
    
    // 模拟会话过期
    cy.clearCookie('session_token')
    
    // 尝试访问受保护的页面
    cy.visit('/profile')
    
    // 应该被重定向到登录页
    cy.url().should('include', '/login')
    cy.get('[data-cy=session-expired-message]')
      .should('contain', 'Your session has expired')
  })

  it('应该能够成功登出', () => {
    // 先登录
    cy.visit('/login')
    cy.get('[data-cy=username]').type('testuser')
    cy.get('[data-cy=password]').type('password123')
    cy.get('[data-cy=login-button]').click()
    
    // 点击登出
    cy.get('[data-cy=logout-button]').click()
    
    // 验证已登出
    cy.url().should('include', '/login')
    cy.window().its('localStorage.token').should('not.exist')
  })
})
