# START_HERE — V4.5

把赛题、全部附件、官方规则和已有材料交给 AI，然后使用：

> 读取 `SKILL.md` 与 `MASTER_ROUTER.md`，执行数学建模工作流 V4.5。先完成 M0 与 M1。不要直接推荐算法。请先把题目规则、数据文件、字段语义、跨表关系、数据质量、P0/P1 坑点、错误理解的后果、关键规律和可利用结构弄清楚，并输出 Modeling Eligibility Report。只有 Gate=PASS 后再进入 M2。

## 已有论文但结果不好

不要先润色。

先检查：
`M1 → M2 → M3 ↔ M4`

尤其确认：
- 原题有没有误读；
- 数据字段有没有理解错；
- 规则实现是否一致；
- 数据规律是否支持当前模型；
- 当前差距来自模型还是算法。

## 模型已冻结

进入：
`M5 → M6`

## 答辩

进入 M7。


## 如果题目属于运筹优化

额外读取：
`branches/B5_OPERATIONS_RESEARCH_OPTIMIZATION.md`

并在正式写论文前检查：
`templates/SOLUTION_QUALITY_CONTRACT_TEMPLATE.md`


## V4.5 写作/视觉启动

从 M1 起就维护：
- `templates/PAPER_NARRATIVE_SPINE_TEMPLATE.md`
- `templates/EVIDENCE_STORYBOARD_TEMPLATE.md`

开始正式绘图前读取：
- `docs/VISUAL_GRAMMAR_V4.5.md`
- `scripts/paper_plot_style.py`
