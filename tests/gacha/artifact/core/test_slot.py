"""Tests PaimonOS' Artifact Slot implementation.

Copyright (c) 2026 WhiteWaxula
SPDX-License-Identifier: MIT
"""

import pytest

from paimon_os.gacha.artifact.core import ArtifactSlot


@pytest.mark.parametrize(
    ("slot", "value"),
    [
        (ArtifactSlot.FLOWER, "flower"),
        (ArtifactSlot.PLUME, "plume"),
        (ArtifactSlot.SANDS, "sands"),
        (ArtifactSlot.GOBLET, "goblet"),
        (ArtifactSlot.CIRCLET, "circlet"),
    ],
)
def test_slot_definition(slot: ArtifactSlot, value: str) -> None:
    """Asserts each artifact slot takes the expected value.

    :param slot: The artifact slot to be tested.
    :param value: The expected artifact slot value.
    """
    assert slot.value == value


@pytest.mark.parametrize(
    ("slot", "display_name"),
    [
        (ArtifactSlot.FLOWER, "Flower of Life"),
        (ArtifactSlot.PLUME, "Plume of Death"),
        (ArtifactSlot.SANDS, "Sands of Eon"),
        (ArtifactSlot.GOBLET, "Goblet of Eonothem"),
        (ArtifactSlot.CIRCLET, "Circlet of Logos"),
    ],
)
def test_slot_display_name(slot: ArtifactSlot, display_name: str) -> None:
    """Asserts each artifact slot has the correct display name.

    :param slot: The artifact slot to be tested.
    :param display_name: The expected artifact slot display name.
    """
    assert slot.display_name == display_name
    assert str(slot) == display_name
