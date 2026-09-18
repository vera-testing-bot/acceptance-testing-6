"""Seed test, so a shard repo's CI has something to run."""

import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from shard_app import add, load_yaml


def test_add() -> None:
    assert add(2, 3) == 5


def test_load_yaml_rejects_unsafe_directives() -> None:
    """Unsafe YAML directives (e.g. ``!!python/object``) must be rejected."""
    unsafe = "!!python/object:os.system ['echo pwned']\n"
    with pytest.raises(yaml.YAMLError):
        load_yaml(unsafe)


def test_load_yaml_accepts_safe_input() -> None:
    assert load_yaml("key: value\n") == {"key": "value"}


def test_unsafe_vera_settings_are_rejected() -> None:
    """The checked-in ``.vera/settings.yaml`` carries an unsafe directive."""
    settings = Path(__file__).resolve().parents[1] / ".vera" / "settings.yaml"
    with pytest.raises(yaml.YAMLError):
        load_yaml(settings.read_text())
