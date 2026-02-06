# Skills 依赖关系图 | Skills Dependency Graph

可视化展示 skills 之间的依赖关系和推荐组合。

Visualize dependencies and recommended combinations between skills.

---

## 整体架构图 | Overall Architecture

```mermaid
graph TB
    subgraph "工作流 Skills | Workflow Skills"
        DW[日常测试工作流<br/>Daily Testing Workflow]
        SW[迭代测试工作流<br/>Sprint Testing Workflow]
        RW[发布测试工作流<br/>Release Testing Workflow]
    end
    
    subgraph "核心测试 Skills | Core Testing Skills"
        FT[功能测试<br/>Functional Testing]
        AT[API 测试<br/>API Testing]
        AUTO[自动化测试<br/>Automation Testing]
        MT[手动测试<br/>Manual Testing]
    end
    
    subgraph "专项测试 Skills | Specialized Testing Skills"
        PT[性能测试<br/>Performance Testing]
        ST[安全测试<br/>Security Testing]
        ACT[可访问性测试<br/>Accessibility Testing]
        MOB[移动端测试<br/>Mobile Testing]
    end
    
    subgraph "测试管理 Skills | Test Management Skills"
        TCW[测试用例编写<br/>Test Case Writing]
        TCR[测试用例评审<br/>Test Case Reviewer]
        BR[缺陷上报<br/>Bug Reporting]
        TR[测试报告<br/>Test Reporting]
        TS[测试策略<br/>Test Strategy]
        RA[需求分析<br/>Requirements Analysis]
    end
    
    subgraph "AI 辅助 Skills | AI-Assisted Skills"
        AI[AI 辅助测试<br/>AI-Assisted Testing]
    end
    
    subgraph "高级 Skills | Advanced Skills"
        TSG[测试策略生成器<br/>Test Strategy Generator]
        TMA[测试度量分析<br/>Test Metrics Analysis]
        SO[Skills 编排器<br/>Skill Orchestrator]
    end
    
    %% 工作流依赖
    DW --> RA
    DW --> TS
    DW --> TCW
    DW --> FT
    DW --> AUTO
    DW --> MT
    DW --> BR
    DW --> TR
    
    SW --> DW
    SW --> TS
    SW --> TR
    
    RW --> SW
    RW --> PT
    RW --> ST
    RW --> ACT
    
    %% 核心测试依赖
    FT --> RA
    FT --> TCW
    AT --> TCW
    AUTO --> FT
    AUTO --> AT
    MT --> RA
    
    %% 专项测试依赖
    PT --> AUTO
    ST --> AUTO
    ACT --> FT
    MOB --> FT
    MOB --> AUTO
    
    %% 测试管理依赖
    TCW --> RA
    TCR --> TCW
    BR --> FT
    TR --> TS
    TS --> RA
    
    %% AI 辅助依赖
    AI --> TCW
    AI --> AUTO
    AI --> BR
    
    %% 高级 Skills 依赖
    TSG --> RA
    TSG --> TS
    TMA --> TR
    SO --> DW
    SO --> SW
    SO --> RW
    
    %% 样式
    classDef workflow fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    classDef core fill:#fff3e0,stroke:#e65100,stroke-width:2px
    classDef specialized fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef management fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px
    classDef ai fill:#fce4ec,stroke:#880e4f,stroke-width:2px
    classDef advanced fill:#fff9c4,stroke:#f57f17,stroke-width:2px
    
    class DW,SW,RW workflow
    class FT,AT,AUTO,MT core
    class PT,ST,ACT,MOB specialized
    class TCW,TCR,BR,TR,TS,RA management
    class AI ai
    class TSG,TMA,SO advanced
```

---

## 工作流详细依赖 | Workflow Detailed Dependencies

### 日常测试工作流 | Daily Testing Workflow

```mermaid
graph LR
    DW[日常测试工作流]
    
    subgraph "早晨例行 | Morning Routine"
        RA1[需求分析]
        TS1[测试策略]
    end
    
    subgraph "测试执行 | Test Execution"
        TCW1[测试用例编写]
        FT1[功能测试]
        AUTO1[自动化测试]
        MT1[手动测试]
    end
    
    subgraph "缺陷管理 | Defect Management"
        BR1[缺陷上报]
    end
    
    subgraph "下午审查 | Afternoon Review"
        TR1[测试报告]
    end
    
    DW --> RA1
    DW --> TS1
    DW --> TCW1
    DW --> FT1
    DW --> AUTO1
    DW --> MT1
    DW --> BR1
    DW --> TR1
    
    RA1 --> TCW1
    TCW1 --> FT1
    FT1 --> AUTO1
    FT1 --> BR1
    TR1 --> TS1
```

### 迭代测试工作流 | Sprint Testing Workflow

```mermaid
graph LR
    SW[迭代测试工作流]
    
    subgraph "Sprint 规划 | Sprint Planning"
        TS2[测试策略]
        RA2[需求分析]
    end
    
    subgraph "Sprint 执行 | Sprint Execution"
        DW2[日常测试工作流]
    end
    
    subgraph "Sprint 评审 | Sprint Review"
        TR2[测试报告]
        TMA2[测试度量分析]
    end
    
    SW --> TS2
    SW --> RA2
    SW --> DW2
    SW --> TR2
    SW --> TMA2
    
    TS2 --> DW2
    DW2 --> TR2
    TR2 --> TMA2
```

### 发布测试工作流 | Release Testing Workflow

```mermaid
graph LR
    RW[发布测试工作流]
    
    subgraph "发布规划 | Release Planning"
        TS3[测试策略]
        TSG3[测试策略生成器]
    end
    
    subgraph "专项测试 | Specialized Testing"
        PT3[性能测试]
        ST3[安全测试]
        ACT3[可访问性测试]
    end
    
    subgraph "发布验证 | Release Validation"
        FT3[功能测试]
        AUTO3[自动化测试]
    end
    
    subgraph "发布报告 | Release Reporting"
        TR3[测试报告]
        TMA3[测试度量分析]
    end
    
    RW --> TS3
    RW --> TSG3
    RW --> PT3
    RW --> ST3
    RW --> ACT3
    RW --> FT3
    RW --> AUTO3
    RW --> TR3
    RW --> TMA3
```

---

## 测试类型依赖关系 | Testing Type Dependencies

### 功能测试生态 | Functional Testing Ecosystem

```mermaid
graph TB
    RA[需求分析] --> TCW[测试用例编写]
    TCW --> FT[功能测试]
    FT --> AUTO[自动化测试]
    FT --> BR[缺陷上报]
    TCW --> TCR[测试用例评审]
    AUTO --> AI[AI 辅助测试]
    BR --> TR[测试报告]
    
    style RA fill:#e8f5e9
    style TCW fill:#e8f5e9
    style FT fill:#fff3e0
    style AUTO fill:#fff3e0
    style BR fill:#e8f5e9
    style TCR fill:#e8f5e9
    style AI fill:#fce4ec
    style TR fill:#e8f5e9
```

### API 测试生态 | API Testing Ecosystem

```mermaid
graph TB
    RA2[需求分析] --> TCW2[测试用例编写]
    TCW2 --> AT[API 测试]
    AT --> AUTO2[自动化测试]
    AUTO2 --> PT[性能测试]
    AT --> ST[安全测试]
    AUTO2 --> TR2[测试报告]
    
    style RA2 fill:#e8f5e9
    style TCW2 fill:#e8f5e9
    style AT fill:#fff3e0
    style AUTO2 fill:#fff3e0
    style PT fill:#f3e5f5
    style ST fill:#f3e5f5
    style TR2 fill:#e8f5e9
```

### 移动端测试生态 | Mobile Testing Ecosystem

```mermaid
graph TB
    RA3[需求分析] --> TCW3[测试用例编写]
    TCW3 --> MOB[移动端测试]
    MOB --> FT2[功能测试]
    MOB --> AUTO3[自动化测试]
    MOB --> PT2[性能测试]
    AUTO3 --> TR3[测试报告]
    
    style RA3 fill:#e8f5e9
    style TCW3 fill:#e8f5e9
    style MOB fill:#f3e5f5
    style FT2 fill:#fff3e0
    style AUTO3 fill:#fff3e0
    style PT2 fill:#f3e5f5
    style TR3 fill:#e8f5e9
```

---

## 推荐组合 | Recommended Combinations

### 组合 1: 新功能完整测试流程

```mermaid
graph LR
    A[需求分析] --> B[测试策略]
    B --> C[测试用例编写]
    C --> D[功能测试]
    D --> E[自动化测试]
    E --> F[测试报告]
    
    style A fill:#90caf9
    style B fill:#90caf9
    style C fill:#90caf9
    style D fill:#90caf9
    style E fill:#90caf9
    style F fill:#90caf9
```

**Skills**: requirements-analysis → test-strategy → test-case-writing → functional-testing → automation-testing → test-reporting

### 组合 2: API 开发测试流程

```mermaid
graph LR
    A2[需求分析] --> B2[测试用例编写]
    B2 --> C2[API 测试]
    C2 --> D2[自动化测试]
    D2 --> E2[测试报告]
    
    style A2 fill:#ce93d8
    style B2 fill:#ce93d8
    style C2 fill:#ce93d8
    style D2 fill:#ce93d8
    style E2 fill:#ce93d8
```

**Skills**: requirements-analysis → test-case-writing → api-testing → automation-testing → test-reporting

### 组合 3: 性能优化测试流程

```mermaid
graph LR
    A3[测试策略] --> B3[性能测试]
    B3 --> C3[测试度量分析]
    C3 --> D3[测试报告]
    
    style A3 fill:#a5d6a7
    style B3 fill:#a5d6a7
    style C3 fill:#a5d6a7
    style D3 fill:#a5d6a7
```

**Skills**: test-strategy → performance-testing → test-metrics-analysis → test-reporting

### 组合 4: 安全审计流程

```mermaid
graph LR
    A4[测试策略] --> B4[安全测试]
    B4 --> C4[测试用例编写]
    C4 --> D4[测试报告]
    
    style A4 fill:#ffcc80
    style B4 fill:#ffcc80
    style C4 fill:#ffcc80
    style D4 fill:#ffcc80
```

**Skills**: test-strategy → security-testing → test-case-writing → test-reporting

### 组合 5: 探索性测试流程

```mermaid
graph LR
    A5[需求分析] --> B5[手动测试]
    B5 --> C5[缺陷上报]
    C5 --> D5[测试报告]
    
    style A5 fill:#ef9a9a
    style B5 fill:#ef9a9a
    style C5 fill:#ef9a9a
    style D5 fill:#ef9a9a
```

**Skills**: requirements-analysis → manual-testing → bug-reporting → test-reporting

---

## Skills 互补关系 | Skills Complementary Relationships

### 强互补（经常一起使用）

| Skill A | Skill B | 关系说明 |
|---------|---------|----------|
| requirements-analysis | test-case-writing | 需求分析后编写测试用例 |
| test-case-writing | functional-testing | 用例指导功能测试 |
| functional-testing | automation-testing | 功能测试后自动化 |
| automation-testing | test-reporting | 自动化结果生成报告 |
| test-strategy | test-reporting | 策略指导报告内容 |
| bug-reporting | functional-testing | 缺陷验证需要功能测试 |
| api-testing | automation-testing | API 测试通常自动化 |
| performance-testing | test-metrics-analysis | 性能数据需要分析 |

### 弱互补（偶尔一起使用）

| Skill A | Skill B | 关系说明 |
|---------|---------|----------|
| manual-testing | automation-testing | 手动测试可转为自动化 |
| security-testing | api-testing | API 安全测试 |
| accessibility-testing | functional-testing | 可访问性功能测试 |
| mobile-testing | performance-testing | 移动端性能测试 |

---

## Skills 依赖层级 | Skills Dependency Levels

### Level 0: 基础层（无依赖）

- requirements-analysis
- test-strategy

### Level 1: 核心层（依赖基础层）

- test-case-writing
- manual-testing

### Level 2: 执行层（依赖核心层）

- functional-testing
- api-testing
- bug-reporting

### Level 3: 自动化层（依赖执行层）

- automation-testing
- performance-testing
- security-testing
- accessibility-testing
- mobile-testing

### Level 4: 管理层（依赖多层）

- test-case-reviewer
- test-reporting

### Level 5: 工作流层（编排多个 skills）

- daily-testing-workflow
- sprint-testing-workflow
- release-testing-workflow

### Level 6: 高级层（智能化）

- ai-assisted-testing
- test-strategy-generator
- test-metrics-analysis
- skill-orchestrator

---

## 使用建议 | Usage Recommendations

### 初学者路径

```
requirements-analysis → test-case-writing → manual-testing → bug-reporting
```

### 中级路径

```
requirements-analysis → test-strategy → test-case-writing → functional-testing → automation-testing → test-reporting
```

### 高级路径

```
test-strategy-generator → skill-orchestrator → [multiple skills] → test-metrics-analysis
```

### 专项路径

**性能测试专项**:
```
test-strategy → performance-testing → test-metrics-analysis → test-reporting
```

**安全测试专项**:
```
test-strategy → security-testing → test-case-writing → test-reporting
```

**移动端测试专项**:
```
requirements-analysis → mobile-testing → automation-testing → test-reporting
```

---

## 相关资源 | Related Resources

- [Skills 索引](skills-index.md) - 按类别/场景/标签查找 skills
- [使用场景索引](docs/use-case-index.md) - 详细的场景指导
- [学习路径](docs/guides/learning-paths.md) - 系统学习指南
- [工作流模板](templates/workflow-templates/) - 预定义的 skill 组合

---

**最后更新 | Last Updated**: 2024-02-06
