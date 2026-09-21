"""Artifact definition.

Copyright (c) 2026 WhiteWaxula
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .rarity import ArtifactRarity
    from .slot import ArtifactSlot
    from .stat import ArtifactStat


@dataclass(frozen=True)
class Artifact:
    """An abstraction of Genshin Impact's Artifacts."""

    rarity: ArtifactRarity
    slot: ArtifactSlot
    main_stat: ArtifactStat
    sub_stats: tuple[ArtifactStat, ...]

    @cached_property
    def crit_value(self) -> float:
        """Calculates the crit value of the artifact.

        :return: The crit value of the artifact.
        """
        raise NotImplementedError

    def describe(self) -> str:
        """Retrieve a detailed, human-readable description of the artifact.

        :return: A pretty description of the artifact.
        """
        return (
            f"- Slot: {self.slot}\n"
            f"- Rarity: {self.rarity}\n"
            f"- Main stat: {self.main_stat}\n"
            f"- Sub stats:\n" + ("\n".join(f"\t- {substat}" for substat in self.sub_stats))
        )
