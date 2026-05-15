# reimage1804_c02 CPMG N=8 two-average autosave review

Date: 2026-05-15 07:52-08:00 EDT
Job: `nv23_cpmg_20260515_072306_auto_cpmg`

## Scope

Bridge-free running-autosave sanity check only. No queue mutation, stop request, or terminal marking was performed.

## Bridge state

- Status snapshot before review: running at 2/12 completed averages, `Final = 43.000 kcps`, monitor active, `last_error` empty, `stop_requested=false`.
- Status snapshot after review: still running at 2/12 completed averages, monitor active, `last_error` empty, `stop_requested=false`.
- Queued/staging were not touched.

## Data verified

- Raw-exported autosave MAT: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-CPMG-vary-tau-2026-05-15-072537.mat`.
- Saved data now contain 2 averages x 50000 repetitions, `CPMG.xml`, tau 0.45..1.60 us, 37 points, snake scan order.
- `do_adiabatic_inversion=0`.
- Readout role expectation remains: readout1 true-0 reference, readout2 pi/ms=1 reference, readout3 final CPMG echo candidate signal. Terminal review must still verify saved metadata.
- Scan-order-aware drift diagnostic used `Scan.ScanOrderEachAvg` / snake mode and found no flagged averages.

## Provisional readout3 target check

Expected target taus from f13 ~= 384.6 kHz:

- 1/(4 f13) target: 0.650 us; nearest sampled tau 0.642 us.
- 1/(2 f13) target: 1.300 us; nearest sampled tau 1.312 us.

Combined readout3 final-echo / linear self-baseline:

- nearest 0.650 us target: 1.0197, local z about +1.96.
- nearest 1.300 us target: 0.9822, local z about +0.20 versus its local neighbors.

The two stored averages disagree locally enough that this is not evidence for or against a 13C feature. The 2-average subset is only 100k shots/point of the planned 600k shots/point.

## Interpretation

This is a nonterminal sanity check. It confirms the autosave is readable, readout3 can be tracked in the planned target windows, and no hard anomaly is apparent. It does not support a 13C claim or a rejection. Continue waiting for later even-subset or terminal evidence unless a hard anomaly appears.

## Artifacts

- Summary JSON: `work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_summary_2avg_20260515_0752.json`
- Raw export JSON: `work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_raw_2avg_20260515_0752.json`
- Drift JSON: `work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_drift_2avg_20260515_0752.json`
- Figure: `work/artifacts/figures/reimage1804_c02_cpmg_n8_autosave_2avg_20260515_0752.png`
- Status snapshots: `work/artifacts/bridge_results/reimage1804_c02_cpmg_n8_status_before_2avg_autosave_review_20260515_0752.json`, `work/artifacts/bridge_results/reimage1804_c02_cpmg_n8_status_after_2avg_autosave_review_20260515_0800.json`
