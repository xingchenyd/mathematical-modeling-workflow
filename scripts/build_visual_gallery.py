"""Build deterministic publication-style galleries used as regression previews."""
from __future__ import annotations
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from paper_plot_style import (  # noqa: E402
    SEMANTIC, apply_paper_style, add_panel_label, comparison_dotplot,
    convergence_gap, heatmap, pareto_scatter, save_figure, style_axes,
)
from visual_lint import lint_figure  # noqa: E402


def main():
    apply_paper_style()
    out = ROOT / "examples"
    out.mkdir(exist_ok=True)

    fig, axes = plt.subplots(2, 3, figsize=(7.2, 5.25), layout="constrained")

    # (a) paired comparison: dumbbell instead of thick grouped bars
    labels = ["方案A", "方案B", "方案C", "方案D", "方案E", "方案F"]
    comparison_dotplot(axes[0, 0], labels, [11.2, 10.6, 10.2, 9.8, 9.1, 8.9],
                       [9.5, 9.2, 8.8, 8.5, 8.3, 8.0], xlabel="完成时间 / h")
    add_panel_label(axes[0, 0], "(a)")
    axes[0, 0].legend(frameon=False, loc="lower right")

    # (b) incumbent/bound convergence
    it = np.arange(1, 8)
    convergence_gap(axes[0, 1], it, [110, 96, 90, 87, 85.3, 84.5, 84.1],
                    [70, 74, 77, 79, 80.5, 81.2, 81.8])
    add_panel_label(axes[0, 1], "(b)")
    axes[0, 1].legend(frameon=False, loc="best")

    # (c) pareto
    x = np.array([8.1, 8.4, 8.8, 9.3, 9.9, 10.6])
    y = np.array([91.9, 93.2, 94.1, 94.8, 95.1, 95.25])
    pareto_scatter(axes[0, 2], x, y, recommended_index=3, xlabel="成本 / 千元", ylabel="服务率 / %")
    add_panel_label(axes[0, 2], "(c)")
    axes[0, 2].legend(frameon=False, loc="lower right")

    # (d) sequential heatmap
    mat = np.array([[8, 2, 0, 1, 0], [3, 12, 4, 1, 0], [0, 5, 16, 6, 1], [0, 1, 5, 14, 4], [0, 0, 1, 4, 10]])
    heatmap(axes[1, 0], mat, xticklabels=["P1", "P2", "P3", "P4", "P5"],
            yticklabels=["A", "B", "C", "D", "E"], semantics="sequential")
    axes[1, 0].set_xlabel("目标节点")
    axes[1, 0].set_ylabel("来源节点")
    add_panel_label(axes[1, 0], "(d)")

    # (e) uncertainty ribbon
    xx = np.arange(1, 11)
    mean = np.array([8.8, 8.7, 8.5, 8.35, 8.28, 8.22, 8.20, 8.18, 8.17, 8.16])
    sd = np.array([.35, .30, .26, .22, .18, .16, .15, .14, .14, .13])
    axes[1, 1].plot(xx, mean, color=SEMANTIC["final"], marker="o", label="Mean")
    axes[1, 1].fill_between(xx, mean-sd, mean+sd, color=SEMANTIC["alternative"], alpha=.18, linewidth=0, label="±1 SD")
    axes[1, 1].set_xlabel("随机种子批次")
    axes[1, 1].set_ylabel("目标值")
    style_axes(axes[1, 1], grid="y")
    axes[1, 1].legend(frameon=False)
    add_panel_label(axes[1, 1], "(e)")

    # (f) feasibility frontier
    cap = np.arange(6, 14)
    objective = np.array([np.nan, np.nan, 102, 94, 89, 86, 84.7, 84.2])
    feasible = ~np.isnan(objective)
    axes[1, 2].plot(cap[feasible], objective[feasible], color=SEMANTIC["final"], marker="o")
    axes[1, 2].scatter(cap[~feasible], np.full((~feasible).sum(), 104), marker="x", s=36, color=SEMANTIC["risk"], label="不可行")
    axes[1, 2].axvline(8, color=SEMANTIC["baseline"], ls="--", lw=1.0, label="可行边界")
    axes[1, 2].set_xlabel("可用设备数")
    axes[1, 2].set_ylabel("最优目标值")
    style_axes(axes[1, 2], grid="y")
    axes[1, 2].legend(frameon=False, loc="upper right")
    add_panel_label(axes[1, 2], "(f)")

    issues = lint_figure(fig)
    errors = [x for x in issues if x.severity == "ERROR"]
    if errors:
        raise RuntimeError(errors)
    save_figure(fig, out / "publication_visual_gallery", formats=("pdf", "svg", "png"))
    plt.close(fig)
    print("Publication gallery built")
    for issue in issues:
        print(f"{issue.severity}: {issue.code}: {issue.message}")


if __name__ == "__main__":
    main()
