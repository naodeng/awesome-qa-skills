/**
 * Cucumber 配置文件
 * 定义不同的测试配置和运行选项
 */

module.exports = {
  // 默认配置
  default: {
    require: [
      'step-definitions/**/*.js',
      'support/**/*.js'
    ],
    format: [
      'progress-bar',
      'html:reports/cucumber-report.html',
      'json:reports/cucumber-report.json',
      'junit:reports/cucumber-report.xml'
    ],
    formatOptions: {
      snippetInterface: 'async-await'
    },
    publishQuiet: true,
    dryRun: false,
    failFast: false,
    strict: true,
    parallel: 1
  },

  // 冒烟测试配置
  smoke: {
    require: [
      'step-definitions/**/*.js',
      'support/**/*.js'
    ],
    format: ['progress-bar'],
    tags: '@smoke',
    publishQuiet: true
  },

  // 回归测试配置
  regression: {
    require: [
      'step-definitions/**/*.js',
      'support/**/*.js'
    ],
    format: [
      'progress-bar',
      'html:reports/regression-report.html'
    ],
    tags: 'not @skip and not @wip',
    publishQuiet: true,
    parallel: 2
  },

  // 快速测试配置（跳过慢速测试）
  quick: {
    require: [
      'step-definitions/**/*.js',
      'support/**/*.js'
    ],
    format: ['progress-bar'],
    tags: 'not @slow and not @skip',
    publishQuiet: true
  },

  // CI/CD 配置
  ci: {
    require: [
      'step-definitions/**/*.js',
      'support/**/*.js'
    ],
    format: [
      'progress-bar',
      'json:reports/cucumber-report.json',
      'junit:reports/cucumber-report.xml'
    ],
    tags: 'not @skip and not @wip',
    publishQuiet: true,
    parallel: 4,
    retry: 1
  },

  // 开发配置（详细输出）
  dev: {
    require: [
      'step-definitions/**/*.js',
      'support/**/*.js'
    ],
    format: [
      'progress-bar',
      '@cucumber/pretty-formatter'
    ],
    publishQuiet: true,
    failFast: true
  },

  // 调试配置
  debug: {
    require: [
      'step-definitions/**/*.js',
      'support/**/*.js'
    ],
    format: ['progress-bar'],
    publishQuiet: true,
    failFast: true,
    parallel: 1,
    retry: 0
  },

  // 干运行（检查步骤定义）
  'dry-run': {
    require: [
      'step-definitions/**/*.js',
      'support/**/*.js'
    ],
    format: ['progress-bar'],
    dryRun: true,
    publishQuiet: true
  }
};
