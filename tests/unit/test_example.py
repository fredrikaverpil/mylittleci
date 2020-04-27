"""Test the example CLI binary."""

from subprocess import run
from typing import List

import pytest
from hypothesis import given
from hypothesis import strategies
from mylittleci.cli import example


def test_example_binary(capfd: pytest.Class) -> None:
    """Add numbers together using binary and assert the output to stdout."""
    cmd = ["example", "--sum", "666", "999"]
    proc = run(cmd, check=False)
    assert proc.returncode == 0
    captured = capfd.readouterr()
    # print(captured)  # debug
    assert captured.out.rstrip() == "1665".rstrip()
    assert captured.err == ""


@given(integers=strategies.lists(strategies.integers()))
def test_example_api(integers: List[int]) -> None:
    """Add numbers together using the API."""
    result = example.run(integers=integers)
    assert result == sum(integers)
