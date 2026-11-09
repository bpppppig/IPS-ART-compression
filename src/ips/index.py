"""Cycle index and anchor plane (implementation pending)."""

from __future__ import annotations

import numpy as np


def build_index(record_id: str, offsets, lengths) -> bytes:
    """Build the external index: cycle identifier, byte offset, sample count."""
    raise NotImplementedError("Implementation will be released upon acceptance.")


def lookup_cycle(index: bytes, cycle_id: int) -> tuple[int, int]:
    """Return ``(byte_offset, n)`` for a cycle without scanning the payload."""
    raise NotImplementedError("Implementation will be released upon acceptance.")


def encode_anchor_plane(anchors: dict, lo: float, hi: float) -> bytes:
    """Pack five anchor positions (10 bit) and amplitudes (12 bit) into 14 bytes."""
    raise NotImplementedError("Implementation will be released upon acceptance.")


def decode_anchor_plane(plane: bytes, lo: float, hi: float) -> dict:
    """Read the anchor plane without inflating the compressed payload."""
    raise NotImplementedError("Implementation will be released upon acceptance.")
