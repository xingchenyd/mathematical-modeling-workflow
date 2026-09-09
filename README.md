# 数学建模工作流 V4.6

一个可直接安装的 Agent Skill，面向数学建模竞赛的完整生命周期：题意与数据取证、模型设计、运筹优化/预测统计、求解质量认证、独立验证、优秀论文级叙事与出版级可视化、LaTeX 与提交审计。

## 安装为 Skill

将整个目录放到：

```text
~/.agents/skills/mathematical-modeling-workflow/
```

目录名必须保持 `mathematical-modeling-workflow`，以匹配 `SKILL.md` 的 `name`。

Codex/Claude Code 等支持 Agent Skills 的运行时可从 `SKILL.md` 自动判断何时加载。

## 使用

新比赛最简单的指令：

> 使用 mathematical-modeling-workflow skill 完成这次数学建模任务。先读全部题目和附件，执行 M0、M1；不要直接选算法。Modeling Eligibility Gate 通过后再进入建模与求解，并用独立 Validator 和 Solution Quality Contract 决定是否冻结结果。

## V4.6 重点

- 正式 Agent Skill 封装与 progressive disclosure；
- 恢复 B1–B5 五类题型分支；
- 保留 V4.5 Narrative Spine / Paragraph Logic / Evidence Storyboard；
- 保留 V4.4 Bound / Gap / Solver Certificate / Solution Quality Contract；
- 保留湖南赛区当前 LaTeX/PDF/页码/页数规则；
- 新增 publication-grade plotting system；
- 新增 scikit-learn diagnostic display adapters；
- 新增 visual lint 与 Skill 结构验证；
- 新增 pressure-test/eval 场景，防止后续版本退化。

## 可视化原则

“漂亮”不是高饱和颜色或复杂图形，而是：图型正确、语义清晰、配色统一、感知可靠、印刷可读、证据密度高、不会误导。

最终图优先输出 PDF/SVG 矢量格式；位图至少 300–400 dpi。连续数值色图优先使用感知均匀的 `viridis` / `cividis`；只有存在真实中心（如 0、baseline 差值）时才使用 diverging colormap。
