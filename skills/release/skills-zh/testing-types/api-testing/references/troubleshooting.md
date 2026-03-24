## 故障排除

### 常见问题

#### 1. Newman 运行失败

**问题：** `newman: command not found`

**解决方案：**
```bash
# 全局安装 Newman
npm install -g newman

# 或使用 npx（无需全局安装）
npx newman run collection.json
```

#### 2. 环境变量未生效

**问题：** 测试中的变量显示为 `{{variable}}`

**解决方案：**
- 确保使用 `-e` 参数指定环境文件
- 检查环境文件中变量名是否正确
- 在 Postman 中验证变量是否正确设置

```bash
newman run collection.json -e environment.json
```

#### 3. 证书验证错误

**问题：** `SSL certificate problem`

**解决方案：**
```bash
# 开发环境可临时禁用 SSL 验证（不推荐生产环境）
newman run collection.json --insecure

# 或指定 CA 证书
newman run collection.json --ssl-client-cert-list cert-list.json
```

#### 4. 请求超时

**问题：** `Error: ETIMEDOUT` 或 `Error: ESOCKETTIMEDOUT`

**解决方案：**
```bash
# 增加超时时间（毫秒）
newman run collection.json --timeout-request 30000

# 添加请求延迟
newman run collection.json --delay-request 500
```

#### 5. 响应数据格式不匹配

**问题：** JSON Schema 验证失败

**解决方案：**
- 使用 Postman 的 Schema 生成功能
- 检查 API 文档确认数据结构
- 使用 `pm.response.json()` 打印实际响应

```javascript
// 在 Tests 中添加调试信息
console.log(pm.response.json());
```

#### 6. 动态数据依赖问题

**问题：** 后续请求依赖前一个请求的数据

**解决方案：**
```javascript
// 在第一个请求的 Tests 中保存数据
pm.environment.set("userId", pm.response.json().id);

// 在后续请求中使用
// URL: {{baseUrl}}/users/{{userId}}
```

#### 7. 批量运行测试失败

**问题：** 单个测试通过，批量运行失败

**解决方案：**
- 检查测试之间的数据依赖
- 确保每个测试独立可运行
- 添加适当的延迟：`--delay-request 200`
- 使用 `--bail` 在首次失败时停止

