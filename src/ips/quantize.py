"""Amplitude quantization (implementation pending)."""

from __future__ import annotations

import numpy as np


def quantization_step(lo: float, hi: float, q: int = 12) -> float:
    """Return the maximum amplitude error of a uniform ``q``-bit quantizer.

    The step is ``(hi - lo) / (2**q - 1)``; the returned value is half a step.
    """
    raise NotImplementedError("Implementation will be released upon acceptance.")


def quantize_amplitudes(values: np.ndarray, lo: float, hi: float, q: int = 12) -> np.ndarray:
    """Map amplitudes in ``[lo, hi]`` to ``q``-bit integer codes (round to nearest)."""
    raise NotImplementedError("Implementation will be released upon acceptance.")


def dequantize(codes: np.ndarray, lo: float, hi: float, q: int = 12) -> np.ndarray:
    """Map ``q``-bit codes back to amplitudes in mmHg."""
    raise NotImplementedError("Implementation will be released upon acceptance.")
