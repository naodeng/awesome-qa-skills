import { defineConfig, devices } from '@playwright/test';

/**
 * Playwright 配置文件
 * 
 * 配置说明：
 * - testDir: 测试文件目录
 * - fullyParallel: 并行运行所有测试
 * - retries: CI 环境重试次数
 * - reporter: 测试报告格式
 * - use: 全局测试配置
 * - projects: 多浏览器测试配置
 */

export default defineConfig({
  // 测试文件目录
  testDir: './tests',
  
  // 完全并行运行测试（提高速度）
  fullyParallel: true,
  
  // CI 环境禁止 .only
  forbidOnly: !!process.env.CI,
  
  // CI 环境失败重试2次
  retries: process.env.CI ? 2 : 0,
  
  // CI 环境使用1个 worker，本地使用默认值
  workers: process.env.CI ? 1 : undefined,
  
  // 测试报告格式
  reporter: [
    ['html', { open: 'never' }],
    ['list'],
    ['json', { outputFile: 'test-results.json' }]
  ],
  
  // 全局测试配置
  use: {
    // 基础 URL
    baseURL: 'https://demo.playwright.dev',
    
    // 首次重试时记录 trace
    trace: 'on-first-retry',
    
    // 失败时截图
    screenshot: 'only-on-failure',
    
    // 失败时录制视频
    video: 'retain-on-failure',
    
    // 浏览器上下文选项
    viewport: { width: 1280, height: 720 },
    
    // 忽略 HTTPS 错误
    ignoreHTTPSErrors: true,
    
    // 默认超时时间
    actionTimeout: 10000,
    navigationTimeout: 30000,
  },
  
  // 多浏览器测试配置
  projects: [
    {
      name: 'chromium',
      use: { 
        ...devices['Desktop Chrome'],
        // Chrome 特定配置
        launchOptions: {
          args: ['--disable-web-security'],
        },
      },
    },
    
    {
      name: 'firefox',
      use: { 
        ...devices['Desktop Firefox'],
      },
    },
    
    {
      name: 'webkit',
      use: { 
        ...devices['Desktop Safari'],
      },
    },
    
    // 移动端测试（可选）
    // {
    //   name: 'Mobile Chrome',
    //   use: { 
    //     ...devices['Pixel 5'],
    //   },
    // },
    
    // {
    //   name: 'Mobile Safari',
    //   use: { 
    //     ...devices['iPhone 12'],
    //   },
    // },
  ],
  
  // Web Server 配置（如果需要启动本地服务器）
  // webServer: {
  //   command: 'npm run start',
  //   url: 'http://localhost:3000',
  //   reuseExistingServer: !process.env.CI,
  //   timeout: 120000,
  // },
});
