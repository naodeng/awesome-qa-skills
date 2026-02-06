#!/bin/bash

# Quality Check - 检查 skills 质量
# Usage: ./quality-check.sh [skill-path]

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# 检查路径
CHECK_PATH="${1:-skills}"

echo -e "${CYAN}"
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║              Skills 质量检查工具                          ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# 统计变量
TOTAL_CHECKS=0
PASSED_CHECKS=0
FAILED_CHECKS=0
WARNING_CHECKS=0

# 存储问题
declare -a ERRORS
declare -a WARNINGS

# 检查函数
check_skill() {
    local skill_path=$1
    local skill_name=$(basename "$skill_path")
    
    echo -e "${BLUE}检查 Skill: $skill_name${NC}"
    
    local skill_errors=0
    local skill_warnings=0
    
    # 1. 检查 SKILL.md 是否存在
    TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
    if [ ! -f "$skill_path/SKILL.md" ]; then
        echo -e "${RED}  ✗ SKILL.md 文件缺失${NC}"
        ERRORS+=("$skill_name: SKILL.md 文件缺失")
        FAILED_CHECKS=$((FAILED_CHECKS + 1))
        skill_errors=$((skill_errors + 1))
    else
        echo -e "${GREEN}  ✓ SKILL.md 存在${NC}"
        PASSED_CHECKS=$((PASSED_CHECKS + 1))
        
        # 检查 frontmatter
        TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
        if ! grep -q "^---" "$skill_path/SKILL.md"; then
            echo -e "${RED}  ✗ SKILL.md 缺少 frontmatter${NC}"
            ERRORS+=("$skill_name: SKILL.md 缺少 frontmatter")
            FAILED_CHECKS=$((FAILED_CHECKS + 1))
            skill_errors=$((skill_errors + 1))
        else
            PASSED_CHECKS=$((PASSED_CHECKS + 1))
            
            # 检查必需字段
            local required_fields=("name" "description")
            for field in "${required_fields[@]}"; do
                TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
                if ! grep -q "^${field}:" "$skill_path/SKILL.md"; then
                    echo -e "${RED}  ✗ SKILL.md 缺少字段: $field${NC}"
                    ERRORS+=("$skill_name: SKILL.md 缺少字段 $field")
                    FAILED_CHECKS=$((FAILED_CHECKS + 1))
                    skill_errors=$((skill_errors + 1))
                else
                    PASSED_CHECKS=$((PASSED_CHECKS + 1))
                fi
            done
            
            # 检查推荐字段
            local recommended_fields=("version" "last-updated" "category" "level" "tags")
            for field in "${recommended_fields[@]}"; do
                TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
                if ! grep -q "^${field}:" "$skill_path/SKILL.md"; then
                    echo -e "${YELLOW}  ⚠ SKILL.md 建议添加字段: $field${NC}"
                    WARNINGS+=("$skill_name: SKILL.md 建议添加字段 $field")
                    WARNING_CHECKS=$((WARNING_CHECKS + 1))
                    skill_warnings=$((skill_warnings + 1))
                else
                    PASSED_CHECKS=$((PASSED_CHECKS + 1))
                fi
            done
        fi
    fi
    
    # 2. 检查 prompts 目录
    TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
    if [ ! -d "$skill_path/prompts" ]; then
        echo -e "${RED}  ✗ prompts/ 目录缺失${NC}"
        ERRORS+=("$skill_name: prompts/ 目录缺失")
        FAILED_CHECKS=$((FAILED_CHECKS + 1))
        skill_errors=$((skill_errors + 1))
    else
        echo -e "${GREEN}  ✓ prompts/ 目录存在${NC}"
        PASSED_CHECKS=$((PASSED_CHECKS + 1))
        
        # 检查是否有提示词文件
        TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
        prompt_count=$(find "$skill_path/prompts" -name "*.md" | wc -l)
        if [ "$prompt_count" -eq 0 ]; then
            echo -e "${RED}  ✗ prompts/ 目录为空${NC}"
            ERRORS+=("$skill_name: prompts/ 目录为空")
            FAILED_CHECKS=$((FAILED_CHECKS + 1))
            skill_errors=$((skill_errors + 1))
        else
            echo -e "${GREEN}  ✓ 包含 $prompt_count 个提示词文件${NC}"
            PASSED_CHECKS=$((PASSED_CHECKS + 1))
        fi
    fi
    
    # 3. 检查 quick-start.md
    TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
    if [ ! -f "$skill_path/quick-start.md" ]; then
        echo -e "${YELLOW}  ⚠ quick-start.md 建议添加${NC}"
        WARNINGS+=("$skill_name: 建议添加 quick-start.md")
        WARNING_CHECKS=$((WARNING_CHECKS + 1))
        skill_warnings=$((skill_warnings + 1))
    else
        echo -e "${GREEN}  ✓ quick-start.md 存在${NC}"
        PASSED_CHECKS=$((PASSED_CHECKS + 1))
    fi
    
    # 4. 检查 output-formats.md
    TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
    if [ ! -f "$skill_path/output-formats.md" ]; then
        echo -e "${YELLOW}  ⚠ output-formats.md 建议添加${NC}"
        WARNINGS+=("$skill_name: 建议添加 output-formats.md")
        WARNING_CHECKS=$((WARNING_CHECKS + 1))
        skill_warnings=$((skill_warnings + 1))
    else
        echo -e "${GREEN}  ✓ output-formats.md 存在${NC}"
        PASSED_CHECKS=$((PASSED_CHECKS + 1))
    fi
    
    # 5. 检查 examples 目录
    TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
    if [ ! -d "$skill_path/examples" ]; then
        echo -e "${YELLOW}  ⚠ examples/ 目录建议添加${NC}"
        WARNINGS+=("$skill_name: 建议添加 examples/ 目录")
        WARNING_CHECKS=$((WARNING_CHECKS + 1))
        skill_warnings=$((skill_warnings + 1))
    else
        echo -e "${GREEN}  ✓ examples/ 目录存在${NC}"
        PASSED_CHECKS=$((PASSED_CHECKS + 1))
        
        # 检查示例数量
        example_count=$(find "$skill_path/examples" -type d -mindepth 1 -maxdepth 1 | wc -l)
        if [ "$example_count" -eq 0 ]; then
            echo -e "${YELLOW}  ⚠ examples/ 目录为空，建议添加代码示例${NC}"
            WARNINGS+=("$skill_name: examples/ 目录为空")
            WARNING_CHECKS=$((WARNING_CHECKS + 1))
            skill_warnings=$((skill_warnings + 1))
        else
            echo -e "${GREEN}  ✓ 包含 $example_count 个示例${NC}"
        fi
    fi
    
    # 6. 检查 Markdown 文件格式
    for md_file in "$skill_path"/*.md "$skill_path"/prompts/*.md; do
        [ ! -f "$md_file" ] && continue
        
        TOTAL_CHECKS=$((TOTAL_CHECKS + 1))
        
        # 检查是否有标题
        if ! grep -q "^#" "$md_file"; then
            echo -e "${YELLOW}  ⚠ $(basename "$md_file") 缺少标题${NC}"
            WARNINGS+=("$skill_name: $(basename "$md_file") 缺少标题")
            WARNING_CHECKS=$((WARNING_CHECKS + 1))
            skill_warnings=$((skill_warnings + 1))
        else
            PASSED_CHECKS=$((PASSED_CHECKS + 1))
        fi
    done
    
    # 输出 skill 检查结果
    echo ""
    if [ $skill_errors -eq 0 ] && [ $skill_warnings -eq 0 ]; then
        echo -e "${GREEN}  ✓ $skill_name 质量检查通过${NC}"
    elif [ $skill_errors -eq 0 ]; then
        echo -e "${YELLOW}  ⚠ $skill_name 有 $skill_warnings 个警告${NC}"
    else
        echo -e "${RED}  ✗ $skill_name 有 $skill_errors 个错误和 $skill_warnings 个警告${NC}"
    fi
    echo ""
}

# 遍历检查
if [ -f "$CHECK_PATH/SKILL.md" ]; then
    # 检查单个 skill
    check_skill "$CHECK_PATH"
elif [ -d "$CHECK_PATH" ]; then
    # 检查目录下所有 skills
    for skill_dir in "$CHECK_PATH"/*/*; do
        [ ! -d "$skill_dir" ] && continue
        [[ "$(basename "$skill_dir")" == "_"* ]] && continue
        
        check_skill "$skill_dir"
    done
else
    echo -e "${RED}错误: 路径不存在: $CHECK_PATH${NC}"
    exit 1
fi

# 输出统计信息
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${CYAN}质量检查统计${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "  总检查项: ${BLUE}$TOTAL_CHECKS${NC}"
echo -e "  通过: ${GREEN}$PASSED_CHECKS${NC}"
echo -e "  失败: ${RED}$FAILED_CHECKS${NC}"
echo -e "  警告: ${YELLOW}$WARNING_CHECKS${NC}"
echo ""

# 计算通过率
if [ $TOTAL_CHECKS -gt 0 ]; then
    PASS_RATE=$((PASSED_CHECKS * 100 / TOTAL_CHECKS))
    echo -e "  通过率: ${BLUE}${PASS_RATE}%${NC}"
    echo ""
fi

# 输出错误列表
if [ ${#ERRORS[@]} -gt 0 ]; then
    echo -e "${RED}错误列表:${NC}"
    for error in "${ERRORS[@]}"; do
        echo -e "  ${RED}✗${NC} $error"
    done
    echo ""
fi

# 输出警告列表
if [ ${#WARNINGS[@]} -gt 0 ]; then
    echo -e "${YELLOW}警告列表:${NC}"
    for warning in "${WARNINGS[@]}"; do
        echo -e "  ${YELLOW}⚠${NC} $warning"
    done
    echo ""
fi

# 建议
if [ $FAILED_CHECKS -gt 0 ] || [ $WARNING_CHECKS -gt 0 ]; then
    echo -e "${YELLOW}改进建议:${NC}"
    if [ $FAILED_CHECKS -gt 0 ]; then
        echo "  1. 修复所有错误项（必需）"
    fi
    if [ $WARNING_CHECKS -gt 0 ]; then
        echo "  2. 处理警告项以提高质量（推荐）"
    fi
    echo "  3. 参考 CONTRIBUTING.md 了解规范"
    echo "  4. 使用 skill-generator.sh 创建新 skill"
    echo ""
fi

# 生成报告
REPORT_FILE=".kiro/quality-report-$(date +%Y%m%d-%H%M%S).txt"
mkdir -p .kiro
{
    echo "Skills 质量检查报告"
    echo "生成时间: $(date)"
    echo "检查路径: $CHECK_PATH"
    echo ""
    echo "统计信息:"
    echo "  总检查项: $TOTAL_CHECKS"
    echo "  通过: $PASSED_CHECKS"
    echo "  失败: $FAILED_CHECKS"
    echo "  警告: $WARNING_CHECKS"
    echo "  通过率: ${PASS_RATE}%"
    echo ""
    if [ ${#ERRORS[@]} -gt 0 ]; then
        echo "错误列表:"
        for error in "${ERRORS[@]}"; do
            echo "  - $error"
        done
        echo ""
    fi
    if [ ${#WARNINGS[@]} -gt 0 ]; then
        echo "警告列表:"
        for warning in "${WARNINGS[@]}"; do
            echo "  - $warning"
        done
    fi
} > "$REPORT_FILE"

echo -e "${BLUE}报告已保存到: $REPORT_FILE${NC}"
echo ""

# 退出码
if [ $FAILED_CHECKS -eq 0 ]; then
    if [ $WARNING_CHECKS -eq 0 ]; then
        echo -e "${GREEN}✓ 所有检查通过！${NC}"
        exit 0
    else
        echo -e "${YELLOW}⚠ 检查通过，但有 $WARNING_CHECKS 个警告${NC}"
        exit 0
    fi
else
    echo -e "${RED}✗ 发现 $FAILED_CHECKS 个错误${NC}"
    exit 1
fi
