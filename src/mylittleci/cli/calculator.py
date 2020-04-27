"""Add N numbers together.

Usage:

    .. runblock:: console

        $ example --help

    .. runblock:: console

        $ example --sum 666 999

"""

import argparse
import sys

from mylittleci.lib.simplemath import calculate_sum


def get_parser() -> argparse.ArgumentParser:
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
        help="integers to sum",
    )
    return parser


def main() -> None:
    """Take args and run."""
    parser = get_parser()
    args = parser.parse_args()
    if not args.integers:
        parser.print_help()
        sys.exit(2)
    result = calculate_sum(args.integers)
    print(result)


if __name__ == "__main__":
    main()
