"""Artifact stat definition.

Copyright (c) 2026 WhiteWaxula
SPDX-License-Identifier: MIT
"""

from dataclasses import dataclass
from enum import StrEnum


class ArtifactStatType(StrEnum):
    """Defines the possible stat types of Genshin Impact's artifacts."""

    HP: str = "hp"
    ATK: str = "atk"
    DEF: str = "def"

    HP_PERCENT: str = "hp_percentage"
    ATK_PERCENT: str = "atk_percentage"
    DEF_PERCENT: str = "def_percentage"

    ELEMENTAL_MASTERY: str = "em"
    ENERGY_RECHARGE: str = "er"
    CRIT_RATE: str = "cr"
    CRIT_DMG: str = "cd"

    HEALING_BONUS: str = "healing_bonus"

    @property
    def display_name(self) -> str:
        """Retrieve the name to be displayed of the artifact stat type.

        :return: The full and correct name of the artifact stat type.
        """
        return {
            self.HP: "HP",
            self.ATK: "ATK",
            self.DEF: "DEF",
            self.HP_PERCENT: "HP%",
            self.ATK_PERCENT: "ATK%",
            self.DEF_PERCENT: "DEF%",
            self.ELEMENTAL_MASTERY: "Elemental Mastery",
            self.ENERGY_RECHARGE: "Energy Recharge",
            self.CRIT_RATE: "CRIT Rate",
            self.CRIT_DMG: "CRIT DMG",
            self.HEALING_BONUS: "Healing Bonus",
        }[self]

    def __str__(self) -> str:
        """Retrieve human-readable representation of the artifact stat type.

        :return: The human-readable representation of the artifact stat type.
        """
        return self.display_name


@dataclass(frozen=True)
class ArtifactStat:
    """Defines Genshin Impact artifact's stats."""

    type: ArtifactStatType
    value: float

    @property
    def display_name(self) -> str:
        """Retrieve the name to be displayed of the artifact stat.

        :return: The full and correct name of the artifact stat.
        """
        return f"{self.type}={self.value:.4f}"

    def __str__(self) -> str:
        """Retrieve human-readable representation of the artifact stat.

        :return: The human-readable representation of the artifact stat.
        """
        return self.display_name
