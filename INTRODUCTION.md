# Introduction

Continuous physiological monitoring produces high-resolution waveforms whose
volume grows with both sampling rate and monitoring duration. Invasive arterial
pressure is a representative case: the signal is recorded at several hundred
samples per second for the entire duration of surgery, and downstream use
involves two different access patterns. Clinical summaries such as systolic and
diastolic pressure, pulse pressure, and hypotension episodes are computed over
long stretches, whereas waveform inspection and model training require the
samples themselves.

IPS addresses both patterns with one representation. The design rests on three
contributions.

1. **Structure.** Cycles are delimited by diastolic troughs and described by five
   clinical anchors. Three of them (the two boundary troughs and the systolic
   peak) are always retained; the dicrotic notch and the post-notch diastolic
   peak are retained when detected. Anchors are therefore reproduced exactly
   before quantization, independently of the point budget.

2. **Control.** The remaining points are allocated by recursive
   maximum-deviation splitting, driven either by a point budget `K` or by a
   vertical-deviation threshold `alpha`. A tolerance `epsilon` can be inverted
   into a minimum budget, subject to the quantization limit of the storage
   format.

3. **Access.** The five anchors are also stored in a small uncompressed plane,
   so landmark-derived quantities can be answered without decompressing the
   waveform, while independently decodable per-cycle blocks support local
   reconstruction.

The evaluation in the paper reports rate, reconstruction error, landmark
fidelity, and access cost on 105 public ART records (1,518,283 cycles), and
compares IPS with keypoint-based, symbolic, sampling-based, learned, and
error-bounded compressors.

This repository will contain the reference implementation of the encoder,
decoder, and query path, together with the scripts that reproduce the reported
measurements.
