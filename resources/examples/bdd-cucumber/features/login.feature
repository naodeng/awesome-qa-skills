# language: zh-CN
功能: 用户登录
  作为一个用户
  我想要登录系统
  以便访问我的账户

  背景:
    假如 用户在登录页面

  @smoke @login
  场景: 管理员成功登录
    假如 用户名是 "admin"
    而且 密码是 "admin123"
    当 用户点击登录按钮
    那么 用户应该看到欢迎消息 "欢迎, 管理员"
    而且 用户应该在首页

  @smoke @login
  场景: 普通用户成功登录
    假如 用户名是 "user1"
    而且 密码是 "user123"
    当 用户点击登录按钮
    那么 用户应该看到欢迎消息 "欢迎, user1"
    而且 用户应该在首页

  @login @negative
  场景: 用户名为空时登录失败
    假如 用户名是 ""
    而且 密码是 "password"
    当 用户点击登录按钮
    那么 用户应该看到错误消息 "请输入用户名"
    而且 用户应该仍在登录页面

  @login @negative
  场景: 密码为空时登录失败
    假如 用户名是 "admin"
    而且 密码是 ""
    当 用户点击登录按钮
    那么 用户应该看到错误消息 "请输入密码"
    而且 用户应该仍在登录页面

  @login @negative
  场景: 无效凭证登录失败
    假如 用户名是 "invalid"
    而且 密码是 "wrong"
    当 用户点击登录按钮
    那么 用户应该看到错误消息 "用户名或密码错误"
    而且 用户应该仍在登录页面

  @login
  场景大纲: 使用不同凭证登录
    假如 用户名是 "<username>"
    而且 密码是 "<password>"
    当 用户点击登录按钮
    那么 登录结果应该是 "<result>"

    例子:
      | username | password | result  |
      | admin    | admin123 | success |
      | user1    | user123  | success |
      | user2    | pass456  | success |
      | invalid  | wrong    | error   |
      |          | password | error   |
      | username |          | error   |

  @login @security
  场景: 多次登录失败后账户锁定
    假如 用户名是 "admin"
    当 用户尝试使用错误密码登录 3 次
    那么 用户应该看到错误消息 "账户已被锁定"
    而且 用户应该无法登录

  @login @remember
  场景: 记住我功能
    假如 用户名是 "admin"
    而且 密码是 "admin123"
    而且 用户勾选了"记住我"选项
    当 用户点击登录按钮
    那么 用户应该成功登录
    而且 应该设置记住我的 Cookie

  @login @logout
  场景: 用户登出
    假如 用户已登录
    当 用户点击登出按钮
    那么 用户应该返回登录页面
    而且 用户会话应该被清除
