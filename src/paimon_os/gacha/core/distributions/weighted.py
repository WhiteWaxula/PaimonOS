"""Implements PaimonOS weighted distribution.

Copyright (c) 2026 WhiteWaxula
SPDX-License-Identifier: MIT
"""

from dataclasses import dataclass
from math import isfinite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import random


@dataclass(frozen=True, slots=True)
class WeightedDistribution[T]:
    """Implements a weighted distribution within PaimonOS."""

    weights: tuple[tuple[T, float], ...]

    def __post_init__(self) -> None:
        """Validate the provided distribution."""
        if not self.weights:
            raise ValueError("A weighted distribution cannot be empty")

        for item, weight in self.weights:
            if not isfinite(weight):
                raise ValueError(f"Distribution item '{item}' has invalid weight: {weight}")

            if weight < 0:
                raise ValueError(f"Distribution item '{item}' has negative weight: {weight}")

        if sum(weight for _, weight in self.weights) <= 0:
            raise ValueError("At least one distribution item must have positive weight")

    def sample(self, rng: random.Random) -> T:
        """Sample from the weighted distribution.

        :param rng: An RNG object for experiment reproducibility.
        :return: An item sampled from the weighted distribution.
        """
        items, weights = zip(*self.weights, strict=True)
        return rng.choices(items, weights=weights, k=1)[0]
