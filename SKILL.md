---
name: mathematical-modeling-workflow
description: 面向数学建模竞赛的证据驱动、模块化 AI 工作流。覆盖材料审计、题意分析、数据与 Benchmark、模型设计、Baseline/Bound、搜索空间工程、求解优化、独立验证、消融/收敛/稳定性/敏感性、逐节论文工程、图表、真实参考文献核验与最终提交。适用于 CUMCM、MCM/ICM 及类似数学建模任务。
---

# 数学建模工作流 Skill

当用户提供数学建模赛题、数据、现有代码、现有论文或高分论文，并希望完成分析、建模、求解、优化、验证或成稿时，使用本 Skill。

## 强制入口

先读：

1. `MASTER_ROUTER.md`
2. 根据当前阶段只加载对应的 `M0`–`M6` 模块

不要一次性把全部模块视为当前执行清单。

## 主流程

`M0 → M1 → M2 → (M3 ↔ M4) → M5 → M6`

- M0：项目控制与证据治理
- M1：题意、数据与 Benchmark
- M2：模型设计与搜索空间工程
- M3：求解与优化
- M4：验证与实验
- M5：论文工程
- M6：视觉、真实参考文献、排版与提交

## 不可违反

- 不得未读题直接选算法。
- 不得虚构数据、结果、Gap、Bound、运行状态、参考文献或 DOI。
- Solver 的 `optimal` 不能自动外推为原问题全局最优。
- 最终结果必须经过独立 Validator。
- 正文参考文献必须先核验真实性，再按 `[1]` 等统一编号实际引用。
- 参考文献表中不得存在正文从未引用的装饰文献。
- 论文数字必须来自 Single Source of Truth。
- 核心算法可加粗；普通结果数字和百分比不加粗。
- 图表必须绑定 Claim；公式必须解释现实含义。

## 结束条件

只有 M0–M6 对应 Gate 均通过后，才能给出：

`MODEL CONVERGED — FREEZE`

`PAPER CONVERGED — FREEZE`

`READY TO SUBMIT`
