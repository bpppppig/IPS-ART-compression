# IPS: Semantic Compression of High-Density Periodic Vital-Sign Signals

**Status: placeholder repository.** The full implementation, the processed cycle
tables, and the experiment scripts will be released here upon acceptance of the
associated paper. This repository currently contains the interface skeleton, the
data-format specification, and the reproduction map only.

## What is IPS

IPS is a cycle-structured codec for invasive arterial pressure (ART) waveforms.
Each cardiac cycle is represented by a small set of clinically defined anchors
(two diastolic troughs and the systolic peak, plus the dicrotic notch and the
post-notch diastolic peak when detected) together with supplementary points
chosen under a point budget `K` or a vertical-deviation threshold `alpha`.
A separate, uncompressed anchor plane answers landmark-derived queries without
decompressing the waveform.

See `INTRODUCTION.md` for the problem statement and the three contributions.

## Repository layout

    src/ips/          core library (interfaces only in this snapshot)
    scripts/          command-line entry points used in the paper
    docs/             data format, bitstream layout, reproduction map
    data/             data schema; no measurements are redistributed here
    tests/            smoke tests

## Data

The paper uses 105 invasive ART records from a public surgical vital-sign
database, segmented into 1,518,283 cardiac cycles. The source waveforms are not
redistributed; only the processed per-cycle tables will be released. The schema
is specified in `docs/data_format.md`.

## Quick start

    pip install -r requirements.txt
    python scripts/encode_record.py --cycles <record>_cycles.npy --signal <record>.csv

Commands will be functional once the implementation is released.

## Reproduction

`docs/reproduction.md` maps each table and figure of the paper to the script
that produces it.

## License

License terms will be finalized upon acceptance. The planned terms are MIT for
code and CC BY 4.0 for the processed cycle tables.

## Citation

Citation information will be added upon publication.
