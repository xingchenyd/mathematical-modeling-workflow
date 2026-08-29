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
