"""Shared paper plotting style for the mathematical-modeling workflow V4.5.

The module standardizes semantics, not decoration. Use colors according to meaning,
and choose chart type before styling.
"""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
from matplotlib import font_manager

PALETTE = {
    "final": "#355F8A",
    "alternative": "#5D8DB8",
    "light": "#A7C2DC",
    "baseline": "#737B86",
    "improvement": "#5C8D75",
    "secondary": "#C9824B",
    "risk": "#D46A65",
    "severe_risk": "#A94E4A",
    "special": "#8B6FA8",
    "grid": "#D2D7DD",
    "text": "#2F3E4D",
    "background": "#FAFAFA",
}

MARKERS = ("o", "s", "^", "D", "P", "X")
LINESTYLES = ("-", "--", "-.", ":")


def _choose_cjk_font() -> str | None:
    names = {f.name for f in font_manager.fontManager.ttflist}
    for family in (
        "Noto Sans CJK SC",
        "Noto Sans CJK JP",
        "Source Han Sans SC",
        "Microsoft YaHei",
        "PingFang SC",
        "SimHei",
    ):
        if family in names:
            return family
    return None


def apply_paper_style() -> None:
    """Apply final-size defaults suitable for LaTeX paper figures."""
    family = _choose_cjk_font()
    params = {
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.edgecolor": "#BFC5CC",
        "axes.labelcolor": PALETTE["text"],
        "axes.titlecolor": PALETTE["text"],
        "axes.titlesize": 10.5,
        "axes.labelsize": 9.0,
        "xtick.labelsize": 8.0,
        "ytick.labelsize": 8.0,
        "legend.fontsize": 8.0,
        "axes.linewidth": 0.8,
        "grid.color": PALETTE["grid"],
        "grid.linewidth": 0.6,
        "grid.alpha": 0.55,
        "lines.linewidth": 1.6,
        "lines.markersize": 4.2,
        "legend.frameon": False,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "axes.unicode_minus": False,
        "savefig.bbox": "tight",
    }
    if family:
        params["font.family"] = family
    plt.rcParams.update(params)


def bar_width(n_series: int) -> float:
    """Return conservative grouped-bar width by number of series."""
    if n_series <= 1:
        return 0.52
    if n_series == 2:
        return 0.31
    if n_series in (3, 4):
        return 0.21
    raise ValueError("For >4 series, prefer dot/heatmap/small-multiples instead of grouped bars.")


def style_axes(ax, *, grid: str | None = "y"):
    """Apply light axes styling without adding chart-specific semantics."""
    ax.spines["left"].set_color("#BFC5CC")
    ax.spines["bottom"].set_color("#BFC5CC")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(colors=PALETTE["text"])
    if grid == "y":
        ax.grid(axis="y", color=PALETTE["grid"], lw=0.6, alpha=0.55)
        ax.set_axisbelow(True)
    elif grid == "x":
        ax.grid(axis="x", color=PALETTE["grid"], lw=0.6, alpha=0.55)
        ax.set_axisbelow(True)
    elif grid == "both":
        ax.grid(True, color=PALETTE["grid"], lw=0.6, alpha=0.55)
        ax.set_axisbelow(True)
    return ax


def place_legend(ax, *, outside: bool = False, ncol: int = 1):
    if outside:
        return ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5), ncol=ncol, frameon=False)
    return ax.legend(frameon=False, ncol=ncol)


def add_panel_label(ax, label: str) -> None:
    ax.text(-0.08, 1.04, label, transform=ax.transAxes, va="top", ha="left",
            fontsize=10.5, fontweight="bold", color=PALETTE["text"])


def save_figure(fig, path_base: str | Path, *, raster_dpi: int = 400,
                formats: Iterable[str] = ("pdf", "png")) -> list[Path]:
    base = Path(path_base)
    base.parent.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []
    for ext in formats:
        out = base.with_suffix(f".{ext}")
        kwargs = {"bbox_inches": "tight"}
        if ext.lower() in {"png", "jpg", "jpeg"}:
            kwargs["dpi"] = raster_dpi
        fig.savefig(out, **kwargs)
        outputs.append(out)
    return outputs


def self_test(output_dir: str | Path) -> list[Path]:
    """Generate a small preview to verify fonts, palette, widths and export."""
    import numpy as np

    apply_paper_style()
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(1, 3, figsize=(7.1, 2.55), constrained_layout=True)

    # Narrow grouped bars
    x = np.arange(4)
    w = bar_width(2)
    axes[0].bar(x - w/2, [10, 8, 7, 6], width=w, color=PALETTE["baseline"], label="Baseline")
    axes[0].bar(x + w/2, [8, 6.5, 5.8, 5.4], width=w, color=PALETTE["final"], label="Final")
    axes[0].set_xticks(x, ["阶段1", "阶段2", "阶段3", "阶段4"])
    axes[0].set_ylabel("目标值")
    style_axes(axes[0], grid="y")
    add_panel_label(axes[0], "(a)")
    axes[0].legend(frameon=False, fontsize=7)

    # Best-so-far + bound
    it = np.arange(1, 7)
    incumbent = [100, 91, 86, 84, 83, 82.5]
    bound = [70, 72, 74, 75.5, 76, 77]
    axes[1].plot(it, incumbent, color=PALETTE["final"], marker="o", label="Best feasible")
    axes[1].plot(it, bound, color=PALETTE["baseline"], ls="--", marker="s", label="Bound")
    axes[1].set_xlabel("迭代")
    axes[1].set_ylabel("目标值")
    style_axes(axes[1], grid="y")
    add_panel_label(axes[1], "(b)")
    axes[1].legend(frameon=False, fontsize=7)

    # Pareto-like scatter
    cost = np.array([10, 9.2, 8.7, 8.4, 8.1, 7.8])
    service = np.array([92, 93, 94.2, 94.8, 95.0, 95.1])
    axes[2].scatter(cost, service, s=28, color=PALETTE["alternative"], alpha=.75,
                    edgecolors="white", linewidths=.4)
    axes[2].scatter([8.4], [94.8], s=42, color=PALETTE["final"], marker="D", label="推荐点")
    axes[2].set_xlabel("成本")
    axes[2].set_ylabel("服务率/%")
    style_axes(axes[2], grid="both")
    add_panel_label(axes[2], "(c)")
    axes[2].legend(frameon=False, fontsize=7)

    return save_figure(fig, output_dir / "visual_style_preview", formats=("pdf", "png"))


if __name__ == "__main__":
    self_test(Path(__file__).resolve().parents[1] / "examples")
