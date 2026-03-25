#!/bin/bash

# K6 性能测试运行脚本

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# 脚本目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS_DIR="$SCRIPT_DIR/scripts"
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

# 检查 K6 是否安装
check_k6() {
    if ! command -v k6 &> /dev/null; then
        print_error "K6 未安装"
        print_info "请访问 https://k6.io/docs/getting-started/installation/ 安装 K6"
        exit 1
    fi
    print_success "K6 已安装: $(k6 version)"
}

# 创建报告目录
create_report_dir() {
    if [ ! -d "$REPORTS_DIR" ]; then
        mkdir -p "$REPORTS_DIR"
        print_info "创建报告目录: $REPORTS_DIR"
    fi
}

# 运行负载测试
run_load_test() {
    print_info "========================================="
    print_info "  运行负载测试 (Load Test)"
    print_info "========================================="
    
    k6 run \
        --out json="$REPORTS_DIR/load-test-$(date +%Y%m%d-%H%M%S).json" \
        "$SCRIPTS_DIR/load-test.js"
    
    print_success "负载测试完成！"
}

# 运行压力测试
run_stress_test() {
    print_info "========================================="
    print_info "  运行压力测试 (Stress Test)"
    print_info "========================================="
    
    k6 run \
        --out json="$REPORTS_DIR/stress-test-$(date +%Y%m%d-%H%M%S).json" \
        "$SCRIPTS_DIR/stress-test.js"
    
    print_success "压力测试完成！"
}

# 运行尖峰测试
run_spike_test() {
    print_info "========================================="
    print_info "  运行尖峰测试 (Spike Test)"
    print_info "========================================="
    
    k6 run \
        --out json="$REPORTS_DIR/spike-test-$(date +%Y%m%d-%H%M%S).json" \
        "$SCRIPTS_DIR/spike-test.js"
    
    print_success "尖峰测试完成！"
}

# 运行 API 测试
run_api_test() {
    print_info "========================================="
    print_info "  运行 API 性能测试"
    print_info "========================================="
    
    k6 run \
        --out json="$REPORTS_DIR/api-test-$(date +%Y%m%d-%H%M%S).json" \
        "$SCRIPTS_DIR/api-test.js"
    
    print_success "API 测试完成！"
}

# 运行所有测试
run_all_tests() {
    print_info "========================================="
    print_info "  运行所有性能测试"
    print_info "========================================="
    
    run_load_test
    sleep 5
    
    run_api_test
    sleep 5
    
    print_warning "跳过压力测试和尖峰测试（耗时较长）"
    print_info "如需运行，请使用: ./run-tests.sh stress 或 ./run-tests.sh spike"
    
    print_success "所有测试完成！"
}

# 显示帮助信息
show_help() {
    cat << EOF
用法: $0 [测试类型]

测试类型:
    load        运行负载测试
    stress      运行压力测试
    spike       运行尖峰测试
    api         运行 API 性能测试
    all         运行所有测试（不包括压力和尖峰测试）
    help        显示帮助信息

示例:
    $0 load         # 运行负载测试
    $0 api          # 运行 API 测试
    $0 all          # 运行所有测试

环境变量:
    BASE_URL        目标 URL（默认: https://test.k6.io）
    VUS             虚拟用户数（覆盖脚本中的配置）
    DURATION        测试持续时间（覆盖脚本中的配置）

示例:
    BASE_URL=https://example.com $0 load
    VUS=100 DURATION=10m $0 api

EOF
}

# 主函数
main() {
    local test_type="${1:-help}"
    
    if [ "$test_type" = "help" ] || [ "$test_type" = "-h" ] || [ "$test_type" = "--help" ]; then
        show_help
        exit 0
    fi
    
    print_info "========================================="
    print_info "  K6 性能测试运行器"
    print_info "========================================="
    
    # 检查依赖
    check_k6
    create_report_dir
    
    # 运行测试
    case "$test_type" in
        load)
            run_load_test
            ;;
        stress)
            run_stress_test
            ;;
        spike)
            run_spike_test
            ;;
        api)
            run_api_test
            ;;
        all)
            run_all_tests
            ;;
        *)
            print_error "未知的测试类型: $test_type"
            show_help
            exit 1
            ;;
    esac
    
    print_info "报告已保存到: $REPORTS_DIR"
}

# 执行主函数
main "$@"
