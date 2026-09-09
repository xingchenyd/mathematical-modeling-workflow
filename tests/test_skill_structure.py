from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_skill import validate


def test_skill_structure():
    assert validate(ROOT) == []


def test_all_branches_restored():
    for i in range(1, 6):
        assert list((ROOT / "references").glob(f"B{i}_*.md")), f"missing B{i} branch"
