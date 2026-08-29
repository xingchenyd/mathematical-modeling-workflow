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
