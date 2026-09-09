"""Local validator for the Agent Skill package.

This is not a replacement for the official `skills-ref validate`; it checks the
core Agent Skills constraints and repository invariants without third-party YAML
dependencies.
"""
from __future__ import annotations
from pathlib import Path
import re
import sys

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_REFS = [
    "MASTER_ROUTER.md", "M0_PROJECT_CONTROL.md", "M1_PROBLEM_DATA_BENCHMARK.md",
    "M2_MODEL_DESIGN.md", "M3_SOLVING_OPTIMIZATION.md", "M4_VALIDATION_EXPERIMENTS.md",
    "M5_PAPER_ENGINEERING.md", "M6_VISUAL_REFERENCES_SUBMISSION.md", "M7_DEFENSE_JUDGE_REVIEW.md",
    "B1_PREDICTION_STATISTICAL_INFERENCE.md", "B2_PREDICTION_TO_DECISION.md",
    "B3_DYNAMIC_STOCHASTIC_DECISION.md", "B4_COUNTERFACTUAL_EXTERNAL_VALIDATION.md",
    "B5_OPERATIONS_RESEARCH_OPTIMIZATION.md", "PUBLICATION_VISUAL_SYSTEM.md",
]


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("SKILL.md frontmatter is not closed")
    fm = text[4:end]
    result: dict[str, str] = {}
    for line in fm.splitlines():
        if not line or line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"\'')
    result["__body__"] = text[end + 5:]
    return result


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    skill = root / "SKILL.md"
    if not skill.exists():
        return ["Missing SKILL.md"]
    try:
        meta = parse_frontmatter(skill.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"Invalid frontmatter: {exc}"]
    name = meta.get("name", "")
    desc = meta.get("description", "")
    body = meta.get("__body__", "")
    if not NAME_RE.fullmatch(name): errors.append("name must use lowercase letters, numbers, hyphens")
    if len(name) > 64: errors.append("name exceeds 64 chars")
    if root.name != name: errors.append(f"directory name '{root.name}' must match skill name '{name}'")
    if not desc or len(desc) > 1024: errors.append("description must be 1..1024 chars")
    if len(body.splitlines()) > 500: errors.append("SKILL.md body exceeds recommended 500 lines")
    for ref in REQUIRED_REFS:
        if not (root / "references" / ref).exists(): errors.append(f"missing reference: {ref}")
    for script in ["paper_plot_style.py", "visual_lint.py", "sklearn_paper_display.py"]:
        if not (root / "scripts" / script).exists(): errors.append(f"missing script: {script}")
    return errors


if __name__ == "__main__":
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errs = validate(root)
    if errs:
        print("FAIL")
        for err in errs: print("-", err)
        raise SystemExit(1)
    print("PASS: skill structure and metadata validated")
