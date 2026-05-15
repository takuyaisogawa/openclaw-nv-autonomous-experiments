# reimage1804_c02 CPMG N=8 eight-average autosave review

Date: 2026-05-15 08:56 EDT
Job: `nv23_cpmg_20260515_072306_auto_cpmg`

## Scope

Bridge-free running-autosave sanity check only. No queue mutation, stop request, or terminal marking was performed.

## Bridge state

- Status snapshot before review: running with 8/12 completed averages, `Final = 38.216 kcps`, monitor active, `last_error` empty, `stop_requested=false`.
- Status snapshot after review / queue check: still running with 8/12 completed averages, queued=0, staging=0, monitor active, `last_error` empty, `stop_requested=false`.
- Counts are lower than the previous six-average snapshot but still well above the 8 kcps minimum-final-count gate and no hard anomaly was present.

## Data verified

- Raw-exported autosave MAT: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-CPMG-vary-tau-2026-05-15-072537.mat`.
- Saved data contained 8 stored averages x 50000 repetitions, `CPMG.xml`, tau 0.45..1.60 us, 37 points, snake scan order.
- Eight averages are an even snake-order-balanced subset: 400k current shots/point of the planned 600k shots/point.
- `do_adiabatic_inversion=0`.
- Readout role expectation remains: readout1 true-0 reference, readout2 pi/ms1 reference, readout3 final CPMG echo candidate signal. Terminal review must still verify saved metadata.
- Scan-order-aware drift diagnostic over all 8 saved averages used `Scan.ScanOrderEachAvg` / snake mode and found no flagged averages.

## Provisional readout3 target check

Expected target taus from f13 ~= 384.6 kHz:

- 1/(4 f13) target: 0.650 us; nearest sampled tau 0.642 us.
- 1/(2 f13) target: 1.300 us; nearest sampled tau 1.312 us.

Eight-average combined readout3 final-echo / linear self-baseline:

- nearest 0.650 us target: 0.9983, local z about +1.00.
- nearest 1.300 us target: 0.9978, local z about +0.01.

These are effectively baseline at both target conventions and do not show a robust target-tau dip. This remains a nonterminal subset, not terminal evidence for or against 13C.

## Interpretation

The eight-average subset now represents two-thirds of the planned shot budget and remains near baseline at both target tau conventions. This further weakens the expectation of a large CPMG-visible 13C dip in this run, but the correct decision is still to wait for terminal 12-average data unless a hard anomaly appears. Terminal review should compare raw readouts, readout3 self-baseline, reference-normalized views, local target neighborhoods, and off-target/reference behavior before any 13C conclusion.

## Artifacts

- Summary JSON: `work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_summary_8avg_20260515_0856.json`
- Raw export JSON: `work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_raw_8avg_20260515_0856.json`
- Drift JSON: `work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_drift_8avg_20260515_0856.json`
- Figure: `work/artifacts/figures/reimage1804_c02_cpmg_n8_autosave_8avg_20260515_0856.png`
- Status snapshots: `work/artifacts/bridge_results/reimage1804_c02_cpmg_n8_status_before_8avg_autosave_review_20260515_0856.json`, `work/artifacts/bridge_results/reimage1804_c02_cpmg_n8_status_after_8avg_autosave_review_20260515_0856.json`
- Queue check: `work/artifacts/bridge_results/reimage1804_c02_cpmg_n8_queue_check_after_8avg_autosave_review_20260515_0856.json`
