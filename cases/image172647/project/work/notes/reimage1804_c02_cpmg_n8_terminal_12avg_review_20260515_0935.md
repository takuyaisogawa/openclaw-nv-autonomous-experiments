# reimage1804_c02 CPMG N=8 terminal 12-average review (2026-05-15 09:35 EDT)

## Bridge/result status

Bridge job `nv23_cpmg_20260515_072306_auto_cpmg` completed cleanly at 2026-05-15 09:32:49 EDT. Copied terminal result/status snapshots:

- `work/artifacts/bridge_results/reimage1804_c02_cpmg_n8_terminal_result_20260515_0935.json`
- `work/artifacts/bridge_results/reimage1804_c02_cpmg_n8_terminal_status_20260515_0935.json`

Terminal result verified healthy counts and saved data:

- pre-run TrackCenter final: 38.694 kcps
- post-run final: 44.535 kcps
- savedexperiment: `1DExp-seq-CPMG-vary-tau-2026-05-15-072537.mat`
- sequence: `CPMG.xml`
- scan: `tau = 0.45..1.60 us`, 37 points, snake order
- acquisition: 12 averages x 50000 reps = 600k shots/point
- `do_adiabatic_inversion = 0`

Artifacts:

- raw export: `work/artifacts/analysis/reimage1804_c02_cpmg_n8_terminal_raw_12avg_20260515_0935.json`
- terminal summary: `work/artifacts/analysis/reimage1804_c02_cpmg_n8_terminal_summary_12avg_20260515_0935.json`
- drift diagnostic: `work/artifacts/analysis/reimage1804_c02_cpmg_n8_terminal_drift_12avg_20260515_0935.json`
- terminal figure: `work/artifacts/figures/reimage1804_c02_cpmg_n8_terminal_12avg_20260515_0935.png`
- target-region review: `work/artifacts/analysis/reimage1804_c02_cpmg_n8_terminal_target_region_review_20260515_0945.json`
- target-region figure: `work/artifacts/figures/reimage1804_c02_cpmg_n8_terminal_target_region_20260515_0945.png`

The scan-order-aware drift diagnostic used `Scan.ScanOrderEachAvg` / snake order and found no flagged averages.

## Target-region interpretation

The prelaunch model gave expected 13C Larmor `f13 ~= 384.6 kHz`, so `1/(4 f13) ~= 0.6500 us`. The model also estimated the first-target CPMG filter-width scale as about `tau/N ~= 81 ns`, so the correct terminal check is the target region, not only the single nearest grid point.

Terminal readout3/final-echo evidence:

- nearest point to 0.6500 us: tau 0.6417 us, readout3/self = 0.9871
- target-region minimum: tau 0.6736 us, offset +23.6 ns from the model target, readout3/self = 0.9528
- reference-normalized diagnostics at 0.6736 us also show the feature: readout3/readout1-baseline = 0.9518 and readout3/readout2-baseline = 0.9568
- the same point stays below baseline in the even-subset trend after 6, 8, 10, and 12 averages
- the alternate `1/(2 f13) ~= 1.300 us` convention has only weak/percent-scale support, not a comparable feature

This is not a normalization-only feature and is inside the modeled CPMG target region. It therefore strengthens the weak det-shift Ramsey 13C candidate rather than downgrading it.

## Project-level conclusion

- Aligned NV branch: `reimage1804_c02` remains the accepted magnetic-field-aligned NV branch from terminal strong-pi pODMR, with lower-than-expected contrast caveat.
- T2star: the det=1.5, det=1.0, and det=1.25 Ramsey data support a short/few-us T2star order. A precise scalar remains method-sensitive; the supported conclusion is approximately 2-3 us rather than a claim-grade single number.
- 13C: the Ramsey-only evidence was weak, but terminal CPMG now corroborates it with a target-region readout3/final-echo dip near the `1/(4 f13)` convention. Supported conclusion: `reimage1804_c02` likely has a weak/moderate nearby-13C-like coupling signature. The current data do not support a precise coupling extraction or strong publication-grade claim.

No further bridge experiment is required for the original project objective unless Takuya wants a stronger follow-up such as a fine CPMG scan around 0.60-0.72 us or a phase-readout XY8/DDRF-style discriminator.
