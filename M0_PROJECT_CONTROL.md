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
