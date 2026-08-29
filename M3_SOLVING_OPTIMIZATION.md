# M3 求解与优化

目标：把“可行模型”变成“有竞争力方案”。

---

# 3.1 Hybrid Solver 默认思想

\[
Fast\ Search + Exact\ Optimization
\]

启发式负责：
> 创造新的结构。

精确模型负责：
> 在结构之间做全局组合。

常见组合：
- Greedy + MILP；
- ALNS + MILP；
- ALNS + CP-SAT；
- Column Generation + MILP；
- Beam Search + Exact Local Repair；
- Benders；
- LNS + Min-cost flow。

---

# 3.2 算法职责必须明确

禁止：
> 使用 ALNS、CP-SAT、MILP 求解。

必须：
> ALNS 负责候选结构搜索；MILP 在候选域内做人员/路线全局组合；CP-SAT 负责具体时间资源排班。

---

# 3.3 初始解

记录：

```text
Method:
Why feasible:
Objective:
Secondary metrics:
Runtime:
Main weakness:
```

---

# 3.4 Optimization History

每一次优化必须记录：

```text
Iteration:
Starting solution:
Observed bottleneck:
Evidence:
Modification:
Expected gain:
Result:
Improvement:
Trade-off:
Validator:
Accepted:
```

所有优化曲线和消融都从此表产生。

---

# 3.5 Diagnose

每轮至少检查：
- 哪些对象贡献成本最高；
- 哪些资源利用率最低/最高；
- 哪些约束 binding；
- 哪类样本失败；
- 哪些路线低效；
- 哪些冲突反复出现；
- Gap 主要来自哪里。

---

# 3.6 Attribute

把瓶颈归因：

\[
Data / Model / Parameter / SearchSpace / Algorithm / Numerical
\]

不先归因，不换算法。

---

# 3.7 Solution-Driven Regeneration

根据当前解定向生成：

- 新路线；
- 新列；
- 新邻域；
- 新时间模式；
- 新特征；
- 新局部组合；
- 双/三方案重构；
- 新机型/资源组合。

核心问题：
> 当前优解告诉我们“搜索空间里缺了什么”？

---

# 3.8 Pair/Triple Reconstruction

对于组合优化题，优先尝试：
- 同时释放 2 个方案再重构；
- 同时释放 3 个方案再重构；
- 再做全局主问题。

原因：
> 单点插入只能在原结构附近移动，无法跨越组合障碍。

---

# 3.9 动态候选扩池

触发条件：
- Gap 长期不降；
- 当前解存在高成本结构；
- 多次局部修复无效；
- 新负约化成本列仍存在；
- Benchmark 显示当前候选太浅。

扩池后必须重新全局求解，而不是只把新候选局部塞进去。

---

# 3.10 高级分支

## Column Generation
Restricted Master → Dual → Pricing → Add Columns → Repeat。

## ALNS
编码 → Destroy → Repair → Acceptance → Weight Update → Stop。

## CP-SAT
Interval → NoOverlap → Resource Capacity → Time Window → Objective。

## Benders
Master 决定高层离散决策；Subproblem 检查/优化下层连续或排班问题。

---

# 3.11 Q3/动态问题特别规则

若存在“路线 + 时刻 + 具体资源”耦合：
- 不应长期停留在“先路线后排班”的单向修复；
- 若结果明显落后，应尝试 timed columns / event-based scheduling / rolling horizon；
- 第二阶段目标若依赖第一阶段基准，应允许在不破坏一级目标的前提下重构基准网络，而不只在固定网络上填空。

---

# 3.12 接受/拒绝新方案

只有同时满足：
- 主目标改善，或在主目标锁定下次目标改善；
- 硬约束通过；
- Validator PASS；
- 没有不可接受 trade-off；

才进入 Final Candidate。

---

# 3.13 停止条件

综合使用：
- 时间预算；
- 连续 N 轮无改善；
- 相对改善 < ε；
- Gap 达标；
- 候选池饱和；
- 多 seed 不再产生更优结构；
- 继续优化 ROI 低于论文/审计风险。

---

# 3.14 M3 输出

```text
Current Best:
B2:
Bound:
Gap:
Optimization History:
Main remaining bottleneck:
Next candidate expansion:
```
