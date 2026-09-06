# M7 答辩与评委审查

答辩不是论文缩写，而是把最重要的判断链展示出来：

\[
难点 \rightarrow 证据 \rightarrow 为什么这样建 \rightarrow 结果 \rightarrow 可信度 \rightarrow 边界
\]

---

# 7.1 前2–3页

必须让评委看到：
- 全题闭环；
- 数据流；
- 小问依赖；
- 最大 P0/P1 难点；
- 总方法。

---

# 7.2 每一问

建议三类页：

### 问题与选择
> 最难点是什么？哪条数据/规则决定了模型？

### 方法
> 只讲2–4个决定性机制。

### 证据
> 主结果 + Baseline + Gap/误差 + Validator/区间。

---

# 7.3 Why-not-Alternative

准备回答：
- 为什么不用常见算法；
- 为什么不用更复杂模型；
- 为什么不随机切分；
- 为什么不连续优化；
- 为什么 Gap 不是全局；
- 为什么某字段不能使用。

---

# 7.4 Pitfall Defense

每个最重要 P0 坑点准备：
1. 正确解释；
2. 错误解释会导致什么；
3. 我们如何检测；
4. Validator 如何保证。

这类回答非常能证明“不是碰巧算出结果”。

---

# 7.5 Data Defense

准备：
- 数据文件关系；
- 关键字段；
- 主要数据问题；
- 最影响建模的3个规律；
- 信息泄漏/独立样本/外推边界。

---

# 7.5A Local Case Study Defense

复杂模型准备一个“30–60秒能讲清”的局部案例：
- 一条小路线；
- 一个局部覆盖；
- 一个动态状态；
- 一个预测样本。

目的是回答：
> “你们这个公式在现实里到底做了什么？”

PPT上的案例图可以采用16:9页面布局，但论文本身不强制图形比例。

# 7.6 可行性→卓越性

先证明：
- 规则正确；
- 0硬约束错误；
- 输出可复算。

再证明：
- 比 B2 好；
- Gap；
- 稳定；
- 鲁棒；
- 现实解释。

---

# 7.7 备份页

建议：
- Pitfall Ledger 摘要；
- Data Relationship Map；
- 关键公式；
- solver log；
- Gap；
- Validator；
- 消融；
- 敏感性；
- 参考文献；
- 失败方案；
- Why-not 对照。

---

# 7.8 Defense Gate

```text
Problem understanding:
Data understanding:
Pitfall explanation:
Model motivation:
Why-not alternatives:
Feasibility:
Performance:
Uncertainty:
Limitations:
Backup:
PASS/FAIL
```
