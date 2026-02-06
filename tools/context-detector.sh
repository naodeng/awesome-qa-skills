#!/bin/bash

# Context Detector - 检测项目上下文（类型、技术栈、测试框架）
# Usage: ./context-detector.sh [project-path]

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# 项目路径
PROJECT_PATH="${1:-.}"

# 检查项目路径是否存在
if [ ! -d "$PROJECT_PATH" ]; then
    echo -e "${RED}错误: 项目路径不存在: $PROJECT_PATH${NC}"
    exit 1
fi

echo -e "${BLUE}检测项目上下文...${NC}"
echo -e "${BLUE}项目路径: $PROJECT_PATH${NC}"
echo ""

# 初始化结果
PROJECT_TYPE=""
FRAMEWORKS=()
TEST_FRAMEWORKS=()
LANGUAGES=()

# 检测项目类型
detect_project_type() {
    if [ -f "$PROJECT_PATH/package.json" ] || [ -f "$PROJECT_PATH/index.html" ]; then
        if [ -d "$PROJECT_PATH/android" ] || [ -d "$PROJECT_PATH/ios" ]; then
            PROJECT_TYPE="mobile"
        else
            PROJECT_TYPE="web"
        fi
    elif [ -f "$PROJECT_PATH/pubspec.yaml" ]; then
        PROJECT_TYPE="mobile"
    elif [ -f "$PROJECT_PATH/pom.xml" ] || [ -f "$PROJECT_PATH/build.gradle" ]; then
        if [ -d "$PROJECT_PATH/src/main/webapp" ]; then
            PROJECT_TYPE="web"
        else
            PROJECT_TYPE="api"
        fi
    elif [ -f "$PROJECT_PATH/requirements.txt" ] || [ -f "$PROJECT_PATH/setup.py" ]; then
        if [ -d "$PROJECT_PATH/templates" ] || [ -d "$PROJECT_PATH/static" ]; then
            PROJECT_TYPE="web"
        else
            PROJECT_TYPE="api"
        fi
    elif [ -f "$PROJECT_PATH/go.mod" ]; then
        PROJECT_TYPE="api"
    elif [ -f "$PROJECT_PATH/Cargo.toml" ]; then
        PROJECT_TYPE="api"
    else
        PROJECT_TYPE="unknown"
    fi
}

# 检测前端框架
detect_frontend_frameworks() {
    if [ -f "$PROJECT_PATH/package.json" ]; then
        local pkg_content=$(cat "$PROJECT_PATH/package.json")
        
        if echo "$pkg_content" | grep -q '"react"'; then
            FRAMEWORKS+=("react")
        fi
        
        if echo "$pkg_content" | grep -q '"vue"'; then
            FRAMEWORKS+=("vue")
        fi
        
        if echo "$pkg_content" | grep -q '"@angular/core"'; then
            FRAMEWORKS+=("angular")
        fi
        
        if echo "$pkg_content" | grep -q '"next"'; then
            FRAMEWORKS+=("nextjs")
        fi
        
        if echo "$pkg_content" | grep -q '"nuxt"'; then
            FRAMEWORKS+=("nuxtjs")
        fi
        
        if echo "$pkg_content" | grep -q '"svelte"'; then
            FRAMEWORKS+=("svelte")
        fi
        
        if echo "$pkg_content" | grep -q '"react-native"'; then
            FRAMEWORKS+=("react-native")
        fi
    fi
    
    if [ -f "$PROJECT_PATH/pubspec.yaml" ]; then
        if grep -q "flutter:" "$PROJECT_PATH/pubspec.yaml"; then
            FRAMEWORKS+=("flutter")
        fi
    fi
}

# 检测后端框架
detect_backend_frameworks() {
    if [ -f "$PROJECT_PATH/package.json" ]; then
        local pkg_content=$(cat "$PROJECT_PATH/package.json")
        
        if echo "$pkg_content" | grep -q '"express"'; then
            FRAMEWORKS+=("express")
        fi
        
        if echo "$pkg_content" | grep -q '"koa"'; then
            FRAMEWORKS+=("koa")
        fi
        
        if echo "$pkg_content" | grep -q '"nestjs"'; then
            FRAMEWORKS+=("nestjs")
        fi
    fi
    
    if [ -f "$PROJECT_PATH/requirements.txt" ]; then
        if grep -q "django" "$PROJECT_PATH/requirements.txt"; then
            FRAMEWORKS+=("django")
        fi
        
        if grep -q "flask" "$PROJECT_PATH/requirements.txt"; then
            FRAMEWORKS+=("flask")
        fi
        
        if grep -q "fastapi" "$PROJECT_PATH/requirements.txt"; then
            FRAMEWORKS+=("fastapi")
        fi
    fi
    
    if [ -f "$PROJECT_PATH/pom.xml" ]; then
        if grep -q "spring-boot" "$PROJECT_PATH/pom.xml"; then
            FRAMEWORKS+=("spring-boot")
        fi
    fi
    
    if [ -f "$PROJECT_PATH/go.mod" ]; then
        if grep -q "gin-gonic/gin" "$PROJECT_PATH/go.mod"; then
            FRAMEWORKS+=("gin")
        fi
        
        if grep -q "echo" "$PROJECT_PATH/go.mod"; then
            FRAMEWORKS+=("echo")
        fi
    fi
}

# 检测测试框架
detect_test_frameworks() {
    # JavaScript/TypeScript
    if [ -f "$PROJECT_PATH/package.json" ]; then
        local pkg_content=$(cat "$PROJECT_PATH/package.json")
        
        if echo "$pkg_content" | grep -q '"jest"'; then
            TEST_FRAMEWORKS+=("jest")
        fi
        
        if echo "$pkg_content" | grep -q '"vitest"'; then
            TEST_FRAMEWORKS+=("vitest")
        fi
        
        if echo "$pkg_content" | grep -q '"mocha"'; then
            TEST_FRAMEWORKS+=("mocha")
        fi
        
        if echo "$pkg_content" | grep -q '"playwright"'; then
            TEST_FRAMEWORKS+=("playwright")
        fi
        
        if echo "$pkg_content" | grep -q '"cypress"'; then
            TEST_FRAMEWORKS+=("cypress")
        fi
        
        if echo "$pkg_content" | grep -q '"@testing-library"'; then
            TEST_FRAMEWORKS+=("testing-library")
        fi
    fi
    
    # Python
    if [ -f "$PROJECT_PATH/requirements.txt" ] || [ -f "$PROJECT_PATH/requirements-dev.txt" ]; then
        if grep -q "pytest" "$PROJECT_PATH/requirements.txt" "$PROJECT_PATH/requirements-dev.txt" 2>/dev/null; then
            TEST_FRAMEWORKS+=("pytest")
        fi
        
        if grep -q "unittest" "$PROJECT_PATH/requirements.txt" "$PROJECT_PATH/requirements-dev.txt" 2>/dev/null; then
            TEST_FRAMEWORKS+=("unittest")
        fi
        
        if grep -q "behave" "$PROJECT_PATH/requirements.txt" "$PROJECT_PATH/requirements-dev.txt" 2>/dev/null; then
            TEST_FRAMEWORKS+=("behave")
        fi
    fi
    
    # Java
    if [ -f "$PROJECT_PATH/pom.xml" ]; then
        if grep -q "junit" "$PROJECT_PATH/pom.xml"; then
            TEST_FRAMEWORKS+=("junit")
        fi
        
        if grep -q "testng" "$PROJECT_PATH/pom.xml"; then
            TEST_FRAMEWORKS+=("testng")
        fi
        
        if grep -q "cucumber" "$PROJECT_PATH/pom.xml"; then
            TEST_FRAMEWORKS+=("cucumber")
        fi
    fi
    
    # Go
    if [ -f "$PROJECT_PATH/go.mod" ]; then
        if grep -q "testify" "$PROJECT_PATH/go.mod"; then
            TEST_FRAMEWORKS+=("testify")
        fi
    fi
}

# 检测编程语言
detect_languages() {
    if [ -f "$PROJECT_PATH/package.json" ]; then
        LANGUAGES+=("javascript")
        if [ -f "$PROJECT_PATH/tsconfig.json" ]; then
            LANGUAGES+=("typescript")
        fi
    fi
    
    if [ -f "$PROJECT_PATH/requirements.txt" ] || [ -f "$PROJECT_PATH/setup.py" ]; then
        LANGUAGES+=("python")
    fi
    
    if [ -f "$PROJECT_PATH/pom.xml" ] || [ -f "$PROJECT_PATH/build.gradle" ]; then
        LANGUAGES+=("java")
    fi
    
    if [ -f "$PROJECT_PATH/go.mod" ]; then
        LANGUAGES+=("go")
    fi
    
    if [ -f "$PROJECT_PATH/Cargo.toml" ]; then
        LANGUAGES+=("rust")
    fi
    
    if [ -f "$PROJECT_PATH/pubspec.yaml" ]; then
        LANGUAGES+=("dart")
    fi
}

# 执行检测
detect_project_type
detect_frontend_frameworks
detect_backend_frameworks
detect_test_frameworks
detect_languages

# 输出结果（JSON 格式）
echo -e "${GREEN}检测完成！${NC}"
echo ""
echo "{"
echo "  \"project_type\": \"$PROJECT_TYPE\","
echo "  \"languages\": ["
for i in "${!LANGUAGES[@]}"; do
    if [ $i -eq $((${#LANGUAGES[@]} - 1)) ]; then
        echo "    \"${LANGUAGES[$i]}\""
    else
        echo "    \"${LANGUAGES[$i]}\","
    fi
done
echo "  ],"
echo "  \"frameworks\": ["
for i in "${!FRAMEWORKS[@]}"; do
    if [ $i -eq $((${#FRAMEWORKS[@]} - 1)) ]; then
        echo "    \"${FRAMEWORKS[$i]}\""
    else
        echo "    \"${FRAMEWORKS[$i]}\","
    fi
done
echo "  ],"
echo "  \"test_frameworks\": ["
for i in "${!TEST_FRAMEWORKS[@]}"; do
    if [ $i -eq $((${#TEST_FRAMEWORKS[@]} - 1)) ]; then
        echo "    \"${TEST_FRAMEWORKS[$i]}\""
    else
        echo "    \"${TEST_FRAMEWORKS[$i]}\","
    fi
done
echo "  ]"
echo "}"

# 保存到缓存文件
CACHE_FILE="$PROJECT_PATH/.kiro/context-cache.json"
mkdir -p "$PROJECT_PATH/.kiro"
cat > "$CACHE_FILE" << EOF
{
  "project_type": "$PROJECT_TYPE",
  "languages": [$(IFS=,; echo "\"${LANGUAGES[*]//,/\",\"}\"")],
  "frameworks": [$(IFS=,; echo "\"${FRAMEWORKS[*]//,/\",\"}\"")],
  "test_frameworks": [$(IFS=,; echo "\"${TEST_FRAMEWORKS[*]//,/\",\"}\"")],
  "detected_at": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
}
EOF

echo ""
echo -e "${BLUE}上下文已缓存到: $CACHE_FILE${NC}"
echo ""
echo -e "${YELLOW}推荐的 Skills:${NC}"

# 根据检测结果推荐 skills
if [ "$PROJECT_TYPE" = "web" ]; then
    echo "  - functional-testing (Web 功能测试)"
    echo "  - automation-testing (自动化测试)"
    if [[ " ${TEST_FRAMEWORKS[@]} " =~ " playwright " ]]; then
        echo "  - 使用 Playwright 示例"
    elif [[ " ${TEST_FRAMEWORKS[@]} " =~ " cypress " ]]; then
        echo "  - 使用 Cypress 示例"
    fi
fi

if [ "$PROJECT_TYPE" = "api" ]; then
    echo "  - api-testing (API 测试)"
    echo "  - automation-testing (自动化测试)"
    echo "  - performance-testing (性能测试)"
fi

if [ "$PROJECT_TYPE" = "mobile" ]; then
    echo "  - mobile-testing (移动端测试)"
    echo "  - functional-testing (功能测试)"
    if [[ " ${FRAMEWORKS[@]} " =~ " flutter " ]]; then
        echo "  - 使用 Flutter 测试框架"
    elif [[ " ${FRAMEWORKS[@]} " =~ " react-native " ]]; then
        echo "  - 使用 Detox 或 Appium"
    fi
fi

echo ""
