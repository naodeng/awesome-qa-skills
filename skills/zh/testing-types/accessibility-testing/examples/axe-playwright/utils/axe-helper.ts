import { Page } from '@playwright/test';
import * as fs from 'fs';
import * as path from 'path';

/**
 * axe-core 辅助函数
 * 提供违规报告保存、打印等功能
 */

/**
 * 违规项接口
 */
export interface AxeViolation {
  id: string;
  impact: 'minor' | 'moderate' | 'serious' | 'critical';
  description: string;
  help: string;
  helpUrl: string;
  tags: string[];
  nodes: Array<{
    html: string;
    target: string[];
    failureSummary: string;
  }>;
}

/**
 * 保存违规项到文件
 * 
 * @param page - Playwright Page 对象
 * @param violations - 违规项数组
 * @param filename - 文件名（不含扩展名）
 */
export async function saveViolations(
  page: Page,
  violations: AxeViolation[],
  filename: string
): Promise<void> {
  // 创建报告目录
  const reportDir = path.join(process.cwd(), 'a11y-reports');
  if (!fs.existsSync(reportDir)) {
    fs.mkdirSync(reportDir, { recursive: true });
  }

  // 保存 JSON 报告
  const jsonPath = path.join(reportDir, `${filename}.json`);
  fs.writeFileSync(jsonPath, JSON.stringify(violations, null, 2));
  console.log(`📄 违规报告已保存: ${jsonPath}`);

  // 保存截图
  const screenshotPath = path.join(reportDir, `${filename}.png`);
  await page.screenshot({ path: screenshotPath, fullPage: true });
  console.log(`📸 截图已保存: ${screenshotPath}`);

  // 生成 HTML 报告
  const htmlPath = path.join(reportDir, `${filename}.html`);
  const html = generateHtmlReport(violations, filename);
  fs.writeFileSync(htmlPath, html);
  console.log(`📊 HTML 报告已保存: ${htmlPath}`);
}

/**
 * 打印违规项摘要到控制台
 * 
 * @param violations - 违规项数组
 */
export function printViolationsSummary(violations: AxeViolation[]): void {
  console.log('\n❌ 发现可访问性违规项:\n');
  console.log(`总计: ${violations.length} 个违规项\n`);

  // 按影响级别分组
  const byImpact = violations.reduce((acc, v) => {
    acc[v.impact] = (acc[v.impact] || 0) + 1;
    return acc;
  }, {} as Record<string, number>);

  console.log('按影响级别统计:');
  if (byImpact.critical) console.log(`  🔴 Critical: ${byImpact.critical}`);
  if (byImpact.serious) console.log(`  🟠 Serious: ${byImpact.serious}`);
  if (byImpact.moderate) console.log(`  🟡 Moderate: ${byImpact.moderate}`);
  if (byImpact.minor) console.log(`  🟢 Minor: ${byImpact.minor}`);

  console.log('\n详细信息:\n');

  violations.forEach((violation, index) => {
    const impactIcon = getImpactIcon(violation.impact);
    console.log(`${index + 1}. ${impactIcon} ${violation.id}`);
    console.log(`   描述: ${violation.description}`);
    console.log(`   影响: ${violation.impact}`);
    console.log(`   帮助: ${violation.helpUrl}`);
    console.log(`   受影响元素: ${violation.nodes.length} 个`);
    
    // 打印前 3 个受影响的元素
    violation.nodes.slice(0, 3).forEach((node, nodeIndex) => {
      console.log(`   ${nodeIndex + 1}) ${node.html.substring(0, 80)}...`);
      console.log(`      ${node.failureSummary}`);
    });
    
    if (violation.nodes.length > 3) {
      console.log(`   ... 还有 ${violation.nodes.length - 3} 个元素`);
    }
    console.log('');
  });
}

/**
 * 获取影响级别图标
 */
function getImpactIcon(impact: string): string {
  const icons: Record<string, string> = {
    critical: '🔴',
    serious: '🟠',
    moderate: '🟡',
    minor: '🟢',
  };
  return icons[impact] || '⚪';
}

/**
 * 生成 HTML 报告
 */
function generateHtmlReport(violations: AxeViolation[], title: string): string {
  const violationsByImpact = violations.reduce((acc, v) => {
    if (!acc[v.impact]) acc[v.impact] = [];
    acc[v.impact].push(v);
    return acc;
  }, {} as Record<string, AxeViolation[]>);

  const impactColors: Record<string, string> = {
    critical: '#dc2626',
    serious: '#ea580c',
    moderate: '#ca8a04',
    minor: '#16a34a',
  };

  return `
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>可访问性测试报告 - ${title}</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      line-height: 1.6;
      color: #1f2937;
      background: #f9fafb;
      padding: 2rem;
    }
    .container {
      max-width: 1200px;
      margin: 0 auto;
      background: white;
      border-radius: 8px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
      padding: 2rem;
    }
    h1 {
      font-size: 2rem;
      margin-bottom: 0.5rem;
      color: #111827;
    }
    .meta {
      color: #6b7280;
      margin-bottom: 2rem;
    }
    .summary {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem;
      margin-bottom: 2rem;
    }
    .summary-card {
      padding: 1.5rem;
      border-radius: 8px;
      border-left: 4px solid;
    }
    .summary-card.critical { border-color: #dc2626; background: #fef2f2; }
    .summary-card.serious { border-color: #ea580c; background: #fff7ed; }
    .summary-card.moderate { border-color: #ca8a04; background: #fefce8; }
    .summary-card.minor { border-color: #16a34a; background: #f0fdf4; }
    .summary-card h3 {
      font-size: 0.875rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.5rem;
      opacity: 0.8;
    }
    .summary-card .count {
      font-size: 2rem;
      font-weight: bold;
    }
    .violation {
      border: 1px solid #e5e7eb;
      border-radius: 8px;
      padding: 1.5rem;
      margin-bottom: 1.5rem;
    }
    .violation-header {
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-bottom: 1rem;
    }
    .impact-badge {
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 600;
      text-transform: uppercase;
      color: white;
    }
    .impact-badge.critical { background: #dc2626; }
    .impact-badge.serious { background: #ea580c; }
    .impact-badge.moderate { background: #ca8a04; }
    .impact-badge.minor { background: #16a34a; }
    .violation-title {
      font-size: 1.25rem;
      font-weight: 600;
      flex: 1;
    }
    .violation-description {
      color: #4b5563;
      margin-bottom: 1rem;
    }
    .violation-help {
      background: #f3f4f6;
      padding: 1rem;
      border-radius: 4px;
      margin-bottom: 1rem;
    }
    .violation-help a {
      color: #2563eb;
      text-decoration: none;
    }
    .violation-help a:hover {
      text-decoration: underline;
    }
    .nodes {
      margin-top: 1rem;
    }
    .node {
      background: #f9fafb;
      border-left: 3px solid #d1d5db;
      padding: 1rem;
      margin-bottom: 0.5rem;
      border-radius: 4px;
    }
    .node-html {
      font-family: 'Courier New', monospace;
      font-size: 0.875rem;
      background: #1f2937;
      color: #f9fafb;
      padding: 0.75rem;
      border-radius: 4px;
      overflow-x: auto;
      margin-bottom: 0.5rem;
    }
    .node-summary {
      color: #6b7280;
      font-size: 0.875rem;
    }
    .tags {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-top: 1rem;
    }
    .tag {
      background: #e5e7eb;
      padding: 0.25rem 0.5rem;
      border-radius: 4px;
      font-size: 0.75rem;
      color: #4b5563;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>可访问性测试报告</h1>
    <div class="meta">
      <p>测试: ${title}</p>
      <p>时间: ${new Date().toLocaleString('zh-CN')}</p>
      <p>总违规项: ${violations.length}</p>
    </div>

    <div class="summary">
      ${Object.entries(violationsByImpact).map(([impact, items]) => `
        <div class="summary-card ${impact}">
          <h3>${impact}</h3>
          <div class="count">${items.length}</div>
        </div>
      `).join('')}
    </div>

    ${violations.map((violation, index) => `
      <div class="violation">
        <div class="violation-header">
          <span class="impact-badge ${violation.impact}">${violation.impact}</span>
          <h2 class="violation-title">${index + 1}. ${violation.id}</h2>
        </div>
        
        <p class="violation-description">${violation.description}</p>
        
        <div class="violation-help">
          <strong>如何修复:</strong> ${violation.help}<br>
          <a href="${violation.helpUrl}" target="_blank">查看详细文档 →</a>
        </div>

        <div class="nodes">
          <strong>受影响的元素 (${violation.nodes.length}):</strong>
          ${violation.nodes.map((node, nodeIndex) => `
            <div class="node">
              <div class="node-html">${escapeHtml(node.html)}</div>
              <div class="node-summary">${node.failureSummary}</div>
            </div>
          `).join('')}
        </div>

        <div class="tags">
          ${violation.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
        </div>
      </div>
    `).join('')}
  </div>
</body>
</html>
  `;
}

/**
 * 转义 HTML 特殊字符
 */
function escapeHtml(text: string): string {
  const map: Record<string, string> = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#039;',
  };
  return text.replace(/[&<>"']/g, m => map[m]);
}

/**
 * 按影响级别过滤违规项
 */
export function filterByImpact(
  violations: AxeViolation[],
  impacts: Array<'minor' | 'moderate' | 'serious' | 'critical'>
): AxeViolation[] {
  return violations.filter(v => impacts.includes(v.impact));
}

/**
 * 按标签过滤违规项
 */
export function filterByTags(
  violations: AxeViolation[],
  tags: string[]
): AxeViolation[] {
  return violations.filter(v => 
    tags.some(tag => v.tags.includes(tag))
  );
}

/**
 * 生成违规项统计
 */
export function getViolationStats(violations: AxeViolation[]): {
  total: number;
  byImpact: Record<string, number>;
  byTag: Record<string, number>;
} {
  const byImpact = violations.reduce((acc, v) => {
    acc[v.impact] = (acc[v.impact] || 0) + 1;
    return acc;
  }, {} as Record<string, number>);

  const byTag = violations.reduce((acc, v) => {
    v.tags.forEach(tag => {
      acc[tag] = (acc[tag] || 0) + 1;
    });
    return acc;
  }, {} as Record<string, number>);

  return {
    total: violations.length,
    byImpact,
    byTag,
  };
}
