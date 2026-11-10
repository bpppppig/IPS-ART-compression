# Figures

Reference figures produced from the full dataset (105 VitalDB ABP records,
1,518,283 accepted cycles). They are provided so that readers can compare their
own runs against the reported results; the raw waveforms are not redistributed.

## `paper/` — final figures used in the manuscript

| File | Shows | Analysis script |
|---|---|---|
| `fig1_selection.pdf` | Selection criterion on one cycle: four landmark-delimited regions, the five clinical anchors, and the maximum-vertical-deviation points on the upstroke and the peak-to-notch segment. | `merge_figs.py` |
| `fig2_anchoring.pdf` | Anchor-constrained vs anchor-free reconstruction of the same cycle at `K = 8`, with the notch-depth error annotated. | `panel_alpha_d.py` |
| `fig3_block_size.pdf` | Effect of block size `B` on encoded rate (compact and split layouts) and on point-query latency. | `plot_storage.py` |
| `fig4_rate_distortion.pdf` | Rate–distortion curves (MSE and systolic-peak error) and the learned-autoencoder comparison. | `plot_rd_final.py` |

## `supplementary/` — additional analysis plots

| File | Shows | Analysis script |
|---|---|---|
| `residual_rate_distortion.png` | Rate–distortion with *measured* bit rates: MSE, Pearson `r`, and pulse-pressure error against bits per point after 12-bit quantization and zlib. | `bitrate_eval.py` |
| `method_comparison.png` | All compared methods against the number of stored values per cycle. | `baseline_rd.py` |
| `anchor_ablation_k8.png` | Ablation at `K = 8`: anchor-free vs anchor-constrained selection (rate–fidelity, peak/pulse-pressure error, shape fidelity). | `sweep_fidelity.py` |
| `bendpoint_distribution.png` | Per-record shoulder-point ratio vs above-chord ratio for non-anchor bend points. | `plot_bendpoint_dist.py` |

## Notes

- The figures are the ABP version used in the submission; axis labels read
  `ABP (mmHg)`.
- Data inputs for the plots are the result CSVs produced by the scripts above
  (for example `block_sweep.csv` for Fig. 3). Those CSVs are not shipped here.
- Figure-generation scripts belong to the research code base and are listed in
  `docs/reproduction.md`; they will be included with the implementation at
  release.
- Figures are released under CC BY 4.0, consistent with the processed cycle
  tables.
