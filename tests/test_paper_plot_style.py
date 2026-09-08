from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("paper_plot_style", ROOT / "scripts" / "paper_plot_style.py")
mod = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(mod)


def test_bar_widths():
    assert 0.45 <= mod.bar_width(1) <= 0.60
    assert 0.28 <= mod.bar_width(2) <= 0.34
    assert 0.18 <= mod.bar_width(3) <= 0.25


def test_palette_semantics():
    assert mod.PALETTE["final"] == "#355F8A"
    assert mod.PALETTE["baseline"] == "#737B86"
    assert mod.PALETTE["risk"] == "#D46A65"


def test_self_test_exports(tmp_path):
    outputs = mod.self_test(tmp_path)
    assert {p.suffix for p in outputs} == {".pdf", ".png"}
    assert all(p.exists() and p.stat().st_size > 1000 for p in outputs)
