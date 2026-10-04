"""Implements PaimonOS weighted distribution.

Copyright (c) 2026 WhiteWaxula
SPDX-License-Identifier: MIT
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import random


@dataclass(frozen=True, slots=True)
class WeightedDistribution[T]:
    """Implements a weighted distribution within PaimonOS."""

    weights: tuple[tuple[T, float], ...]

    def sample(self, rng: random.Random) -> T:
        """Sample from the weighted distribution.

        :param rng: An RNG object for experiment reproducibility.
        :return: An item sampled from the weighted distribution.
        """
        items, weights = zip(*self.weights, strict=True)
        return rng.choices(items, weights=weights, k=1)[0]
