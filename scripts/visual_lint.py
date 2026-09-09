"""Lightweight static lint for Matplotlib figures used in contest papers."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable
import matplotlib.pyplot as plt
from matplotlib.container import BarContainer
from matplotlib.colors import to_hex

from paper_plot_style import grayscale_distance

@dataclass
class VisualIssue:
    severity: str
    code: str
    message: str


def lint_figure(fig, *, require_axis_labels: bool = True) -> list[VisualIssue]:
    issues: list[VisualIssue] = []
    if not fig.axes:
        return [VisualIssue("ERROR", "NO_AXES", "Figure contains no axes.")]

    for idx, ax in enumerate(fig.axes):
        prefix = f"axes[{idx}]"
        # Colorbar axes typically have no x/y labels; exempt narrow axes.
        bbox = ax.get_position()
        likely_colorbar = bbox.width < 0.08 or bbox.height < 0.08
        if require_axis_labels and not likely_colorbar:
            if not ax.get_xlabel() and len(ax.get_xticks()) > 1:
                issues.append(VisualIssue("WARN", "MISSING_XLABEL", f"{prefix}: x-axis label missing."))
            if not ax.get_ylabel() and len(ax.get_yticks()) > 1:
                issues.append(VisualIssue("WARN", "MISSING_YLABEL", f"{prefix}: y-axis label missing."))

        # Paper figures normally rely on LaTeX captions instead of a large in-axes title.
        if ax.get_title().strip():
            issues.append(VisualIssue("INFO", "IN_AXES_TITLE", f"{prefix}: consider moving the title to the LaTeX caption."))

        # Tiny visible text is risky after final-size insertion.
        for text in [*ax.get_xticklabels(), *ax.get_yticklabels(), ax.xaxis.label, ax.yaxis.label]:
            if text.get_visible() and text.get_text().strip() and text.get_fontsize() < 7.0:
                issues.append(VisualIssue("WARN", "TINY_TEXT", f"{prefix}: visible text below 7 pt."))
                break

        # Bar overload and width checks.
        bar_containers = [c for c in ax.containers if isinstance(c, BarContainer)]
        if bar_containers:
            total_bars = sum(len(c.patches) for c in bar_containers)
            if total_bars > 20:
                issues.append(VisualIssue("WARN", "BAR_OVERLOAD", f"{prefix}: {total_bars} bars; prefer dot plot/heatmap/small multiples."))
            for c in bar_containers:
                widths = [p.get_width() for p in c.patches]
                if widths and max(widths) > 0.65 and len(c.patches) >= 3:
                    issues.append(VisualIssue("WARN", "THICK_BARS", f"{prefix}: bars appear wider than publication default."))
                    break

        # More than 12 categorical x tick labels is rarely readable vertically.
        labels = [t.get_text() for t in ax.get_xticklabels() if t.get_text().strip()]
        if len(labels) > 12:
            issues.append(VisualIssue("WARN", "TOO_MANY_X_CATEGORIES", f"{prefix}: {len(labels)} x categories; consider horizontal dot/heatmap."))

        # Detect low grayscale separation between line colors (approximate).
        colors = []
        for line in ax.lines:
            try:
                colors.append(to_hex(line.get_color()))
            except Exception:
                pass
        unique = list(dict.fromkeys(colors))
        for i in range(len(unique)):
            for j in range(i + 1, len(unique)):
                if grayscale_distance(unique[i], unique[j]) < 0.045:
                    issues.append(VisualIssue("INFO", "LOW_GRAY_CONTRAST", f"{prefix}: line colors {unique[i]} and {unique[j]} may merge in grayscale; use marker/linestyle redundancy."))
                    break

    return issues


def assert_no_errors(fig) -> None:
    errors = [i for i in lint_figure(fig) if i.severity == "ERROR"]
    if errors:
        raise AssertionError("; ".join(i.message for i in errors))
