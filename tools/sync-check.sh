#!/bin/bash

# Sync Check - 检查中英文版本是否同步
# Usage: ./sync-check.sh [directory]

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# 检查目录
CHECK_DIR="${1:-skills}"

echo -e "${BLUE}检查中英文版本同步状态...${NC}"
echo -e "${BLUE}检查目录: $CHECK_DIR${NC}"
echo ""

# 统计变量
TOTAL_SKILLS=0
SYNCED_SKILLS=0
UNSYNCED_SKILLS=0
MISSING_EN=0
MISSING_ZH=0

# 存储不同步的 skills
declare -a UNSYNCED_LIST

# 检查 testing-types
if [ -d "$CHECK_DIR/testing-types" ]; then
    echo -e "${YELLOW}检查测试类型 Skills...${NC}"
    
    for zh_skill in "$CHECK_DIR/testing-types"/*; do
        # 跳过非目录和特殊文件
        [ ! -d "$zh_skill" ] && continue
        [[ "$(basename "$zh_skill")" == "_"* ]] && continue
        [[ "$(basename "$zh_skill")" == *"-en" ]] && continue
        
        skill_name=$(basename "$zh_skill")
        en_skill="$CHECK_DIR/testing-types/${skill_name}-en"
        
        TOTAL_SKILLS=$((TOTAL_SKILLS + 1))
        
        # 检查英文版本是否存在
        if [ ! -d "$en_skill" ]; then
            echo -e "${RED}  ✗ $skill_name - 缺少英文版本${NC}"
            MISSING_EN=$((MISSING_EN + 1))
            UNSYNCED_SKILLS=$((UNSYNCED_SKILLS + 1))
            UNSYNCED_LIST+=("$skill_name (缺少英文版)")
            continue
        fi
        
        # 检查文件同步
        is_synced=true
        
        # 检查 SKILL.md
        if [ -f "$zh_skill/SKILL.md" ] && [ -f "$en_skill/SKILL.md" ]; then
            zh_version=$(grep "^version:" "$zh_skill/SKILL.md" | head -1 | awk '{print $2}')
            en_version=$(grep "^version:" "$en_skill/SKILL.md" | head -1 | awk '{print $2}')
            
            if [ "$zh_version" != "$en_version" ]; then
                echo -e "${YELLOW}  ⚠ $skill_name - 版本不一致 (中文: $zh_version, 英文: $en_version)${NC}"
                is_synced=false
            fi
            
            zh_updated=$(grep "^last-updated:" "$zh_skill/SKILL.md" | head -1 | awk '{print $2}')
            en_updated=$(grep "^last-updated:" "$en_skill/SKILL.md" | head -1 | awk '{print $2}')
            
            if [ "$zh_updated" != "$en_updated" ]; then
                echo -e "${YELLOW}  ⚠ $skill_name - 更新日期不一致 (中文: $zh_updated, 英文: $en_updated)${NC}"
                is_synced=false
            fi
        else
            echo -e "${RED}  ✗ $skill_name - SKILL.md 文件缺失${NC}"
            is_synced=false
        fi
        
        # 检查 prompts 目录
        if [ -d "$zh_skill/prompts" ] && [ -d "$en_skill/prompts" ]; then
            zh_prompts=$(find "$zh_skill/prompts" -name "*.md" ! -name "*_EN.md" | wc -l)
            en_prompts=$(find "$en_skill/prompts" -name "*.md" | wc -l)
            
            if [ "$zh_prompts" != "$en_prompts" ]; then
                echo -e "${YELLOW}  ⚠ $skill_name - 提示词文件数量不一致 (中文: $zh_prompts, 英文: $en_prompts)${NC}"
                is_synced=false
            fi
        fi
        
        # 检查 examples 目录
        if [ -d "$zh_skill/examples" ] && [ -d "$en_skill/examples" ]; then
            zh_examples=$(find "$zh_skill/examples" -type d -mindepth 1 -maxdepth 1 | wc -l)
            en_examples=$(find "$en_skill/examples" -type d -mindepth 1 -maxdepth 1 | wc -l)
            
            if [ "$zh_examples" != "$en_examples" ]; then
                echo -e "${YELLOW}  ⚠ $skill_name - 示例数量不一致 (中文: $zh_examples, 英文: $en_examples)${NC}"
                is_synced=false
            fi
        fi
        
        if [ "$is_synced" = true ]; then
            echo -e "${GREEN}  ✓ $skill_name - 已同步${NC}"
            SYNCED_SKILLS=$((SYNCED_SKILLS + 1))
        else
            UNSYNCED_SKILLS=$((UNSYNCED_SKILLS + 1))
            UNSYNCED_LIST+=("$skill_name")
        fi
    done
fi

# 检查 testing-workflows
if [ -d "$CHECK_DIR/testing-workflows" ]; then
    echo ""
    echo -e "${YELLOW}检查工作流 Skills...${NC}"
    
    for zh_skill in "$CHECK_DIR/testing-workflows"/*; do
        [ ! -d "$zh_skill" ] && continue
        [[ "$(basename "$zh_skill")" == *"-en" ]] && continue
        
        skill_name=$(basename "$zh_skill")
        en_skill="$CHECK_DIR/testing-workflows/${skill_name}-en"
        
        TOTAL_SKILLS=$((TOTAL_SKILLS + 1))
        
        if [ ! -d "$en_skill" ]; then
            echo -e "${RED}  ✗ $skill_name - 缺少英文版本${NC}"
            MISSING_EN=$((MISSING_EN + 1))
            UNSYNCED_SKILLS=$((UNSYNCED_SKILLS + 1))
            UNSYNCED_LIST+=("$skill_name (缺少英文版)")
            continue
        fi
        
        # 简化检查（工作流通常更新频繁）
        is_synced=true
        
        if [ -f "$zh_skill/SKILL.md" ] && [ -f "$en_skill/SKILL.md" ]; then
            zh_updated=$(grep "^last-updated:" "$zh_skill/SKILL.md" 2>/dev/null | head -1 | awk '{print $2}')
            en_updated=$(grep "^last-updated:" "$en_skill/SKILL.md" 2>/dev/null | head -1 | awk '{print $2}')
            
            if [ -n "$zh_updated" ] && [ -n "$en_updated" ] && [ "$zh_updated" != "$en_updated" ]; then
                echo -e "${YELLOW}  ⚠ $skill_name - 更新日期不一致${NC}"
                is_synced=false
            fi
        fi
        
        if [ "$is_synced" = true ]; then
            echo -e "${GREEN}  ✓ $skill_name - 已同步${NC}"
            SYNCED_SKILLS=$((SYNCED_SKILLS + 1))
        else
            UNSYNCED_SKILLS=$((UNSYNCED_SKILLS + 1))
            UNSYNCED_LIST+=("$skill_name")
        fi
    done
fi

# 输出统计信息
echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}同步状态统计${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "  总 Skills 数: ${BLUE}$TOTAL_SKILLS${NC}"
echo -e "  已同步: ${GREEN}$SYNCED_SKILLS${NC}"
echo -e "  未同步: ${YELLOW}$UNSYNCED_SKILLS${NC}"
echo -e "  缺少英文版: ${RED}$MISSING_EN${NC}"
echo ""

# 计算同步率
if [ $TOTAL_SKILLS -gt 0 ]; then
    SYNC_RATE=$((SYNCED_SKILLS * 100 / TOTAL_SKILLS))
    echo -e "  同步率: ${BLUE}${SYNC_RATE}%${NC}"
    echo ""
fi

# 输出不同步列表
if [ ${#UNSYNCED_LIST[@]} -gt 0 ]; then
    echo -e "${YELLOW}需要同步的 Skills:${NC}"
    for skill in "${UNSYNCED_LIST[@]}"; do
        echo -e "  - $skill"
    done
    echo ""
fi

# 建议
if [ $UNSYNCED_SKILLS -gt 0 ]; then
    echo -e "${YELLOW}建议操作:${NC}"
    echo "  1. 检查不同步的 skills，更新版本号和日期"
    echo "  2. 确保中英文内容保持一致"
    echo "  3. 运行 git diff 查看具体差异"
    echo "  4. 更新后重新运行此脚本验证"
    echo ""
fi

# 生成报告文件
REPORT_FILE=".kiro/sync-report-$(date +%Y%m%d-%H%M%S).txt"
mkdir -p .kiro
{
    echo "中英文同步检查报告"
    echo "生成时间: $(date)"
    echo ""
    echo "统计信息:"
    echo "  总 Skills 数: $TOTAL_SKILLS"
    echo "  已同步: $SYNCED_SKILLS"
    echo "  未同步: $UNSYNCED_SKILLS"
    echo "  缺少英文版: $MISSING_EN"
    echo "  同步率: ${SYNC_RATE}%"
    echo ""
    if [ ${#UNSYNCED_LIST[@]} -gt 0 ]; then
        echo "需要同步的 Skills:"
        for skill in "${UNSYNCED_LIST[@]}"; do
            echo "  - $skill"
        done
    fi
} > "$REPORT_FILE"

echo -e "${BLUE}报告已保存到: $REPORT_FILE${NC}"
echo ""

# 退出码
if [ $UNSYNCED_SKILLS -eq 0 ]; then
    echo -e "${GREEN}✓ 所有 Skills 已同步！${NC}"
    exit 0
else
    echo -e "${YELLOW}⚠ 发现 $UNSYNCED_SKILLS 个未同步的 Skills${NC}"
    exit 1
fi
