"""IPS: cycle-structured semantic codec for arterial pressure waveforms.

Placeholder package. Public functions are declared with their intended
contracts; implementations will be added upon acceptance.
"""

from .codec import decode_record, encode_record, query_anchor
from .keypoints import select_key_points
from .landmarks import anchor_indices, detect_dpeak, detect_notch
from .quantize import dequantize, quantize_amplitudes, quantization_step
from .segmentation import segment_cycles

__all__ = [
    "segment_cycles",
    "anchor_indices",
    "detect_notch",
    "detect_dpeak",
    "select_key_points",
    "quantize_amplitudes",
    "dequantize",
    "quantization_step",
    "encode_record",
    "decode_record",
    "query_anchor",
]
