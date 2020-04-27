"""mylittleci gateway pattern for Loguru logger."""

import sys

from loguru import logger

from typing import Any


def default_logger() -> Any:
    """Set up the generic logger based on Loguru.

    Usage:
        .. code-block:: python

            from mylittleci.lib.logger import default_logger
            logger = default_logger()
            logger.info("Hello, world")


    Loguru documentation:
        https://github.com/Delgan/loguru
    """
    # Add changes to logger here
    return logger
