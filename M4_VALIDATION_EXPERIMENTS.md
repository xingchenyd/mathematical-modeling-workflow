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
