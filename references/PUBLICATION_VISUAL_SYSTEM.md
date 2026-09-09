# Publication Visual System V4.6
## 数学建模论文出版级可视化系统

目标不是“让图更花哨”，而是让图在论文最终尺寸下同时满足：**正确、可读、统一、可靠、克制、可复核**。

---

# 1. 视觉优先级


default order:

```text
统计/数学含义正确
> 图型与问题匹配
> 信息层级清楚
> 感知可靠
> 全文风格统一
> 美观
```

任何美化不得改变数据含义、隐藏异常、夸大差异或制造不存在的中心/趋势。

---

# 2. Claim → Visual Question → Chart

每张图先填写：

```text
Claim:
What must the reader see?
- comparison
- ranking
- trend
- distribution
- relationship
- uncertainty
- spatial/network structure
- schedule/resource conflict
- optimization convergence/gap
- multiobjective trade-off
```

然后选图：

| 视觉问题 | 优先图型 |
|---|---|
| 2–5类别绝对比较 | bar / dot |
| 6–12类别 | horizontal dot/bar |
| >12类别 | sorted dot / heatmap / small multiples |
| 成对方案逐项变化 | dumbbell / slope |
| 时间趋势 | line |
| 优化收敛 | incumbent + bound + gap band |
| 分布 | ECDF / box / violin + raw points |
| 两连续变量 | scatter + appropriate fit |
| 多目标 | Pareto scatter/frontier |
| 阵列/OD/相关矩阵 | heatmap |
| 路线/网络 | map/network diagram |
| 资源占用 | Gantt / interval plot |
| 阶段贡献 | waterfall / contribution plot |
| 不确定性 | interval/ribbon/fan chart |
| 分类模型 | confusion matrix + ROC/PR/calibration as appropriate |
| 回归模型 | actual-vs-predicted + residual diagnostic |

如果图只是在重复一个表中的精确数字，不画。

---

# 3. 图型拒绝规则

- >4 组 grouped bars：拒绝，改 dot/heatmap/small multiples。
- >12 个竖直类别：拒绝，改横向排序或矩阵图。
- 同一数据同时 table + bar 且没有新增模式信息：删图。
- 3D 柱/饼：默认拒绝。
- 类别很多的 pie/donut：拒绝。
- 无意义双Y轴：拒绝。
- 只有1个数值的“图”：拒绝。
- `jet/rainbow` 用于连续数值：拒绝。
- Diverging colormap 没有真实中点：拒绝。

---

# 4. 统一语义颜色

颜色是“语义”，不是随机装饰。

| 角色 | 默认 |
|---|---|
| Final/主方案 | 深蓝 |
| Alternative | 浅蓝 |
| Baseline | 中性灰 |
| Improvement/可行改善 | 柔和绿 |
| Secondary | 柔和橙 |
| Risk/Violation | 鲑红 |
| Severe Risk | 暗红 |
| Special/Policy | 柔和紫 |

同一篇论文中这些语义不得互换。

类别型图若类别本身没有上述语义，使用 colorblind-friendly qualitative palette，并辅以 marker/linestyle，而不是只靠颜色。

---

# 5. Colormap 语义

根据 Matplotlib / ColorBrewer 的色图分类原则：

### Sequential
适合有序、非负、从低到高的数值。

优先：
- `viridis`
- `cividis`
- `Blues`
- `YlGnBu`

### Diverging
只有当数据存在有意义的中点（0、baseline、target等）时使用。

优先：
- `RdBu_r`
- `BrBG`
- `PuOr`

### Cyclic
角度、方向、相位、一天中的时间等首尾相接变量。

优先：`twilight_shifted`。

### Qualitative
离散类别使用离散 palette，不使用连续 colormap。

---

# 6. 最终尺寸排版

论文图按最终插入尺寸制作，不先画超大图再暴力缩小。

默认：
- 单栏约 3.45 in 宽；
- 双栏/通栏约 6.9 in 宽；
- tick 约 8 pt；
- axis label 约 9 pt；
- legend 约 8 pt；
- line 约 1.6 pt；
- marker 约 4–5 pt。

避免：
- 小于7 pt的可见文字；
- 标注挤压；
- 图例挡住数据；
- 大片空白；
- 图内重复大标题。

图题由 LaTeX caption 承担，图内部尽量只保留坐标、panel label和必要 annotation。

---

# 7. 柱宽

- 单系列：0.45–0.60，默认0.52；
- 双系列：0.28–0.34，默认0.31；
- 3–4系列：0.18–0.25，默认0.21；
- >4系列：不继续缩柱，换图型。

柱不是越粗越醒目；柱组应保留足够负空间。

---

# 8. Layout

默认使用 Matplotlib `layout="constrained"`，优先解决多面板、colorbar、legend与坐标标签重叠。

多面板只在两个/多个视觉证据属于同一个 Claim 时组合，例如：

- (a) 空间位置；(b) 候选排名；
- (a) 局部机制；(b) 全局分布；
- (a) ROC；(b) PR；(c) calibration。

不要为了“高级感”强行拼图。

---

# 9. Scikit-learn 图形

scikit-learn 的 `Display` API 用于**可靠地计算并表达模型诊断**，不是统一美术风格库。

推荐：
- `ConfusionMatrixDisplay`
- `RocCurveDisplay`
- `PrecisionRecallDisplay`
- `CalibrationDisplay`
- `PredictionErrorDisplay`

原则：

```text
scikit-learn: metric/display semantics
Matplotlib: final paper styling
```

使用 `scripts/sklearn_paper_display.py`，让 sklearn display 和全文 house style 一致。

分类不应只画 ROC：类别不平衡时 PR 通常更有解释价值；若模型输出概率并用于决策，增加 calibration；混淆矩阵必须明确是否按 true/pred/all normalize。

回归至少检查：actual-vs-predicted 或 residual-vs-predicted；散点图只是诊断，不替代 MAE/RMSE/R² 等定量评价。

---

# 10. 统计可靠性

视觉必须与验证设计一致：

- 测试集/OOF/OOT 的预测诊断不能偷偷混入训练集；
- error bars/CI 必须说明来源；
- stochastic algorithm 的均值线应配 seed distribution / interval；
- smoothing/fit line 必须说明方法，不用无依据高阶多项式；
- y轴截断若可能夸大差异，必须显式说明；
- 数量级差太大时考虑 log scale，但必须解释。

---

# 11. 颜色与灰度

最终重要图必须通过：

1. 彩色阅读；
2. 灰度/黑白打印；
3. 颜色缺失时仍可通过 marker/linestyle/label 理解。

禁止只用红/绿作为唯一编码。

---

# 12. 图后文字

每张核心图后写：

```text
Observation → Mechanism → Modeling/Decision Implication → Boundary (if needed)
```

不要写“由图可知效果较好”。

---

# 13. 自动化

正式出图建议：

```bash
python scripts/build_visual_gallery.py
pytest -q tests/test_visual_style.py tests/test_sklearn_display.py
```

单张最终图生成后，在代码中运行 `visual_lint.lint_figure(fig)`；WARN必须人工复核，ERROR必须修复。

---

# 14. 外部依据

- Matplotlib: Customizing with style sheets and rcParams
  https://matplotlib.org/stable/users/explain/customizing.html
- Matplotlib: Choosing Colormaps
  https://matplotlib.org/stable/tutorials/colors/colormaps.html
- Matplotlib: Constrained Layout
  https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html
- scikit-learn: Visualizations with Display Objects
  https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_display_object_visualization.html
- ColorBrewer: sequential/diverging/qualitative scheme guidance
  https://colorbrewer2.org/learnmore/schemes.html
