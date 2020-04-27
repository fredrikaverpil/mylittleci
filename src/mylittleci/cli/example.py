"""Add N numbers together.

Usage:

    .. runblock:: console

        $ example --help

    .. runblock:: console

        $ example --sum 666 999

    .. doctest::

        >>> from mylittleci.cli import example
        >>> example.run(integers=[666, 990])
        1656

"""

import argparse
from typing import List


def _parsed_args() -> argparse.Namespace:
    """Return the parsed arguments."""
    parser = argparse.ArgumentParser(
        description="Process some integers",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--sum",
        dest="integers",
        metavar="N",
        type=int,
        nargs="+",
        help="an integer for the accumulator",
    )

    return parser.parse_args()


def run(integers: List[int]) -> int:
    """Run main program."""
    result = sum(integers)
    print(result)
    return result


def main() -> None:
    """Take args and run."""
    args = _parsed_args()
    run(args.integers)


if __name__ == "__main__":
    main()
