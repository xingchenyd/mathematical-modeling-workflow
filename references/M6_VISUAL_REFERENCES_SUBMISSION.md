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

---

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

# 6.25 Publication Visual System【V4.6】

Final figures additionally load `PUBLICATION_VISUAL_SYSTEM.md` and use the bundled scripts.

Required sequence:

```text
Claim
→ Visual Question
→ Visualization Eligibility
→ Chart Type
→ Data/metric verification
→ House Style
→ visual_lint
→ grayscale/final-size inspection
→ vector-first export
→ SSOT cross-check
```

For machine-learning evaluation, prefer official scikit-learn `Display` objects for confusion matrix, ROC, precision-recall, calibration and regression prediction-error diagnostics, then style the Matplotlib artists with the shared house style. Do not replace metric semantics with decorative custom charts.

Every important continuous heatmap must use a colormap class appropriate to its data semantics; diverging maps require a meaningful center.
