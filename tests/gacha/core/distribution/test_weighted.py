"""Tests PaimonOS' weighted distribution implementation.

Copyright (c) 2026 WhiteWaxula
SPDX-License-Identifier: MIT
"""

import math
import random
import re
from dataclasses import FrozenInstanceError

import pytest

from paimon_os.gacha.core.distributions import WeightedDistribution


def test_immutability() -> None:
    """Asserts that distributions are immutable."""
    distribution = WeightedDistribution((("a", 0.5), ("b", 0.3)))

    with pytest.raises(FrozenInstanceError):
        distribution.weights = (("a", 0.5), ("b", 0.3), ("c", 0.2))


def test_empty_distribution() -> None:
    """Asserts that a weighted distribution cannot be created from an empty tuple."""
    with pytest.raises(ValueError, match="A weighted distribution cannot be empty"):
        WeightedDistribution(())


def test_negative_weight() -> None:
    """Asserts that a weighted distribution cannot be created with negative weights."""
    with pytest.raises(
        ValueError, match=re.escape("Distribution item 'b' has negative weight: -1.0")
    ):
        WeightedDistribution((("a", 0.5), ("b", -1.0)))


@pytest.mark.parametrize("weight", [float("nan"), math.inf, -math.inf])
def test_invalid_weights(weight: float) -> None:
    """Asserts that a weighted distribution cannot be created from illegal values.

    :param weight: The invalid weight to be tested.
    """
    with pytest.raises(
        ValueError, match=re.escape(f"Distribution item 'b' has invalid weight: {weight}")
    ):
        WeightedDistribution((("a", 1.0), ("b", weight)))


def test_zero_valued_distribution() -> None:
    """Asserts that a weighted distribution with weight sum = 0 cannot be created."""
    with pytest.raises(
        ValueError, match="At least one distribution item must have positive weight"
    ):
        WeightedDistribution((("a", 0), ("b", 0)))


@pytest.mark.parametrize("seed", range(20))
def test_draw_from_distribution(seed: int) -> None:
    """Asserts that all drawn items belong to the distribution.

    :param seed: The random seed to be used for testing.
    """
    weighted_elements = ("a", 0.5), ("b", 0.3)
    distribution_items = {element[0] for element in weighted_elements}

    distribution = WeightedDistribution(weighted_elements)
    rng = random.Random(seed)

    for _ in range(1000):
        item = distribution.sample(rng)
        assert item in distribution_items


@pytest.mark.parametrize("seed", range(20))
def test_reproducibility(seed: int) -> None:
    """Asserts the reproducibility of drawing from the distribution.

    :param seed: The random seed to be used for testing.
    """
    weighted_elements = (("a", 0.5), ("b", 0.3))

    distribution = WeightedDistribution(weighted_elements)

    rng_1 = random.Random(seed)
    rng_2 = random.Random(seed)

    for _ in range(1000):
        item_1 = distribution.sample(rng_1)
        item_2 = distribution.sample(rng_2)

        assert item_1 == item_2


@pytest.mark.parametrize("seed", range(20))
def test_zero_prob_not_drawn(seed: int) -> None:
    """Asserts that elements with no weight are never drawn."""
    distribution = WeightedDistribution((("a", 0.0), ("b", 1.0), ("c", 0.0)))
    rng = random.Random(seed)

    assert distribution.sample(rng) == "b"


@pytest.mark.parametrize("seed", range(20))
def test_weights(seed: int) -> None:
    """Asserts the weighted distribution draws items according to given weights.

    :param seed: The random seed to be used for testing.
    """
    distribution = WeightedDistribution((("a", 0.5), ("b", 0.3), ("c", 0.2)))
    rng = random.Random(seed)

    counts = {item: 0 for item, _ in distribution.weights}
    num_draws = 10000
    for _ in range(num_draws):
        item = distribution.sample(rng)
        counts[item] += 1

    relative_freqs = {item: freq / num_draws for item, freq in counts.items()}

    for item, expected_prob in distribution.weights:
        assert relative_freqs[item] == pytest.approx(expected_prob, abs=2e-2)
