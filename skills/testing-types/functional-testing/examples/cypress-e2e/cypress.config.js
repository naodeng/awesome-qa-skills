const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    baseUrl: 'https://example.cypress.io',
    viewportWidth: 1280,
    viewportHeight: 720,
    video: true,
    screenshotOnRunFailure: true,
    
    // 测试文件配置
    specPattern: 'cypress/e2e/**/*.cy.{js,jsx,ts,tsx}',
    
    // 超时配置
    defaultCommandTimeout: 10000,
    pageLoadTimeout: 30000,
    
    // 重试配置
    retries: {
      runMode: 2,
      openMode: 0
    },
    
    setupNodeEvents(on, config) {
      // 实现 node 事件监听器
      on('task', {
        log(message) {
          console.log(message)
          return null
        }
      })
    },
  },
  
  // 组件测试配置
  component: {
    devServer: {
      framework: 'react',
      bundler: 'vite',
    },
  },
})
