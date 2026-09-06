# M2 数学抽象、模型设计与方法选择

M2 的入口不是“这个题看起来适合什么算法”，而是 M1 的 Modeling Eligibility Report。

---

# 2.1 Evidence-to-Model Mapping

先建立：

| Evidence | Mathematical consequence |
|---|---|
| Pitfall P01 | 必须逐阶段状态约束 |
| Finding F03 | 可以按组聚合 |
| Finding F05 | 时间窗窄，需显式时序 |
| Data limitation D02 | 不支持连续外推 |

任何核心模型结构都应能追溯到：
- 题面；
- 数据；
- 假设；
- Benchmark；
中的至少一个来源。

---

# 2.2 先选数学问题类型，再选算法

顺序：

1. 现实问题；
2. 数学抽象；
3. 候选模型；
4. 求解架构；
5. 具体算法/软件。

例如：

> 动态容量取送问题  
> → MILP/候选列模型  
> → 列生成 + 整数主问题  
> → 具体求解器。

禁止：
> “我会 XGBoost/遗传算法，所以用它。”

---

# 2.2A Complexity Classification ≠ Solver Conclusion

识别 NP-hard / combinatorial explosion 有价值，但不能直接推出“必须使用启发式”。

需要继续判断：
- 实际实例规模；
- 结构是否可分解；
- LP/MILP/CP 松弛是否强；
- 是否存在小的局部精确子问题；
- 求解器是否能在时间预算内给出 Bound/Gap。

因此：
- NP-hard + 实例可控 → 仍可 Exact-first；
- 完整规模过大 → 候选生成、分解、启发式、列生成等；
- 启发式的价值是获得好解或生成结构，不等同于最优证书。

# 2.3 Model Candidate Competition

至少 2–4 个合理候选。

比较：
- Fidelity；
- Solvability；
- Explainability；
- Data compatibility；
- Validation potential；
- Evidence support。

每个候选必须写：
> 哪些 Pitfall/Finding 支持它？它解决不了什么？

---

# 2.4 Why-not-Alternative

对最终主模型至少回答：
> 为什么不用另一个常见模型？

原因必须基于：
- 数据规模；
- 数据结构；
- 约束；
- 可解释性；
- 最优性需求；
- 验证需求。

---

# 2.5 B0 / B1 / B2

## B0
验证题意、指标、数据处理。

## B1
Verified Feasible Baseline：
- 硬约束通过；
- 输出完整；
- 可独立复算。

## B2
Strong Baseline：
用成熟合理方法，防止 Final 只打败弱基线。

---

# 2.6 Bound Before Complexity

优化题在高级算法前尽量找：
- 容量界；
- 工作量界；
- 距离/时间界；
- LP relaxation；
- 对偶界；
- 松弛模型。

Bound Card 必须写：
> 放松了什么、对哪个空间有效、能证明什么、不能证明什么。

---

# 2.7 Search Space Engineering 必须来自结构证据

先问：
> 完整空间为何爆炸？数据/规则有什么结构可压缩？

方法：
- 聚合；
- 候选列；
- 分解；
- 无损预筛；
- 局部精确；
- 滚动窗口；
- 代理筛选。

每一种压缩都必须说明：
> 会不会丢掉潜在最优结构？

---

# 2.7A Controlled Relaxation / Simplification

遇到模型过大或迟迟不可行时，可以简化，但必须标注简化的身份：

### Diagnostic Relaxation
只用于定位困难，例如临时放松某类约束，看不可行来自哪里。

### Baseline / Bound Relaxation
用于构造基线、下界/上界或理解问题难度。

### Final-Eligible Simplification
只有证明不会改变题目核心要求、或误差边界可接受并被题目允许时，才能进入最终模型。

禁止：
> 为了“算出结果”把 K覆盖改成1覆盖、删除时间窗、忽略必须资源，然后把简化问题答案当原题最终答案。

每次简化记录：
```text
Original requirement:
Relaxation:
Purpose:
Effect on feasible region:
Effect on objective/bound:
Can enter final answer?: YES/NO
```

# 2.8 Analytical Reduction

先检查能否：
- 闭式消元；
- 单调性；
- 阈值；
- DP；
- 网络流；
- 无损剪枝；
- 精确线性化。

能解析解决的不要全部塞进通用启发式。

---

# 2.9 Formal Model

必须包含：
- 集合；
- 参数；
- 变量；
- 状态；
- 目标；
- 约束；
- 边界/初值；
- 定义域；
- 单位；
- 规模。

---

# 2.10 Constraint Traceability

每条关键规则：

| 题面/数据依据 | 数学表达 | 代码实现 | Validator |
|---|---|---|---|

防止论文、代码、验证器三套口径。

---

# 2.11 多目标

若题目明确优先级：
- Lexicographic；
- ε-constraint；
优先于随意加权。

权重只有明确依据时使用。

---

# 2.11A Method Maturity & Reproducibility Check

模型/算法候选除了性能，还检查：
- 是否有可靠文献；
- 是否有可理解的算法机制；
- 是否有成熟实现/官方文档；
- 是否能在竞赛时间内复现；
- 新方法相对传统方法是否真的解决当前瓶颈。

“发表得新”或“名字前沿”都不是单独采用理由。

# 2.12 Solver Selection

### Exact-first
如果模型可稳定表达为 LP/MILP/CP-SAT/Convex，规模可控：
> 优先精确方法，以获得 Bound、Gap、不可行诊断和稳定结果。

### Heuristic / Metaheuristic
用于：
- 大规模；
- 候选生成；
- warm start；
- 邻域搜索；
- 分解补充。

不是“越复杂越高级”。

---

# 2.13 Surrogate Admission

预测模型要进入优化前，必须通过样本外准入。

若未达到门槛：
- 不做无证据连续优化；
- 退回离散已测策略/Pareto；
- 或只生成实验候选。

---

# 2.14 Trust Region / Support

连续候选必须在数据支持域。

可用：
- convex hull；
- nearest neighbor；
- density；
- Mahalanobis；
- physical neighborhood。

---

# 2.15 Decision Resolution

若候选改善小于模型误差/不确定性：
> 不得声称新方案更优。

---

# 2.16 M2 Gate

进入 M3 前：
- 主模型能追溯到 M1 证据；
- B1 已建立；
- B2 已建立或说明为何不可；
- Bound 已尝试；
- Search Space 策略明确；
- 模型与 Solver 匹配；
- 没有明显用算法替代问题理解的情况。
