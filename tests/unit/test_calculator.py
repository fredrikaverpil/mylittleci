"""Test the example calculator CLI binary."""

from subprocess import run
from typing import List

import pytest
from hypothesis import given
from hypothesis import strategies
from mylittleci.lib import simplemath


def test_calculator_binary(capfd: pytest.Class) -> None:
    """Add numbers together using binary and assert the output to stdout."""
    cmd = ["calculator", "--sum", "666", "999"]
    proc = run(cmd, check=False)
    assert proc.returncode == 0
    captured = capfd.readouterr()
    # print(captured)  # debug
    assert captured.out.rstrip() == "1665".rstrip()
    assert captured.err == ""


@pytest.mark.parametrize(
    "cmd, expected_exit_code",
    [
        (["calculator", "--help"], 0),
        (["calculator", "--sum", "1", "2", "3"], 0),
        (["calculator"], 2),
        (["calculator", "--blah"], 2),
    ],
)
def test_calculator_binary_exit_code(
    capfd: pytest.Class, expected_exit_code: int, cmd: List[str]
) -> None:
    """Add numbers together using binary and assert the output to stdout."""
    proc = run(cmd, check=False)
    assert proc.returncode == expected_exit_code


@given(integers=strategies.lists(strategies.integers()))
def test_calculator_api(integers: List[int]) -> None:
    """Add numbers together using the API."""
    result = simplemath.calculate_sum(integers=integers)
    assert result == sum(integers)


def test_calculator_api_type_error() -> None:
    """Add numbers together using the API."""
    with pytest.raises(simplemath.SimpleMathException) as excinfo:
        simplemath.calculate_sum("invalid input")
    assert "You need to provide a list of integers." in str(excinfo)
