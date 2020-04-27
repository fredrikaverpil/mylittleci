"""Sum N integers together."""

from typing import List


class SimpleMathException(Exception):  # noqa: D101
    pass


def calculate_sum(integers: List[int]) -> int:
    """Sum.

    Usage:
        .. doctest::

            >>> from mylittleci.lib.simplepath import calculate_sum
            >>> calculate_sum(integers=[666, 990])
            1656

    """
    try:
        return sum(integers)
    except TypeError:
        raise SimpleMathException("You need to provide a list of integers.")
