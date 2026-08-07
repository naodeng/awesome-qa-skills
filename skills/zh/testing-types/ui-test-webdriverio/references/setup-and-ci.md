# UI 自动化测试 WebdriverIO安装与 CI 说明

## 本地设置

- 给出命令前先确认工具版本和运行时环境。
- 不要把密钥、token 或环境专属值写进已提交测试文件。
- 将生成报告放到 reports 或 build-artifacts 一类目录，并避免误提交。

## 建议执行命令

```bash
npx wdio run "${CONFIG:-wdio.conf.js}"
```

## CI 建议

- Pull Request 阶段运行冒烟覆盖。
- 发布分支或定时任务运行更完整回归。
- 如果工具会产生日志、截图、trace 或结果文件，将它们保存为 CI artifact。
- Pipeline 应因明确断言失败而失败，不因可选产物缺失而失败。
