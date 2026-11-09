# Data

No measurements are redistributed in this snapshot.

## Files to be released

    <record_id>_cycles.npy     per-cycle intervals, shape (n_cycles, 2), uint
    <record_id>.csv           original waveform export (user-supplied)

## Cycle table schema

| column | meaning |
|---|---|
| 0 | first sample index of the cycle (inclusive) |
| 1 | last sample index of the cycle (inclusive) |
| sampling rate | 500 Hz |
| typical length | 200--600 samples (0.4--1.2 s) |

Consecutive cycles share their boundary sample. Intervals rejected by the
segmentation or quality gates are not listed and are reported as gaps.

The full bitstream and index layout is described in `docs/data_format.md`.
