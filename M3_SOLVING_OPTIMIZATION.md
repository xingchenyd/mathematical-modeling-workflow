# M3 求解、诊断与定向优化

M3 不等于“调参”。其核心是：

\[
Solve \rightarrow Diagnose \rightarrow Attribute \rightarrow Regenerate \rightarrow Re-solve
\]

---

# 3.1 初始解

记录：
- 方法；
- 为什么可行；
- 主指标；
- 次指标；
- 运行时间；
- 主要弱点。

---

# 3.2 算法职责

若使用多个方法，分别说明：
> 谁负责候选、谁负责组合、谁负责排班、谁负责局部修复。

禁止只写算法名称串。

---

# 3.3 Optimization History

每轮记录：

```text
Iteration:
Current best:
Observed bottleneck:
Evidence:
Root cause hypothesis:
Modification:
Expected effect:
Actual result:
Trade-off:
Validator:
Accepted:
```

---

# 3.4 Diagnose

至少看：
- 高成本对象；
- 低利用率；
- Binding constraints；
- 时间/资源峰值；
- 未覆盖对象；
- 误差最大样本；
- 候选池缺口；
- 不稳定结构。

---

# 3.5 Root-Cause Attribution

把问题归因到：

1. Problem interpretation；
2. Data meaning/quality；
3. Assumption；
4. Mathematical model；
5. Search space；
6. Algorithm；
7. Numerical implementation。

---

# 3.6 Backtrack Router

### 题意/字段/信息错误
回 M1。

### 模型结构遗漏
回 M2。

### 搜索空间不足
留 M3，扩池/重构。

### 算法未收敛
留 M3，换求解架构/参数。

### 结果缺证据
进入 M4。

不要用“继续调算法”掩盖 M1/M2 错误。

---

# 3.7 Solution-Driven Regeneration

当前解告诉我们：
> 哪类结构还没被搜索到？

定向生成：
- 新路线；
- 新列；
- 新邻域；
- 新时间模式；
- 新特征组合；
- 双/三方案重构。

---

# 3.8 Pair / Triple Reconstruction

单点局部移动无法跨组合障碍时：
- 同时释放 2–3 个结构；
- 精确重构；
- 再回全局主问题。

---

# 3.9 Dynamic Candidate Expansion

触发：
- Gap 长期不降；
- 高成本结构重复；
- 新负约化成本列存在；
- Benchmark 暗示候选不足。

扩池后必须重新全局组合。

---

# 3.10 Warm Start

启发式可作为 MIPStart/incumbent。

论文明确：
> 它用于加速，不改变精确模型可行域，也不把启发式当最优证书。

---

# 3.11 Cross-method Confirmation

关键子问题成本允许时：
- analytic vs MILP；
- DP vs MILP；
- CP-SAT vs MILP；
- 小实例枚举 vs solver。

不同逻辑得到同一结果，是强证据。

---

# 3.12 动态决策

区分：
- first-stage frozen decision；
- new information；
- recourse。

禁止未来信息回写一阶段。

---

# 3.12A Timebox & Stop-loss

每个主要求解阶段设置时间盒，但时间盒服务于“及时改变策略”，不是强迫删除硬约束。

到达时间盒后依次判断：
1. 当前是否已有 B1 可行解；
2. 最大瓶颈属于 M1/M2/M3 哪一层；
3. 是否可以通过解析降维、候选化、分解、warm start 改善；
4. 是否需要把高级优化降级为更稳的 B2/Final Candidate；
5. 继续追求 0.1% 改善是否值得占用验证和论文时间。

Stop-loss 允许：
- 缩小高级搜索范围；
- 减少低ROI算法实验；
- 固化当前最佳已验证方案；
- 将未完成高级优化写为局限。

Stop-loss 不允许：
- 删除题目硬约束后仍声称解了原题。

# 3.13 停止

综合：
- 时间；
- 连续无改善；
- Gap；
- 候选饱和；
- 多 seed；
- ROI；
- 论文与验证风险。

停止不意味着一定全局最优。

---

# 3.14 M3 输出

```text
Current Best:
B2:
Bound:
Gap:
Main bottleneck:
Root-cause class:
Next action:
Backtrack target (if any):
```


---

# 3.15 Solver Engineering Protocol【V4.4】

使用商业/开源求解器时记录：

```text
Solver:
Version:
Model type:
Variables:
Binary/integer/continuous:
Constraints:
Presolve:
Time limit:
MIPGap target:
Seed:
Threads:
Warm start:
Status:
Incumbent:
Best bound:
Final gap:
Runtime:
Nodes/iterations:
```

最终论文不一定全部展示，但 Evidence Repository 必须保留。

# 3.16 Warm Start【V4.4】

若有启发式可行解：
> 优先作为 MIPStart / incumbent 提供给精确求解器。

用途：加速，而不是改变原模型最优性边界。

Poor/infeasible start 需要检查，不认为“warm start一定更快”。

# 3.17 Infeasibility Diagnosis【V4.4】

模型不可行时顺序：
1. Pitfall/数据/单位检查；
2. 小实例；
3. IIS / conflict refiner；
4. 分组放松约束；
5. Feasibility Relaxation 只用于定位冲突；
6. 修正真正错误。

禁止为了让模型有解直接删除题面硬约束。

# 3.18 Candidate-Space Saturation【V4.4】

候选列/路线/组合方法必须记录：
- candidate count；
- each expansion gain；
- new best structures；
- reduced cost（若有）；
- consecutive no-improvement rounds。

达到饱和才可把“候选空间不足”的风险降级。

# 3.19 Operations Research Improvement Loop【V4.4】

固定顺序：

```text
Solve
→ Inspect incumbent structure
→ Inspect bound/gap
→ Identify bottleneck constraints
→ Attribute gap
→ Strengthen formulation / expand search space / change decomposition
→ Re-solve
→ Independent validate
```

不是：
> 参数A改一点、参数B改一点，直到看起来不错。
