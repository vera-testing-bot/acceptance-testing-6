"""Trivial module so an acceptance shard repo has code to change."""


def add(left: int, right: int) -> int:
    """Return the sum of two integers."""
    return left + right


def answer() -> int:
    """Return the constant answer to everything."""
    return 42


def reverse_string(text: str) -> str:
    """Return ``text`` with its characters reversed."""
    return text[::-1]
