"""Record-level encoder, decoder, and query path (implementation pending)."""

from __future__ import annotations

import numpy as np


def encode_record(signal: np.ndarray, cycles: np.ndarray, K: int = 8,
                  q: int = 12, block_cycles: int = 1) -> dict:
    """Encode a record into per-cycle blocks plus anchor plane and index.

    Returns a dictionary with the encoded blocks, the anchor plane, the index,
    and the measured bit length used for the reported rate.
    """
    raise NotImplementedError("Implementation will be released upon acceptance.")


def decode_record(encoded: dict) -> np.ndarray:
    """Reconstruct the waveform of the encoded cycles."""
    raise NotImplementedError("Implementation will be released upon acceptance.")


def query_anchor(encoded: dict, quantity: str) -> np.ndarray:
    """Answer a landmark-derived query without decompressing the payload.

    Supported quantities include ``sbp``, ``dbp``, ``pp``, and ``map``.
    """
    raise NotImplementedError("Implementation will be released upon acceptance.")
