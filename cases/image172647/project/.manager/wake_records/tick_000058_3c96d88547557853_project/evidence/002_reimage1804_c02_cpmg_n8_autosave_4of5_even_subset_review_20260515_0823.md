# reimage1804_c02 CPMG N=8 four-of-five even-subset autosave review

Date: 2026-05-15 08:23-08:26 EDT
Job: `nv23_cpmg_20260515_072306_auto_cpmg`

## Scope

Bridge-free running-autosave sanity check only. No queue mutation, stop request, or terminal marking was performed.

## Bridge state

- Status snapshot before review: running with 5/12 completed averages, `Final = 44.086 kcps`, monitor active, `last_error` empty, `stop_requested=false`.
- Status snapshot after review: still running with 5/12 completed averages, monitor active, `last_error` empty, `stop_requested=false`.
- Direct queue check after review: queued=0, staging=0, running=1 (`nv23_cpmg_20260515_072306_auto_cpmg`).

## Data verified

- Raw-exported autosave MAT: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-CPMG-vary-tau-2026-05-15-072537.mat`.
- Saved data contained 5 stored averages x 50000 repetitions, `CPMG.xml`, tau 0.45..1.60 us, 37 points, snake scan order.
- To keep snake-order balance, the analysis used the first 4 averages only: 200k current shots/point of the planned 600k shots/point.
- `do_adiabatic_inversion=0`.
- Readout role expectation remains: readout1 true-0 reference, readout2 pi/ms1 reference, readout3 final CPMG echo candidate signal. Terminal review must still verify saved metadata.
- Scan-order-aware drift diagnostic over all 5 saved averages used `Scan.ScanOrderEachAvg` / snake mode and found no flagged averages.

## Provisional readout3 target check

Expected target taus from f13 ~= 384.6 kHz:

- 1/(4 f13) target: 0.650 us; nearest sampled tau 0.642 us.
- 1/(2 f13) target: 1.300 us; nearest sampled tau 1.312 us.

First-4-average combined readout3 final-echo / linear self-baseline:

- nearest 0.650 us target: 0.9908, local z about +0.54.
- nearest 1.300 us target: 0.9971, local z about -0.53.

These are near baseline and do not show a robust target-tau dip. Per-average behavior remains mixed; this is still a nonterminal subset, not evidence for or against 13C.

## Interpretation

This review confirms that the later autosave remains readable, the bridge remains healthy, no average-drift flag appeared, and the balanced first-4-average subset does not show an obvious target-tau CPMG feature. Because only 200k of the planned 600k shots/point are represented and the job is still running, do not promote this to a 13C conclusion or rejection. Continue to terminal data unless a hard anomaly appears.

## Artifacts

- Summary JSON: `work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_summary_4of5_even_subset_20260515_0823.json`
- Raw export JSON: `work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_raw_4of5_20260515_0823.json`
- Drift JSON: `work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_drift_4of5_20260515_0823.json`
- Figure: `work/artifacts/figures/reimage1804_c02_cpmg_n8_autosave_4of5_even_subset_20260515_0823.png`
- Status snapshots: `work/artifacts/bridge_results/reimage1804_c02_cpmg_n8_status_before_4of5_autosave_review_20260515_0823.json`, `work/artifacts/bridge_results/reimage1804_c02_cpmg_n8_status_after_4of5_autosave_review_20260515_0823.json`
