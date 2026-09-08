# 数学建模工作流 V4.5
## Gold-Standard Convergence + Operations Research + Narrative & Visual Grammar

V4.5 在 V4.4 的“结果质量认证 + 运筹优化专项”上，继续补齐所有题型共享的论文表达底座：

- Narrative Spine；
- Question Progression；
- Paragraph Logic；
- Evidence-Calibrated Language；
- Evidence Storyboard；
- Figure Decision Tree；
- Shared Semantic Palette；
- Visual Audit；
- Cross-Question Synthesis。

主流程仍然是：

`M0 → M1 → M2 → (M3 ↔ M4) → M5 → M6 → M7`

**不新增 M8。**

## V4.5 的核心变化

### 研究叙事

`题意/数据 → Narrative Seeds → 模型递进 → 证据链 → Narrative Spine`

### 论文段落

`Claim → Evidence → Reasoning → Implication`

### 图表

`Claim → Visual Question → Chart Type → Semantic Style → Visual Audit`

## 视觉默认

- Final 深蓝 `#355F8A`；
- Baseline 灰 `#737B86`；
- Risk 鲑红 `#D46A65`；
- 低饱和、浅灰细网格、弱化外框；
- 类别≥6优先横向，≥12优先dot/heatmap；
- 分组柱宽按系列数控制；
- 不使用默认Matplotlib风格直接投稿；
- 线图优先PDF/SVG，位图300–400dpi；
- 图内部少放大标题，由LaTeX caption承担完整标题。

统一绘图入口：`scripts/paper_plot_style.py`。

## 运筹优化

出现路径、调度、选址、资源配置、网络流、MILP/CP-SAT等结构时加载：
`branches/B5_OPERATIONS_RESEARCH_OPTIMIZATION.md`

B5 自动继承 V4.5 的叙事和视觉规则。

## 湖南赛区

继续执行已确认的 V4.3.3 定制口径：摘要无页码、正文从1开始、正文29–30页目标/≤30页、附录≤20页、完整最终代码、LaTeX原生可搜索PDF。
