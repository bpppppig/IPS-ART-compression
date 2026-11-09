"""Keypoint selection (implementation pending)."""

from __future__ import annotations

import numpy as np


def select_key_points(
    signal: np.ndarray,
    K: int,
    return_alpha: bool = False,
    seed_indices: list[int] | None = None,
    distance: str = "vertical",
) -> np.ndarray:
    """Select ``K`` keypoints by recursive maximum-deviation splitting.

    Parameters
    ----------
    signal : ndarray, shape (n,)
        One cardiac cycle.
    K : int
        Point budget. The effective budget is
        ``min(n, max(K, len(seed_indices)))``, so anchors are never dropped.
    return_alpha : bool
        Also return the equivalent vertical-deviation threshold.
    seed_indices : list of int, optional
        Anchors that must be retained.
    distance : {"vertical", "perpendicular"}
        Deviation measure; ``vertical`` is used by IPS, ``perpendicular``
        reproduces the classical RDP criterion.

    Returns
    -------
    ndarray of int
        Ascending sample indices (and the equivalent threshold when requested).
    """
    raise NotImplementedError("Implementation will be released upon acceptance.")
