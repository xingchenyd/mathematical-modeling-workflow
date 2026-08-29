# 数学建模工作流

> Evidence-Grounded Modular AI Workflow for Mathematical Modeling Competitions

这是一个面向数学建模竞赛的模块化 AI Skill / Workflow，目标不是“一键生成论文”，而是让 AI 在有限竞赛时间内按证据链完成：**读题 → 建模 → 求解 → 优化 → 验证 → 实验 → 写作 → 引用 → 提交**。

## 快速开始

1. AI 先读 [`SKILL.md`](SKILL.md)。
2. 再读 [`MASTER_ROUTER.md`](MASTER_ROUTER.md)。
3. 只加载当前阶段需要的 M0–M6 模块。
4. 新比赛从 M0 + M1 开始。
5. 求解阶段执行 `M3 ↔ M4` 反馈循环。
6. 模型冻结后进入 M5，终稿进入 M6。

## 核心特色

- 模块化路由，避免超长 Prompt 一次加载；
- Problem / Acceptance Contract；
- B0/B1/B2 三层 Baseline；
- Bound 与 Gap 边界；
- Search Space Engineering；
- Hybrid Solver；
- Solution-Driven Regeneration；
- 独立 Validator；
- 消融、收敛、多 Seed、敏感性；
- 逐小节、逐段、逐句 Paper Engineering；
- Figure Contract；
- **参考文献真实性 Gate + Reference Ledger + 正文 `[1]` 引用覆盖审计**；
- Single Source of Truth；
- Claim Strength C0–C5；
- 最终 Submission Gate。

## 仓库结构

```text
.
├── SKILL.md
├── AGENTS.md
├── START_HERE.md
├── MASTER_ROUTER.md
├── M0_PROJECT_CONTROL.md
├── M1_PROBLEM_DATA_BENCHMARK.md
├── M2_MODEL_DESIGN.md
├── M3_SOLVING_OPTIMIZATION.md
├── M4_VALIDATION_EXPERIMENTS.md
├── M5_PAPER_ENGINEERING.md
├── M6_VISUAL_REFERENCES_SUBMISSION.md
├── templates/
├── docs/
├── CONTRIBUTING.md
├── CHANGELOG.md
├── CITATION.md
└── LICENSE
```

## 参考文献底线

任何文献进入最终论文前必须核验作者、准确题名、期刊/会议、年份、卷期页码/文章号和 DOI（如有）。查不到就不猜。最终要求：

- Bibliography 中每篇文献至少被正文引用一次；
- 正文每个 `[n]` 都能映射到第 n 条文献；
- 无重复文献；
- 无未核验文献；
- 无编造 DOI。

## License

MIT License.

---

## V4.0 详细说明

# 数学建模竞赛 AI 工作流 V4.0
## Modular Evidence-Grounded Competition System

V4.0 不再把所有规则串成一条 170+ 步的长流程，而采用：

\[
\boxed{
MASTER\_ROUTER
+
M0\sim M6
+
Templates
}
\]

主控只负责“现在进入哪个模块”，各模块只加载当前阶段需要的规则。

## 模块

| 模块 | 名称 | 核心任务 |
|---|---|---|
| M0 | 项目控制与证据治理 | 材料、规则、Contract、Issue、Decision、SSOT |
| M1 | 题意、数据与 Benchmark | 三遍读题、规则审计、EDA、高分论文差距分析 |
| M2 | 建模设计与搜索空间 | 候选模型、B0/B1/B2、Bound、Search Space、正式模型 |
| M3 | 求解与优化 | Hybrid Solver、诊断、解驱动再生成、重优化 |
| M4 | 验证与实验 | 独立 Validator、Gap、消融、收敛、稳定性、敏感性 |
| M5 | 论文工程 | 从标题、摘要到结论的逐节、逐段、逐句写作协议 |
| M6 | 视觉、参考文献、排版与提交 | Figure/Table、引用真实性、[1] 编号、AI合规、最终提交 |

## 执行原则

1. 比赛开始只读 `MASTER_ROUTER.md + M0 + M1`。
2. 题意冻结后加载 M2。
3. 模型成形后进入 `M3 <-> M4` 循环。
4. 模型未冻结时可以同步积累 M5 的证据，但不得正式锁定摘要。
5. 模型冻结后完整加载 M5。
6. 成稿后加载 M6 做视觉、引用、排版和提交审计。
7. 官方竞赛规则优先级永远高于本仓库默认规范。
8. 任何结果、文献、DOI、Gap、算法性能都不得虚构。

## 最终目标

不是“写出最多模型”，而是：

\[
\boxed{
正确的问题
+
合理的模型
+
有竞争力的结果
+
明确的最优性边界
+
可复核的证据
+
高密度论文表达
+
真实可核验引用
}
\]

