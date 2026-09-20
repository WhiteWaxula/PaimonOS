"""Artifact rarity definition.

Copyright (c) 2026 WhiteWaxula
SPDX-License-Identifier: MIT
"""

from enum import IntEnum


class ArtifactRarity(IntEnum):
    """Defines the possible rarity values of Genshin Impact's artifacts."""

    ONE_STAR: int = 1
    TWO_STAR: int = 2
    THREE_STAR: int = 3
    FOUR_STAR: int = 4
    FIVE_STAR: int = 5

    @property
    def display_name(self) -> str:
        """Retrieve the name to be displayed of the artifact rarity.

        :return: The full and correct name of the artifact rarity.
        """
        return "⭐" * self.value

    def __str__(self) -> str:
        """Retrieve human-readable representation of the artifact rarity.

        :return: The human-readable representation of the artifact rarity.
        """
        return self.display_name
