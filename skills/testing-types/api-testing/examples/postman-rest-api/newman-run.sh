#!/bin/bash

# Newman Test Runner Script
# 用于运行 Postman 集合测试的自动化脚本

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 脚本目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COLLECTION_FILE="$SCRIPT_DIR/User-API-Tests.postman_collection.json"
ENVIRONMENT_FILE="$SCRIPT_DIR/API-Environment.postman_environment.json"
REPORT_DIR="$SCRIPT_DIR/reports"

# 打印带颜色的消息
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 检查 Newman 是否安装
check_newman() {
    if ! command -v newman &> /dev/null; then
        print_error "Newman 未安装"
        print_info "请运行: npm install -g newman"
        exit 1
    fi
    print_success "Newman 已安装: $(newman --version)"
}

# 检查 Newman HTML Reporter 是否安装
check_html_reporter() {
    if ! npm list -g newman-reporter-html &> /dev/null && ! npm list newman-reporter-html &> /dev/null; then
        print_warning "Newman HTML Reporter 未安装"
        print_info "安装中: npm install -g newman-reporter-html"
        npm install -g newman-reporter-html
    fi
}

# 创建报告目录
create_report_dir() {
    if [ ! -d "$REPORT_DIR" ]; then
        mkdir -p "$REPORT_DIR"
        print_info "创建报告目录: $REPORT_DIR"
    fi
}

# 运行测试
run_tests() {
    local env_option=""
    
    if [ -f "$ENVIRONMENT_FILE" ]; then
        env_option="-e $ENVIRONMENT_FILE"
    fi
    
    print_info "开始运行 API 测试..."
    print_info "集合文件: $COLLECTION_FILE"
    
    newman run "$COLLECTION_FILE" \
        $env_option \
        --reporters cli,html \
        --reporter-html-export "$REPORT_DIR/test-report-$(date +%Y%m%d-%H%M%S).html" \
        --color on \
        --delay-request 100 \
        --timeout-request 10000
    
    local exit_code=$?
    
    if [ $exit_code -eq 0 ]; then
        print_success "所有测试通过！"
        print_info "报告已生成: $REPORT_DIR"
    else
        print_error "测试失败，退出码: $exit_code"
        exit $exit_code
    fi
}

# 运行特定文件夹的测试
run_folder_tests() {
    local folder_name="$1"
    
    print_info "运行文件夹测试: $folder_name"
    
    newman run "$COLLECTION_FILE" \
        -e "$ENVIRONMENT_FILE" \
        --folder "$folder_name" \
        --reporters cli \
        --color on
}

# 显示帮助信息
show_help() {
    cat << EOF
用法: $0 [选项]

选项:
    -h, --help              显示帮助信息
    -f, --folder <name>     运行特定文件夹的测试
    -i, --iteration <n>     运行 n 次迭代
    -d, --delay <ms>        请求之间的延迟（毫秒）
    --no-color              禁用颜色输出
    --bail                  首次失败时停止

示例:
    $0                                  # 运行所有测试
    $0 -f "User Management"             # 运行用户管理测试
    $0 -i 3                             # 运行 3 次迭代
    $0 -d 500                           # 请求间延迟 500ms

EOF
}

# 主函数
main() {
    local folder=""
    local iterations=1
    local delay=100
    local bail_flag=""
    local color_flag="--color on"
    
    # 解析命令行参数
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                show_help
                exit 0
                ;;
            -f|--folder)
                folder="$2"
                shift 2
                ;;
            -i|--iteration)
                iterations="$2"
                shift 2
                ;;
            -d|--delay)
                delay="$2"
                shift 2
                ;;
            --no-color)
                color_flag=""
                shift
                ;;
            --bail)
                bail_flag="--bail"
                shift
                ;;
            *)
                print_error "未知选项: $1"
                show_help
                exit 1
                ;;
        esac
    done
    
    print_info "========================================="
    print_info "  Postman API 测试运行器"
    print_info "========================================="
    
    # 检查依赖
    check_newman
    check_html_reporter
    create_report_dir
    
    # 运行测试
    if [ -n "$folder" ]; then
        run_folder_tests "$folder"
    else
        run_tests
    fi
}

# 执行主函数
main "$@"
