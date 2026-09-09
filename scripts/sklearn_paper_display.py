"""Publication-styled adapters around scikit-learn Display objects.

scikit-learn computes canonical diagnostic displays; Matplotlib is then used to
apply the workflow's final paper styling. This keeps metric semantics separate
from aesthetics.
"""
from __future__ import annotations

from typing import Any
import matplotlib.pyplot as plt
import warnings
import sklearn

from paper_plot_style import SEMANTIC, apply_paper_style, style_axes



def _sklearn_ge_19() -> bool:
    try:
        parts = sklearn.__version__.split(".")
        return (int(parts[0]), int(parts[1])) >= (1, 9)
    except Exception:
        return False

def _curve_style():
    style = {"color": SEMANTIC["final"], "lw": 1.8}
    return {"curve_kwargs": style} if _sklearn_ge_19() else style

def _ax(ax=None, kind="single"):
    apply_paper_style()
    if ax is not None:
        return ax.figure, ax
    fig, ax = plt.subplots(figsize=(3.45, 3.0), layout="constrained")
    return fig, ax


def confusion_matrix(y_true, y_pred, *, labels=None, normalize="true", ax=None, colorbar=False):
    from sklearn.metrics import ConfusionMatrixDisplay
    fig, ax = _ax(ax)
    disp = ConfusionMatrixDisplay.from_predictions(
        y_true, y_pred, labels=labels, normalize=normalize,
        cmap="Blues", colorbar=colorbar, ax=ax, values_format=".2f" if normalize else "d"
    )
    style_axes(ax, grid=None)
    ax.set_xlabel("预测类别")
    ax.set_ylabel("真实类别")
    return disp


def roc_curve(y_true, y_score, *, name=None, ax=None):
    from sklearn.metrics import RocCurveDisplay
    fig, ax = _ax(ax)
    with warnings.catch_warnings():
        if not _sklearn_ge_19():
            warnings.filterwarnings("ignore", category=FutureWarning, module="sklearn")
        disp = RocCurveDisplay.from_predictions(
            y_true, y_score, name=name, ax=ax,
        plot_chance_level=True,
        chance_level_kw={"color": SEMANTIC["baseline"], "lw": 1.0, "ls": "--"},
            **_curve_style(),
        )
    ax.set_xlabel("假阳性率")
    ax.set_ylabel("真阳性率")
    style_axes(ax, grid="both")
    return disp


def precision_recall(y_true, y_score, *, name=None, ax=None):
    from sklearn.metrics import PrecisionRecallDisplay
    fig, ax = _ax(ax)
    with warnings.catch_warnings():
        if not _sklearn_ge_19():
            warnings.filterwarnings("ignore", category=FutureWarning, module="sklearn")
        disp = PrecisionRecallDisplay.from_predictions(
            y_true, y_score, name=name, ax=ax,
        plot_chance_level=True,
        chance_level_kw={"color": SEMANTIC["baseline"], "lw": 1.0, "ls": "--"},
            **_curve_style(),
        )
    ax.set_xlabel("召回率")
    ax.set_ylabel("精确率")
    style_axes(ax, grid="both")
    return disp


def calibration(y_true, y_prob, *, name=None, n_bins=8, strategy="quantile", ax=None):
    from sklearn.calibration import CalibrationDisplay
    fig, ax = _ax(ax)
    disp = CalibrationDisplay.from_predictions(
        y_true, y_prob, name=name, n_bins=n_bins, strategy=strategy, ax=ax,
        color=SEMANTIC["final"], marker="o", lw=1.7,
    )
    style_axes(ax, grid="both")
    return disp


def prediction_error(y_true, y_pred, *, kind="actual_vs_predicted", ax=None):
    from sklearn.metrics import PredictionErrorDisplay
    fig, ax = _ax(ax)
    disp = PredictionErrorDisplay.from_predictions(
        y_true, y_pred, kind=kind, ax=ax,
        scatter_kwargs={"s": 18, "alpha": 0.55, "color": SEMANTIC["alternative"], "edgecolors": "none"},
        line_kwargs={"color": SEMANTIC["severe_risk"], "lw": 1.3, "ls": "--"},
    )
    if kind == "actual_vs_predicted":
        ax.set_xlabel("预测值")
        ax.set_ylabel("真实值")
    else:
        ax.set_xlabel("预测值")
        ax.set_ylabel("残差")
    style_axes(ax, grid="both")
    return disp
