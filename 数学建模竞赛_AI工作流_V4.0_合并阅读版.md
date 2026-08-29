# 数学建模竞赛 AI 工作流 V4.0 — 合并阅读版
> 模块化执行时优先使用文件夹内 MASTER_ROUTER + 对应 M0-M6；本文件仅便于整体审阅。



---

# 数学建模竞赛 AI 工作流 V4.0
## Modular Evidence-Grounded Competition System

V4.0 不再把所有规则串成一条 170+ 步的长流程，而采用：

\[
\boxed{
MASTER\_ROUTER
+
M0\sim M6
+
Templates
}
\]

主控只负责“现在进入哪个模块”，各模块只加载当前阶段需要的规则。

## 模块

| 模块 | 名称 | 核心任务 |
|---|---|---|
| M0 | 项目控制与证据治理 | 材料、规则、Contract、Issue、Decision、SSOT |
| M1 | 题意、数据与 Benchmark | 三遍读题、规则审计、EDA、高分论文差距分析 |
| M2 | 建模设计与搜索空间 | 候选模型、B0/B1/B2、Bound、Search Space、正式模型 |
| M3 | 求解与优化 | Hybrid Solver、诊断、解驱动再生成、重优化 |
| M4 | 验证与实验 | 独立 Validator、Gap、消融、收敛、稳定性、敏感性 |
| M5 | 论文工程 | 从标题、摘要到结论的逐节、逐段、逐句写作协议 |
| M6 | 视觉、参考文献、排版与提交 | Figure/Table、引用真实性、[1] 编号、AI合规、最终提交 |

## 执行原则

1. 比赛开始只读 `MASTER_ROUTER.md + M0 + M1`。
2. 题意冻结后加载 M2。
3. 模型成形后进入 `M3 <-> M4` 循环。
4. 模型未冻结时可以同步积累 M5 的证据，但不得正式锁定摘要。
5. 模型冻结后完整加载 M5。
6. 成稿后加载 M6 做视觉、引用、排版和提交审计。
7. 官方竞赛规则优先级永远高于本仓库默认规范。
8. 任何结果、文献、DOI、Gap、算法性能都不得虚构。

## 最终目标

不是“写出最多模型”，而是：

\[
\boxed{
正确的问题
+
合理的模型
+
有竞争力的结果
+
明确的最优性边界
+
可复核的证据
+
高密度论文表达
+
真实可核验引用
}
\]


---

# MASTER ROUTER V4.0
## 总控路由器

本文件不负责教 AI 每一步“怎么做”，只负责判断当前应进入哪个模块。

---

# 1. 生命周期

\[
\boxed{
M0
\rightarrow
M1
\rightarrow
M2
\rightarrow
(M3\leftrightarrow M4)
\rightarrow
M5
\rightarrow
M6
}
\]

### M0：先确认“项目和规则”
若材料、规则、版本、输出格式不明确，不允许进入 M1。

### M1：确认“题目真正是什么”
只有 Problem Contract、Rule Audit、Data Audit 和基本 Benchmark 完成后进入 M2。

### M2：确认“应该建什么模型”
必须建立模型候选、Baseline、Bound 尝试、搜索空间策略，再进入 M3。

### M3：真正求解
输出 Current Best Solution。

### M4：验证和实验
任何 M3 的新 Final Candidate 必须先经过 M4 才能被接受。

若 M4 发现：
- 约束错误；
- Gap 主要来自候选空间；
- 不稳定；
- 关键样本失败；

则返回 M3。

### M5：论文工程
只有主要模型冻结、核心结果可复算后正式写终稿。

### M6：视觉、引用、排版、提交
最终 PDF/Word/LaTeX 必须在 M6 中通过：
- Figure/Table Audit；
- Reference Integrity Gate；
- Citation Coverage Gate；
- Typography Gate；
- Submission Gate。

---

# 2. 路由判断

## 若用户刚给题目
加载：M0 + M1。

## 若用户问“用什么模型”
先检查 M1 是否完成；未完成不得直接选模型。

## 若模型已有但结果很差
加载：M2 + M3 + M4。

## 若用户给高分论文要求比较
加载：M1 的 Benchmark/Delta Matrix；必要时 M3/M4 比较算法与证据。

## 若用户说“继续优化”
加载：M3 + M4，不重新从 M0 开始。

## 若用户说“开始写论文”
先确认：
- Validator PASS；
- SSOT 建立；
- Final Candidate 冻结或明确为 Draft Candidate；
然后加载 M5。

## 若用户说“检查参考文献/格式/提交”
加载 M6。

---

# 3. Gate 状态

项目状态必须始终维护：

```text
M0 PROJECT CONTROL: PASS/FAIL
M1 UNDERSTANDING & DATA: PASS/FAIL
M2 MODEL DESIGN: PASS/FAIL
M3 SOLVER: ACTIVE/FROZEN
M4 EVIDENCE: PASS/PARTIAL/FAIL
M5 PAPER: DRAFT/FROZEN
M6 SUBMISSION: PASS/FAIL
```

---

# 4. 不允许的行为

- 一次把 M0–M6 全部塞进一个 prompt 后自由发挥；
- 材料未读完直接写模型；
- 模型未验证直接写摘要结论；
- Solver “optimal” 就宣称原问题全局最优；
- 引用没核验就编进参考文献；
- 参考文献表里有正文从未引用的“装饰文献”；
- 正文出现 [7] 但参考文献中没有第 7 条；
- 图表没有 Claim；
- 优化无 Baseline、无对比；
- 灵敏度不区分“固定方案压力测试”和“重新优化”。

---

# 5. 冻结标准

当且仅当：
- P0=0；
- P1=0 或已明确接受；
- Validator PASS；
- 核心结果稳定；
- Bound/Gap 有合理解释；
- 关键实验完成；
- 论文 Claim 有证据；
- 引用可核验；
- 提交规则通过；

才允许：

```text
MODEL CONVERGED — FREEZE
PAPER CONVERGED — FREEZE
READY TO SUBMIT
```


---

# M0 项目控制与证据治理

目标：让整个竞赛项目有唯一事实源、唯一当前方案和明确的审计轨迹。

---

# 0.1 Material Gate

列出：
- 赛题；
- 数据附件；
- 官方规则；
- 官方格式；
- 评分要求；
- 已有代码；
- 已有论文；
- 已有结果；
- 参考高分论文；
- 支撑材料。

输出：

```text
MATERIAL GATE
题面：
数据：
规则：
格式：
已有工程：
版本冲突：
缺失项：
Gate = PASS / FAIL
```

如果存在多个版本，必须先确定：
- 哪个是官方最新版；
- 哪个是当前代码；
- 哪个是当前论文；
- 哪个结果是 current best。

---

# 0.2 Problem Contract

每问记录：

```text
Question:
Known:
Decision / Target:
Primary Objective:
Secondary Objectives:
Hard Constraints:
Soft Constraints:
Required Outputs:
Evaluation Metrics:
Dependencies:
Ambiguities:
Forbidden Changes:
```

任何后续模型变化都不得悄悄改变此 Contract。

---

# 0.3 Acceptance Contract

每问提前定义完成条件：

```text
- 题面全部要求已回答；
- 硬约束全部通过；
- 主目标可计算；
- 关键次目标可计算；
- 至少 B1 Verified Baseline；
- 尽可能有 Bound / Benchmark；
- 最终结果可独立验证；
- 论文有“分析→模型→算法→结果→验证”闭环。
```

---

# 0.4 Issue Ledger

严重级：

P0：答案错误/提交无效  
P1：核心建模/求解缺陷  
P2：证据/实验/论文完整性问题  
P3：排版/语言/次要优化

格式：

```text
Issue ID:
Severity:
Problem:
Evidence:
Impact:
Fix:
Success Test:
Status:
```

CLOSED 的 Issue 只有出现 NEW EVIDENCE 才重新打开。

---

# 0.5 Decision Log

每个重大决策：

```text
Decision:
Alternatives:
Why chosen:
Evidence:
Risk:
Revisit trigger:
```

禁止同一问题反复推翻而没有新证据。

---

# 0.6 Single Source of Truth

所有最终数值只允许来自：

```text
results_master.csv
final_results.json
```

字段示例：

```text
Q1_primary
Q1_secondary
Q1_bound
Q1_gap
Q1_validator
...
```

摘要、正文、表格、图、结论均从 SSOT 读取。

---

# 0.7 Claim Ledger

每个强结论：

```text
Claim ID:
Claim:
Question:
Strength: C0-C5
Evidence:
SSOT Field:
Validator:
Figure/Table:
Paper Section:
Status:
```

等级：

C0 观察  
C1 可行  
C2 比基线改进  
C3 当前候选域最优  
C4 有有效 Bound 支持的近优  
C5 严格证明全局最优

---

# 0.8 Reference Ledger 初始化

从比赛开始就建立，不要到写论文时临时拼参考文献。

```text
Citation Key:
Authors:
Title:
Venue:
Year:
Volume/Issue:
Pages/Article:
DOI:
Publisher URL:
Verification Source:
Verified Date:
Used For:
Planned Paper Section:
Status: UNVERIFIED / VERIFIED / REJECTED
```

UNVERIFIED 文献禁止进入终稿参考文献。

---

# 0.9 项目状态

每次阶段性汇报：

```text
Current Module:
Current Question:
Current Model:
Current Best:
Bound:
Gap:
Validator:
Open P0:
Open P1:
Next Highest-ROI Action:
```


---

# M1 题意、数据与 Benchmark

目标：解决“我们到底在解决什么问题”和“优秀方案通常从哪里突破”。

---

# 1.1 三遍读题

## 第一遍：系统
只回答：
- 实体；
- 资源；
- 行为；
- 决策；
- 目标。

输出 100–200 字问题本质摘要。

## 第二遍：逐问
每问：

```text
Known
Need to Decide
Must Satisfy
Need to Optimize
Need to Output
```

## 第三遍：易错规则
扫描：
- 至少/至多；
- 先/后；
- 首次/最后；
- 同一；
- 可选/必选；
- 是否取整；
- 是否跨天；
- 状态何时更新；
- 容量是总量还是逐阶段；
- 资源何时释放/恢复。

形成：

| 题面原句 | 数学含义 | 常见误读 | Validator 检查 |
|---|---|---|---|

---

# 1.2 小问递进图

建立 Q1/Q2/Q3 依赖关系。

必须明确：
- 哪些约束继承；
- 哪些性质失效；
- 哪些变量新增；
- 哪些算法可复用；
- 哪些结果不能直接继承。

---

# 1.3 Data Audit

## 文件层
行数、列数、Sheet、编码、文件版本。

## 字段层
类型、缺失、重复、异常、单位。

## 逻辑层
时间先后、起终点、集合关系、总量、唯一性、守恒。

## 跨表层
ID 是否匹配、距离矩阵是否对称/完整、时间是否同一时区/日期口径。

输出：

```text
DATA AUDIT
File:
Field:
Logic:
Cross-table:
Critical anomalies:
Treatment:
Gate = PASS / FAIL
```

---

# 1.4 EDA 的目的

EDA 不是“为了有图”，而是为了回答建模问题。

每个探索任务写：

```text
Question:
Method:
Observed Structure:
Evidence:
Modeling Consequence:
```

优先寻找：
- 分布结构；
- 空间簇；
- 网络流；
- 时间窗；
- 供需平衡；
- 资源瓶颈；
- 长尾/异常；
- 可聚合结构。

每张 EDA 图后必须回答：
> 这张图改变了哪个建模决定？

没有答案则不进入正文。

---

# 1.5 Benchmark Evidence Matrix

对高分论文/文献做以下提取：

| 维度 | 内容 |
|---|---|
| 问题抽象 | 它把问题看成什么 |
| 模型 | 主模型是什么 |
| 搜索空间 | 如何压缩 |
| Baseline | 如何构造 |
| Bound | 是否有 |
| Solver | 启发式/精确方法如何协作 |
| Regeneration | 是否动态扩池/重构 |
| Result | 关键指标 |
| Validation | 如何复核 |
| Experiments | 消融/收敛/稳定/敏感 |
| Figures | 最有解释力的图 |
| Writing | 最值得借鉴的结构 |
| Limitation | 它承认什么没证明 |

---

# 1.6 Delta Matrix：我们 vs 高分论文

必须生成一张内部表：

| Task | 我们做到 | 高分论文做到 | 我们独有 | 我们缺失 | 优先级 |
|---|---|---|---|---|---|

分类至少包含：
- 规则审计；
- Baseline；
- Bound；
- Search Space；
- Solver；
- 动态扩池；
- 多架次重构；
- 时空联合；
- Validator；
- Gap；
- Ablation；
- Convergence；
- Stability；
- Sensitivity；
- Figure；
- Writing；
- Reference Verification；
- Reproducibility。

这张表用于决定“下一步改什么”，不是用来吹嘘。

---

# 1.7 文献/高分论文的使用边界

可以借鉴：
- 问题结构；
- 模型族；
- 算法思路；
- 实验设计；
- 论文组织；
- 引用线索。

禁止：
- 复制结果；
- 复制数据；
- 无引用复述独创方法；
- 把别人模型改名当创新；
- 用高分论文结果替代自己程序结果。

---

# 1.8 M1 Gate

进入 M2 前必须满足：
- Problem Contract 可冻结；
- 规则易错点已列；
- Data Audit PASS；
- 小问依赖清楚；
- Benchmark 已建立；
- 当前主要差距已知。


---

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


---

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


---

# M4 验证与实验

目标：证明“结果不是只看起来合理”。

---

# 4.1 独立 Validator

必须与求解逻辑分离。

只读取：
- 原始数据；
- 最终结果文件。

重新计算：
- ID覆盖；
- 重复/遗漏；
- 路径；
- 容量；
- 时间；
- 资源；
- 状态递推；
- 目标函数；
- 输出格式。

---

# 4.2 Validator 报告

```text
File integrity:
Coverage:
Resource:
Time:
State:
Objective recalculation:
Hard violations:
Metric differences:
PASS / FAIL
```

Solver status 不属于独立验证证据。

---

# 4.3 Constraint Slack

可行不代表安全。

计算：
- minimum slack；
- 5% quantile；
- median；
- boundary count。

分析：
> 哪一类约束是真正瓶颈？

---

# 4.4 Improvement

至少比较：

\[
B1 \rightarrow B2 \rightarrow Final
\]

若有多个优化模块：

\[
B2 \rightarrow +A \rightarrow +B \rightarrow Final
\]

---

# 4.5 Ablation

每个“算法创新”原则上都对应一个消融。

表：

| Variant | Module A | Module B | Module C | Primary | Runtime |
|---|---|---|---|---:|---:|

正文回答：
- 哪个模块贡献最大；
- 是否互补；
- 是否只是增加计算时间。

---

# 4.6 Convergence

迭代算法记录：
- iteration；
- runtime；
- current objective；
- best-so-far。

论文优先展示 best-so-far。

不能写：
> 收敛到全局最优。

除非有严格证明。

可以写：
> 进入经验稳定平台。

---

# 4.7 Stability

随机算法建议 5–10 seeds，时间允许时更多。

报告：
- Best；
- Mean；
- Median；
- Std；
- Worst。

如果波动大，必须承认。

---

# 4.8 Sensitivity

分两类：

## 算法参数
检验算法配置是否脆弱。

## 业务参数
检验结论是否稳健。

每个参数固定写：
1. 为什么选；
2. 基准值；
3. 扰动范围；
4. 固定方案回放 or 重新优化；
5. 结果；
6. 机制；
7. 结论边界。

---

# 4.9 固定方案压力测试 vs 重新优化

### 固定方案压力测试
结论只能说明：
> 当前方案在更严格条件下的裕度/脆弱性。

### 参数变化后重新优化
才能说明：
> 系统在新参数下的最优/最好已知响应。

两者不得混写。

---

# 4.10 Gap Attribution

若 Gap 大，判断来自：
- Bound 太松；
- Candidate Pool 不足；
- Solver 未收敛；
- Local optimum；
- 模型结构本身导致代价。

输出：

```text
UB:
LB:
Gap:
LB tightness:
Search-space limitation:
Algorithm limitation:
Most likely source:
Next action:
```

---

# 4.11 Claim Strength 审计

论文中：
- “可行”至少 C1；
- “提高 x%”至少 C2；
- “候选域最优”至少 C3；
- “Gap≤x%”至少 C4；
- “全局最优”必须 C5。

---

# 4.12 M4 Gate

Final Candidate 进入 M5 前：
- Validator PASS；
- Baseline 对比；
- Bound/Gap 有合理表述；
- 主要算法改进有证据；
- 随机算法有稳定性；
- 敏感性结论边界明确。


---

# M5 论文工程
## 从标题到结论的逐节、逐段、逐句写作协议

目标：让 AI 不仅知道“这一章写什么”，还知道“第一段、公式前、公式后、表后、图后和过渡句分别写什么”。

---

# 5.1 Paper Architecture

正式写作前先填：

| Section | Purpose | Reader leaves knowing | Core Claim | Evidence | Figure/Table | Target Length |
|---|---|---|---|---|---|---|

无 Architecture 不开始全文。

---

# 5.2 Section Contract

每个小节写前：

```text
Section:
Purpose:
Reader enters knowing:
Reader leaves knowing:
Paragraph 1:
Paragraph 2:
Paragraph 3:
Equation:
Table:
Figure:
Claim:
Forbidden repetition:
Transition:
Target length:
```

写后：

```text
Purpose answered?
Unsupported claim?
Repeated material?
Formula unexplained?
Figure unexplained?
Number outside SSOT?
Overclaim?
PASS / REWRITE
```

---

# 5.3 标题

默认结构：

\[
研究对象 + 主要数学结构/核心方法 + 任务
\]

最多 1–2 个方法词。

不要堆：
> ALNS-MILP-CP-SAT-Benders-Column Generation。

---

# 5.4 摘要总结构

```text
总述段
Q1段
Q2段
Q3段
总体验证/机制段
关键词
```

---

# 5.5 摘要总述段

## 第一句：对象
只写研究对象和任务。

## 第二句：困难
写 3–5 个真正耦合结构，不抄全部题面。

## 第三句：统一框架
给全文技术主线。若是自定义核心框架可加粗。

## 第四句：多目标/总体原则
如果是多目标，必须把目标逐个说清：
- 一级是什么；
- 二级是什么；
- 后续是什么。

禁止：
> 建立多目标模型。

而不解释目标。

---

# 5.6 每问摘要六槽

## Slot A：本问特殊结构
相较上一问新增什么/利用什么性质。

## Slot B：模型
建立什么数学模型，联合决定哪些变量。

模型第一次出现后 1–2 句内必须回答：
- 决定什么；
- 优化什么；
- 关键约束是什么。

## Slot C：目标
一级/二级目标顺序。

## Slot D：算法职责
不能只列算法名。

应写：
> **ALNS** 负责候选搜索，**列生成** 负责基于对偶信息扩池，**MILP** 负责候选域全局组合。

## Slot E：结果
只写：
- 主指标；
- 规模；
- 最重要 1 个次指标。

数字不加粗。

## Slot F：可信度
理论下界 / Gap / Baseline / Validator。

---

# 5.7 摘要结尾

最多 2–3 句：
1. 独立验证；
2. 全文机制；
3. 必要局限。

避免空话：
> 具有重要现实意义。

---

# 5.8 问题重述

## 1.1 背景
1–2 段：
- 系统；
- 资源；
- 决策冲突。

不要写行业百科。

## 1.2 问题要求
每问一段：

\[
新增条件 \rightarrow 决策 \rightarrow 目标 \rightarrow 输出
\]

此处不出现具体算法。

---

# 5.9 问题分析——每问 5 段

## 第1段：数学本质
> 问题 X 本质上属于……

并说明与标准问题相比新增什么。

## 第2段：核心难点
每个难点必须解释“为什么影响结果”。

## 第3段：可利用结构
这是最重要的一段：
> 虽然规模大，但存在 A/B/C 性质，因此可以压缩……

## 第4段：模型选择
> 若直接 A 会……；B 能……；因此选择 B。

## 第5段：求解路线
> 本问采用“预处理—候选生成—全局组合—验证”。

自然过渡到模型。

---

# 5.10 数据处理

每个数据小节按：

### 段1
数据组成/规模。

### 段2
缺失、异常、单位、时间处理。

### 段3
处理后规模。

结构性统计每个结论都用：
1. 观察；
2. 证据；
3. 建模后果。

图前：
> 为判断……绘制图X。

图后：
> 图X显示……；说明……；因此模型……

---

# 5.11 模型假设

每条假设三句：
1. 假设；
2. 依据；
3. 影响边界/后续敏感性。

禁止：
> 为方便计算……

---

# 5.12 符号说明

只放跨章节高频量。

表：
| 符号 | 含义 | 单位 |

局部算法变量现场定义。

---

# 5.13 每问模型建立

推荐结构：

```text
X.1 建模思路
X.2 模型准备/状态表示
X.3 集合与参数
X.4 决策变量
X.5 目标函数
X.6 约束条件
X.7 完整模型与规模
```

---

# 5.14 模型准备——逐段

## 第1段
为什么不能直接逐对象/逐弧建模。

最好给量级。

## 第2段
采用什么新表示：
- 候选列；
- 事件；
- 状态标签；
- 时间块；
- 聚合组。

## 第3段
新表示固化了什么、消掉了什么。

## 第4段
主问题还决定什么。

## 第5段
如何恢复最终逐对象输出。

---

# 5.15 决策变量写法

每个变量：
1. 公式；
2. 取值；
3. 现实含义。

按：
- 核心决策；
- 状态；
- 辅助变量
分组。

---

# 5.16 目标函数写法

固定：
1. 题意引入；
2. 公式；
3. 各项解释；
4. 多目标协调。

如果字典序：
> 为什么不用简单加权？
> 上一层如何锁定？
> 容差是什么？

---

# 5.17 约束写法

每组约束：

### 小标题
现实含义。

### 引入句
为什么需要。

### 公式

### 新符号解释

### 现实解释
该式保证什么。

### 特殊情况
必要时说明边界。

推荐顺序：
覆盖 → 流守恒 → 容量 → 顺序 → 时间 → 资源 → 状态 → 逻辑 → 定义域。

---

# 5.18 算法章节

推荐：

```text
X.8 求解难点
X.9 总体算法框架
X.10 初始解
X.11 核心算法
X.12 针对本题改进
X.13 伪代码/流程
X.14 停止与复杂度
```

## 求解难点第一段
回答：
> 为什么不能直接交给 solver？

## 总体算法
每层一句职责。

## 核心算法
如果是 ALNS：
- 编码；
- Destroy；
- Repair；
- Acceptance；
- Weight；
- Stop。

每个算子都必须写：
> 操作什么；为什么有效；如何保持/恢复可行。

## 针对本题改进
固定：
- 标准算法弱点；
- 本文修改；
- 为什么针对本题；
- 后文用什么实验验证。

---

# 5.19 结果章节——八段协议

## 第1段：直接回答题目
> 最终方案……

紧接核心表。

## 第2段：Baseline
主目标从 A→B，说明改善比例。

## 第3段：改善机制
为什么会改善，不只报数字。

## 第4段：Bound/Gap
说明界来源、Gap、可以证明什么、不能证明什么。

## 第5段：方案结构
谁在主导解、哪类资源最紧、为什么。

## 第6段：核心图
图后“观察—原因—含义”。

## 第7段：独立验证
从最终文件重算，报告违规/差异。

## 第8段：Trade-off/局限
若次目标变差必须主动解释。

---

# 5.20 优化过程

若有多轮优化：
- 相同任务口径才能直接比较；
- 每个阶段写“做了什么→改善多少→为什么”。

优化图横轴可用阶段，纵轴主目标或相对改善。

---

# 5.21 模型检验

区分：
- 小实例/极端场景正确性；
- Validator；
- 指标反算；
- Constraint Slack。

---

# 5.22 消融

必须对应算法创新。

正文：
1. 哪个模块贡献最大；
2. 为什么；
3. 是否互补；
4. 是否只增加运行时间。

---

# 5.23 收敛

写：
> 前 N 轮快速改善，随后平台；后 M 轮无改善，因此停止。

禁止：
> 收敛到全局最优。

除非严格证明。

---

# 5.24 稳定性

写 seed 数和 Best/Mean/Std/Worst。

若波动大必须承认。

---

# 5.25 敏感性

每个参数：
1. 为什么选；
2. 基准；
3. 范围；
4. 固定回放/重优化；
5. 图表；
6. 机制；
7. 决策含义；
8. 结论边界。

---

# 5.26 模型评价

## 优点
不要写“科学准确”。

每个优点：
- 机制；
- 证据；
- 结果。

## 局限
- 什么限制；
- 为什么；
- 影响什么；
- 不影响什么。

## 改进
与局限一一对应。

---

# 5.27 结论

### 第1段
统一框架。

### 第2–4段
逐问核心结果 + 最强证据，不重讲算法。

### 最后一段
全题机制：
> 从 Q1 到 Q3，瓶颈怎样转移？

不要在结论首次出现新模型/新实验。

---

# 5.28 正文强调规则

按当前约定：

建议加粗：
- **具体核心算法**
- **核心自定义求解框架**
- 必要算法模块名

不加粗：
- 数字；
- 百分数；
- “问题一”；
- 普通模型名；
- 一般结论。

章节标题本身按模板处理。

---

# 5.29 First Impression Gate

第1页：
- 问题；
- 难点；
- 框架；
- 三问方法；
- 核心结果；
- 可信度。

第3页前：
- 三问递进；
- 总技术路线；
- 问题分析主体。

如果第3页还在大篇幅讲背景，FAIL。


---

# M6 视觉、参考文献、排版与提交

目标：保证最终作品不仅内容正确，而且“看得懂、引用真、格式对、能提交”。

---

# 6.1 Figure Contract

每张图在生成前先写：

```text
Figure ID:
Question:
Claim:
Input Data:
Figure Type:
Why this type:
Axes:
Units:
Legend:
Main message:
Paper location:
Caption:
```

没有 Claim 的图原则上不进正文。

---

# 6.2 图形选择

空间：map / scatter / MDS  
流动：Sankey / network / OD heatmap  
排班：Gantt / timeline  
收敛：best-so-far curve  
分布：ECDF / box / violin  
敏感：line / heatmap  
Gap：UB-LB plot  
多目标：Pareto frontier

---

# 6.3 禁止图

- 3D 柱图；
- 大类别饼图；
- 不同单位直接放同一普通柱图；
- 表已经足够清楚又重复画柱图；
- 无色标热力图；
- 无时间轴甘特；
- 收敛图不画 best-so-far；
- 图中文字过小；
- 图后没有正文分析；
- 纯装饰流程图。

---

# 6.4 图前/图后

图前：
> 为验证/观察……，绘制图X。

图后至少三句：
1. 观察到什么；
2. 为什么；
3. 对模型/结果意味着什么。

必要时：
4. 该图不能证明什么。

---

# 6.5 Figure Hierarchy

Hero Figure：全篇 1–2 张  
Core Evidence：每问 1–3 张  
Supporting：敏感性、补充诊断，可入附录

---

# 6.6 表格

优先三线表。

分类：
- Data Table；
- Symbol Table；
- Result Table；
- Evidence Table。

表后不逐项念数字，只写：
- 最大变化；
- 核心对比；
- 异常；
- 机制。

---

# 6.7 公式排版

每个关键公式：

\[
文字引入 \rightarrow 公式 \rightarrow 新符号解释 \rightarrow 现实含义
\]

正文真正会引用的公式才编号。

一个量全篇一个符号。

---

# 6.8 参考文献真实性 Gate

这是 V4.0 新增强制 Gate。

任何文献进入终稿前必须标记 `VERIFIED`。

## 核验优先级

优先核对：
1. 期刊/出版社官方页面；
2. DOI 官方解析页；
3. Crossref；
4. Web of Science / Scopus / Google Scholar 等索引；
5. 作者/机构正式仓储。

不允许只根据：
- 博客；
- 二次转载；
- AI记忆；
- 搜索摘要标题；

就写完整参考文献。

---

# 6.9 每篇文献必须核验的字段

```text
Authors
Exact Title
Venue
Year
Volume
Issue
Pages / Article Number
DOI
Publisher URL
```

如果任一字段无法确认：
- 不要猜；
- 标记 `PARTIAL`；
- 不进入最终参考文献，除非官方格式允许且核心字段已可靠确认。

尤其禁止“补一个看起来像真的 DOI”。

---

# 6.10 Reference Ledger

最终至少包含：

| Key | Authors | Title | Year | Venue | DOI | Verified Source | Used For | Cited? |
|---|---|---|---:|---|---|---|---|---|

每一条必须同时满足：
- `Verified = YES`
- `Cited = YES`

---

# 6.11 正文引用 Gate

参考文献不是装饰。

必须满足：

### 规则 A
参考文献表中的每一条都至少在正文引用一次。

### 规则 B
正文中的每个 `[n]` 都必须能映射到参考文献第 n 条。

### 规则 C
不能出现：
- `[7]` 但列表只有 6 条；
- 列表有 `[9]` 但正文从未出现 `[9]`；
- 同一论文重复列两次不同编号。

### 规则 D
若采用数字顺序编码：
- 参考文献编号原则上按首次出现顺序排列；
- 如果官方模板另有规定，官方优先。

---

# 6.12 什么地方应该引用

以下位置原则上需要引用：

## 模型/算法首次正式出现
例如：
> 使用 **ALNS** 进行大邻域搜索[4]。

最好引用算法原始论文或权威来源。

## 经典模型定义/分类
例如：
> 该问题可视为 Pickup and Delivery Problem 的扩展[2,3]。

## 外部理论/公式来源
不是自己推导的经典结论应引用。

## 公开数据/行业参数
若不是赛题附件提供，应引用数据源。

## 与文献方法比较
引用对应论文。

---

# 6.13 什么地方不需要乱引

通常不需要给以下内容塞引用：
- 赛题附件直接给出的数值；
- 自己运行得到的结果；
- 自己推导的简单代数；
- 自己定义的变量；
- 常识性连接句。

引用应服务于：
> 来源、归属、可追溯性。

---

# 6.14 引用位置

引用应紧跟被支持的陈述。

推荐：

> Ropke 和 Pisinger 提出的自适应大邻域搜索通过动态调整算子权重改善搜索效率[4]。

不推荐整段最后堆：
> ……[1][2][3][4][5]

而读者不知道谁支持哪句话。

---

# 6.15 数字编号格式

若官方格式使用数字编号：

正文可使用：
- [1]
- [2,3]
- [4–6]

但必须统一风格。

不要：
- 一会儿上标；
- 一会儿括号；
- 一会儿作者年份。

官方模板优先。

---

# 6.16 算法引用策略

优先引用：
1. 原始提出论文；
2. 权威改进论文；
3. 高相关应用论文。

例如论文使用：
- **ALNS**：至少应有原始/经典 ALNS 文献；
- **Column Generation**：应有 Dantzig-Wolfe/列生成或 Branch-and-Price 权威来源；
- **CP-SAT**：若正文详细依赖其机制，可引用官方/权威技术资料；
- 经典 VRP/PDPTW：可引用经典或综述。

避免为了数量堆大量低相关文献。

---

# 6.17 高分论文作为参考来源

高分参赛论文可以用于：
- 对比方法；
- 写作结构；
- Benchmark；

但若正文实质采用其特定方法/结构，应明确引用对应论文或其公开来源。

若竞赛规则不允许引用未公开参赛材料，则不能直接列入参考文献；只在内部 Benchmark 使用。

---

# 6.18 文献核验流程

每条候选文献：

```text
Step 1: 搜索准确标题
Step 2: 打开 publisher / DOI / Crossref
Step 3: 核对作者
Step 4: 核对题名
Step 5: 核对期刊/会议
Step 6: 核对年份卷期页码
Step 7: 核对 DOI
Step 8: 写入 Reference Ledger
Step 9: 标记正文首次引用位置
Step 10: 最终 Citation Coverage Audit
```

如果搜索不到：
> 不准凭记忆补齐。

---

# 6.19 Citation Coverage Audit

最终自动检查：

```text
References in bibliography: N
Unique citations in text: M
Orphan bibliography entries:
Broken citation numbers:
Duplicate references:
Unverified references:
PASS / FAIL
```

只有：
- Orphan = 0；
- Broken = 0；
- Duplicate = 0；
- Unverified = 0；

才 PASS。

---

# 6.20 AI 使用与参考文献规则冲突

若官方比赛规定：
- AI 工具必须作为参考文献第一条；
- 或 AI 使用详情必须放附录；

则官方规则覆盖“按首次出现顺序”的默认规范。

必须在 M0 读取官方规则后，把这项写进 Submission Contract。

---

# 6.21 版式

官方模板优先。

若未规定，可默认：
- A4；
- 正文 10.5–12 pt；
- 首行 2 字符；
- 行距约 1.3–1.5；
- 图题下方；
- 表题上方；
- 页码底部居中；
- 一级/二级标题层次明显；
- 页内图、表、公式与文字密度平衡。

---

# 6.22 加粗

正文中只建议加粗：
- **核心具体算法**
- **核心自定义求解框架**
- 必要算法模块名

不加粗：
- 数字；
- 百分比；
- 普通结论；
- 普通模型名称。

---

# 6.23 First Page Gate

第一页必须让评委知道：
- 研究对象；
- 难点；
- 总方法；
- 各问方法；
- 核心结果；
- 可信度。

---

# 6.24 First Three Pages Gate

第3页前应完成：
- 问题重述；
- 三问递进；
- 主要问题分析；
- 总体技术路线/框架图。

---

# 6.25 Page Density Audit

避免：
- 一页全是字；
- 一页全公式；
- 一页只有一张大图；
- 大量空白；
- 表格挤成不可读。

---

# 6.26 支撑材料

建议包含：
- 核心代码；
- Validator；
- final results；
- README；
- requirements；
- run_all；
- figure source data；
- sensitivity/ablation records；
- AI usage；
- Reference Ledger。

---

# 6.27 Reproducibility Gate

必须能回答：
- 输入在哪里；
- 环境；
- 命令；
- 随机种子；
- 输出；
- 哪个文件是 SSOT；
- 如何运行 Validator。

---

# 6.28 Final Submission Gate

逐项检查：
- 文件名；
- 页数；
- 匿名；
- 参考文献；
- 正文引用；
- AI规则；
- 附录；
- 支撑材料；
- 结果文件；
- PDF 可打开；
- 图表清晰；
- 公式无乱码。

输出：

```text
VISUAL: PASS/FAIL
REFERENCE INTEGRITY: PASS/FAIL
CITATION COVERAGE: PASS/FAIL
TYPOGRAPHY: PASS/FAIL
REPRODUCIBILITY: PASS/FAIL
AI COMPLIANCE: PASS/FAIL
SUBMISSION: PASS/FAIL
```
