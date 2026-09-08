# M4 验证、实验与结论边界

M4 不只是检查“solver说可行”。

它要验证：
1. 我们理解得对不对；
2. 数据口径对不对；
3. 模型实现对不对；
4. 结果是否可信；
5. 结论说到什么程度。

---

# 4.1 Validation Pyramid

## V0 数据
ID、单位、时间、关系、异常处理。

## V1 规则/坑点
对 Pitfall Ledger 的 detection test 建最小例子。

## V2 小实例
手工/枚举可验证。

## V3 Solver/代码
求解状态、数值问题。

## V4 独立最终输出
只读 raw data + final output 重算。

## V5 论文数字
SSOT 与正文一致。

## V6 Claim
结论强度不超过证据。

---

# 4.2 Wrong-Path Unit Tests

对 P0/P1 坑点保留最小测试。

目的：
> 防止后续重构代码时又把已纠正的规则改错。

---

# 4.3 独立 Validator

不得读取 solver 的“feasible”标签作为结论。

重新计算：
- 覆盖；
- 资源；
- 时间；
- 状态；
- 目标；
- 输出格式。

---

# 4.4 Common-Sense Check

这是正式 Gate。

问：
- 数量级合理吗？
- 有没有明显违反现实的极端值？
- 最优方案是否出现难以解释的结构？
- 如果模型预测“2000个资源服务1000人”这类结果，是否应该回查？

若常识失败：
> 不允许因为 solver status 正常而直接接受。

---

# 4.4A Local Mechanism Replay / Micro Case Study

对于复杂模型，除全局 Validator 外，尽量选一个局部小实例，把关键机制“人能读懂地回放一遍”。

例子可以是：
- 3个节点的一条路线；
- 2–3个传感器的局部覆盖；
- 一个资源在两个时间段的状态变化；
- 一个预测样本从特征到输出的全过程。

至少展示：
1. 原始局部输入；
2. 模型变量/状态如何变化；
3. 关键约束如何起作用；
4. 局部结果是否可手算或直觉检查。

它既是解释工具，也是 Common-Sense Check 的增强版。

# 4.5 Constraint Slack

报告：
- min；
- 5% quantile；
- median；
- boundary count。

帮助识别真正脆弱约束。

---

# 4.6 Improvement

至少：
\[
B1 \rightarrow B2 \rightarrow Final
\]

必须同口径。

---

# 4.7 Ablation

每个算法/模型改进尽量对应消融。

说明：
- 贡献；
- 计算代价；
- 是否互补。

---

# 4.8 Convergence

迭代算法：
- current；
- best-so-far；
- time；
- iteration。

只能说经验平台，除非严格证明全局收敛。

---

# 4.9 Stability

随机算法多 seed。

报告：
Best / Mean / Median / Std / Worst。

---

# 4.10 Sensitivity

敏感性对象优先来自：
- Assumption Risk Register；
- Constraint Slack；
- Data Findings；
- 业务关键参数。

区分：
- 固定方案压力测试；
- 参数变化后重新优化。

---

# 4.11 Prediction Validation

验证切分必须模拟真实部署：
- 时间 → OOT/rolling；
- 独立个体 → LOO/nested；
- 群组 → leave-one-group-out；
- i.i.d. 才随机 K-fold。

---

# 4.12 Uncertainty

预测/外推不能只有点值。

可用：
- bootstrap；
- conformal；
- ensemble envelope；
- Bayesian；
- scenario；
- robust bound。

明确区间性质。

---

# 4.13 Gap Attribution

Gap 大时判断：
- LB 太松；
- Search Space 不足；
- Solver 未收敛；
- 局部最优；
- 模型代价本身。

不同原因对应 M2/M3 不同动作。

---

# 4.14 External / Counterfactual Validation

有真实历史方案时：
- 冻结同一评价口径；
- 复现现实；
- 同实例重优化；
- 分离不可控背景。

---

# 4.15 Claim Strength

C0 观察  
C1 可行  
C2 比基线改进  
C3 候选域最优  
C4 Bound-supported near-optimal  
C5 全局最优证明

“全局最优”只允许 C5。

---

# 4.15A Scheduled Re-read R2 / R3

### R2 — 第一版完整结果出现后
重新阅读全文题面，只问：
> “这个能运行的模型，究竟是不是在解决原题？”

重点找：
- 遗漏总量；
- 隐含先后；
- 错误输出口径；
- 多目标优先级漂移；
- 数据字段含义被建模过程悄悄改变。

### R3 — 模型冻结前
逐条执行：

\[
题面规则 \leftrightarrow 数学模型 \leftrightarrow 代码 \leftrightarrow Validator
\]

R2/R3 发现 P0/P1 必须回退，不能以“来不及了”为理由直接封版。

# 4.16 Backtrack Decision

M4 最后必须给：

```text
Failure source:
M1 / M2 / M3 / none
Evidence:
Required correction:
Can current result remain as baseline?
```

---


# 4.16A Evidence Storyboard：证据先定，图表后定【V4.5】

M4 结束前把 Claim Ledger 转成 `Evidence Storyboard`。每个核心结论只选择最合适的载体：

```text
Claim ID:
Claim:
Evidence type:
Evidence strength:
Best medium: TEXT / TABLE / FIGURE / EQUATION / CASE-STUDY
Why this medium:
Alternative medium rejected:
Source file/result:
Paper section:
```

选择原则：
- 精确数值 → 表格优先；
- 趋势/收敛/阶段变化 → 折线或贡献图；
- 分布/稳定性 → 箱线/ECDF/小提琴；
- 结构/网络/调度 → 网络图、路线骨架、Gantt；
- 权衡 → Pareto scatter；
- 矩阵/OD/相关结构 → heatmap；
- 复杂机制 → Local Case Study + 简化示意图。

一个 Claim 原则上只保留一个“主证据图”；如果表和图表达完全相同，删掉其中一个。

---

# 4.16B Cross-Question Synthesis Evidence【V4.5】

如果多问存在递进，M4 必须尝试构造一次跨问题比较，而不是只给每问独立结果。

至少比较：
- 新增约束/状态；
- 主指标变化；
- 资源利用变化；
- 瓶颈转移；
- 算法/模型为什么随之升级。

若没有受控实验，禁止把总变化强行分解为“X贡献70%、Y贡献30%”。

---

# 4.16C Language Evidence Calibration【V4.5】

在进入 M5 前，为核心 Claim 标注允许语言：

| Evidence level | 允许表述 |
|---|---|
| Observation | “观察到”“呈现” |
| Repeated/robust observation | “稳定呈现”“在多组设置下保持” |
| Mechanism + supporting evidence | “表明”“支持……机制” |
| Controlled ablation | “主要收益来自…”（仅限被隔离因素） |
| Valid bound/certificate | “Gap为…”“达到理论界” |
| Full-space proof | “全局最优/理论上限” |

禁止把相关性写成因果，把候选域最优写成原问题全局最优，把单次结果写成“显著”。


# 4.17 M4 Gate

进入终稿前：
- V0–V4 关键层通过；
- Baseline；
- Bound/Gap有边界；
- 关键算法改进有证据；
- 随机算法稳定；
- 不确定性/敏感性有结论；
- Common-sense Check PASS；
- 关键复杂机制已尽量完成 Local Mechanism Replay；
- R2/R3 Re-read 无未处理 P0/P1；
- 无未处理 P0/P1。


---

# 4.18 Reference-Range / Answer-Accuracy Audit【V4.3.2】

如果题目具有：
- 明确可计算答案；
- 明确答案数量级；
- 容易由硬约束检验真假的结果；
- 官方要求提交结构化附件；

则不能只依赖论文叙述“看起来合理”。

增加：

```text
Primary result:
Independent recomputation:
Simple theoretical bound:
Reference/benchmark range (if legitimate):
Common-sense range:
Structured attachment value:
Paper value:
Consistent?:
PASS/FAIL
```

若数据结果直接违反题面约束：
> 优先判断题意、数据、模型或实现存在问题，禁止通过文字解释掩盖。

---

# 4.19 Structured Attachment Validator【V4.3.2】

对题目要求上传的附件，建立独立 Validator：

1. 文件可以正常读取；
2. Schema 正确；
3. 每个必需 ID 都存在；
4. 不多、不少、不重复；
5. 类型/单位正确；
6. 所有硬约束通过；
7. 汇总指标从附件可反算；
8. 论文中的所有对应结果与附件一致。

Attachment Validator FAIL -> P0，不能提交。


---

# 4.20 Solution Quality Contract【V4.4】

每个主要优化问题都必须维护：

```text
Question:
Primary metric:
B1 verified baseline:
B2 strong baseline:
Best feasible solution:
Strict LB / UB / ceiling:
Candidate-pool bound:
Solver best bound:
Gap type:
Current gap:
Benchmark range:
Independent validator:
Numerical closure:
Multi-seed stability:
Unsearched structure:
Remaining structural risk:
Allowed claim:
Freeze allowed: YES/NO
```

只有 `Freeze allowed=YES` 才能成为终稿 Final。

# 4.21 Solver Certificate【V4.4】

如果使用精确 Solver，保存：
- status；
- objective；
- best bound；
- MIP gap；
- runtime；
- node count；
- optimal/infeasible/unbounded/time-limit。

表述边界：
- Full model OPTIMAL → 可按模型空间声明全局最优；
- Restricted candidate model OPTIMAL → 只能声明候选域最优；
- Time limit + gap → 声明可行解及 Gap；
- No valid full-space bound → 不写“距离全局最优仅x%”。

# 4.22 Numerical Closure Certificate【V4.4】

对有守恒/平衡的模型量化：

```text
Max flow-balance residual:
Max energy-balance residual:
Max inventory residual:
Max equality violation:
Max inequality violation:
Objective recomputation difference:
```

不是只写“约束满足”。

# 4.23 Gap Decomposition【V4.4】

将最终差距拆成：

```text
Modeling gap:
Relaxation/bound gap:
Search-space gap:
Solver gap:
Heuristic gap:
Data/uncertainty gap:
```

然后确定下一轮最高ROI动作。

# 4.24 Feasibility Frontier Search【V4.4】

对关键硬约束可搜索临界值：
- budget；
- fleet size；
- capacity；
- deadline；
- emission cap；
- service rate；
- robustness budget。

输出：
> 约束收紧到什么程度开始不可行。

这比只做 ±10% 敏感性更能说明系统极限。

# 4.25 Robustness Ladder【V4.4】

若存在不确定性，推荐：

```text
Deterministic solution
→ Stress test
→ Failure exposure
→ Define uncertainty set/scenarios
→ Robust/Stochastic model
→ Worst-case/scenario replay
→ Price of Robustness
→ Recourse/Rolling update if applicable
```

Price of Robustness：
\[
PoR=\frac{Z_{robust}-Z_{det}}{|Z_{det}|}
\]
（最大化问题按对应定义调整）。

# 4.26 Cross-method Confirmation【V4.4】

关键子问题若可行，至少用另一种逻辑复核：
- brute-force small instance；
- DP；
- network flow；
- alternative solver；
- analytic bound；
- independent reconstruction。

# 4.27 Quality Freeze Gate【V4.4】

不允许因为“已经有0违规结果”就自动冻结。

冻结必须同时回答：
1. Correct? 
2. How good? 
3. Compared with what? 
4. What can be proven? 
5. What remains unsearched? 
6. Is further improvement still high ROI?
