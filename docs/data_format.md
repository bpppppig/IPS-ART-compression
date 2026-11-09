# Data format

## 1. Processed cycle tables

File name: `<record_id>_cycles.npy`

| property | value |
|---|---|
| dtype | unsigned integer |
| shape | `(n_cycles, 2)` |
| columns | `[start_sample, end_sample]`, inclusive |
| sampling rate | 500 Hz |
| cycle length | 200--600 samples (0.4--1.2 s) |

Each row delimits one cardiac cycle in the original record. Consecutive cycles
share their boundary sample and otherwise do not overlap. Intervals that fail
segmentation or the quality gates are absent from the table and are reported as
gaps; they are never interpolated.

## 2. Per-cycle block (compressed payload)

| field | width | notes |
|---|---|---|
| amplitude range | 64 bit | two float32 values `lo`, `hi` |
| amplitudes | `K x 12 bit` | uniform quantization of `[lo, hi]` |
| positions | `K x pos_bits` | ascending differences, `pos_bits = ceil(log2 n)` |
| anchor bitmap | 5 bit | presence of the five landmark types (optional) |

The block is entropy-coded with zlib. The quantization step is
`(hi - lo) / (2^q - 1)` with `q = 12`, so the maximum amplitude error is half a
step. Positions are stored losslessly.

## 3. Anchor plane

| field | width |
|---|---|
| five anchor positions | `5 x 10 bit` |
| five anchor amplitudes | `5 x 12 bit` |
| total | 110 bit, stored as 14 bytes |

The plane shares the per-cycle amplitude range with the payload, so a query
reads the 8-byte range header together with the plane.

## 4. Index entry

| field | width |
|---|---|
| record identifier | implementation defined |
| cycle identifier | implementation defined |
| byte offset | 8 byte |
| sample count `n` | 4 byte |

The index is stored separately from the data blocks; binary search on the cycle
identifier locates a block without scanning the encoded waveform.

## 5. Rate conventions

Three accountings are reported in the paper and are not interchangeable:
per-cycle payload, per-cycle block, and single-stream. Rates are always quoted
in bits per original sample (bpp) and labelled with the convention used.
