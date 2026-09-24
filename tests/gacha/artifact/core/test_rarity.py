"""Tests PaimonOS' Artifact Rarity implementation.

Copyright (c) 2026 WhiteWaxula
SPDX-License-Identifier: MIT
"""

import pytest

from paimon_os.gacha.artifact.core import ArtifactRarity


@pytest.mark.parametrize(
    ("rarity", "value"),
    [
        (ArtifactRarity.ONE_STAR, 1),
        (ArtifactRarity.TWO_STAR, 2),
        (ArtifactRarity.THREE_STAR, 3),
        (ArtifactRarity.FOUR_STAR, 4),
        (ArtifactRarity.FIVE_STAR, 5),
    ],
)
def test_rarity_definition(rarity: ArtifactRarity, value: int) -> None:
    """Asserts each artifact rarity takes the expected value.

    :param rarity: The artifact rarity to be tested.
    :param value: The expected rarity value.
    """
    assert rarity.value == value, f"Rarity {rarity} takes value != {value}"


@pytest.mark.parametrize(
    ("rarity", "display_name"),
    [
        (ArtifactRarity.ONE_STAR, "⭐"),
        (ArtifactRarity.TWO_STAR, "⭐⭐"),
        (ArtifactRarity.THREE_STAR, "⭐⭐⭐"),
        (ArtifactRarity.FOUR_STAR, "⭐⭐⭐⭐"),
        (ArtifactRarity.FIVE_STAR, "⭐⭐⭐⭐⭐"),
    ],
)
def test_rarity_display_name(rarity: ArtifactRarity, display_name: str) -> None:
    """Asserts each artifact rarity has the correct display name.

    :param rarity: The artifact rarity to be tested.
    :param display_name: The expected rarity display name.
    """
    assert rarity.display_name == display_name
    assert str(rarity) == display_name
