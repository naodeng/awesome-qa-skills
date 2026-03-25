#!/bin/bash

# OWASP ZAP 安全扫描运行脚本

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# 脚本目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPORTS_DIR="$SCRIPT_DIR/reports"

# 打印函数
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

# 检查 Docker 是否安装
check_docker() {
    if ! command -v docker &> /dev/null; then
        print_error "Docker 未安装"
        print_info "请访问 https://docs.docker.com/get-docker/ 安装 Docker"
        exit 1
    fi
    print_success "Docker 已安装"
}

# 创建报告目录
create_report_dir() {
    if [ ! -d "$REPORTS_DIR" ]; then
        mkdir -p "$REPORTS_DIR"
        print_info "创建报告目录: $REPORTS_DIR"
    fi
}

# 拉取 ZAP Docker 镜像
pull_zap_image() {
    print_info "拉取 OWASP ZAP Docker 镜像..."
    docker pull owasp/zap2docker-stable
    print_success "镜像拉取完成"
}

# 运行基线扫描
run_baseline_scan() {
    local target_url="$1"
    local timestamp=$(date +%Y%m%d-%H%M%S)
    
    print_info "========================================="
    print_info "  运行基线扫描 (Baseline Scan)"
    print_info "========================================="
    print_info "目标 URL: $target_url"
    
    docker run -u $(id -u):$(id -g) \
        -v "$SCRIPT_DIR:/zap/wrk/:rw" \
        -t owasp/zap2docker-stable \
        zap-baseline.py \
        -t "$target_url" \
        -r "reports/baseline-scan-$timestamp.html" \
        -J "reports/baseline-scan-$timestamp.json" \
        -w "reports/baseline-scan-$timestamp.md"
    
    print_success "基线扫描完成！"
    print_info "报告位置: $REPORTS_DIR/baseline-scan-$timestamp.html"
}

# 运行完整扫描
run_full_scan() {
    local target_url="$1"
    local timestamp=$(date +%Y%m%d-%H%M%S)
    
    print_info "========================================="
    print_info "  运行完整扫描 (Full Scan)"
    print_info "========================================="
    print_warning "完整扫描包含主动攻击，请确保有权限测试目标系统"
    print_info "目标 URL: $target_url"
    
    docker run -u $(id -u):$(id -g) \
        -v "$SCRIPT_DIR:/zap/wrk/:rw" \
        -t owasp/zap2docker-stable \
        zap-full-scan.py \
        -t "$target_url" \
        -r "reports/full-scan-$timestamp.html" \
        -J "reports/full-scan-$timestamp.json"
    
    print_success "完整扫描完成！"
    print_info "报告位置: $REPORTS_DIR/full-scan-$timestamp.html"
}

# 运行 API 扫描
run_api_scan() {
    local api_definition="$1"
    local target_url="$2"
    local timestamp=$(date +%Y%m%d-%H%M%S)
    
    print_info "========================================="
    print_info "  运行 API 扫描 (API Scan)"
    print_info "========================================="
    print_info "API 定义: $api_definition"
    print_info "目标 URL: $target_url"
    
    docker run -u $(id -u):$(id -g) \
        -v "$SCRIPT_DIR:/zap/wrk/:rw" \
        -t owasp/zap2docker-stable \
        zap-api-scan.py \
        -t "$api_definition" \
        -f openapi \
        -r "reports/api-scan-$timestamp.html" \
        -J "reports/api-scan-$timestamp.json"
    
    print_success "API 扫描完成！"
    print_info "报告位置: $REPORTS_DIR/api-scan-$timestamp.html"
}

# 显示帮助信息
show_help() {
    cat << EOF
用法: $0 [扫描类型] [目标]

扫描类型:
    baseline <url>              运行基线扫描
    full <url>                  运行完整扫描（包含主动攻击）
    api <definition> <url>      运行 API 扫描
    help                        显示帮助信息

示例:
    $0 baseline https://example.com
    $0 full https://example.com
    $0 api swagger.json https://api.example.com

注意:
    - 基线扫描：快速扫描，适合 CI/CD
    - 完整扫描：深度扫描，包含主动攻击，需要授权
    - API 扫描：针对 REST API 的安全测试

EOF
}

# 主函数
main() {
    local scan_type="${1:-help}"
    
    if [ "$scan_type" = "help" ] || [ "$scan_type" = "-h" ] || [ "$scan_type" = "--help" ]; then
        show_help
        exit 0
    fi
    
    print_info "========================================="
    print_info "  OWASP ZAP 安全扫描工具"
    print_info "========================================="
    
    # 检查依赖
    check_docker
    create_report_dir
    pull_zap_image
    
    # 运行扫描
    case "$scan_type" in
        baseline)
            if [ -z "$2" ]; then
                print_error "请提供目标 URL"
                show_help
                exit 1
            fi
            run_baseline_scan "$2"
            ;;
        full)
            if [ -z "$2" ]; then
                print_error "请提供目标 URL"
                show_help
                exit 1
            fi
            run_full_scan "$2"
            ;;
        api)
            if [ -z "$2" ] || [ -z "$3" ]; then
                print_error "请提供 API 定义文件和目标 URL"
                show_help
                exit 1
            fi
            run_api_scan "$2" "$3"
            ;;
        *)
            print_error "未知的扫描类型: $scan_type"
            show_help
            exit 1
            ;;
    esac
    
    print_info "所有报告已保存到: $REPORTS_DIR"
}

# 执行主函数
main "$@"
