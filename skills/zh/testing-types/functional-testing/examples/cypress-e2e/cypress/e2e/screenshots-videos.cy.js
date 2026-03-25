/**
 * Cypress 截图和视频录制示例
 * 
 * 功能：
 * - 自动截图
 * - 手动截图
 * - 视频录制
 * - 失败时截图
 */

describe('截图和视频录制功能', () => {
  beforeEach(() => {
    cy.visit('https://example.cypress.io/commands/actions')
  })

  it('应该在测试失败时自动截图', () => {
    // 这个测试会失败，Cypress 会自动截图
    cy.get('.action-email')
      .type('test@example.com')
      .should('have.value', 'wrong@example.com') // 故意失败
  })

  it('应该手动截图整个页面', () => {
    // 手动截图整个页面
    cy.screenshot('full-page')
    
    // 验证页面元素
    cy.get('.action-email').should('be.visible')
  })

  it('应该截图特定元素', () => {
    // 截图特定元素
    cy.get('.action-email')
      .screenshot('email-input-field')
      .type('test@example.com')
    
    // 截图填充后的状态
    cy.get('.action-email')
      .screenshot('email-input-filled')
  })

  it('应该在不同视口尺寸下截图', () => {
    // 桌面视图
    cy.viewport(1920, 1080)
    cy.screenshot('desktop-view')
    
    // 平板视图
    cy.viewport(768, 1024)
    cy.screenshot('tablet-view')
    
    // 手机视图
    cy.viewport(375, 667)
    cy.screenshot('mobile-view')
  })

  it('应该在交互过程中截图', () => {
    // 初始状态
    cy.screenshot('01-initial-state')
    
    // 输入邮箱
    cy.get('.action-email')
      .type('test@example.com')
    cy.screenshot('02-email-entered')
    
    // 输入文本
    cy.get('.action-disabled')
      .type('Disabled input', { force: true })
    cy.screenshot('03-text-entered')
    
    // 最终状态
    cy.screenshot('04-final-state')
  })

  it('应该使用自定义截图选项', () => {
    // 截图时隐藏特定元素
    cy.screenshot('custom-screenshot', {
      capture: 'viewport', // 'fullPage', 'viewport', 'runner'
      clip: { x: 0, y: 0, width: 1000, height: 600 },
      scale: false,
      disableTimersAndAnimations: true,
      blackout: ['.sensitive-data'] // 隐藏敏感数据
    })
  })

  it('应该在滚动页面时截图', () => {
    cy.visit('https://example.cypress.io')
    
    // 滚动到页面顶部
    cy.scrollTo('top')
    cy.screenshot('page-top')
    
    // 滚动到页面中间
    cy.scrollTo('center')
    cy.screenshot('page-center')
    
    // 滚动到页面底部
    cy.scrollTo('bottom')
    cy.screenshot('page-bottom')
  })

  it('应该在等待元素出现后截图', () => {
    // 等待元素出现
    cy.get('.action-email', { timeout: 10000 })
      .should('be.visible')
      .screenshot('element-appeared')
  })
})

describe('视频录制功能', () => {
  // 注意：视频录制在 cypress.config.js 中配置
  // video: true 会自动录制所有测试

  it('应该录制完整的测试流程', () => {
    cy.visit('https://example.cypress.io/commands/actions')
    
    // 执行一系列操作
    cy.get('.action-email')
      .type('test@example.com')
      .should('have.value', 'test@example.com')
    
    cy.get('.action-disabled')
      .type('Disabled input', { force: true })
    
    // 视频会自动录制整个过程
  })

  it('应该录制用户交互流程', () => {
    cy.visit('https://example.cypress.io/commands/actions')
    
    // 模拟真实用户操作
    cy.get('.action-email')
      .click()
      .type('user@example.com')
      .blur()
    
    cy.get('.action-focus')
      .focus()
      .should('have.class', 'focus')
    
    cy.get('.action-blur')
      .type('About to blur')
      .blur()
      .should('have.class', 'error')
  })

  it('应该录制表单提交流程', () => {
    cy.visit('https://example.cypress.io/commands/actions')
    
    // 填写表单
    cy.get('.action-email')
      .type('test@example.com')
    
    // 提交表单（如果有提交按钮）
    // cy.get('button[type="submit"]').click()
    
    // 验证结果
    cy.get('.action-email')
      .should('have.value', 'test@example.com')
  })
})

describe('截图和视频的最佳实践', () => {
  it('应该在关键步骤截图', () => {
    cy.visit('https://example.cypress.io/commands/actions')
    
    // 步骤1：页面加载
    cy.screenshot('step-1-page-loaded')
    
    // 步骤2：输入数据
    cy.get('.action-email').type('test@example.com')
    cy.screenshot('step-2-data-entered')
    
    // 步骤3：验证结果
    cy.get('.action-email').should('have.value', 'test@example.com')
    cy.screenshot('step-3-validation-passed')
  })

  it('应该在错误发生时截图', () => {
    cy.visit('https://example.cypress.io/commands/actions')
    
    cy.get('.action-email').then(($el) => {
      if ($el.val() !== 'expected@example.com') {
        cy.screenshot('error-unexpected-value')
      }
    })
  })

  it('应该使用描述性的截图名称', () => {
    cy.visit('https://example.cypress.io/commands/actions')
    
    // 好的命名：描述性强
    cy.screenshot('login-page-email-field-empty')
    
    cy.get('.action-email').type('test@example.com')
    cy.screenshot('login-page-email-field-filled')
    
    // 避免：模糊的命名
    // cy.screenshot('test1')
    // cy.screenshot('screenshot')
  })

  it('应该组织截图到不同文件夹', () => {
    cy.visit('https://example.cypress.io/commands/actions')
    
    // 使用路径组织截图
    cy.screenshot('actions/email-input')
    cy.screenshot('actions/focus-blur')
    cy.screenshot('actions/form-submission')
  })
})

describe('性能和存储优化', () => {
  it('应该只在必要时截图', () => {
    cy.visit('https://example.cypress.io/commands/actions')
    
    // 只在关键步骤截图，避免过多截图
    cy.get('.action-email').type('test@example.com')
    
    // 只在验证失败时截图
    cy.get('.action-email').then(($el) => {
      const value = $el.val()
      if (value !== 'test@example.com') {
        cy.screenshot('validation-failed')
      }
    })
  })

  it('应该使用条件截图', () => {
    const shouldScreenshot = Cypress.env('SCREENSHOT_ON_PASS') || false
    
    cy.visit('https://example.cypress.io/commands/actions')
    cy.get('.action-email').type('test@example.com')
    
    if (shouldScreenshot) {
      cy.screenshot('conditional-screenshot')
    }
  })
})
