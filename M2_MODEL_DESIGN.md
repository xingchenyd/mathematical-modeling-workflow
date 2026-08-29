# M2 建模设计与搜索空间工程

目标：回答“应该建什么模型、怎样让模型既贴题又可求”。

---

# 2.1 Model Candidate Competition

至少提出 2–4 个候选模型。

评分维度：

\[
Fidelity + Solvability + Explainability + EvidencePotential
\]

表：

| 模型 | 贴题性 | 可求性 | 可解释性 | 可验证性 | 风险 |
|---|---:|---:|---:|---:|---|

必须说明：
> 为什么最终不选另一个候选。

---

# 2.2 三层 Baseline

## B0 Naive
最简单方法，验证题意和指标。

## B1 Verified Feasible
必须通过所有硬约束，是正式上界/性能基线。

## B2 Strong Baseline
采用合理成熟方法，避免 Final 只打败故意很差的基线。

最终高级方法必须至少对 B2 解释增益。

---

# 2.3 Bound Designer

优化题在正式高级求解前尝试：
- 容量下界；
- 工作量下界；
- 距离下界；
- 最快速度下界；
- LP 松弛；
- Lagrangian；
- 对偶界；
- 忽略部分约束的松弛模型。

每个 Bound：

```text
Name:
Derivation:
Relaxed Constraints:
Value:
Valid Scope:
What It Proves:
What It Does Not Prove:
```

---

# 2.4 Gap 类型

严格区分：

1. Full-space Lower Bound Gap
2. Candidate-pool Gap
3. Solver MIP Gap
4. Empirical Benchmark Difference

正文不能混用。

---

# 2.5 Search Space Engineering

先问：
> 原始完整空间为什么不可求？

再设计：

## 聚合
必须证明等价或说明损失。

## 候选列
把局部复杂结构封装。

## 分解
Master + Subproblem。

## 局部精确
启发式定位，MILP/CP 精修。

## 滚动窗口
动态问题分时段。

## 代理筛选
廉价评分后只精算 Top-K。

---

# 2.6 Search Space Ledger

```text
Original Space:
Main explosion source:
Compression:
Candidate Types:
What may be missing:
How to expand:
Saturation criterion:
```

---

# 2.7 正式模型

必须包含：

1. 集合；
2. 参数；
3. 核心决策变量；
4. 状态变量；
5. 辅助变量；
6. 主目标；
7. 次目标；
8. 约束；
9. 边界/初始；
10. 定义域；
11. 单位；
12. 模型规模。

---

# 2.8 多目标

题目出现：
- 首先；
- 其次；
- 在不增加……前提下；

优先用：

### Lexicographic
\[
f_1 \succ f_2 \succ f_3
\]

### ε-constraint
锁定一级目标后再优化二级。

权重法只有权重有依据时才用。

---

# 2.9 约束四联表

每条关键约束必须有：

| 题面规则 | 数学式 | 代码位置 | Validator |
|---|---|---|---|

任何一列缺失都说明模型链未闭合。

---

# 2.10 模型规模审计

统计：
- binary；
- integer；
- continuous；
- constraints；
- candidate count；
- estimated complexity。

然后决定：
> 直接精确求 / 分解 / 候选化 / 启发式。

---

# 2.11 M2 Gate

进入 M3 前：
- B1 PASS；
- B2 建立或有合理替代；
- Bound 已尝试；
- Search Space 策略明确；
- Formal Model 完整；
- 规模与 Solver 策略匹配。
