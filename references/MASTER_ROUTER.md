# MASTER ROUTER V4.6

## 0. General rule

This workflow is gated but iterative, not a one-way waterfall.

`M0 → M1 → M2 → (M3 ↔ M4) → M5 → M6 → M7`

If later evidence reveals a problem, backtrack to the correct root cause instead of only tuning solver parameters.

---

# 1. New contest

Load:
- `M0_PROJECT_CONTROL.md`
- `M1_PROBLEM_DATA_BENCHMARK.md`

Do not choose a final model/algorithm before `MODELING ELIGIBILITY REPORT = PASS`.

M1 must establish:
- exact task and deliverables;
- P0/P1 pitfalls and wrong-path consequences;
- data inventory/dictionary/relations/quality;
- information availability / leakage risks;
- target observability / experimental unit when relevant;
- structural findings that actually change modeling decisions;
- dangerous assumptions;
- problem structure and plausible model families;
- Narrative Seeds and Visual Questions.

---

# 2. Branch routing after M1

- prediction/statistics/small-sample/lifetime → `B1_PREDICTION_STATISTICAL_INFERENCE.md`
- prediction enters decision optimization → `B2_PREDICTION_TO_DECISION.md`
- dynamic/stochastic/feedback/recourse → `B3_DYNAMIC_STOCHASTIC_DECISION.md`
- historical/counterfactual/external validation → `B4_COUNTERFACTUAL_EXTERNAL_VALIDATION.md`
- operations research/combinatorial optimization → `B5_OPERATIONS_RESEARCH_OPTIMIZATION.md`

Branches add domain-specific rules; they do not override shared M0–M7 gates.

---

# 3. M2 Model Design

Load `M2_MODEL_DESIGN.md`.

Required order:
1. Evidence-to-model mapping;
2. mathematical structure;
3. 2–4 model candidates;
4. B0/B1/B2;
5. Bound / ceiling / reference performance;
6. search-space engineering;
7. formal model;
8. solver architecture.

NP-hard is not an instruction to use a metaheuristic. Check exact/structured methods first when the actual instance allows it.

---

# 4. M3 ↔ M4 Solve / Validate Loop

Load:
- `M3_SOLVING_OPTIMIZATION.md`
- `M4_VALIDATION_EXPERIMENTS.md`

Main loop:

`Solve → Diagnose → Attribute → Regenerate/Strengthen → Re-solve → Independent Validate`

Backtrack routing:
- problem/data/field semantics/leakage → M1;
- mathematical abstraction/constraint/assumption → M2;
- candidate-space/solver/algorithm → M3;
- evidence/uncertainty/quality certification → M4.

Before freeze, require:
- Independent Validator;
- appropriate baseline comparison;
- Bound/Gap/ceiling attempt;
- Solution Quality Contract;
- claim-strength boundary;
- structured attachment validator when required.

`0 constraint violations` means feasible, not automatically competitive or optimal.

---

# 5. M5 Narrative and Paper Engineering

Load:
- `M5_PAPER_ENGINEERING.md`
- `PAPER_NARRATIVE_AND_LANGUAGE.md`

Required shared grammar:
- Narrative Spine;
- question inheritance/change/upgrade chain;
- Paragraph Logic = Claim → Evidence → Reasoning → Implication;
- evidence-calibrated wording;
- Cross-Question Synthesis for progressive multi-question problems;
- result section = answer → baseline → bound/gap → mechanism → validator → boundary.

Do not finalize the abstract until SSOT, Claim Ledger and Solution Quality Contract are stable.

---

# 6. M6 Visual / Reference / Submission

Load:
- `M6_VISUAL_REFERENCES_SUBMISSION.md`
- `PUBLICATION_VISUAL_SYSTEM.md`

Before final figures:
1. turn Claim Ledger into Evidence Storyboard;
2. decide text vs table vs figure;
3. pass Visualization Eligibility;
4. select chart type by visual question;
5. apply shared plotting style;
6. run visual lint and grayscale/final-size audit;
7. export vector-first;
8. cross-check values against SSOT.

For ML diagnostics, use scikit-learn Display objects for metric semantics and shared Matplotlib styling for final appearance.

For the current Hunan 2026 competition setup, also load `HUNAN_2026_COMPETITION_PROFILE.md`.

---

# 7. M7 Defense

Load `M7_DEFENSE_JUDGE_REVIEW.md`.

Defense should explain:
- what was difficult;
- why this model/method was chosen;
- what evidence proves feasibility and quality;
- what cannot be claimed;
- what the main bottleneck/limit is.

---

# 8. Re-read checkpoints

- R1: before M1→M2;
- R2: after first complete feasible result;
- R3: before model freeze.

At R3 trace:

`Problem statement → Formal model → Code → Validator → Paper claim`

P0/P1 mismatch requires backtracking.

---

# 9. State summary

```text
M0 PROJECT CONTROL: PASS/FAIL
M1 MODELING ELIGIBILITY: PASS/FAIL
M2 MODEL DESIGN: PASS/FAIL
M3 SOLVER: ACTIVE/FROZEN
M4 EVIDENCE & QUALITY: PASS/PARTIAL/FAIL
M5 NARRATIVE & PAPER: DRAFT/FROZEN
M6 VISUAL/REFERENCE/SUBMISSION: PASS/FAIL
M7 DEFENSE: PASS/FAIL
```

Only when relevant gates pass:

```text
MODEL CONVERGED — FREEZE
PAPER CONVERGED — FREEZE
READY TO SUBMIT
```
