# Reproduction map

Status: **pending release**. Each entry names the script that will produce the
corresponding item once the implementation is published.

| Paper item | Script | Status |
|---|---|---|
| Table III (method comparison) | `scripts/run_rate_distortion.py` | pending |
| Table IV (ablation) | `scripts/run_ablation.py` | pending |
| Fig. 1 (selection criterion, anchors) | `merge_figs.py` | figure shipped |
| Fig. 2 (anchoring effect) | `panel_alpha_d.py` | figure shipped |
| Fig. 3 (block size, latency) | `scripts/run_block_sweep.py`, `plot_storage.py` | figure shipped |
| Fig. 4 (rate-distortion, landmark error) | `scripts/run_rate_distortion.py`, `plot_rd_final.py` | figure shipped |
| Supplementary: measured-rate RD | `bitrate_eval.py` | figure shipped |
| Supplementary: method comparison | `baseline_rd.py` | figure shipped |
| Supplementary: anchor ablation (K=8) | `sweep_fidelity.py` | figure shipped |
| Supplementary: bend-point distribution | `plot_bendpoint_dist.py` | figure shipped |
| Rate accounting (bpp, CR) | `scripts/run_bit_accounting.py` | pending |

Figure files and their descriptions are listed in `figures/README.md`.
