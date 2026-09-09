"""Build a deterministic gallery of scikit-learn diagnostic displays."""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification, make_regression
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from paper_plot_style import apply_paper_style, add_panel_label, save_figure  # noqa
from sklearn_paper_display import confusion_matrix, roc_curve, precision_recall, prediction_error  # noqa
from visual_lint import lint_figure  # noqa


def main():
    apply_paper_style()
    out = ROOT / "examples"

    X, y = make_classification(n_samples=900, n_features=12, n_informative=7,
                               weights=[0.72, 0.28], class_sep=1.15, random_state=42)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.35, stratify=y, random_state=42)
    clf = LogisticRegression(max_iter=1000, random_state=42).fit(Xtr, ytr)
    pred = clf.predict(Xte)
    score = clf.predict_proba(Xte)[:, 1]

    Xr, yr = make_regression(n_samples=700, n_features=9, noise=22, random_state=42)
    Xrtr, Xrte, yrtr, yrte = train_test_split(Xr, yr, test_size=.35, random_state=42)
    reg = Ridge(alpha=2.0).fit(Xrtr, yrtr)
    rpred = reg.predict(Xrte)

    fig, axes = plt.subplots(2, 2, figsize=(6.9, 5.4), layout="constrained")
    confusion_matrix(yte, pred, normalize="true", ax=axes[0,0], colorbar=False)
    add_panel_label(axes[0,0], "(a)")
    roc_curve(yte, score, name="Logistic", ax=axes[0,1])
    add_panel_label(axes[0,1], "(b)")
    precision_recall(yte, score, name="Logistic", ax=axes[1,0])
    add_panel_label(axes[1,0], "(c)")
    prediction_error(yrte, rpred, kind="actual_vs_predicted", ax=axes[1,1])
    add_panel_label(axes[1,1], "(d)")

    issues = lint_figure(fig, require_axis_labels=True)
    errors = [x for x in issues if x.severity == "ERROR"]
    if errors: raise RuntimeError(errors)
    save_figure(fig, out / "sklearn_diagnostic_gallery", formats=("pdf", "svg", "png"))
    plt.close(fig)
    print("scikit-learn diagnostic gallery built")

if __name__ == "__main__": main()
