from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from sklearn_paper_display import confusion_matrix, roc_curve, precision_recall, prediction_error


def test_sklearn_display_adapters():
    y = np.array([0,0,1,1,0,1,0,1])
    pred = np.array([0,0,1,0,0,1,1,1])
    score = np.array([.1,.2,.8,.45,.25,.9,.65,.75])
    fig, axes = plt.subplots(2,2, figsize=(6,5), layout="constrained")
    confusion_matrix(y,pred,ax=axes[0,0],colorbar=False)
    roc_curve(y,score,ax=axes[0,1])
    precision_recall(y,score,ax=axes[1,0])
    prediction_error(np.arange(8), np.arange(8)+.2, ax=axes[1,1])
    assert all(len(ax.get_xlabel()) > 0 and len(ax.get_ylabel()) > 0 for ax in axes.flat)
    plt.close(fig)
