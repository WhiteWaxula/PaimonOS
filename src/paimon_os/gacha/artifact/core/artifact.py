"""Artifact definition.

Copyright (c) 2026 WhiteWaxula
SPDX-License-Identifier: MIT
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .stat import ArtifactStatType

if TYPE_CHECKING:
    from .rarity import ArtifactRarity
    from .set import ArtifactSet
    from .slot import ArtifactSlot
    from .stat import ArtifactStat


@dataclass(frozen=True)
class Artifact:
    """An abstraction of Genshin Impact's Artifacts."""

    set: ArtifactSet
    rarity: ArtifactRarity
    slot: ArtifactSlot
    level: int
    main_stat: ArtifactStat
    sub_stats: tuple[ArtifactStat, ...]

    @property
    def crit_value(self) -> float:
        """Calculates the crit value of the artifact.

        :return: The crit value of the artifact.
        """
        return sum(
            stat.value * (2.0 if stat.type == ArtifactStatType.CRIT_RATE else 1.0)
            for stat in (self.main_stat, *self.sub_stats)
            if stat.type in (ArtifactStatType.CRIT_DMG, ArtifactStatType.CRIT_RATE)
        )

    def describe(self) -> str:
        """Retrieve a detailed, human-readable description of the artifact.

        :return: A pretty description of the artifact.
        """
        return (
            f"- Set: {self.set}\n"
            f"- Slot: {self.slot}\n"
            f"- Rarity: {self.rarity}\n"
            f"- Level: {self.level}\n"
            f"- Main stat: {self.main_stat}\n"
            f"- Sub stats:\n" + ("\n".join(f"\t- {substat}" for substat in self.sub_stats))
        )
