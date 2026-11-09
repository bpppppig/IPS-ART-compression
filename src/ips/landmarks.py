"""Clinical landmark detection (implementation pending)."""

from __future__ import annotations

import numpy as np


def detect_notch(cycle: np.ndarray) -> tuple[int, float] | None:
    """Locate the dicrotic notch within one cycle.

    Returns ``(index, prominence)`` or ``None`` when no notch is detected.
    """
    raise NotImplementedError("Implementation will be released upon acceptance.")


def detect_dpeak(cycle: np.ndarray) -> tuple[int, float] | None:
    """Locate the post-notch diastolic peak within one cycle.

    Returns ``(index, prominence)`` or ``None`` when no peak is detected.
    """
    raise NotImplementedError("Implementation will be released upon acceptance.")


def anchor_indices(cycle: np.ndarray, kinds: list[str] | None = None) -> list[int]:
    """Return the retained clinical anchor indices of one cycle.

    ``kinds`` defaults to ``["valley", "peak", "notch", "dpeak"]``. The two
    boundary troughs and the systolic peak are always present in accepted
    cycles; the notch and the diastolic peak only when detected.
    """
    raise NotImplementedError("Implementation will be released upon acceptance.")
