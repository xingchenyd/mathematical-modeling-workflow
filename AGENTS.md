# AGENTS.md — V4.3

## 总控原则

本仓库不是“算法推荐器”，而是一个数学建模竞赛项目控制系统。

### 第一原则
在模型选择之前，先证明你已经理解：
- 题目；
- 数据；
- 规则；
- 可用信息；
- 风险；
- 错误解释的后果。

### 第二原则
任何后续失败都必须做根因分类：

| 根因 | 回退 |
|---|---|
| 题意/口径/字段语义 | M1 |
| 数据质量/信息泄漏/实验单位 | M1 |
| 数学抽象/变量/约束/目标 | M2 |
| 搜索空间/算法/实现 | M3 |
| 证据不足/实验不稳 | M4 |
| 写作表达 | M5 |
| 图表/引用/格式 | M6 |

不允许用“继续调参数”处理所有问题。

## 文件路由

- 新题：M0 + M1
- 建模：M2
- 求解/优化：M3
- 验证/实验：M4
- 论文：M5
- 图表/引用/提交：M6
- 答辩：M7
- 预测/动态/反事实：按 MASTER_ROUTER 加载 branch

## 证据对象

必须维护：
- Problem Contract
- Acceptance Contract
- Pitfall Ledger
- Data Dictionary
- Data Relationship Map
- Data Findings Ledger
- Modeling Eligibility Report
- Baseline/Bound/Search Space Ledgers
- Optimization History
- Validation Matrix
- Claim Ledger
- Reference Ledger
- SSOT
