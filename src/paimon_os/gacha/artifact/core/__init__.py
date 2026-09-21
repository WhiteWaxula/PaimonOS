"""Implements artifacts within PaimonOS.

Copyright (c) 2026 WhiteWaxula
SPDX-License-Identifier: MIT
"""

from .artifact import Artifact
from .rarity import ArtifactRarity
from .slot import ArtifactSlot
from .stat import ArtifactStat, ArtifactStatType

__all__ = [
    "Artifact",
    "ArtifactRarity",
    "ArtifactSlot",
    "ArtifactStat",
    "ArtifactStatType",
]
