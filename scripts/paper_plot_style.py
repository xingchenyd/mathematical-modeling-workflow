"""Publication plotting utilities for mathematical-modeling-workflow V4.6.

The visual system separates *statistical/semantic correctness* from decoration.
Choose the chart from the claim first; then apply the shared house style.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence
import math

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.colors import to_rgb
import numpy as np

# Semantic roles stay stable throughout one paper.
SEMANTIC = {
    "final": "#355F8A",        # deep muted blue
    "alternative": "#6E9CC3",  # lighter blue
    "baseline": "#7A828C",     # neutral gray
    "improvement": "#5F8F79",  # muted green
    "secondary": "#C8874E",    # muted orange
    "risk": "#D06C66",         # muted salmon
    "severe_risk": "#A64B47",  # dark muted red
    "special": "#8A73A8",      # muted violet
    "text": "#334155",
    "grid": "#D9DEE5",
    "axis": "#B8C0C8",
    "background": "#FFFFFF",
}

# Colorblind-friendly qualitative fallback (Okabe-Ito family, slightly muted where useful).
QUALITATIVE = (
    "#0072B2", "#E69F00", "#009E73", "#CC79A7",
    "#56B4E9", "#D55E00", "#F0E442", "#000000",
)

MARKERS = ("o", "s", "^", "D", "P", "X", "v", ">")
LINESTYLES = ("-", "--", "-.", ":")

SEQUENTIAL_CMAPS = {"default": "viridis", "print": "cividis", "blue": "Blues", "bluegreen": "YlGnBu"}
DIVERGING_CMAPS = {"default": "RdBu_r", "brown_green": "BrBG", "purple_orange": "PuOr"}
CYCLIC_CMAPS = {"default": "twilight_shifted"}

@dataclass(frozen=True)
class FigureSize:
    width: float
    height: float

SIZES = {
    "single": FigureSize(3.45, 2.45),
    "wide": FigureSize(6.9, 3.1),
    "two_panel": FigureSize(6.9, 2.85),
    "three_panel": FigureSize(7.2, 2.65),
    "square": FigureSize(3.45, 3.15),
}


def _choose_cjk_font() -> str | None:
    names = {f.name for f in font_manager.fontManager.ttflist}
    for family in (
        "Noto Sans CJK SC", "Source Han Sans SC", "Microsoft YaHei",
        "PingFang SC", "SimHei", "Noto Sans CJK JP",
    ):
        if family in names:
            return family
    return None


def style_path() -> Path:
    return Path(__file__).resolve().parents[1] / "assets" / "styles" / "modeling-paper.mplstyle"


def apply_paper_style() -> None:
    """Apply portable style and a locally available CJK font if present."""
    plt.style.use(style_path())
    mpl.rcParams.update({
        "axes.edgecolor": SEMANTIC["axis"],
        "axes.labelcolor": SEMANTIC["text"],
        "text.color": SEMANTIC["text"],
        "xtick.color": SEMANTIC["text"],
        "ytick.color": SEMANTIC["text"],
        "grid.color": SEMANTIC["grid"],
    })
    family = _choose_cjk_font()
    if family:
        mpl.rcParams["font.family"] = family


def new_figure(kind: str = "single", *, nrows: int = 1, ncols: int = 1,
               layout: str = "constrained", **kwargs):
    """Create a final-size figure with constrained layout by default."""
    apply_paper_style()
    size = SIZES.get(kind, SIZES["single"])
    return plt.subplots(nrows=nrows, ncols=ncols, figsize=(size.width, size.height),
                        layout=layout, **kwargs)


def style_axes(ax, *, grid: str | None = None, zero_line: bool = False):
    ax.spines["left"].set_color(SEMANTIC["axis"])
    ax.spines["bottom"].set_color(SEMANTIC["axis"])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(colors=SEMANTIC["text"], length=3.0, width=0.7)
    ax.set_axisbelow(True)
    if grid in {"x", "y", "both"}:
        ax.grid(axis=grid, color=SEMANTIC["grid"], lw=0.55, alpha=0.55)
    if zero_line:
        ax.axhline(0, color=SEMANTIC["baseline"], lw=0.8, zorder=0)
    return ax


def bar_width(n_series: int) -> float:
    if n_series <= 1:
        return 0.52
    if n_series == 2:
        return 0.31
    if n_series in (3, 4):
        return 0.21
    raise ValueError("More than four grouped series: use dot plot, heatmap, small multiples, or a table.")


def recommend_categorical_chart(n_categories: int, n_series: int = 1, *, paired: bool = False) -> str:
    if paired:
        return "dumbbell-or-slope"
    if n_categories <= 5 and n_series <= 4:
        return "bar"
    if n_categories <= 12:
        return "horizontal-dot-or-bar"
    return "sorted-dot-heatmap-or-small-multiples"


def choose_colormap(kind: str, *, centered: bool = False, print_safe: bool = False) -> str:
    """Choose a colormap by data semantics, not aesthetics.

    kind: ordered/sequential, diverging, cyclic, categorical.
    Diverging is rejected unless a meaningful center exists.
    """
    k = kind.lower()
    if k in {"ordered", "sequential", "magnitude", "nonnegative"}:
        return SEQUENTIAL_CMAPS["print" if print_safe else "default"]
    if k in {"diverging", "deviation", "difference"}:
        if not centered:
            raise ValueError("Diverging colormap requires a meaningful center (e.g. zero or baseline).")
        return DIVERGING_CMAPS["default"]
    if k in {"cyclic", "angle", "phase", "time-of-day"}:
        return CYCLIC_CMAPS["default"]
    if k in {"categorical", "qualitative"}:
        raise ValueError("Categorical data should use a discrete qualitative palette, not a continuous colormap.")
    raise ValueError(f"Unknown colormap semantics: {kind}")


def place_legend(ax, *, outside: bool = False, ncol: int = 1, loc: str = "best"):
    if outside:
        return ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5), ncol=ncol, frameon=False)
    return ax.legend(loc=loc, ncol=ncol, frameon=False)


def add_panel_label(ax, label: str) -> None:
    ax.text(-0.14, 1.07, label, transform=ax.transAxes, va="top", ha="left",
            fontsize=10.0, fontweight="bold", color=SEMANTIC["text"])


def remove_in_axes_title(ax) -> None:
    """Paper captions usually carry the title; keep in-axes titles minimal."""
    ax.set_title("")


def luminance(color: str) -> float:
    r, g, b = to_rgb(color)
    # sRGB relative luminance approximation sufficient for linting.
    def linear(c: float) -> float:
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = linear(r), linear(g), linear(b)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def grayscale_distance(c1: str, c2: str) -> float:
    return abs(luminance(c1) - luminance(c2))


def semantic_cycle(keys: Sequence[str]) -> list[str]:
    return [SEMANTIC[k] for k in keys]


def annotate_point(ax, x, y, text: str, *, xytext=(5, 5), color: str | None = None):
    return ax.annotate(text, (x, y), xytext=xytext, textcoords="offset points",
                       fontsize=8, color=color or SEMANTIC["text"])


def save_figure(fig, path_base: str | Path, *, raster_dpi: int = 400,
                formats: Iterable[str] = ("pdf", "svg", "png")) -> list[Path]:
    """Export vector-first figures plus a high-DPI raster preview."""
    base = Path(path_base)
    base.parent.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []
    for ext in formats:
        out = base.with_suffix(f".{ext}")
        kwargs = {"bbox_inches": "tight", "facecolor": "white"}
        if ext.lower() in {"png", "jpg", "jpeg", "tif", "tiff"}:
            kwargs["dpi"] = raster_dpi
        fig.savefig(out, **kwargs)
        outputs.append(out)
    return outputs


def comparison_dotplot(ax, labels: Sequence[str], baseline: Sequence[float], final: Sequence[float], *, xlabel: str):
    """Preferred over grouped bars for paired comparisons across many categories."""
    y = np.arange(len(labels))
    b = np.asarray(baseline, dtype=float)
    f = np.asarray(final, dtype=float)
    for yi, x0, x1 in zip(y, b, f):
        ax.plot([x0, x1], [yi, yi], color=SEMANTIC["grid"], lw=1.3, zorder=1)
    ax.scatter(b, y, s=24, color=SEMANTIC["baseline"], label="Baseline", zorder=2)
    ax.scatter(f, y, s=28, color=SEMANTIC["final"], label="Final", zorder=3)
    ax.set_yticks(y, labels)
    ax.set_ylabel("方案")
    ax.set_xlabel(xlabel)
    style_axes(ax, grid="x")
    return ax


def convergence_gap(ax, iterations: Sequence[float], incumbent: Sequence[float], bound: Sequence[float], *, ylabel: str = "目标值"):
    x = np.asarray(iterations)
    ax.plot(x, incumbent, color=SEMANTIC["final"], marker="o", label="Best feasible")
    ax.plot(x, bound, color=SEMANTIC["baseline"], marker="s", ls="--", label="Bound")
    ax.fill_between(x, bound, incumbent, color=SEMANTIC["alternative"], alpha=0.10, linewidth=0)
    ax.set_xlabel("迭代")
    ax.set_ylabel(ylabel)
    style_axes(ax, grid="y")
    return ax


def pareto_scatter(ax, x, y, *, recommended_index: int | None = None, xlabel: str, ylabel: str):
    x = np.asarray(x); y = np.asarray(y)
    ax.scatter(x, y, s=26, color=SEMANTIC["alternative"], alpha=0.78,
               edgecolors="white", linewidths=0.35, label="候选方案")
    if recommended_index is not None:
        i = int(recommended_index)
        ax.scatter([x[i]], [y[i]], s=48, marker="D", color=SEMANTIC["final"], label="推荐点", zorder=4)
    ax.set_xlabel(xlabel); ax.set_ylabel(ylabel)
    style_axes(ax, grid="both")
    return ax


def heatmap(ax, matrix, *, xticklabels=None, yticklabels=None, semantics: str = "sequential", center: float | None = None, colorbar=True):
    data = np.asarray(matrix, dtype=float)
    centered = center is not None
    cmap = choose_colormap("diverging" if centered else semantics, centered=centered, print_safe=False)
    if centered:
        vmax = np.nanmax(np.abs(data - center))
        im = ax.imshow(data, cmap=cmap, vmin=center-vmax, vmax=center+vmax, aspect="auto")
    else:
        im = ax.imshow(data, cmap=cmap, aspect="auto")
    if xticklabels is not None: ax.set_xticks(np.arange(len(xticklabels)), xticklabels)
    if yticklabels is not None: ax.set_yticks(np.arange(len(yticklabels)), yticklabels)
    if colorbar: ax.figure.colorbar(im, ax=ax, fraction=0.046, pad=0.03)
    return im
