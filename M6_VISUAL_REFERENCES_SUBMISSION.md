# M6 视觉、参考文献、排版、复现与提交
## Visual Grammar + Evidence Presentation

M6 不负责“把论文变漂亮”，而负责把已经成立的证据以**最少认知负担**呈现出来。

最高原则：

\[
\boxed{
Claim
\rightarrow
Visual\ Question
\rightarrow
Right\ Medium
\rightarrow
Consistent\ Style
\rightarrow
Visual\ Audit
}
\]

---

# 6.0 Rule Profile First

当前 Skill 执行湖南赛区已确认口径：
- 摘要页不显示页码；
- 正文第一页从1开始；
- 正文目标29–30页、硬上限30页；
- 附录≤20页且包含完整最终可运行代码；
- 最终论文必须为原生可搜索非图片PDF；
- 默认 LaTeX。

详见 `docs/HUNAN_2026_COMPETITION_PROFILE.md`。

---

# 6.1 Visualization Eligibility Gate【V4.5】

每张候选图先回答：

```text
Claim ID:
What must the reader SEE rather than READ?:
Relation / Trend / Distribution / Structure / Space / Trade-off / Schedule?:
Would a table/text be clearer?:
If figure removed, which claim becomes weaker?:
KEEP / TABLE / TEXT / DROP
```

如果只想展示一个标量结果，通常不要画图。

例：
- “净收益=18531元/日” → 文字/表；
- “22个中心形成明显时间—收益权衡” → scatter/Pareto；
- “优化阶段边际收益递减” → contribution/waterfall/line；
- “设备配置在空间上分层” → heatmap/map。

---

# 6.2 Figure Decision Tree【V4.5】

## 关系/比较

- 2–5个类别，单指标 → dot/bar；
- ≥6个类别 → 横向 bar/dot；
- ≥12个类别 → dot/heatmap/small multiples，默认拒绝竖柱；
- before/after 或成对方案 → dumbbell/slope；
- 两个连续指标 → scatter；
- 两个目标权衡 → Pareto scatter；
- 多指标但单位不同 → 表格或标准化后 heatmap，不直接并排柱。

## 趋势/过程

- 时间序列 → line；
- 优化迭代 → best-so-far line + bound（若有）；
- 阶段贡献 → waterfall/contribution plot；
- 收敛 Gap → line，明确 UB/LB/Gap 口径。

## 分布

- 分组分布 → box/violin/ECDF；
- 重尾/离群重要 → ECDF/box；
- 只报均值且分布重要 → FAIL。

## 矩阵/结构

- OD/相关/兼容/使用频率 → heatmap；
- 路线/网络 → network/route skeleton；
- 排班 → Gantt/timeline；
- 流量分解 → Sankey（节点数少且流向是重点时）；
- 空间相对结构 → map/MDS；若MDS，仅用于可视化，正文声明不参与优化。

## 状态沿路径变化

- 容量/载荷随航段 → step/stacked bar/route skeleton；
- 库存/油量随时间/节点 → step/line with safety bound。

---

# 6.3 Chart Rejection Rules【V4.5】

默认拒绝：
- 3D图；
- 雷达图作为主要证据；
- >5类的饼图；
- 没有真实中性中心却使用红蓝发散色；
- 无依据双Y轴；
- 20根以上竖直粗柱；
- 表格和柱状图重复同一信息；
- 将不同单位指标直接堆在一张柱状图；
- solver截图/Excel截图；
- 无Baseline的敏感性图；
- 无best-so-far的随机启发式“收敛曲线”；
- Gantt没有资源编号/时间刻度；
- heatmap没有色条或单位。

---

# 6.4 Shared Semantic Palette【V4.5】

优秀论文中常见的有效做法是：白/浅灰底、低饱和蓝+鲑红、浅灰网格、弱化外框。V4.5 固化为**语义色**，而不是每张图自由换色。

默认：

| 语义 | 色值 | 用途 |
|---|---|---|
| Final / Primary | `#355F8A` | 最终方案、主曲线 |
| Alternative | `#5D8DB8` | 主要对比方案 |
| Light alternative | `#A7C2DC` | 次级/区间 |
| Baseline | `#737B86` | 基线/中性 |
| Improvement | `#5C8D75` | 可行改善/正向 |
| Secondary highlight | `#C9824B` | 次级强调 |
| Risk / violation | `#D46A65` | 风险、超限 |
| Severe risk | `#A94E4A` | 关键风险 |
| Special class | `#8B6FA8` | 临时/第三类别 |
| Grid | `#D2D7DD` | 网格 |
| Text | `#2F3E4D` | 图中文字 |
| Background | `#FAFAFA` | 可选浅灰绘图区 |

规则：
- 同一语义全文同色；
- 不因“图太单调”随意引入彩虹色；
- 风险红只用于真正风险/超限，不用来装饰；
- Baseline 默认灰，Final 默认深蓝。

---

# 6.5 Bar / Dot Plot Geometry【V4.5】

之前论文中“柱太粗”是可避免的版式问题。

默认柱宽：

```text
1 series: 0.45–0.60
2 series: 0.28–0.34
3–4 series: 0.18–0.25
```

原则：
> 一组柱总宽度不超过类别间距约75%。

类别多：
- ≥6：优先横向；
- ≥12：优先 dot/heatmap；
- 类别名很长：横向；
- 排名任务：排序后横向 dot/bar。

数值标注：
- 只在少量柱/关键柱上标；
- 不给20根柱逐根贴数字。

---

# 6.6 Line / Scatter / Pareto

## Line

- 时间/迭代有顺序时才连线；
- 主曲线线宽约1.5–2.0 pt；
- marker约3.5–5 pt，只在需要识别离散观测时使用；
- 收敛图优先同时显示 incumbent 与 valid bound（若存在）。

## Scatter

- 点大小只在第三变量真的有意义时编码；
- alpha约0.6–0.8；
- 点边界弱化；
- 标注只给 Pareto/knee/异常/最终点。

## Pareto

必须区分：
- 非支配点；
- 推荐点；
- ideal/nadir（若使用）；
- 选择规则。

---

# 6.7 Heatmap Palette Rule

## 全部非负数据

优先 sequential：
- Blues；
- viridis；
- cividis；
- 自定义浅蓝→深蓝。

## 有明确正负/高低于基准的中心0

才使用 diverging：
> 蓝—浅灰/白—鲑红。

热力图必须：
- 有 colorbar；
- 标单位；
- 类别很多时减少tick但不隐藏关键标签；
- 需要精确读数时配表，不在每格塞文字。

---

# 6.8 Figure Size and Typography【V4.5】

所有字号按“最终插入论文后的物理尺寸”设计，不先画巨大图再缩成邮票。

推荐画布：

```text
单图全宽：6.6–7.1 in × 3.4–4.4 in
双面板全宽：6.8–7.2 in × 3.0–3.8 in
窄单图：3.2–3.5 in × 2.4–3.0 in
```

最终字号：

```text
axis label: 8.5–9.5 pt
ticks: 7.5–8.5 pt
legend: 7.5–8.5 pt
annotation: 7.5–9 pt
panel label: 10–11 pt bold
```

线：

```text
axis/spine: ~0.8 pt
grid: 0.5–0.7 pt
main line: 1.5–2.0 pt
secondary line: 1.0–1.4 pt
```

---

# 6.9 Axes / Grid / Spines

默认：
- white figure background；
- white或`#FAFAFA` axes background；
- top/right spines off；
- left/bottom spines浅灰；
- 只在帮助读数时显示浅灰网格；
- bar通常只开 y-grid；
- network/map不强制网格。

不要使用默认 Matplotlib 蓝橙 + 黑色全边框直接出稿。

---

# 6.10 Legend and Annotation

## Legend

优先级：
1. 图内空白区；
2. 图外右侧/上方；
3. 多面板共享图例。

默认：
- `frameon=False`；
- 不遮挡点/线；
- 类别>6时考虑直接标注或分面。

## Annotation

只标：
- Final；
- Baseline；
- Bound；
- knee point；
- 最大/最小关键值；
- 违反/临界点。

不把每一个点都贴数值。

---

# 6.11 Figure Composition / Multi-panel【V4.5】

多面板只用于回答同一个大问题的互补证据。

推荐：
- `(a) 空间结构 + (b) 指标分布`；
- `(a) 局部机制 + (b) 全局统计`；
- `(a) Baseline→Final + (b) 风险裕度`；
- `(a) 原始需求 + (b) 最终网络`。

禁止：
> 只是为了省页数，把三张无关图塞成(a)(b)(c)。

panel标签固定 `(a)`, `(b)`，位置统一。

---

# 6.12 Table vs Figure

## Table

负责：
- 精确数值；
- 方案详细比较；
- 验证结果；
- 参数与单位。

## Figure

负责：
- 趋势；
- 关系；
- 分布；
- 机制；
- 空间；
- 权衡。

如果表已经清楚给出4个方案的精确指标，不再画一张相同的 grouped bar；改画 Pareto、相对改善或机制图，或者不画。

---

# 6.13 Caption and In-figure Title

正式论文：
- Figure caption 在图下；
- Table title 在表上；
- 正文必须先/后引用。

图内部尽量不放大标题；完整标题交给 LaTeX caption。

好 caption：
> “不同候选中心的净收益—完成时间权衡及推荐点”

差 caption：
> “结果图”

多面板 caption 先给总标题，再解释(a)(b)。

---

# 6.14 Figure Narrative Protocol

图前一句：
> 为什么需要看这张图。

图后 2–4 句：
1. 观察；
2. 机制；
3. 对模型/决策意味着什么；
4. 必要时说明不能证明什么。

禁止：
> “由图可知效果显著。”

---

# 6.15 Color + Grayscale + Print Audit

最终同时检查：
- 彩色屏幕；
- 灰度预览；
- 100%缩放；
- 实际插入宽度。

颜色不能是唯一编码：
- line style；
- marker；
- hatch；
- direct label；

至少使用一种冗余编码。

---

# 6.16 Output Format / LaTeX Integration【V4.5】

优先：
- line art：PDF/SVG；
- raster/heatmap：PNG 300–400 dpi；
- 同时保留 source CSV/JSON；
- `pdf.fonttype=42`，保证字体嵌入和文本质量；
- 不用截图粘贴图。

LaTeX 中建议：

```latex
\includegraphics[width=0.92\textwidth]{figures/fig_name.pdf}
```

多面板优先在 Python 中统一对齐或使用规范 subfigure，不用手工截图拼接。

统一绘图工具：`scripts/paper_plot_style.py`。

规则以当届官方文件为准。

# 6.17 Reference Integrity Gate

每篇终稿文献必须核验：
- 作者；
- 准确题名；
- Venue；
- 年份；
- 卷期/页码/文章号；
- DOI（如有）；
- 可靠来源。

查不到不猜。

AI工具本身不自动列参考文献；正式论文/技术报告按普通文献处理。

---

# 6.18 Citation Coverage

- 参考文献每条至少正文引用一次；
- `[n]` 与第n条对应；
- 无重复；
- 无孤儿条目；
- 算法/经典模型首次正式使用时优先引用原始或权威文献；
- 引用紧跟被支持的陈述，不整段末尾堆编号。

---

# 6.19 Reproducibility

必须能回答：
- 输入；
- 环境；
- 运行命令；
- seed；
- 最终输出；
- SSOT；
- Validator；
- 图的 source data。

所有论文图应能追溯到：
> 正式结果 CSV/JSON → 派生统计 → figure script → PDF/PNG。

---

# 6.20 AI / Contest Compliance

继续执行 2026 规则 Profile：
- 核心建模分析由参赛队主导；
- AI 输出人工核验；
- 参考文献前有 AI 工具使用声明；
- 支撑材料有 `AI 工具使用详情.pdf`；
- 不自行上传未知第三方做 AIGC 检测；
- 竞赛期间不浏览/交流当届赛题答案与代码。

---

# 6.21 湖南赛区 Page / PDF Gate【ACTIVE】

最终执行：

```text
摘要：不显示页码
正文第一页：1
正文/参考文献：连续
附录：继续连续
正文目标：29–30页，≤30
附录：≤20页
PDF：LaTeX原生、可搜索、非图片
```

不再采用通用文件中“摘要显示页码1”的默认口径。

---

# 6.22 Appendix Full-Code Gate

附录必须包含复现最终结果所需的完整最终代码：
- 数据预处理；
- 模型/求解；
- Validator；
- 结果重算；
- 必要实验/绘图。

不包含已经废弃且与最终结果无关的开发分支。

---

# 6.23 Visual Audit Gate【V4.5】

每张正文图逐项：

```text
Claim bound to figure: PASS/FAIL
Correct chart family: PASS/FAIL
No redundant table/figure: PASS/FAIL
Final-size labels readable: PASS/FAIL
Palette semantics consistent: PASS/FAIL
Bar width / line weight appropriate: PASS/NA
Legend does not cover data: PASS/FAIL
Units/axes/colorbar complete: PASS/FAIL
Key point annotated, clutter controlled: PASS/FAIL
Grayscale still interpretable: PASS/FAIL
Caption states message, not “result figure”: PASS/FAIL
Source data traceable: PASS/FAIL
```

任何正文核心图 FAIL → 返工，不提交。

---

# 6.24 Final Submission Gate

```text
CONTENT: PASS/FAIL
NARRATIVE: PASS/FAIL
LANGUAGE PRECISION: PASS/FAIL
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
