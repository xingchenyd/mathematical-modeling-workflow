# AGENTS.md

本仓库是“数学建模工作流”V4.0 的 Agent 执行规范。

## 最高优先级

1. 官方赛题、数据和当届规则优先。
2. `MASTER_ROUTER.md` 决定当前加载哪个模块。
3. 不要一次加载 M0–M6 后自由发挥。
4. 所有核心数字来自 SSOT。
5. 所有强结论来自 Claim Ledger。
6. 参考文献必须真实核验并在正文引用。
7. 最终方案必须由独立 Validator 复核。

## 路由

- 新题：`M0_PROJECT_CONTROL.md` + `M1_PROBLEM_DATA_BENCHMARK.md`
- 建模：`M2_MODEL_DESIGN.md`
- 求解/优化：`M3_SOLVING_OPTIMIZATION.md`
- 验证/实验：`M4_VALIDATION_EXPERIMENTS.md`
- 写论文：`M5_PAPER_ENGINEERING.md`
- 图表/引用/排版/提交：`M6_VISUAL_REFERENCES_SUBMISSION.md`

## 重要禁止项

- 不虚构文献和 DOI。
- 不虚构实验。
- 不把候选池最优称为全局最优。
- 不用装饰图填充正文。
- 不把算法名堆叠当作创新。
- 不在模型尚未验证时锁定摘要和结论。
