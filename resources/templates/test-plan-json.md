# 测试计划模板 - JSON 格式

## 格式说明
适用于 API 集成、自动化工具、程序化处理。

## JSON 结构

```json
{
  "testPlan": {
    "metadata": {
      "id": "TP-2024-001",
      "projectName": "电商平台",
      "version": "v1.0.0",
      "testManager": {
        "name": "张三",
        "email": "zhangsan@example.com",
        "phone": "+86 138-0000-0000"
      },
      "createdDate": "2024-01-15T10:00:00Z",
      "lastUpdated": "2024-01-20T15:30:00Z",
      "status": "approved",
      "approvers": [
        {
          "role": "测试经理",
          "name": "张三",
          "approvedDate": "2024-01-17T14:00:00Z"
        },
        {
          "role": "项目经理",
          "name": "李四",
          "approvedDate": "2024-01-17T15:00:00Z"
        }
      ]
    },
    
    "introduction": {
      "purpose": "本测试计划旨在定义电商平台 v1.0.0 的测试策略、范围、资源、进度和交付物，确保产品质量满足业务需求。",
      "scope": "覆盖所有核心功能模块的测试活动，包括功能测试、集成测试、性能测试、安全测试和用户验收测试。",
      "audience": [
        "测试团队",
        "开发团队",
        "项目经理",
        "产品经理",
        "质量保证团队"
      ],
      "references": [
        {
          "title": "需求规格说明书",
          "url": "./requirements.md",
          "version": "v1.0"
        },
        {
          "title": "系统设计文档",
          "url": "./design.md",
          "version": "v1.0"
        }
      ]
    },
    
    "testScope": {
      "inScope": [
        {
          "module": "用户管理",
          "features": [
            {
              "name": "用户注册",
              "priority": "P0",
              "testTypes": ["功能测试", "安全测试"]
            },
            {
              "name": "用户登录",
              "priority": "P0",
              "testTypes": ["功能测试", "性能测试", "安全测试"]
            },
            {
              "name": "密码重置",
              "priority": "P1",
              "testTypes": ["功能测试", "安全测试"]
            }
          ]
        },
        {
          "module": "订单管理",
          "features": [
            {
              "name": "创建订单",
              "priority": "P0",
              "testTypes": ["功能测试", "集成测试"]
            },
            {
              "name": "订单查询",
              "priority": "P1",
              "testTypes": ["功能测试", "性能测试"]
            }
          ]
        },
        {
          "module": "支付模块",
          "features": [
            {
              "name": "支付宝支付",
              "priority": "P0",
              "testTypes": ["集成测试", "安全测试"]
            },
            {
              "name": "微信支付",
              "priority": "P0",
              "testTypes": ["集成测试", "安全测试"]
            }
          ]
        }
      ],
      "outOfScope": [
        "第三方支付网关内部逻辑",
        "外部 API 服务的功能",
        "历史遗留系统（v0.x）",
        "Beta 功能（计划在 v1.1 测试）"
      ],
      "assumptions": [
        "测试环境与生产环境配置一致",
        "第三方服务在测试期间可用",
        "测试数据已准备完毕"
      ],
      "dependencies": [
        {
          "name": "第三方支付服务",
          "type": "external",
          "criticality": "high"
        },
        {
          "name": "测试环境",
          "type": "internal",
          "criticality": "high"
        }
      ]
    },
    
    "testStrategy": {
      "testTypes": [
        {
          "type": "单元测试",
          "description": "开发人员编写，覆盖率 > 80%",
          "owner": "开发团队",
          "priority": "P0",
          "coverage": 80,
          "tools": ["Jest", "JUnit"]
        },
        {
          "type": "集成测试",
          "description": "模块间接口测试",
          "owner": "QA 团队",
          "priority": "P0",
          "coverage": 90,
          "tools": ["Postman", "REST Assured"]
        },
        {
          "type": "系统测试",
          "description": "端到端功能测试",
          "owner": "QA 团队",
          "priority": "P0",
          "coverage": 95,
          "tools": ["Playwright", "Selenium"]
        },
        {
          "type": "性能测试",
          "description": "负载、压力、稳定性测试",
          "owner": "性能团队",
          "priority": "P1",
          "metrics": {
            "responseTime": "< 2s",
            "concurrentUsers": 1000,
            "tps": "> 500"
          },
          "tools": ["JMeter", "K6"]
        },
        {
          "type": "安全测试",
          "description": "漏洞扫描、渗透测试",
          "owner": "安全团队",
          "priority": "P1",
          "standards": ["OWASP Top 10"],
          "tools": ["OWASP ZAP", "Burp Suite"]
        },
        {
          "type": "UAT",
          "description": "用户验收测试",
          "owner": "业务团队",
          "priority": "P0",
          "tools": ["Manual Testing"]
        }
      ],
      
      "testMethods": [
        "黑盒测试",
        "白盒测试",
        "灰盒测试",
        "探索性测试",
        "自动化测试"
      ],
      
      "testEnvironments": [
        {
          "name": "开发环境",
          "purpose": "开发自测",
          "url": "https://dev.example.com",
          "database": "dev_db",
          "status": "available"
        },
        {
          "name": "测试环境",
          "purpose": "QA 测试",
          "url": "https://test.example.com",
          "database": "test_db",
          "status": "available"
        },
        {
          "name": "预发布环境",
          "purpose": "UAT 测试",
          "url": "https://staging.example.com",
          "database": "staging_db",
          "status": "setup_in_progress"
        },
        {
          "name": "生产环境",
          "purpose": "正式发布",
          "url": "https://www.example.com",
          "database": "prod_db",
          "status": "available",
          "access": "read_only"
        }
      ],
      
      "testTools": [
        {
          "name": "Jira",
          "purpose": "缺陷管理",
          "version": "Cloud",
          "license": "subscription",
          "cost": 10000,
          "currency": "CNY"
        },
        {
          "name": "TestRail",
          "purpose": "用例管理",
          "version": "v7.5",
          "license": "subscription",
          "cost": 15000,
          "currency": "CNY"
        },
        {
          "name": "Playwright",
          "purpose": "UI 自动化",
          "version": "v1.40",
          "license": "open_source",
          "cost": 0
        }
      ]
    },
    
    "schedule": {
      "milestones": [
        {
          "id": "M1",
          "name": "测试计划评审",
          "startDate": "2024-01-15",
          "endDate": "2024-01-17",
          "plannedEffort": 2,
          "actualEffort": 2,
          "status": "completed",
          "deliverables": ["测试计划 v1.0"],
          "owner": "张三"
        },
        {
          "id": "M2",
          "name": "测试用例设计",
          "startDate": "2024-01-18",
          "endDate": "2024-01-25",
          "plannedEffort": 15,
          "actualEffort": 10,
          "status": "in_progress",
          "progress": 67,
          "deliverables": ["测试用例集"],
          "owner": "李四"
        },
        {
          "id": "M3",
          "name": "测试环境搭建",
          "startDate": "2024-01-20",
          "endDate": "2024-01-22",
          "plannedEffort": 5,
          "actualEffort": 0,
          "status": "planned",
          "deliverables": ["测试环境"],
          "owner": "运维团队"
        },
        {
          "id": "M4",
          "name": "功能测试执行",
          "startDate": "2024-01-26",
          "endDate": "2024-02-05",
          "plannedEffort": 30,
          "actualEffort": 0,
          "status": "planned",
          "deliverables": ["测试报告"],
          "owner": "QA 团队"
        }
      ],
      
      "criticalPath": ["M1", "M2", "M3", "M4"],
      
      "dependencies": [
        {
          "from": "M2",
          "to": "M4",
          "type": "finish_to_start"
        },
        {
          "from": "M3",
          "to": "M4",
          "type": "finish_to_start"
        }
      ]
    },
    
    "resources": {
      "team": [
        {
          "id": "T001",
          "name": "张三",
          "role": "测试经理",
          "email": "zhangsan@example.com",
          "skills": ["管理", "规划", "风险管理"],
          "availability": 100,
          "allocation": {
            "M1": 100,
            "M2": 20,
            "M4": 20
          }
        },
        {
          "id": "T002",
          "name": "李四",
          "role": "高级测试工程师",
          "email": "lisi@example.com",
          "skills": ["功能测试", "自动化测试", "API 测试"],
          "availability": 100,
          "allocation": {
            "M2": 100,
            "M4": 100
          }
        },
        {
          "id": "T003",
          "name": "王五",
          "role": "测试工程师",
          "email": "wangwu@example.com",
          "skills": ["功能测试", "手工测试"],
          "availability": 100,
          "allocation": {
            "M4": 100
          }
        }
      ],
      
      "hardware": [
        {
          "type": "测试服务器",
          "quantity": 4,
          "specs": "8核 16GB",
          "purpose": "测试环境"
        },
        {
          "type": "测试客户端",
          "quantity": 10,
          "specs": "标准配置",
          "purpose": "手工测试"
        },
        {
          "type": "移动设备",
          "devices": [
            "iPhone 12", "iPhone 13", "iPhone 14",
            "Samsung Galaxy S21", "Samsung Galaxy S22",
            "Xiaomi 12", "Xiaomi 13"
          ],
          "purpose": "移动端测试"
        }
      ],
      
      "budget": {
        "total": 500000,
        "currency": "CNY",
        "breakdown": [
          {
            "category": "人力成本",
            "amount": 350000,
            "percentage": 70
          },
          {
            "category": "工具许可证",
            "amount": 50000,
            "percentage": 10
          },
          {
            "category": "硬件设备",
            "amount": 80000,
            "percentage": 16
          },
          {
            "category": "其他费用",
            "amount": 20000,
            "percentage": 4
          }
        ]
      }
    },
    
    "deliverables": [
      {
        "name": "测试计划",
        "type": "document",
        "owner": "张三",
        "plannedDate": "2024-01-17",
        "actualDate": "2024-01-17",
        "status": "completed",
        "location": "/docs/test-plan.md"
      },
      {
        "name": "测试用例",
        "type": "document",
        "owner": "李四",
        "plannedDate": "2024-01-25",
        "actualDate": null,
        "status": "in_progress",
        "location": "/test-cases/"
      },
      {
        "name": "测试脚本",
        "type": "code",
        "owner": "钱七",
        "plannedDate": "2024-02-05",
        "actualDate": null,
        "status": "planned",
        "location": "/tests/"
      },
      {
        "name": "测试报告",
        "type": "document",
        "owner": "王五",
        "frequency": "daily",
        "status": "ongoing",
        "location": "/reports/"
      }
    ],
    
    "riskManagement": {
      "risks": [
        {
          "id": "R001",
          "description": "需求变更频繁",
          "impact": "测试用例需重写",
          "probability": "high",
          "severity": "high",
          "riskLevel": "high",
          "mitigation": "需求冻结机制，变更控制流程",
          "owner": "产品经理",
          "status": "monitoring"
        },
        {
          "id": "R002",
          "description": "测试环境不稳定",
          "impact": "测试进度延迟",
          "probability": "medium",
          "severity": "high",
          "riskLevel": "high",
          "mitigation": "提前搭建，准备备用环境",
          "owner": "运维团队",
          "status": "monitoring"
        },
        {
          "id": "R003",
          "description": "关键人员离职",
          "impact": "知识流失，进度延迟",
          "probability": "low",
          "severity": "high",
          "riskLevel": "medium",
          "mitigation": "文档化，交叉培训，知识共享",
          "owner": "张三",
          "status": "monitoring"
        }
      ],
      
      "contingencyPlans": [
        {
          "scenario": "测试进度严重延迟",
          "plan": "压缩非关键测试，聚焦核心功能，增加人力资源"
        },
        {
          "scenario": "发现严重缺陷",
          "plan": "延期发布，确保质量，制定修复计划"
        }
      ]
    },
    
    "entryCriteria": [
      {
        "criterion": "需求文档已评审并冻结",
        "status": "met",
        "verifiedBy": "产品经理",
        "verifiedDate": "2024-01-10"
      },
      {
        "criterion": "设计文档已完成",
        "status": "met",
        "verifiedBy": "架构师",
        "verifiedDate": "2024-01-12"
      },
      {
        "criterion": "开发代码已提交并通过代码审查",
        "status": "in_progress",
        "verifiedBy": "开发经理",
        "verifiedDate": null
      },
      {
        "criterion": "单元测试覆盖率 > 80%",
        "status": "in_progress",
        "currentValue": 75,
        "targetValue": 80,
        "verifiedBy": "开发团队",
        "verifiedDate": null
      }
    ],
    
    "exitCriteria": [
      {
        "criterion": "所有计划的测试用例已执行",
        "targetValue": 100,
        "currentValue": 0,
        "unit": "percent"
      },
      {
        "criterion": "测试覆盖率 > 90%",
        "targetValue": 90,
        "currentValue": 0,
        "unit": "percent"
      },
      {
        "criterion": "无 P0/P1 级别缺陷",
        "targetValue": 0,
        "currentValue": 0,
        "unit": "count"
      },
      {
        "criterion": "P2 级别缺陷 < 5 个",
        "targetValue": 5,
        "currentValue": 0,
        "unit": "count"
      },
      {
        "criterion": "缺陷修复率 > 95%",
        "targetValue": 95,
        "currentValue": 0,
        "unit": "percent"
      }
    ],
    
    "defectManagement": {
      "priorityDefinitions": [
        {
          "priority": "P0",
          "name": "Blocker",
          "definition": "系统崩溃，核心功能不可用",
          "responseTime": "立即",
          "resolutionTime": "4小时"
        },
        {
          "priority": "P1",
          "name": "Critical",
          "definition": "重要功能不可用",
          "responseTime": "2小时",
          "resolutionTime": "1天"
        },
        {
          "priority": "P2",
          "name": "Major",
          "definition": "功能部分不可用",
          "responseTime": "1天",
          "resolutionTime": "3天"
        }
      ],
      
      "workflow": [
        "New",
        "Assigned",
        "In Progress",
        "Fixed",
        "Verified",
        "Closed",
        "Reopened"
      ],
      
      "reportingRequirements": [
        "清晰的标题",
        "详细的重现步骤",
        "预期结果 vs 实际结果",
        "环境信息",
        "截图/日志",
        "严重程度和优先级"
      ]
    },
    
    "communication": {
      "meetings": [
        {
          "name": "每日站会",
          "frequency": "daily",
          "duration": 15,
          "participants": ["测试团队"],
          "purpose": "进度同步，问题讨论"
        },
        {
          "name": "测试评审会",
          "frequency": "weekly",
          "duration": 60,
          "participants": ["全体"],
          "purpose": "测试结果评审"
        }
      ],
      
      "reports": [
        {
          "type": "每日报告",
          "frequency": "daily",
          "recipients": ["项目经理", "测试经理"],
          "content": ["测试进度", "缺陷统计", "风险预警"]
        },
        {
          "type": "每周报告",
          "frequency": "weekly",
          "recipients": ["全体"],
          "content": ["测试总结", "度量指标", "下周计划"]
        }
      ],
      
      "channels": [
        {
          "name": "Jira",
          "purpose": "缺陷跟踪"
        },
        {
          "name": "Slack",
          "purpose": "即时沟通"
        },
        {
          "name": "Email",
          "purpose": "正式通知"
        }
      ]
    },
    
    "metrics": {
      "testMetrics": [
        {
          "name": "测试用例数",
          "target": 500,
          "current": 335,
          "unit": "count"
        },
        {
          "name": "测试用例执行率",
          "target": 100,
          "current": 0,
          "unit": "percent"
        },
        {
          "name": "测试覆盖率",
          "target": 90,
          "current": 0,
          "unit": "percent"
        },
        {
          "name": "缺陷发现率",
          "target": 80,
          "current": 0,
          "unit": "percent"
        },
        {
          "name": "自动化覆盖率",
          "target": 70,
          "current": 30,
          "unit": "percent"
        }
      ],
      
      "qualityMetrics": [
        {
          "name": "缺陷密度",
          "formula": "缺陷数 / KLOC",
          "target": "< 2",
          "current": 0
        },
        {
          "name": "缺陷修复率",
          "formula": "已修复缺陷 / 总缺陷",
          "target": "> 95%",
          "current": 0
        }
      ]
    }
  }
}
```

## JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "testPlan": {
      "type": "object",
      "required": ["metadata", "testScope", "testStrategy", "schedule"],
      "properties": {
        "metadata": {
          "type": "object",
          "required": ["id", "projectName", "version", "status"]
        }
      }
    }
  }
}
```

## 使用示例

### 1. 加载测试计划
```javascript
const testPlan = require('./test-plan.json');
console.log(testPlan.testPlan.metadata.projectName);
```

### 2. 查询测试范围
```javascript
const inScope = testPlan.testPlan.testScope.inScope;
inScope.forEach(module => {
  console.log(`模块: ${module.module}`);
  module.features.forEach(feature => {
    console.log(`  - ${feature.name} (${feature.priority})`);
  });
});
```

### 3. 生成报告
```javascript
const metrics = testPlan.testPlan.metrics.testMetrics;
metrics.forEach(metric => {
  const progress = (metric.current / metric.target * 100).toFixed(2);
  console.log(`${metric.name}: ${progress}%`);
});
```

## 最佳实践

1. **使用 JSON Schema 验证**: 确保数据格式正确
2. **版本控制**: 使用 Git 管理
3. **API 集成**: 与测试管理系统集成
4. **自动化处理**: 程序化生成和更新
5. **数据一致性**: 保持字段命名统一
6. **文档化**: 添加注释说明字段含义
