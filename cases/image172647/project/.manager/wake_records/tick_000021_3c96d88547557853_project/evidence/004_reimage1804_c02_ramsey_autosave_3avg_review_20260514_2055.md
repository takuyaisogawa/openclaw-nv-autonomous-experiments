# reimage1804_c02 Ramsey 3-average autosave provisional review

Created: 2026-05-14T20:57 EDT

Bridge job `nv23_ramsey_20260514_201034_auto_ramsey` is still running. The status snapshot copied at 20:54 EDT showed phase `run_experiment_scan_point`, 3/8 averages completed, final count text `Final = 43.380 kcps`, monitor active, no monitor error, and `stop_requested=false`. No bridge queue mutation was performed.

I raw-exported the in-progress savedexperiment:

- Raw export: `work/artifacts/analysis/reimage1804_c02_ramsey_autosave_raw_3avg_20260514_2055.json`
- Summary: `work/artifacts/analysis/reimage1804_c02_ramsey_autosave_3avg_summary_20260514_2055.json`
- Figure: `work/artifacts/figures/reimage1804_c02_ramsey_autosave_3avg_20260514_2055.png`
- Status snapshot: `work/artifacts/bridge_results/reimage1804_c02_ramsey_t2star_scout_running_status_3avg_20260514_2055.json`

## Review

The autosave has 3 stored averages out of the planned 8. The scan is still the intended `ramsey.xml` tau scan: 0..8 us, 43 points, 50,000 repetitions per average, `det=1.5 MHz`, snake scan order. Readout roles remain readout 1 as the mS=0 reference and readout 2 as the Ramsey signal (`full_experiment=0`).

The combined raw and fitted-baseline-normalized views still show visible structure, but this is an odd intermediate snake-order subset (forward, reverse, forward), not a balanced terminal acquisition. The combined signal-self-baseline FFT target-bin amplitudes are weak/inconsistent:

- carrier near det=1.5 MHz: about 0.46%
- det - 13C sideband target: about 1.24%
- det + 13C sideband target: about 1.71%
- direct 13C Larmor bin near 384 kHz: about 1.57%

Average-to-average target-bin support is not stable enough for a 13C claim. The low carrier bin also argues against fitting T2star from this running snapshot.

## Decision

No T2star or 13C conclusion is made from the 3-average autosave. Treat it as provenance only. Continue waiting for the terminal 8-average savedexperiment unless a hard anomaly appears.

## Drift diagnostic

Scan-order-aware drift diagnostic artifact: `work/artifacts/analysis/reimage1804_c02_ramsey_autosave_3avg_drift_20260514_2059.json`. It used `Scan.ScanOrderEachAvg`, mode `snake`, 3 averages, and found no flagged average indices. Treat this as advisory provenance only; the job is still running.
