"""Pytest configuration."""

import pathlib

import pytest


@pytest.fixture(name="repo_root")
def fixture_repo_root() -> pathlib.Path:
    """Return the repository root."""
    return pathlib.Path("..").resolve()
