# reimage1804_c02 CPMG N=8 six-average autosave review

Date: 2026-05-15 08:30 EDT
Job: `nv23_cpmg_20260515_072306_auto_cpmg`

## Scope

Bridge-free running-autosave sanity check only. No queue mutation, stop request, or terminal marking was performed.

## Bridge state

- Status snapshot before review: running with 6/12 completed averages, `Final = 44.086 kcps`, monitor active, `last_error` empty, `stop_requested=false`.
- Status snapshot after review: still running with 6/12 completed averages, monitor active, `last_error` empty, `stop_requested=false`.
- Direct queue check after review: queued=0, staging=0, running=1 (`nv23_cpmg_20260515_072306_auto_cpmg`).

## Data verified

- Raw-exported autosave MAT: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-CPMG-vary-tau-2026-05-15-072537.mat`.
- Saved data contained 6 stored averages x 50000 repetitions, `CPMG.xml`, tau 0.45..1.60 us, 37 points, snake scan order.
- Six averages are an even snake-order-balanced subset: 300k current shots/point of the planned 600k shots/point.
- `do_adiabatic_inversion=0`.
- Readout role expectation remains: readout1 true-0 reference, readout2 pi/ms1 reference, readout3 final CPMG echo candidate signal. Terminal review must still verify saved metadata.
- Scan-order-aware drift diagnostic over all 6 saved averages used `Scan.ScanOrderEachAvg` / snake mode and found no flagged averages.

## Provisional readout3 target check

Expected target taus from f13 ~= 384.6 kHz:

- 1/(4 f13) target: 0.650 us; nearest sampled tau 0.642 us.
- 1/(2 f13) target: 1.300 us; nearest sampled tau 1.312 us.

Six-average combined readout3 final-echo / linear self-baseline:

- nearest 0.650 us target: 0.9850, local z about +0.39.
- nearest 1.300 us target: 0.9947, local z about -0.44.

These are near baseline and do not show a robust target-tau dip. This remains a nonterminal subset, not evidence for or against 13C.

## Interpretation

The later even subset is cleaner than the earlier one- and two-average snapshots: autosave is readable, bridge is healthy, no drift flag appeared, and neither expected CPMG target convention shows a clear readout3/final-echo feature. Because only half of the planned shots are represented and the bridge job is still running, this downgrades obvious early-feature support but does not yet close the 13C branch. Continue to terminal data unless a hard anomaly appears.

## Artifacts

- Summary JSON: `work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_summary_6avg_20260515_0830.json`
- Raw export JSON: `work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_raw_6avg_20260515_0830.json`
- Drift JSON: `work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_drift_6avg_20260515_0830.json`
- Figure: `work/artifacts/figures/reimage1804_c02_cpmg_n8_autosave_6avg_20260515_0830.png`
- Status snapshots: `work/artifacts/bridge_results/reimage1804_c02_cpmg_n8_status_before_6avg_autosave_review_20260515_0830.json`, `work/artifacts/bridge_results/reimage1804_c02_cpmg_n8_status_after_6avg_autosave_review_20260515_0830.json`
