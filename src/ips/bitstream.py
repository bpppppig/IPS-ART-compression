"""Bitstream packing (implementation pending)."""

from __future__ import annotations

import numpy as np


def encode_cycle(cycle: np.ndarray, indices: np.ndarray, q: int = 12,
                 anchor_mask: int | None = None) -> bytes:
    """Encode one cycle into a compressed block.

    Layout: 64-bit amplitude range, ``K`` amplitudes of ``q`` bits, ``K``
    position differences of ``ceil(log2 n)`` bits, optional 5-bit anchor
    bitmap; the byte stream is compressed with zlib.
    """
    raise NotImplementedError("Implementation will be released upon acceptance.")


def decode_cycle(blob: bytes, n: int, q: int = 12) -> tuple[np.ndarray, np.ndarray]:
    """Decode a block into ``(indices, amplitudes)``."""
    raise NotImplementedError("Implementation will be released upon acceptance.")


def pack_bits(values, widths) -> bytes:
    """Pack integer values with fixed bit widths into a byte string."""
    raise NotImplementedError("Implementation will be released upon acceptance.")


def unpack_bits(data: bytes, widths) -> list[int]:
    """Inverse of :func:`pack_bits`."""
    raise NotImplementedError("Implementation will be released upon acceptance.")
