# MASTER ROUTER V4.3

## 1. 总生命周期

\[
M0 \rightarrow M1 \rightarrow M2 \rightarrow (M3\leftrightarrow M4) \rightarrow M5 \rightarrow M6 \rightarrow M7
\]

这是 **有 Gate、可回退** 的生命周期。

---

## 2. M0：确认项目边界

必须确认：
- 官方题面/规则版本；
- 全部数据附件；
- 输出要求；
- 当前已有代码/论文/结果；
- 数据来源与版本；
- 参考资料来源。

M0 FAIL → 不进入 M1。

---

## 3. M1：取得“建模资格”

M1 必须联合完成：
- Problem Forensics；
- Data Forensics；
- Pitfall & Wrong-Path Analysis；
- EDA & Findings；
- 信息可用性/实验单位/目标可观测性；
- Benchmark；
- Problem Structure Classification。

最后输出 `MODELING ELIGIBILITY REPORT`。

Gate=FAIL → 继续 M1，不允许推荐最终模型和算法。

---

## 3.1 M1→M2 前的 Re-read Checkpoint R1

正式取得建模资格前，重新逐句对照原题：
- 是否有条件只存在题面而未进入 Problem Contract；
- 是否遗漏总量、先后、范围、优先级或输出口径；
- 每个 P0/P1 是否已进入 Pitfall Ledger；
- Conceptual System Sketch 是否与题面一致。

R1 FAIL → 继续 M1。

## 4. M2：选择数学抽象与方法

M2 只消费已经通过 M1 的证据。

顺序：
1. 数学结构；
2. 候选模型；
3. B0/B1/B2；
4. Bound；
5. Search Space；
6. Formal Model；
7. Solver Architecture。

禁止先从“我熟悉什么算法”出发。

---

## 5. M3/M4：求解—验证反馈循环

M3：
> 求解、诊断、扩展、优化。

M4：
> 验证、Gap、消融、稳定、不确定性、常识审计。

### Backtrack Router

M4/M3 若发现：

- 题面解释/数据语义错误 → 回 M1；
- 模型遗漏关键机制 → 回 M2；
- 候选空间/算法不足 → 回 M3；
- 证据不足 → M4；
- 只是论文表达问题 → M5/M6。

---

## 5.1 第二、第三次 Re-read

### R2 — 第一版完整结果后
重新读题，检查“模型虽然能跑，但解决的是不是原题”。

### R3 — 模型冻结前
执行题面 → 数学模型 → 代码 → Validator 四联审计。

任一 R2/R3 发现 P0/P1 → 按 Backtrack Router 回退。

## 6. M5–M7

M5：论文  
M6：图表、真实引用、排版、提交  
M7：答辩

摘要最后定稿。

---

## 7. 题型分支

### 预测/统计/寿命/小样本
加载 `branches/B1_PREDICTION_STATISTICAL_INFERENCE.md`

### 预测进入优化
加载 `branches/B2_PREDICTION_TO_DECISION.md`

### 动态/随机/反馈
加载 `branches/B3_DYNAMIC_STOCHASTIC_DECISION.md`

### 现实/历史方案比较
加载 `branches/B4_COUNTERFACTUAL_EXTERNAL_VALIDATION.md`

---

## 8. 状态

```text
M0 PROJECT CONTROL: PASS/FAIL
M1 PROBLEM & DATA UNDERSTANDING: PASS/FAIL
M2 MODEL DESIGN: PASS/FAIL
M3 SOLVER: ACTIVE/FROZEN
M4 EVIDENCE: PASS/PARTIAL/FAIL
M5 PAPER: DRAFT/FROZEN
M6 SUBMISSION: PASS/FAIL
M7 DEFENSE: PASS/FAIL
```

只有最终所有必要 Gate 通过才可输出：

```text
MODEL CONVERGED — FREEZE
PAPER CONVERGED — FREEZE
READY TO SUBMIT
```


---

# V4.3.3 官方规则解释增强

M0 开始时，必须把所有提醒分类为：
- NATIONAL HARD RULE
- REGIONAL HARD RULE
- OFFICIAL FAQ
- ADVISORY
- INTERNAL

M4 对“具有明确数值答案/明确附件格式”的题目启用：
`Reference-Range / Answer-Accuracy Audit`
和
`Structured Attachment Validator`。

M6 必须额外验证：
- 摘要页从1开始编页码；
- 非图片/可搜索PDF为强烈推荐而非全国取消资格条件；
- 全部完整代码出现在论文附录；
- 支撑材料清单放附录靠前；
- AI工具不自动列入参考文献；
- 不要求自行做AIGC率检测；
- 全国附录不限页，赛区20页要求只有在正式赛区文件存在时才升级为硬规则。


---

# V4.3.3 湖南赛区默认覆盖

进入 M0 时自动加载：
`docs/HUNAN_2026_COMPETITION_PROFILE.md`

M5/M6 默认执行：
- abstract page = no visible page number；
- body first page = 1；
- body target 29–30 / hard cap 30；
- appendix cap 20；
- full runnable source in appendix；
- LaTeX-first；
- searchable/non-image PDF only。

这些不是可选建议，而是当前用户工作流的执行默认值。
