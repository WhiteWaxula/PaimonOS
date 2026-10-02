"""Tests PaimonOS' Artifact Stat implementation.

Copyright (c) 2026 WhiteWaxula
SPDX-License-Identifier: MIT
"""

from dataclasses import FrozenInstanceError

import pytest

from paimon_os.gacha.artifact.core import (
    Artifact,
    ArtifactRarity,
    ArtifactSlot,
    ArtifactStat,
    ArtifactStatType,
)


def create_artifact(
    slot: ArtifactSlot | None = None,
    main_stat: ArtifactStat | None = None,
    sub_stats: tuple[ArtifactStat, ...] | None = None,
) -> Artifact:
    """Create an artifact for testing purposes.

    :param slot: The artifact slot, defaults to None
    :param main_stat: The main stat to be used, defaults to None
    :param sub_stats: The sub stats to be used, defaults to None
    :return: An artifact with the specified characteristics.
    """
    # Step 1: Assigning default values if not given
    slot = slot if slot is not None else ArtifactSlot.PLUME
    main_stat = (
        main_stat if main_stat is not None else ArtifactStat(ArtifactStatType.CRIT_RATE, 10.5)
    )
    sub_stats = sub_stats if sub_stats is not None else ()

    # Step 2: Create and return the artifact
    return Artifact("Example Set", ArtifactRarity.FIVE_STAR, slot, 0, main_stat, sub_stats)


def test_artifact_inmutability() -> None:
    """Asserts that artifacts are inmutable."""
    artifact = create_artifact()
    with pytest.raises(FrozenInstanceError):
        artifact.set = "Another example set"


def test_artifact_describe() -> None:
    """Asserts that artifact descriptions take the expected value."""
    artifact = create_artifact(
        slot=ArtifactSlot.PLUME,
        main_stat=ArtifactStat(ArtifactStatType.ATK, 53.5),
        sub_stats=(
            ArtifactStat(ArtifactStatType.CRIT_DMG, 20.5),
            ArtifactStat(ArtifactStatType.CRIT_RATE, 10.5),
        ),
    )

    assert artifact.describe() == (
        "- Set: Example Set\n"
        "- Slot: Plume of Death\n"
        "- Rarity: ⭐⭐⭐⭐⭐\n"
        "- Level: 0\n"
        "- Main stat: ATK=53.5000\n"
        "- Sub stats:\n"
        "\t- CRIT DMG=20.5000\n"
        "\t- CRIT Rate=10.5000"
    )


def test_crit_value_no_crit() -> None:
    """Asserts crit value is 0.0 when the artifact has no crit."""
    artifact = create_artifact(main_stat=ArtifactStat("HP", 10), sub_stats=())
    assert artifact.crit_value == 0.0


def test_crit_value_main_stat_only() -> None:
    """Asserts crit value considers the main stat."""
    crit_dmg_artifact = create_artifact(
        ArtifactSlot("circlet"),
        main_stat=ArtifactStat(ArtifactStatType.CRIT_DMG, 7.5),
        sub_stats=(),
    )
    assert crit_dmg_artifact.crit_value == pytest.approx(7.5)

    crit_rate_artifact = create_artifact(
        main_stat=ArtifactStat(ArtifactStatType.CRIT_RATE, 5.5),
        sub_stats=(),
    )
    assert crit_rate_artifact.crit_value == pytest.approx(11.0)


def test_crit_value_substats_only() -> None:
    """Asserts crit value considers the sub stats."""
    crit_dmg_substat_artifact = create_artifact(
        slot=ArtifactSlot("plume"),
        main_stat=ArtifactStat(ArtifactStatType.ATK, 5.5),
        sub_stats=(ArtifactStat(ArtifactStatType.CRIT_DMG, 3.5),),
    )
    assert crit_dmg_substat_artifact.crit_value == pytest.approx(3.5)

    crit_rate_substat_artifact = create_artifact(
        slot=ArtifactSlot("plume"),
        main_stat=ArtifactStat(ArtifactStatType.ATK, 10.0),
        sub_stats=(ArtifactStat(ArtifactStatType.CRIT_RATE, 5.5),),
    )
    assert crit_rate_substat_artifact.crit_value == pytest.approx(11)

    crit_dmg_crit_rate_artifact = create_artifact(
        slot=ArtifactSlot("plume"),
        main_stat=ArtifactStat(ArtifactStatType.ATK, 5.5),
        sub_stats=(
            ArtifactStat(ArtifactStatType.CRIT_RATE, 5.5),
            ArtifactStat(ArtifactStatType.CRIT_DMG, 13.0),
        ),
    )
    assert crit_dmg_crit_rate_artifact.crit_value == pytest.approx(24.0)


def test_crit_value_main_and_substats() -> None:
    """Asserts crit value considers both main and sub stats together."""
    cr_artifact = create_artifact(
        slot=ArtifactSlot("circlet"),
        main_stat=ArtifactStat(ArtifactStatType.CRIT_RATE, 10.5),
        sub_stats=(ArtifactStat(ArtifactStatType.CRIT_DMG, 5.5),),
    )
    assert cr_artifact.crit_value == pytest.approx(26.5)

    cd_artifact = create_artifact(
        slot=ArtifactSlot("circlet"),
        main_stat=ArtifactStat(ArtifactStatType.CRIT_DMG, 10.0),
        sub_stats=(ArtifactStat(ArtifactStatType.CRIT_RATE, 5.5),),
    )
    assert cd_artifact.crit_value == pytest.approx(21)
