# reimage1804_c02 det=1.25 MHz Ramsey autosave target-bin trend (20260515_0549)

## Scope

Bridge-free trend comparison across running autosave reviews of job `nv23_ramsey_20260515_030822_auto_ramsey`. No bridge queue mutation was performed.

## Target-bin amplitudes (readout2 / signal self-baseline, %)

| averages used | shots/point | direct 13C | det-13C | carrier | det+13C | old det=1 high/static | static low | prev 1.9 MHz |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 100000 | 0.97 | 1.22 | 1.29 | 0.71 | 0.71 | 1.33 | 1.13 |
| 4 | 200000 | 0.21 | 0.96 | 1.10 | 1.04 | 0.52 | 0.84 | 0.89 |
| 6 | 300000 | 0.13 | 1.13 | 1.40 | 1.10 | 0.50 | 0.65 | 0.64 |
| 8 | 400000 | 0.27 | 0.99 | 1.31 | 1.22 | 0.14 | 0.71 | 0.36 |
| 10 | 500000 | 0.58 | 1.08 | 1.36 | 1.17 | 0.21 | 0.56 | 0.20 |

## Provisional interpretation

Reviewed 5 det=1.25 MHz running-autosave snapshots from 2 to 10 balanced averages. The carrier bin stayed about 1.29, 1.10, 1.40, 1.31, 1.36% and det+13C about 0.71, 1.04, 1.10, 1.22, 1.17%, while the previous 1.9 MHz region fell to 1.13, 0.89, 0.64, 0.36, 0.20% and the old det=1 high/static region to 0.71, 0.52, 0.50, 0.14, 0.21%. This favors continued attention to the det=1.25 carrier/high-sideband model over the old static/high-region explanation, but it remains running-autosave provenance only because target amplitudes are about-percent/sub-percent and terminal 16-average data are still required.

This remains nonterminal/provisional. Terminal 16-average raw/readout-aware review is still required before any T2star or 13C conclusion.

## Artifacts

- Trend JSON: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_ramsey_det1p25_autosave_target_trend_20260515_0549.json`
- Trend figure: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/figures/reimage1804_c02_ramsey_det1p25_autosave_target_trend_20260515_0549.png`
