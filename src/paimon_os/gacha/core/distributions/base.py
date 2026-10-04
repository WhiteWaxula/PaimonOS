"""Implements PaimonOS base/generic mathematical distribution.

Copyright (c) 2026 WhiteWaxula
SPDX-License-Identifier: MIT
"""

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    import random


class Distribution[T](Protocol):
    """Defines any mathematical distribution within PaimonOS."""

    def sample(self, rng: random.Random) -> T:
        """Sample the distribution providing an item of it as a result.

        :param rng: An RNG object for experiment reproducibility.
        :return: An item sampled from the distribution.
        """
        ...
