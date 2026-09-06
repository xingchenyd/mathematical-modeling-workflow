# M6 视觉、参考文献、排版、复现与提交

---

# 6.0 Official Rule Profile First

排版前先加载当届官方格式，不能把培训经验当作硬规则。

例如 2026 CUMCM：
- 摘要专用页原则上不超过一页；
- 正文从第四页开始，不要目录，正文不超过30页；
- 引用公开资料必须列参考文献并在正文标注；
- 官方未统一规定字号、字体、行距和颜色时，不得把个人培训偏好冒充官方要求。

详见 `docs/CUMCM_2026_RULE_PROFILE.md`。

# 6.1 Figure Contract

每张图：

```text
Claim:
Data source:
Why this figure:
Why this chart type:
Axes/Units:
Expected takeaway:
Paper location:
```

---

# 6.2 数据图的职责

EDA 图必须对应 Data Findings Ledger。

优先：
- 结构；
- 瓶颈；
- 时间/空间；
- 分布；
- 关系；
- 模型假设检查。

禁止为了“数据处理有图”而画无意义统计图。

---

# 6.3 结果图的职责

一张图证明一个机制：
- 收敛；
- Gap；
- 资源冲突；
- Pareto；
- 灵敏度；
- 不确定性；
- 解结构。

---

# 6.4 图前/图后

图前：
> 为什么需要看它。

图后：
1. 看到了什么；
2. 为什么；
3. 对模型/结论意味着什么；
4. 必要时说明不能证明什么。

---

# 6.4A Evidence Density > Page Count

页数上限是约束，不是必须填满的目标。

优先删除：
- 不支持任何 Claim 的图；
- 重复同一数据的图+表；
- 大段背景百科；
- 为凑页数添加的算法介绍；
- 无结果意义的调试图。

判断标准：
> 删除这一段/图会不会削弱一个重要论证？

不会 → 删除或移附录。

# 6.5 表格

优先三线表。

表后不逐个念数字，只分析：
- 关键差异；
- 机制；
- 异常；
- Trade-off。

---

# 6.5A Color + Grayscale Dual Audit

彩图可以使用，但不得让颜色成为唯一信息编码。

最终图同时检查：
- 彩色屏幕；
- 灰度打印/预览。

必要时同时使用：
- 线型；
- marker；
- 填充纹理；
- 文字标签。

避免仅依赖红/绿区别。

图的长宽比由内容和版面决定，论文图不强制 16:9。

# 6.6 Reference Integrity Gate

每篇终稿文献必须核验：
- 作者；
- 准确题名；
- Venue；
- 年份；
- 卷期/页码/文章号；
- DOI（如有）；
- Publisher/DOI/Crossref等可靠来源。

查不到不猜。

---

# 6.7 Citation Coverage

数字编号制下：

- 参考文献每条至少正文引用一次；
- 正文 `[n]` 必须对应第 n 条；
- 无重复；
- 无孤儿条目；
- 无未核验条目。

算法/经典模型首次正式使用时优先引用原始或权威文献。

---

# 6.8 引用位置

引用紧跟被支持的陈述。

不要整段末尾堆 `[1][2][3][4]`。

---

# 6.9 版式

官方模板优先。

默认：
- 字体可读；
- 首行缩进；
- 图题下、表题上；
- 图表公式与文字密度平衡。

---

# 6.10 强调

正文只建议加粗：
- 核心具体算法；
- 核心自定义求解框架；
- 必要算法模块。

数字、百分比、普通结论不加粗。

---

# 6.10A Contest Communication Compliance

竞赛期间必须服从当届交流与网络使用纪律。

以 2026 CUMCM 为例，官方规则明确禁止在贴吧、QQ群、微信群、直播间、知乎、小红书、CSDN、GitHub 等交流平台浏览、发布或讨论与**当届赛题相关**的内容。

因此：
- 不能在竞赛期间搜索 GitHub 上的当届赛题现成解；
- 不能公开上传当届题目、代码、结果用于交流；
- 可以依据官方允许范围查阅一般性公开资料、学术论文、算法文档，但必须避免进入当届赛题讨论/答案交流。

规则以当届官方文件为准。

# 6.11 Reproducibility

必须能回答：
- 输入；
- 环境；
- 命令；
- seed；
- 输出；
- SSOT；
- Validator。

---

# 6.11A AI Usage Compliance — 2026 CUMCM

若当届为 2026 CUMCM，AI 使用遵守官方试行规定：
- 核心建模和分析应主要由参赛队主导；
- AI 生成内容必须逐项人工检查与验证；
- 论文参考文献之前放置“AI工具使用声明”；
- 若使用 AI，支撑材料中提交“AI工具使用详情.pdf”，记录工具/模型、使用阶段、主要提示方式、采纳修改和人工核验。

不要把“AI一定会被某种水印/查重检测”之类未经官方支持的说法写成规则。

# 6.11B Submission Freeze Window

根据比赛总时长动态设置封版窗口。

推荐原则：
- 截止前约 5%–8% 总时长：停止高风险模型重构，重点处理论文、图表、引用、附件和一致性；
- 截止前约 60 分钟：原则上只修 P0 提交风险；
- 任何新结果若不能完成 Validator + SSOT + 论文一致性闭环，不替换当前 Final Candidate。

封版目的不是“提前停止思考”，而是防止最后一次未验证改动毁掉已经正确的提交。


# 6.11C Electronic Paper Gate — 2026 CUMCM

电子版论文逐项检查：

- [ ] 单独一个 PDF 或 Word 文件；
- [ ] 建议 PDF；
- [ ] 文件 ≤ 20 MB；
- [ ] 文件本身不压缩；
- [ ] 不含承诺书；
- [ ] 不含编号专用页；
- [ ] 第1页为摘要专用页；
- [ ] 包含正文之后的完整附录；
- [ ] 附录含支撑材料文件列表；
- [ ] 附录含建模使用的全部完整、可运行源程序代码；
- [ ] 全文件无身份/学校/赛区信息。

# 6.11D Supporting Material Gate — 2026 CUMCM

- [ ] 独立于参赛论文；
- [ ] ZIP 或 RAR；
- [ ] ≤ 20 MB；
- [ ] 包含全部可运行源程序；
- [ ] 包含自主查阅使用的数据资料（官方赛题原始数据无需重复提交）；
- [ ] 包含必要的中间结果/图表；
- [ ] 若使用 AI，包含 `AI 工具使用详情.pdf`；
- [ ] 内容与论文一致；
- [ ] 无身份/学校/赛区信息。

# 6.11E Anonymity & Metadata Gate

不仅检查正文肉眼可见内容，还检查：

```text
PDF/Word author metadata:
Document properties:
File names:
Folder names:
Absolute local paths:
Source-code headers/comments:
Image metadata if relevant:
Support archive internal paths:
```

任何可识别参赛者、学校或赛区的信息 → FAIL。

# 6.11F AI Declaration Exact-Meaning Gate

使用 AI 时，论文参考文献之前设置：

> 本参赛队在竞赛过程中使用了 AI 工具，主要用于【简要用途，如语言润色、代码调试等】，详细使用情况见支撑材料。

未使用时：

> 本参赛队在竞赛过程中未使用任何 AI 工具。

并确认 `AI 工具使用详情.pdf` 至少包含：
- 工具名称、版本/型号；
- 使用目的和环节；
- 主要提示方式/过程；
- AI 输出的采纳、人工修改和核验情况（语言润色除外）。

# 6.11G Contest Independence Gate

竞赛期间确认：

- [ ] 未接受指导教师对当届赛题的任何形式指导；
- [ ] 未与队外人员讨论赛题；
- [ ] 未浏览/参与当届赛题网络讨论；
- [ ] 未从 GitHub/CSDN/知乎等获取当届赛题现成答案、代码或结果；
- [ ] 使用的公开资料均为允许的普通公开资料，并按规范引用。

# 6.11H MD5 Integrity Gate — 2026 CUMCM

在 2026-09-13 20:00 前：

```text
paper_final locked:
support_final locked:
paper MD5:
support MD5:
MD5 uploaded:
files changed after MD5?:
if YES -> regenerate & re-upload:
PASS/FAIL
```

注意：
> 打开并保存、自动保存、重新压缩支撑材料等操作都可能改变 MD5。

最终备案后不再修改。

# 6.11I Electronic Upload Window — 2026 CUMCM

电子文件正式上传窗口：

`2026-09-13 20:30 ~ 2026-09-14 14:00`

这个窗口只用于上传已经在 20:00 前完成 MD5 封存的最终文件，**不是继续修改论文的额外竞赛时间**。

同时检查所在赛区是否有额外纸质/电子材料要求。


# 6.12 Final Submission Gate

```text
CONTENT: PASS/FAIL
VISUAL: PASS/FAIL
REFERENCE INTEGRITY: PASS/FAIL
CITATION COVERAGE: PASS/FAIL
ANONYMITY & METADATA: PASS/FAIL
ELECTRONIC PAPER: PASS/FAIL
SUPPORTING MATERIAL: PASS/FAIL
REPRODUCIBILITY: PASS/FAIL
AI COMPLIANCE: PASS/FAIL
CONTEST INDEPENDENCE: PASS/FAIL
MD5 INTEGRITY: PASS/FAIL
FORMAT: PASS/FAIL
SUBMISSION: PASS/FAIL
```


---

# 6.13 Searchable PDF Quality Check【V4.3.2】

2026报名通知“建议使用非图片 PDF 格式”。

因此提交前检查：

```text
Text selectable/copyable:
Search works:
Equations render as vector/text where possible:
No full-page scan unless unavoidable:
PDF opens normally:
Font embedding:
PASS/RECOMMEND FIX
```

这是高优先级质量要求，但全国文件没有写成：
> “图片PDF必然取消参赛资格”。

不得夸大规则。

---

# 6.14 Page Number Gate【V4.3.2】

全国规则：

```text
电子版第1页：摘要专用页
摘要页页码：1
位置：页脚中部
后续连续编号
```

禁止使用：
> 摘要无页码、正文第一页从1开始

这一做法与2026全国格式规范冲突。

默认不设置复杂页眉。

---

# 6.15 Support-Material List Placement【V4.3.2】

附录开头优先放支撑材料文件清单。

推荐：

| 序号 | 文件名 | 相对路径 | 文件用途 | 对应问题 | 是否可运行 |
|---|---|---|---|---|---|

这样满足全国“附录应包括支撑材料文件列表”的要求，并方便专家核验。

---

# 6.16 Source-Code Completeness Gate【V4.3.2】

论文附录：
- 必须包含全部完整、可运行源程序。

支撑材料：
- 必须包含相同/对应的原始可运行源文件。

最终检查：

```text
Every executed source file listed?:
Full source in appendix?:
Runnable source in support archive?:
Version consistent?:
Outputs reproduce paper?:
PASS/FAIL
```

---

# 6.17 AI Placement Audit【V4.3.2】

正文30页中的顺序：

```text
...
模型评价/结论
AI 工具使用声明
参考文献
[正文结束]
附录
```

AI 工具使用详情不需要复制为论文附录正文内容。

支撑材料中：
`AI 工具使用详情.pdf`

附录支撑材料清单中：
列出该文件。

AI 工具本身无需自动列为参考文献。

---

# 6.18 Third-party AIGC/Plagiarism Upload Warning【V4.3.2】

组委会问答不要求参赛队自行进行 AIGC 检测。

竞赛期间：
- 不把整篇论文上传未知第三方 AIGC 检测平台；
- 不把赛题、代码、结果上传非官方查重平台；
- 避免内容泄露与知识产权风险。

真正需要做的是：
- AI 使用真实披露；
- 人工逐项核验；
- 正确引用；
- 不抄袭；
- 不虚构。

---

# 6.19 National-vs-Regional Page Limit Gate【V4.3.2】

全国：
> 正文 <=30页；附录不限页。

赛区若正式要求例如：
> 附录只计前20页 / 总页数控制

则将正式文件写入：
`Regional Override Gate`

没有赛区正式文件时：
> 只作为 advisory，不得标记为全国硬规则。

---

# 6.20 Structured Deliverable Submission Gate【V4.3.2】

若赛题另有结果附件：

- [ ] 文件名/格式符合赛题；
- [ ] 所有字段正确；
- [ ] 所有硬约束通过；
- [ ] 结果与论文完全一致；
- [ ] 独立 Validator PASS；
- [ ] 不包含身份信息；
- [ ] 放入题目要求的正确上传位置。

该 Gate 优先级等同于论文 PDF 正确性。


---

# 6.21 湖南赛区页码 Gate【V4.3.3】

最终执行：

```text
摘要：不显示页码
正文第一页：1
正文/参考文献：连续
附录：继续连续
```

LaTeX 示例逻辑：

```latex
% 摘要页
\thispagestyle{empty}

% 正文开始
\clearpage
\setcounter{page}{1}
\pagestyle{plain}
```

页脚居中，默认不使用页眉。

---

# 6.22 LaTeX-native PDF Gate【V4.3.3】

最终论文必须由 LaTeX 或等价原生排版系统直接生成文本型 PDF。

默认禁止：
- 扫描PDF；
- 每页截图拼PDF；
- 将整篇Word逐页转图片后再合并；
- 任何导致全文文字不可搜索的输出链。

检查：

```text
Searchable text:
Selectable text:
Embedded fonts:
Vector equations:
No full-page rasterization:
References clickable/consistent if enabled:
PASS/FAIL
```

FAIL → 不提交。

---

# 6.23 湖南赛区页数 Gate【V4.3.3】

```text
Abstract: 1 page
Body + AI declaration + References: <=30 pages
Appendix: <=20 pages
Target total main PDF: <=51 pages
```

正文优先29–30页。

如果超限：
1. 删除重复论述；
2. 表格压缩；
3. 次要图移附录；
4. 合并重复公式；
5. 减少算法百科；
6. 优化LaTeX浮动体；
7. 精简代码冗余。

禁止：
- 删除关键验证；
- 删除完整代码的一部分；
- 缩小到不可读字号；
- 通过截图压缩页面内容。

---

# 6.24 Appendix Full-Code Gate【V4.3.3】

附录必须包含：
- 最终数据预处理代码；
- 模型构建代码；
- 求解代码；
- Validator；
- 结果重算代码；
- 必要绘图/实验代码。

不包含：
- 已弃用实验分支；
- 无关调试脚本；
- 缓存文件；
- 重复实现。

这保证“完整”是：
> 完整重现最终论文结果所需的全部代码，
而不是把项目中每一个废弃脚本都打印进去。
