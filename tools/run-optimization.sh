#!/bin/bash

# Run Optimization - 执行优化任务的辅助脚本
# Usage: ./run-optimization.sh [phase]

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# 显示横幅
show_banner() {
    echo -e "${CYAN}"
    echo "╔═══════════════════════════════════════════════════════════╗"
    echo "║                                                           ║"
    echo "║        Awesome QA Skills - 优化执行助手                   ║"
    echo "║                                                           ║"
    echo "╚═══════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

# 显示菜单
show_menu() {
    echo -e "${BLUE}请选择要执行的优化阶段：${NC}"
    echo ""
    echo "  ${GREEN}1.${NC} 阶段 1: 完成基础设施 (P0)"
    echo "     - 创建模板文件"
    echo "     - 创建剩余工具脚本"
    echo ""
    echo "  ${GREEN}2.${NC} 阶段 2: 增强提示词 (P0)"
    echo "     - 为所有 skills 添加代码示例"
    echo "     - 添加 troubleshooting 章节"
    echo "     - 创建分层提示词"
    echo ""
    echo "  ${GREEN}3.${NC} 阶段 3: 优化工作流 (P0)"
    echo "     - 添加步骤追踪"
    echo "     - 创建执行日志模板"
    echo "     - 添加健康度评分"
    echo ""
    echo "  ${GREEN}4.${NC} 阶段 4: 上下文感知系统 (P1)"
    echo "     - 集成上下文检测"
    echo "     - 实现上下文适配"
    echo ""
    echo "  ${GREEN}5.${NC} 阶段 5: Skills 依赖管理 (P1)"
    echo "     - 建立依赖关系"
    echo "     - 创建工作流模板"
    echo ""
    echo "  ${GREEN}6.${NC} 创建示例 Skill"
    echo "     - 使用 skill-generator 创建新 skill"
    echo ""
    echo "  ${GREEN}7.${NC} 检测项目上下文"
    echo "     - 运行 context-detector"
    echo ""
    echo "  ${GREEN}8.${NC} 查看优化进度"
    echo "     - 显示已完成和待完成的任务"
    echo ""
    echo "  ${GREEN}9.${NC} 运行质量检查"
    echo "     - 检查代码质量和文档完整性"
    echo ""
    echo "  ${GREEN}0.${NC} 退出"
    echo ""
}

# 阶段 1: 完成基础设施
phase1_infrastructure() {
    echo -e "${BLUE}执行阶段 1: 完成基础设施${NC}"
    echo ""
    
    echo -e "${YELLOW}创建输出格式模板...${NC}"
    mkdir -p templates/output-templates
    
    # Jira 格式模板
    cat > templates/output-templates/jira-format.md << 'EOF'
# Jira 格式输出模板

## 测试用例格式

| 字段 | 说明 |
|------|------|
| Summary | 测试用例标题 |
| Description | 详细描述 |
| Preconditions | 前置条件 |
| Test Steps | 测试步骤 |
| Expected Result | 预期结果 |
| Priority | 优先级 (Highest/High/Medium/Low) |
| Labels | 标签 |

## 示例

**Summary**: 验证用户登录功能

**Description**: 
测试用户使用正确的用户名和密码登录系统

**Preconditions**:
- 用户已注册
- 系统可访问

**Test Steps**:
1. 打开登录页面
2. 输入用户名
3. 输入密码
4. 点击登录按钮

**Expected Result**:
- 登录成功
- 跳转到首页
- 显示用户信息

**Priority**: High

**Labels**: login, smoke-test, regression
EOF
    
    echo -e "${GREEN}✓ 创建了 Jira 格式模板${NC}"
    
    # TestRail 格式模板
    cat > templates/output-templates/testrail-format.md << 'EOF'
# TestRail 格式输出模板

## 测试用例格式

| 字段 | 说明 |
|------|------|
| Title | 测试用例标题 |
| Section | 所属章节 |
| Template | 模板类型 (Test Case (Steps)) |
| Type | 测试类型 (Functional/Regression/Smoke) |
| Priority | 优先级 (Critical/High/Medium/Low) |
| Estimate | 预计时间 |
| References | 关联需求 |
| Preconditions | 前置条件 |
| Steps | 测试步骤 |
| Expected Result | 预期结果 |

## 示例

**Title**: TC-001: 验证用户登录功能

**Section**: 用户认证

**Template**: Test Case (Steps)

**Type**: Functional

**Priority**: High

**Estimate**: 5m

**References**: REQ-001

**Preconditions**:
用户已注册且账号状态正常

**Steps**:
| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | 打开登录页面 | 显示登录表单 |
| 2 | 输入有效用户名 | 用户名输入框显示输入内容 |
| 3 | 输入有效密码 | 密码输入框显示掩码 |
| 4 | 点击登录按钮 | 系统验证凭据 |
| 5 | 验证登录结果 | 跳转到首页，显示用户信息 |
EOF
    
    echo -e "${GREEN}✓ 创建了 TestRail 格式模板${NC}"
    
    echo -e "${YELLOW}创建工作流模板...${NC}"
    mkdir -p templates/workflow-templates
    
    # 新功能测试流程模板
    cat > templates/workflow-templates/new-feature-testing.md << 'EOF'
# 新功能测试流程模板

## Skills 组合

1. requirements-analysis
2. test-strategy
3. test-case-writing
4. functional-testing
5. automation-testing
6. test-reporting

## 执行步骤

### 步骤 1: 需求分析 (15-30 分钟)

```
@skill requirements-analysis
需求：[在此粘贴功能需求]
```

**输出**：
- 需求分解
- 测试点识别
- 边界值分析

### 步骤 2: 测试策略 (10-20 分钟)

```
@skill test-strategy
基于上述需求分析，制定测试策略
```

**输出**：
- 测试范围
- 测试方法
- 资源需求
- 风险评估

### 步骤 3: 测试用例编写 (30-60 分钟)

```
@skill test-case-writing
基于需求分析和测试策略，编写详细测试用例
```

**输出**：
- 正常场景用例
- 异常场景用例
- 边界值用例

### 步骤 4: 功能测试 (1-2 小时)

```
@skill functional-testing
执行上述测试用例，记录测试结果
```

**输出**：
- 测试执行记录
- 缺陷报告
- 测试覆盖率

### 步骤 5: 自动化测试 (2-4 小时)

```
@skill automation-testing
为核心功能编写自动化测试脚本
技术栈：[Playwright/Cypress/Selenium]
```

**输出**：
- 自动化测试代码
- Page Object Model
- 测试数据

### 步骤 6: 测试报告 (15-30 分钟)

```
@skill test-reporting
生成测试报告
```

**输出**：
- 测试总结
- 缺陷统计
- 覆盖率报告
- 风险评估

## 检查清单

- [ ] 需求已充分理解
- [ ] 测试策略已评审
- [ ] 测试用例已评审
- [ ] 功能测试已完成
- [ ] 关键路径已自动化
- [ ] 测试报告已发布
- [ ] 缺陷已跟踪

## 预计时间

- 总计：5-8 小时
- 可分多天完成

## 相关文档

- [需求文档]
- [测试计划]
- [测试用例]
- [自动化测试代码]
- [测试报告]
EOF
    
    echo -e "${GREEN}✓ 创建了新功能测试流程模板${NC}"
    
    echo ""
    echo -e "${GREEN}阶段 1 完成！${NC}"
    echo ""
}

# 阶段 6: 创建示例 Skill
phase6_create_example() {
    echo -e "${BLUE}创建示例 Skill${NC}"
    echo ""
    
    read -p "Skill 名称 (kebab-case): " skill_name
    read -p "类别 (testing-types/testing-workflows/advanced): " category
    read -p "难度 (beginner/intermediate/advanced/expert): " level
    read -p "语言 (zh/en): " language
    read -p "描述: " description
    
    echo ""
    echo -e "${YELLOW}生成 Skill...${NC}"
    
    ./tools/skill-generator.sh \
        --name "$skill_name" \
        --category "$category" \
        --level "$level" \
        --language "$language" \
        --description "$description"
    
    echo ""
}

# 阶段 7: 检测项目上下文
phase7_detect_context() {
    echo -e "${BLUE}检测项目上下文${NC}"
    echo ""
    
    read -p "项目路径 (默认: 当前目录): " project_path
    project_path=${project_path:-.}
    
    echo ""
    ./tools/context-detector.sh "$project_path"
    echo ""
}

# 阶段 8: 查看优化进度
phase8_show_progress() {
    echo -e "${BLUE}优化进度${NC}"
    echo ""
    
    echo -e "${CYAN}已完成的工作：${NC}"
    echo "  ✅ 规划文档 (100%)"
    echo "  ✅ 核心文档 (100%)"
    echo "  ✅ 目录结构 (100%)"
    echo "  ✅ 部分工具脚本 (40%)"
    echo ""
    
    echo -e "${YELLOW}待完成的工作：${NC}"
    echo "  ⏳ 模板系统 (20%)"
    echo "  ⏳ 提示词增强 (0%)"
    echo "  ⏳ 工作流优化 (0%)"
    echo "  ⏳ 上下文感知 (30%)"
    echo "  ⏳ 代码示例库 (0%)"
    echo ""
    
    echo -e "${BLUE}总体进度：约 17%${NC}"
    echo ""
    
    echo -e "${CYAN}详细信息请查看：${NC}"
    echo "  - OPTIMIZATION_SUMMARY.md"
    echo "  - .kiro/specs/skills-optimization/tasks.md"
    echo ""
}

# 主函数
main() {
    show_banner
    
    if [ $# -eq 0 ]; then
        while true; do
            show_menu
            read -p "请选择 (0-9): " choice
            echo ""
            
            case $choice in
                1)
                    phase1_infrastructure
                    read -p "按 Enter 继续..."
                    ;;
                2)
                    echo -e "${YELLOW}阶段 2 需要手动执行，请参考 OPTIMIZATION_SUMMARY.md${NC}"
                    read -p "按 Enter 继续..."
                    ;;
                3)
                    echo -e "${YELLOW}阶段 3 需要手动执行，请参考 OPTIMIZATION_SUMMARY.md${NC}"
                    read -p "按 Enter 继续..."
                    ;;
                4)
                    echo -e "${YELLOW}阶段 4 需要手动执行，请参考 OPTIMIZATION_SUMMARY.md${NC}"
                    read -p "按 Enter 继续..."
                    ;;
                5)
                    echo -e "${YELLOW}阶段 5 需要手动执行，请参考 OPTIMIZATION_SUMMARY.md${NC}"
                    read -p "按 Enter 继续..."
                    ;;
                6)
                    phase6_create_example
                    read -p "按 Enter 继续..."
                    ;;
                7)
                    phase7_detect_context
                    read -p "按 Enter 继续..."
                    ;;
                8)
                    phase8_show_progress
                    read -p "按 Enter 继续..."
                    ;;
                9)
                    echo -e "${YELLOW}质量检查工具尚未实现${NC}"
                    read -p "按 Enter 继续..."
                    ;;
                0)
                    echo -e "${GREEN}感谢使用！${NC}"
                    exit 0
                    ;;
                *)
                    echo -e "${RED}无效选择，请重试${NC}"
                    read -p "按 Enter 继续..."
                    ;;
            esac
            
            clear
            show_banner
        done
    else
        # 命令行参数模式
        case $1 in
            phase1|1)
                phase1_infrastructure
                ;;
            create|6)
                phase6_create_example
                ;;
            detect|7)
                phase7_detect_context
                ;;
            progress|8)
                phase8_show_progress
                ;;
            *)
                echo -e "${RED}未知命令: $1${NC}"
                echo "Usage: $0 [phase1|create|detect|progress]"
                exit 1
                ;;
        esac
    fi
}

# 运行主函数
main "$@"
