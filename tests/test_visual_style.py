from pathlib import Path
import sys
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from paper_plot_style import bar_width, choose_colormap, new_figure, save_figure, SEMANTIC
from visual_lint import lint_figure


def test_bar_width_rules():
    assert 0.45 <= bar_width(1) <= 0.60
    assert 0.28 <= bar_width(2) <= 0.34
    assert 0.18 <= bar_width(3) <= 0.25


def test_diverging_requires_center():
    try:
        choose_colormap("diverging", centered=False)
    except ValueError:
        pass
    else:
        raise AssertionError("diverging map must require meaningful center")


def test_vector_export_and_lint(tmp_path):
    fig, ax = new_figure("single")
    ax.plot([1,2,3], [3,2,1], color=SEMANTIC["final"])
    ax.set_xlabel("x / unit")
    ax.set_ylabel("y / unit")
    issues = lint_figure(fig)
    assert not [i for i in issues if i.severity == "ERROR"]
    outputs = save_figure(fig, tmp_path / "figure", formats=("pdf","svg","png"))
    for p in outputs: assert p.exists() and p.stat().st_size > 0
    plt.close(fig)
