"""Tests PaimonOS' Artifact Stat implementation.

Copyright (c) 2026 WhiteWaxula
SPDX-License-Identifier: MIT
"""

import pytest

from paimon_os.gacha.artifact.core import ArtifactStatType


@pytest.mark.parametrize(
    ("stat_type", "value"),
    [
        (ArtifactStatType.HP, "hp"),
        (ArtifactStatType.ATK, "atk"),
        (ArtifactStatType.DEF, "def"),
        (ArtifactStatType.HP_PERCENT, "hp_percentage"),
        (ArtifactStatType.ATK_PERCENT, "atk_percentage"),
        (ArtifactStatType.DEF_PERCENT, "def_percentage"),
        (ArtifactStatType.ELEMENTAL_MASTERY, "em"),
        (ArtifactStatType.ENERGY_RECHARGE, "er"),
        (ArtifactStatType.CRIT_RATE, "cr"),
        (ArtifactStatType.CRIT_DMG, "cd"),
        (ArtifactStatType.HEALING_BONUS, "healing_bonus"),
    ],
)
def test_stat_type_definition(stat_type: ArtifactStatType, value: str) -> None:
    """Asserts each artifact stat type takes the expected value.

    :param stat_type: The artifact stat type to be tested.
    :param value: The expected artifact stat type value.
    """
    assert stat_type.value == value


@pytest.mark.parametrize(
    ("stat_type", "display_name"),
    [
        (ArtifactStatType.HP, "HP"),
        (ArtifactStatType.ATK, "ATK"),
        (ArtifactStatType.DEF, "DEF"),
        (ArtifactStatType.HP_PERCENT, "HP(%)"),
        (ArtifactStatType.ATK_PERCENT, "ATK(%)"),
        (ArtifactStatType.DEF_PERCENT, "DEF(%)"),
        (ArtifactStatType.ELEMENTAL_MASTERY, "EM"),
        (ArtifactStatType.ENERGY_RECHARGE, "ER(%)"),
        (ArtifactStatType.CRIT_RATE, "CRIT Rate"),
        (ArtifactStatType.CRIT_DMG, "CRIT DMG"),
        (ArtifactStatType.HEALING_BONUS, "Healing Bonus"),
    ],
)
def test_stat_type_display_name(stat_type: ArtifactStatType, display_name: str) -> None:
    """Asserts each artifact stat type has the expected display name.

    :param stat_type: The artifact stat type to be tested.
    :param display_name: The expected artifact stat type display name.
    """
    assert stat_type.display_name == display_name
    assert str(stat_type) == display_name
