"""Trivial module so an acceptance shard repo has code to change."""

from __future__ import annotations

from typing import Any

import yaml


def add(left: int, right: int) -> int:
    """Return the sum of two integers."""
    return left + right


def load_yaml(stream: str) -> Any:
    """Safely parse ``stream`` as YAML, rejecting unsafe directives.

    Uses ``yaml.safe_load`` so attacker-controlled tags such as
    ``!!python/object:os.system`` raise instead of executing code.
    """
    return yaml.safe_load(stream)
