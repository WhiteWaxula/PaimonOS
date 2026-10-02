"""Artifact slot definition.

Copyright (c) 2026 WhiteWaxula
SPDX-License-Identifier: MIT
"""

from enum import StrEnum


class ArtifactSlot(StrEnum):
    """Defines the possible slots of Genshin Impact's artifacts."""

    FLOWER: str = "flower"
    PLUME: str = "plume"
    SANDS: str = "sands"
    GOBLET: str = "goblet"
    CIRCLET: str = "circlet"

    @property
    def display_name(self) -> str:
        """Retrieve the display name of the artifact slot.

        :return: The full and correct name of the artifact slot.
        """
        return {
            self.FLOWER: "Flower of Life",
            self.PLUME: "Plume of Death",
            self.SANDS: "Sands of Eon",
            self.GOBLET: "Goblet of Eonothem",
            self.CIRCLET: "Circlet of Logos",
        }[self]

    def __str__(self) -> str:
        """Retrieve human-readable representation of the artifact slot.

        :return: The human-readable representation of the artifact slot.
        """
        return self.display_name
