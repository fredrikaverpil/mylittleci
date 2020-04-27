"""Sum N integers together."""

from typing import List


class SimpleMathException(Exception):  # noqa: D101
    pass


def calculate_sum(integers: List[int]) -> int:
    """Return sum of given integers."""
    try:
        return sum(integers)
    except TypeError:
        raise SimpleMathException("You need to provide a list of integers.")
