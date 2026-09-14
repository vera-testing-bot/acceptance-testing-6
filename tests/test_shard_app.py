"""Seed test, so a shard repo's CI has something to run."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from shard_app import add, answer, reverse_string, subtract  # noqa: E402


def test_add() -> None:
    assert add(2, 3) == 5


def test_subtract() -> None:
    assert subtract(5, 3) == 2


def test_answer() -> None:
    assert answer() == 42


def test_reverse_string() -> None:
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""
