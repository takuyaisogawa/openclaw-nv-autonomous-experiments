# reimage1804_c02 Ramsey 6-average autosave provisional review

Created: 2026-05-14T21:23 EDT

Bridge job `nv23_ramsey_20260514_201034_auto_ramsey` is still running. The copied status snapshot at 21:23 EDT showed phase `run_experiment_average_start`, 6/8 averages completed, final count text `Final = 44.135 kcps`, monitor active, no monitor error, and no stop request. No bridge queue mutation was performed.

I raw-exported the in-progress savedexperiment and reviewed the 6-average autosave:

- Raw export: `work/artifacts/analysis/reimage1804_c02_ramsey_autosave_raw_6avg_20260514_2123.json`
- Summary: `work/artifacts/analysis/reimage1804_c02_ramsey_autosave_6avg_summary_20260514_2123.json`
- Figure: `work/artifacts/figures/reimage1804_c02_ramsey_autosave_6avg_20260514_2123.png`
- Drift diagnostic: `work/artifacts/analysis/reimage1804_c02_ramsey_autosave_6avg_drift_20260514_2123.json`
- Status snapshot: `work/artifacts/bridge_results/reimage1804_c02_ramsey_t2star_scout_running_status_6avg_20260514_2123.json`

## Review

The autosave has 6 stored averages out of the planned 8. The scan still matches the intended `ramsey.xml` tau scan: 0..8 us, 43 points, 50,000 repetitions per average, `det=1.5 MHz`, snake scan order. Readout roles remain readout 1 as the mS=0 reference and readout 2 as the Ramsey signal (`full_experiment=0`).

This is now an even snake-order subset, so it is more balanced than the 3-average snapshot, but it is still not terminal. Combined readout2/self-baseline FFT target-bin amplitudes are:

- carrier near det=1.5 MHz: about 0.74%
- det - 13C sideband target: about 1.71%
- det + 13C sideband target: about 1.25%
- direct 13C Larmor bin near 384 kHz: about 0.97%

The det-13C sideband bin is stronger than in the 3-average snapshot, but the deliberate carrier remains weak and target-bin support varies across stored averages. This is not sufficient for a T2star or 13C claim.

## Drift diagnostic

The scan-order-aware drift diagnostic used `Scan.ScanOrderEachAvg` with snake mode for 6 averages and found no flagged average indices. Treat this as advisory provenance only.

## Decision

No T2star or 13C conclusion is made from the 6-average running autosave. Continue waiting for the terminal 8-average savedexperiment unless a hard anomaly appears.
