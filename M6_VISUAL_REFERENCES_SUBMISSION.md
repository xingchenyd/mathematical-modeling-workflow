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
