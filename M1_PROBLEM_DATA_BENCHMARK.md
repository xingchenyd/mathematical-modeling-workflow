# M1 题意与数据联合理解
## Problem & Data Forensics

M1 是 V4.3 的核心前置阶段。

目标不是“清洗完数据”，而是回答：

> 我们是否已经有足够证据证明自己没有理解错题、没有理解错数据，并知道哪些结构真正决定建模？

只有 M1 PASS 才进入 M2。

---

# 1.1 第一遍读题：现实系统

不写公式，不选算法。

输出：
- 实体；
- 资源；
- 行为；
- 时间/空间；
- 谁在做决策；
- 最终需要什么结果。

用 100–200 字写“现实问题本质”。

---

# 1.2 第二遍读题：逐问任务

每问：

```text
Known:
Need to decide/predict:
Must satisfy:
Primary objective:
Secondary objective:
Need to output:
Depends on which earlier question:
```

此时仍不写“用 ALNS / XGBoost”。

---

# 1.3 第三遍读题：规则取证

把自然语言拆成可执行规则。

重点扫描：
- 至少/至多；
- 仅/可以/必须；
- 先/后；
- 首次/最后；
- 每一个/总体；
- 逐段/累计；
- 是否取整；
- 时间窗作用于开始还是完成；
- 状态何时更新；
- 资源何时释放；
- 一级目标是否必须严格优先。

---

# 1.4 Pitfall Ledger：坑点不只记“正确答案”

每个 P0/P1 坑点必须填写：

| 字段 | 内容 |
|---|---|
| Original Rule | 题面原句 |
| Correct Interpretation | 正确数学含义 |
| Plausible Wrong Interpretation | 最容易发生的错误理解 |
| Consequence | 错后会造成什么结果偏差 |
| Model Impact | 影响变量/目标/约束哪一层 |
| Detection Test | 用什么最小例子/反例发现 |
| Validator Rule | 最终程序如何检查 |
| Severity | P0/P1/P2 |

### 原则

如果不能解释“错了会怎样”，说明这个坑还没有真正理解。

---

# 1.5 Wrong-Path Analysis：故意模拟错误路线

对 P0/P1 坑点至少做一次：

> 如果按 plausible wrong interpretation 建模，会出现什么？

输出：
- 伪可行；
- 伪最优；
- 指标系统偏高/偏低；
- 候选空间错误缩小；
- 未来泄漏；
- 约束失效；
- 方向性偏差。

它的目的不是浪费时间，而是建立“为什么必须这样解释”的证据。

---

# 1.5A Scheduled Re-read R1 Preparation

在进入数据结构分析前，先做一次短复读：
- 将 Problem Contract 与原题逐句比对；
- 将 Pitfall Ledger 与原题高风险词逐项比对；
- 标记仍无法确定的语义，不用算法假设强行填空。

真正进入 M2 前还要再执行一次 R1 完整复读。

# 1.6 Data Inventory：先知道到底有什么数据

对所有文件/Sheet/表输出：

```text
File:
Sheet/Table:
Rows:
Columns:
Primary key candidate:
Time field:
Spatial field:
Entity represented:
Question(s) used for:
```

禁止只打开主文件而漏附件。

---

# 1.7 Data Dictionary：逐字段理解语义

对会进入模型/EDA的字段建立：

| 字段 | 类型 | 单位 | 业务含义 | 来源 | 可用时点 | 缺失/异常 | 用途 |
|---|---|---|---|---|---|---|---|

尤其确认：
- 累计量 vs 增量量；
- 状态 vs 决策；
- 真实值 vs 模型生成值；
- 时间点 vs 时间段；
- 计划值 vs 实际值；
- 个体ID vs 分组ID；
- 经/纬度 vs 路网距离。

字段含义不明时，不得擅自猜测。

---

# 1.8 Data Relationship Map：看懂跨表关系

绘制/文字化：

```text
Table A -- key --> Table B
Table B -- key/time --> Table C
...
```

检查：
- 主键是否唯一；
- 外键是否全覆盖；
- 是否有孤立 ID；
- 多对一/一对多关系；
- 时间粒度；
- 空间粒度；
- 同一实体是否在不同表中换了编码。

---

# 1.9 Data Quality Audit

## 文件层
编码、Sheet、版本、重复文件。

## 字段层
类型、缺失、重复、异常、单位、非法范围。

## 逻辑层
守恒、时间顺序、起终点、集合关系、唯一性。

## 跨表层
ID、单位、时间口径、空间口径一致。

输出：

```text
Issue:
Evidence:
Treatment:
Will treatment change the problem?
Residual risk:
```

---

# 1.10 缺失与异常不能机械处理

禁止默认：
> 缺失值全部均值填补；异常值全部删除。

必须先判断：
- 缺失机制；
- 是否题面有特殊含义；
- 是否代表“不适用”；
- 是否是数据错误；
- 是否是稀有但真实的关键样本。

每个处理写：
> 为什么处理、处理后可能带来什么偏差。

---

# 1.11 Information Availability

预测/动态题冻结决策时点的信息集：

```text
Decision Time:
Available:
Unavailable future info:
Derived features:
Leakage risk:
```

任何特征必须证明在决策时已可得。

---

# 1.12 Target Observability

先问：
> 目标是否真的被观测？

如果未观测/右删失：
- 不能把模型外推当 ground truth；
- 结论只能称估计/外推/区间；
- 后续 Claim Strength 自动受限。

---

# 1.13 Experimental Unit

数据行数不等于独立样本数。

记录：
- observation rows；
- independent units；
- repeated measurements；
- groups/batches；
- resampling unit；
- inference unit。

防止伪重复。

---

# 1.13A Conceptual System Sketch：先有现实机制，再有公式

在复杂题中，正式数学表达之前先建立一个概念模型草图。可以是纸笔图、流程图、状态图、空间示意或文字结构图。

至少标出：
- 实体/对象；
- 资源；
- 空间关系；
- 时间/状态；
- 信息流；
- 决策；
- 约束作用位置；
- 输出。

它解决的问题是：
> “我们现在到底在给什么现实系统写方程？”

概念图必须与 Data Relationship Map 区分：前者描述现实系统，后者描述数据文件之间的关系。

# 1.14 Structural EDA：让数据先说话

EDA 不以“图漂亮”为目标。

每个探索任务：

```text
Question:
Method/Figure:
Observed Structure:
Evidence:
Alternative explanation:
Modeling consequence:
Confidence:
```

优先：
- 分布与长尾；
- 空间簇；
- OD/网络；
- 时间趋势/周期/时间窗；
- 资源瓶颈；
- 稀疏性；
- 组间差异；
- 共线/混杂；
- 可聚合/可交换性；
- 不变性；
- 约束触边情况。

---

# 1.15 Data Findings Ledger

每个真正影响后续模型的发现：

```text
Finding ID:
Observation:
Evidence:
Mechanism hypothesis:
Modeling consequence:
Alternative explanation:
Confidence:
Related figure/table:
```

例如：
> 窄时间窗任务占比高 → 排班阶段必须优先保可行；不能只做静态最短路。

---

# 1.16 数据规律必须转成“建模后果”

每一个核心 Finding 必须至少导致一种：

- 删除不合理模型；
- 加入新约束；
- 聚合/分层；
- 特征构造；
- 搜索空间压缩；
- Solver 选择；
- 验证方式改变；
- 敏感性参数选择。

没有建模后果的图，多数不值得进正文。

---

# 1.16A Mechanism Attribute Classification

结合题面、Conceptual Sketch 和 Data Findings，对问题先做机制定性：

- 离散 / 连续 / 混合；
- 确定 / 随机；
- 静态 / 动态；
- 同构 / 异构；
- 集中式 / 网络式；
- 2D / 3D / 图网络；
- 点 / 区域 / 路径 / 流；
- 无状态 / 状态递推；
- 单阶段 / 多阶段；
- 全覆盖 / 部分覆盖 / K覆盖 / 概率覆盖（若适用）。

这一步只决定“数学表达需要具备什么性质”，还不直接指定算法。

# 1.17 Statistical Design Audit

涉及显著性/因素影响时检查：
- 非正交；
- 批次混杂；
- 共线；
- 小样本；
- 多重比较；
- 选择后检验；
- 伪重复。

不支持因果时，只报告关联/策略差异。

---

# 1.18 Assumption Risk Register

假设不是写作装饰。

每个重要假设：

```text
Assumption:
Why needed:
Evidence/support:
What it simplifies:
If false, consequence:
Sensitivity/validation plan:
```

禁止“为了方便计算”而不解释影响。

---

# 1.19 Benchmark：此时才看别人怎么解

先完成自身 Problem/Data Forensics，再看高分论文/文献。

否则容易：
> 先被别人模型锚定，再强行把自己的数据解释成那个模型。

Benchmark Matrix：
- 问题抽象；
- 数据处理；
- 坑点；
- 模型；
- Solver；
- Bound；
- Validator；
- 实验；
- 写作；
- 局限。

---

# 1.20 Delta Matrix

比较：
- 我们发现了什么，他们没发现；
- 他们处理了什么，我们漏了；
- 差距属于数据、模型、算法还是证据。

用于排优先级，不用于吹嘘。

---

# 1.21 Problem Structure Classification

结合题意 + 数据后，再判断属于：
- descriptive；
- diagnostic；
- predictive；
- prescriptive/optimization；
- simulation；
- mechanism；
- evaluation；
- hybrid。

这是“选模型族”的前一步，不是算法名称。

---

# 1.22 Modeling Eligibility Report

M1 最终必须输出：

```text
MODELING ELIGIBILITY REPORT

1. Real problem:
2. Q1/Q2/... exact requirements:
3. P0/P1 pitfalls:
4. Consequence of wrong interpretations:
5. Data inventory:
6. Key data dictionary issues:
7. Data relationship map:
8. Data quality status:
9. Information availability / leakage:
10. Target observability / experimental unit:
11. Main structural findings:
12. Conceptual system sketch / mechanism attributes:
13. Usable invariances / aggregation:
14. Dangerous assumptions:
15. Model families ruled out:
16. Model families still plausible:
17. Main unknown risks:
18. Evidence gaps:
19. R1 Re-read status:
20. Gate = PASS / FAIL
```

### PASS 标准

只有当：
- P0 解释完成；
- 关键字段语义明确；
- 跨表关系明确；
- 数据问题已处理或有明确风险；
- 至少若干核心结构 Finding；
- 主要假设已识别；
- 没有明显信息泄漏；

才进入 M2。

M1 PASS 不意味着“再也不回头”。后续出现新证据时必须回退。
