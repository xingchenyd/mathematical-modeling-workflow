# B5 运筹学 / 运筹优化专用分支
## Operations Research & Prescriptive Optimization Protocol

适用：物流、路径、调度、选址、资源配置、生产、库存、网络流、排班、供应链、多阶段规划等。

---

# 1. 先确认是不是运筹题

核心判据不是“出现最小化”三个字，而是：

> 题目要求在约束下选择一个行动/方案，使目标最好。

即：

\[
\boxed{Decision + Objective + Constraints}
\]

典型输出：
- 哪个中心开；
- 谁分配给谁；
- 车辆走哪条路线；
- 什么时候执行；
- 买多少设备；
- 生产多少；
- 库存多少；
- 哪些任务取消；
- 哪个方案被推荐。

---

# 2. 常见模型映射

| 结构 | 常见模型 |
|---|---|
| 点到点/多源多汇运输 | Network Flow / Transportation |
| 谁服务谁 | Assignment / Matching |
| 选几个中心 | Facility Location / p-median / p-center |
| 路线配送 | VRP / Rich VRP |
| 取送 | PDP / PDPTW |
| 时间窗 | VRPTW / Scheduling |
| 任务排班 | Job Shop / Parallel Machine / RCPSP |
| 容量选择 | Knapsack / Bin Packing |
| 覆盖 | Set Covering / Max Coverage |
| 路线候选组合 | Set Partitioning |
| 跨期库存生产 | Lot Sizing / Inventory Planning |
| 多阶段随机决策 | Stochastic Programming / DP |
| 不确定参数 | Robust Optimization |

不要机械套表，要结合题目和数据。

---

# 3. 建模优先级

1. 题意/Pitfall；
2. 数据结构；
3. 决策变量；
4. 目标优先级；
5. 硬约束；
6. 理论界；
7. 模型规模；
8. Solver/算法。

---

# 4. Exact-first 不是“永远精确法”

若规模可控，优先：
- LP；
- MILP；
- CP-SAT；
- network flow；
- matching；
- shortest path；
- DP。

如果规模爆炸，再考虑：
- decomposition；
- column generation；
- Benders；
- rolling horizon；
- LNS/ALNS；
- heuristic candidate generation。

NP-hard 只说明最坏情况下难，不等于一个具体实例不能精确求解。

---

# 5. 路径/物流题特别检查

必须检查：
- 路线闭合；
- 流守恒；
- subtour；
- 容量逐段更新；
- pickup-before-delivery；
- 时间传播；
- service time；
- 车辆起终点；
- heterogeneous fleet；
- recharge/refuel；
- 司机/车辆/无人机周转；
- 多仓/多中心；
- 禁行/不可达。

---

# 6. 调度题特别检查

必须区分：
- release time；
- due date/deadline；
- processing time；
- setup/turnaround；
- precedence；
- machine/resource availability；
- no-overlap；
- cumulative capacity；
- calendar；
- preemption 是否允许。

时间索引模型变量爆炸时考虑：
- event-based；
- interval variables；
- CP-SAT；
- candidate jobs/columns。

---

# 7. 选址+路径题

如果“选中心”会改变后续路线成本，不能先独立选址再固定路线，除非证明近似合理。

考虑：
- location-routing；
- master location + routing subproblem；
- 全候选枚举（中心数少时）；
- Benders / surrogate screening + exact replay。

---

# 8. 多目标

优先检查题意是否有“首先/其次/在不增加…前提下”。

有 → lexicographic。

没有 → Pareto。

不要随意设：
\[
0.7\,cost+0.3\,time
\]
除非权重有明确依据。

---

# 9. Bound / Ceiling 是运筹题的核心证据

每题至少问：
- 最少需要多少资源？
- 最快物理时间？
- 最少路程？
- 最大理论服务率？
- LP relaxation？
- 忽略冲突后的理想值？

最终结果必须与这些界比较。

---

# 10. Solver 结果不要误读

`OPTIMAL` 的含义取决于你交给 Solver 的模型空间。

如果只对 500 条候选路线求整数主问题：
> OPTIMAL = 500条候选中的最优组合。

不是：
> 原始所有可能路线中的全局最优。

---

# 11. 不可行是信息，不是失败

遇到 infeasible：
- 先查题意/数据；
- 查 IIS/conflict；
- 找哪个约束组冲突；
- 搜索 feasibility frontier。

不要偷偷删除硬约束。

---

# 12. 国赛运筹题建议证据包

至少准备：

```text
Formal model
B1/B2
Bound/Ceiling
Solver log/certificate
Optimization history
Independent validator
Structured output validator
Ablation
Convergence (if heuristic)
Multi-seed (if stochastic)
Sensitivity/feasibility frontier
Pareto (if multiobjective)
Solution Quality Contract
```

---

# 13. 国赛论文推荐结果表

| 指标 | B1 | B2 | Final | Bound/Ceiling | Gap |
|---|---:|---:|---:|---:|---:|

让评委一眼知道：
> 不只是“算出了”，而是“知道算得有多好”。
