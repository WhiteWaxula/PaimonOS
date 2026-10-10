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
        """Validate the provided distribution.

        :raises ValueError: If the distribution is empty, has negative or infinite weights,
        or no items with strictly positive (>0) weights.
        """
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

    def _sample_k_no_replacement(self, rng: random.Random, k: int) -> tuple[T, ...]:
        """Sample k elements from the weighted distribution without replacement.

        :param rng: An RNG object for experiment reproducibility.
        :param k: The number of elements to be sampled.
        :raises ValueError: If  `k` is greater than the number of eligible items.
        :return: A tuple with the k elements sampled from the distribution.
        """
        selected_items: list[T] = []
        current_weights = [(item, weight) for item, weight in self.weights if weight > 0]

        for _ in range(k):
            if not current_weights:
                raise ValueError(
                    f"Cannot choose k={k} items without replacement from given "
                    "weighted distribution, lower k or add more individuals"
                )

            items, weights = zip(*current_weights, strict=True)
            selected_item = rng.choices(items, weights=weights, k=1)[0]

            selected_items.append(selected_item)
            current_weights = [
                (item, weight) for item, weight in current_weights if item != selected_item
            ]

        return tuple(selected_items)

    def sample_k(self, rng: random.Random, k: int, *, replacement: bool = True) -> tuple[T, ...]:
        """Sample k elements from the weighted distribution.

        :param rng: An RNG object for experiment reproducibility.
        :param k: The number of elements to be sampled.
        :param replacement: Whether replacement will be used, defaults to True
        :raises ValueError: If k is zero or negative, or if `k` is greater than retrievable elements
        when replacement is `False`.
        :return: A tuple with the k elements sampled from the distribution.
        """
        if k <= 0:
            raise ValueError(f"At least 1 element must be sampled, but k={k} was provided")

        items, weights = zip(*self.weights, strict=True)

        if replacement:
            return tuple(rng.choices(items, weights=weights, k=k))

        return self._sample_k_no_replacement(rng, k)
