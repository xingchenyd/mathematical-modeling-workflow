# 数学建模工作流 V4.3.3

> Evidence-First, Data-Aware, Iterative & Competition-Executable AI Workflow

V4.3 保留 V4.2 的核心原则：**先证明方向正确，再提高模型和算法质量**；同时把赛前培训中真正具有通用价值的部分融入既有模块：重复审题、概念模型草图、受控简化、局部案例复核、边做边写、信息化章节标题、证据密度、灰度可读性与提交冻结。

本版本明确不包含：
- 自动选题；
- 团队能力评估；
- 三人开发环境统一；
- “NP-hard 就必须用启发式”的错误硬规则。

## 主流程

\[
M0 \rightarrow M1 \rightarrow M2 \rightarrow (M3\leftrightarrow M4) \rightarrow M5 \rightarrow M6 \rightarrow M7
\]

其中：
- M1→M2 仍由 Modeling Eligibility Gate 控制；
- M3/M4 发现根因错误时允许回退到 M1/M2；
- 论文证据不是到 M5 才开始积累，而是从 M1 起持续沉淀；
- M5 负责把已经积累的 Evidence Draft 重构成正式论文；
- M6 在提交前执行官方规则、引用、视觉、复现与冻结审计。

## 模块

| 模块 | 主要任务 |
|---|---|
| M0 | 材料、规则、版本、时间预算、证据治理、提交策略 |
| M1 | 题意与数据取证、坑点、重复审题、概念草图、规律与建模资格 |
| M2 | 数学抽象、候选模型、Baseline、Bound、受控简化、搜索空间与Solver选择 |
| M3 | 求解、诊断、定向优化、时间盒与止损 |
| M4 | Validator、局部案例复核、Gap、消融、收敛、稳定、敏感与不确定性 |
| M5 | Living Paper Finalization：逐节/逐段/逐句论文工程 |
| M6 | 图表、真实文献、2026规则、AI声明、灰度审计、复现与提交冻结 |
| M7 | 答辩：难点—选择—证据—结论—边界 |

## V4.3 新增强调

1. **Scheduled Re-read**：建模前、第一版完整结果后、模型冻结前三次重新对照原题。
2. **Conceptual System Sketch**：公式前先把现实对象、状态、资源和关系画/写清楚。
3. **Mechanism Classification**：确定/随机、静态/动态、离散/连续、同构/异构、2D/3D 等属性先定性，再进入数学表达。
4. **Controlled Relaxation**：简化只允许作为诊断、Baseline、Bound 或经证明不改题意的最终简化，绝不能靠删硬约束“做出结果”。
5. **Local Mechanism Replay**：复杂模型必须尽量用一个局部小例子验证并解释。
6. **Living Paper**：M1–M4 每阶段自动沉淀论文素材，M5 不从零开始写。
7. **Information-rich Titles**：章节标题尽量传递模型/任务信息，而不是“问题一解答”。
8. **Evidence Density > Page Count**：页数上限不是填满目标。
9. **Color + Grayscale Audit**：彩图必须在灰度打印时仍能区分。
10. **Submission Freeze**：临近截止按比例冻结模型，最后阶段只处理提交级风险。

## 2026 CUMCM 专用规则

当比赛为 2026 CUMCM 时，加载 `docs/CUMCM_2026_RULE_PROFILE.md`。官方规则优先于本仓库所有默认值。

## 使用

先读 `SKILL.md` 和 `MASTER_ROUTER.md`。新题只加载 M0 + M1；M1 未 PASS 不进入 M2。


## 2026 官方规则校准

2026 CUMCM 的提交、匿名、AI、MD5 和电子上传要求见 `docs/CUMCM_2026_RULE_PROFILE.md`，该文件优先覆盖通用默认值。


## V4.3.3 官方问答校准

新增对老师/赛区注意事项的“规则分层”：
- 全国硬规则；
- 赛区硬规则；
- 组委会FAQ；
- 经验建议；
- 团队内部截止。

避免把经验建议误写成全国规则。

关键纠正：
- 摘要页必须从页码1开始；
- 全国附录不限页；
- 附录必须放全部完整可运行源程序；
- 非图片PDF是官方“建议”而非明确淘汰条款；
- AI工具无需再作为参考文献条目；
- 不要求自行做第三方AIGC检测。


## 湖南赛区定制默认值

本仓库现在默认按当前已确认的湖南赛区执行口径运行：

- 摘要页不显示页码；
- 正文第一页从页码1开始；
- 正文目标29–30页，硬上限30页；
- 附录控制20页以内；
- 主论文PDF按摘要1页+正文30页+附录20页控制在约51页；
- 附录放全部完整、可运行代码；
- 最终PDF必须为原生可搜索文本PDF；
- 默认使用 LaTeX 生成论文。

详见 `docs/HUNAN_2026_COMPETITION_PROFILE.md`。
