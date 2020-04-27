"""Pytest configuration."""

import pathlib
from typing import Any

import pytest

from mylittleci.lib.logger import default_logger


@pytest.fixture(name="repo_root")
def fixture_repo_root() -> pathlib.Path:
    """Return the repository root."""
    return pathlib.Path("..").resolve()


@pytest.fixture(name="logger")
def fixture_logger() -> Any:
    """Return the loguru logger.

    See ``mylittleci.lib.logger`` for more info.
    """
    return default_logger()
