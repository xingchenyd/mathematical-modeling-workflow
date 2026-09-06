# M0 项目控制、材料与证据治理

M0 的任务不是建模，而是确保后面所有分析都建立在正确版本、完整材料和可追溯事实之上。

---

# 0.1 Material Manifest

读取并登记：

| 类型 | 文件/来源 | 版本 | 是否官方 | 是否可读 | 用途 |
|---|---|---|---|---|---|
| 题面 | | | | | |
| 数据 | | | | | |
| 规则 | | | | | |
| 模板 | | | | | |
| 评分/说明 | | | | | |
| 已有代码 | | | | | |
| 已有论文 | | | | | |
| 高分论文 | | | | | |

如果存在多版本：
> 先冻结“当前权威版本”。

---

# 0.1A Competition Rule Profile

在读取题目同时冻结当届官方规则：

```text
Contest:
Official duration:
Paper page limit:
Abstract rule:
Directory allowed?:
Submission files:
AI usage rule:
Communication restrictions:
Special supporting-material requirements:
```

官方规则永远覆盖培训经验和本手册默认值。

若为 2026 CUMCM，加载 `docs/CUMCM_2026_RULE_PROFILE.md`。

# 0.2 Data Source Manifest

在真正分析数据前，先登记：

```text
File:
Format:
Sheet/Table:
Source:
Official/External:
Time range:
Spatial range:
Unit hints:
Likely keys:
Known caveats:
```

这里不做建模，只防止漏文件、混版本、混来源。

---

# 0.3 Problem Contract

逐问记录：

```text
Question:
Real-world task:
Known:
Decision / Prediction target:
Primary objective:
Secondary objectives:
Hard constraints:
Soft constraints:
Required outputs:
Evaluation metrics:
Dependencies:
Ambiguous wording:
Forbidden changes:
```

Problem Contract 是后续“有没有解决错问题”的审计基准。

---

# 0.4 Acceptance Contract

每问提前定义：

- 题目所有要求均回答；
- 输出格式正确；
- 硬约束可复核；
- 主指标可反算；
- Baseline 存在；
- Bound/Benchmark 已尝试；
- 重要假设有边界；
- 最终结论有对应证据。

---

# 0.4A Competition Time Budget & Freeze Strategy

若为 2026 CUMCM：
- 正式竞赛结束/最终 MD5 时点：9月13日20:00；
- 正式电子文档上传另有后续窗口，不等于模型还可以继续修改；
- 20:00 后不得因为上传窗口仍开放而继续改变论文/支撑材料内容，最终文件必须与备案 MD5 一致。

其余时间预算不采用固定“每问22小时”等硬规则。

# 0.4B Competition Independence & Communication

开始竞赛前把当届独立性规则冻结为 P0：

- 赛题必须由本队独立完成；
- 竞赛期间不得与队外人员讨论当届赛题；
- 指导教师不得进行赛题解释、选题建议、资料提供或论文修改指导；
- 不在 GitHub、CSDN、知乎、微信群等平台浏览/发布/讨论当届赛题相关内容；
- 使用普通公开资料时做好 Reference Ledger 与正文引用。

# 0.4C Anonymous Submission Contract

提交相关文件必须无：
- 姓名；
- 学号；
- 学校；
- 赛区；
- 指导教师；
- 可识别文件路径/用户名；
- PDF/Word 文档属性中的身份信息。

论文、附录、源代码注释、支撑材料文件名和文件夹名均纳入匿名检查。

# 0.4D 2026 MD5 & Upload Contract

若为 2026 CUMCM，冻结：

```text
Competition/MD5 deadline: 2026-09-13 20:00
Electronic upload window: 2026-09-13 20:30 ~ 2026-09-14 14:00
Paper <= 20MB
Support archive <= 20MB
Electronic paper: PDF/Word, single file, uncompressed
Support: ZIP/RAR
Electronic paper excludes commitment + number page
Electronic first page = abstract
``` 



不采用固定“每问22小时”或“6小时以后绝不改”的硬规则，而根据官方总时长建立动态时间预算。

至少划分：
- Understanding / Modeling；
- Solving / Optimization；
- Validation / Evidence；
- Paper Finalization；
- Submission Audit。

原则：
- 越靠近截止时间，越提高验证、论文一致性和提交风险的权重；
- 最后一段时间不再进行高风险模型大改；
- 最后约 5%–8% 的总竞赛时间优先保留给终稿、附件、AI声明、PDF与提交检查；
- 最后约 60 分钟原则上只处理 P0 提交错误，不“顺手再跑一个新模型”。

具体时点由比赛总时长和当前进度动态计算。

# 0.5 初始风险清单

M0 只做“风险占位”，具体分析在 M1。

扫描：
- 时间/单位；
- 向上/向下取整；
- 至少/至多；
- 首次/最后；
- 先/后；
- 动态状态；
- 是否允许跨期；
- 多目标优先级；
- 是否存在未观测目标；
- 是否存在未来信息；
- 外部数据口径。

将可疑项放入 Pitfall Ledger，状态 `TO_ANALYZE`。

---

# 0.6 Issue Ledger

P0：会让答案错误/违规  
P1：核心方向错误/主要结论不可信  
P2：证据不足/实验不完整  
P3：语言/排版

格式：

```text
Issue:
Severity:
Evidence:
Impact:
Fix:
Success test:
Status:
```

---

# 0.7 Decision Log

重大决策：

```text
Decision:
Alternatives:
Why:
Evidence:
Risk:
Revisit trigger:
```

没有新证据不要反复推翻。

---

# 0.7A Living Paper Evidence Store

从比赛开始就维护 `paper/evidence_draft/` 或等价结构，而不是等 M5 才开始整理素材。

按来源沉淀：
- M1：问题分析、数据规律、Pitfall、假设素材；
- M2：模型选择、公式、Why-not、Bound素材；
- M3：算法架构、优化历史；
- M4：Validator、Gap、消融、收敛、稳定、敏感性。

这些内容仍是“证据草稿”，不得直接视为终稿。M5 再按评委阅读顺序重写。

# 0.8 Single Source of Truth

最终数值只来自统一结果源，例如：

```text
results_master.csv
final_results.json
```

摘要、表、图、结论不能各自手改。

---

# 0.9 Claim Ledger

```text
Claim ID:
Claim:
Strength C0-C5:
Evidence:
SSOT field:
Validator:
Paper section:
Status:
```

C0 Observation  
C1 Feasible  
C2 Improved  
C3 Candidate-domain optimal  
C4 Bound-supported near-optimal  
C5 Proven global optimal

---

# 0.10 Reference Ledger

从项目开始维护，避免最后拼文献。

未核验文献不得进入终稿。

---

# 0.11 M0 Gate

PASS 条件：
- 权威题面/规则确定；
- 所有数据附件已登记；
- 当前项目版本确定；
- 输出要求明确；
- Problem/Acceptance Contract 初版完成；
- 高风险措辞已进入待分析清单；
- 当届官方 Rule Profile 已冻结；
- 时间预算与提交冻结原则已建立。


---

# 0.12 Official / Regional / Advisory Rule Classification【V4.3.2】

所有赛前提醒先分类：

```text
NATIONAL HARD RULE
REGIONAL HARD RULE
OFFICIAL FAQ / INTERPRETATION
ADVISORY
TEAM INTERNAL DEADLINE
```

冲突处理：

\[
National > Regional > OfficialFAQ > Advisory > Internal
\]

注意：
- 赛区规则不得违反全国硬规则；
- 老师经验不能覆盖官方格式；
- 内部提前截止只能更早，不能改变全国最终截止。

---

# 0.13 Registration Deadline Profile — 2026【V4.3.2】

2026全国竞赛管理系统报名注册相关截止：
> 9月7日20:00。

团队/学校可以设置更早内部反馈时间，但必须标记：
`TEAM INTERNAL DEADLINE`

不能写成全国统一截止。


---

# 0.14 User-confirmed Hunan Override【V4.3.3】

本仓库当前已确认以下本地执行口径：

```text
Abstract visible page number: NO
Body starts at page: 1
Body target: 29–30
Body hard cap: 30
Appendix cap: 20
Appendix source: full runnable final code
PDF: native/searchable/non-image
Default authoring: LaTeX
```

这些字段在本工作流中视为：
`HUNAN ACTIVE RULE`

不再由通用全国默认排版自动覆盖。
