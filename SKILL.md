---
name: mathematical-modeling-workflow
description: Use when solving, improving, validating, or writing a mathematical-modeling competition problem, especially when the task includes attached datasets, operations research, prediction, simulation, multi-question modeling, result verification, structured deliverables, paper figures, LaTeX, or final submission.
license: MIT
compatibility: Designed for coding-capable agents such as Codex or Claude Code. Python 3.10+ is recommended for bundled plotting and validation scripts; scikit-learn is optional and only needed for ML diagnostic displays.
metadata:
  author: xingchenyd
  version: "4.6"
  language: zh-CN
---

# Mathematical Modeling Workflow V4.6

## Core principle

Do not start by choosing an algorithm. First establish that the problem statement, data semantics, constraints, evaluation criteria, and deliverables are understood correctly; then build, solve, validate, certify, and write the model with evidence proportional to every claim.

## Start here

Read [MASTER_ROUTER](references/MASTER_ROUTER.md). For a new contest, load only:

- [M0 Project Control](references/M0_PROJECT_CONTROL.md)
- [M1 Problem & Data Forensics](references/M1_PROBLEM_DATA_BENCHMARK.md)

Do **not** load every reference at once. Progressively disclose only the stage and branch required by the current task.

## Main lifecycle

`M0 → M1 → M2 → (M3 ↔ M4) → M5 → M6 → M7`

- M0: materials, rule hierarchy, project contracts, evidence governance.
- M1: problem/data forensics, pitfalls, wrong-path consequences, EDA, modeling eligibility.
- M2: mathematical abstraction, baseline/bounds, model and solver architecture.
- M3: solving, diagnosis, search-space regeneration, optimization.
- M4: independent validation, solution-quality certification, experiments, uncertainty.
- M5: paper narrative, paragraph logic, language precision, result storytelling.
- M6: publication graphics, references, LaTeX, structured outputs, submission audit.
- M7: defense and judge-review preparation.

## Branch routing

Load the relevant branch **after M1 identifies the problem structure**:

- prediction/statistical inference → [B1](references/B1_PREDICTION_STATISTICAL_INFERENCE.md)
- prediction entering optimization → [B2](references/B2_PREDICTION_TO_DECISION.md)
- dynamic/stochastic/recourse → [B3](references/B3_DYNAMIC_STOCHASTIC_DECISION.md)
- counterfactual/external validation → [B4](references/B4_COUNTERFACTUAL_EXTERNAL_VALIDATION.md)
- operations research/combinatorial optimization → [B5](references/B5_OPERATIONS_RESEARCH_OPTIMIZATION.md)

For the current Hunan CUMCM setup, also load [Hunan 2026 competition profile](references/HUNAN_2026_COMPETITION_PROFILE.md) before paper finalization.

## Non-negotiable gates

1. **Modeling Eligibility Gate**: no final model before P0/P1 pitfalls, field semantics, cross-table relations, data quality, structural findings, and major assumptions are understood.
2. **Evidence-to-Model Gate**: important variables, constraints, decompositions, and solver choices must trace to problem/data evidence.
3. **Independent Validator Gate**: final outputs must be recomputed from raw data + final result, not trusted from solver feasibility flags.
4. **Solution Quality Gate**: a feasible solution is not automatically good enough; compare against B1/B2, valid bound/ceiling, benchmark, gap, and unsearched structure.
5. **Claim Strength Gate**: candidate-pool optimality, solver gap, and full-space global optimality must never be conflated.
6. **Narrative Gate**: every section serves the paper’s Narrative Spine; every important paragraph follows Claim → Evidence → Reasoning → Implication.
7. **Visual Eligibility Gate**: do not draw a chart merely because data exist. Every figure must answer a visual question and support a Claim.
8. **Visual Quality Gate**: publication figures must use the shared plotting system and pass visual lint/audit before insertion.
9. **Reference Integrity Gate**: verify real references and actual in-text `[n]` coverage; never invent papers or DOI values.
10. **Submission Gate**: paper, appendix, structured attachments, anonymity, AI declaration, LaTeX/PDF, and local competition rules must all pass.

## Publication graphics

Before making final figures, read [Publication Visual System](references/PUBLICATION_VISUAL_SYSTEM.md). Use:

- `scripts/paper_plot_style.py` for Matplotlib publication defaults and semantic colors;
- `scripts/sklearn_paper_display.py` for scikit-learn diagnostic displays with the same house style;
- `scripts/visual_lint.py` to detect common visual failures before export;
- `assets/styles/modeling-paper.mplstyle` as a portable Matplotlib style sheet.

Final figure selection is driven by the claim, not by a preferred library. scikit-learn display objects are useful for statistically correct ML diagnostics; Matplotlib controls the final paper appearance.

## Writing

Before final prose, read:

- [Paper narrative & language](references/PAPER_NARRATIVE_AND_LANGUAGE.md)
- [M5 Paper Engineering](references/M5_PAPER_ENGINEERING.md)

Core algorithms/framework names may be bolded on first important occurrence. Ordinary result numbers, percentages, and generic conclusions should not be bolded.

## Verification before freeze

Run the bundled checks where possible:

```bash
python scripts/validate_skill.py .
pytest -q
python scripts/build_visual_gallery.py
```

Do not claim the skill or a contest solution is “ready” until the relevant checks actually pass.
