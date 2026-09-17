"""Tests that PaimonOS is importable.

Copyright (c) 2026 WhiteWaxula
SPDX-License-Identifier: MIT
"""

import importlib


def test_import() -> None:
    """Tests that PaimonOS can be imported."""
    importlib.import_module("paimon_os")
