import { defineConfig, devices } from '@playwright/test';

/**
 * Playwright 配置文件
 * 用于可访问性测试
 */
export default defineConfig({
  // 测试目录
  testDir: './tests',
  
  // 全局超时
  timeout: 30000,
  
  // 失败重试次数
  retries: process.env.CI ? 2 : 0,
  
  // 并行执行
  fullyParallel: true,
  workers: process.env.CI ? 2 : undefined,
  
  // 报告器
  reporter: [
    ['html', { outputFolder: 'playwright-report' }],
    ['json', { outputFile: 'test-results.json' }],
    ['list']
  ],
  
  // 全局配置
  use: {
    // 基础 URL
    baseURL: 'https://example.com',
    
    // 截图策略
    screenshot: 'only-on-failure',
    
    // 视频录制
    video: 'retain-on-failure',
    
    // 追踪
    trace: 'retain-on-failure',
    
    // 浏览器上下文选项
    viewport: { width: 1280, height: 720 },
    ignoreHTTPSErrors: true,
  },

  // 测试项目配置
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
    // 移动设备测试
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 12'] },
    },
  ],
});
