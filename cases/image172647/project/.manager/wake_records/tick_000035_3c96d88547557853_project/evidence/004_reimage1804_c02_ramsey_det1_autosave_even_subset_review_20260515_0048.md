# reimage1804_c02 det=1 MHz Ramsey autosave even-subset review (20260515_0048)

## Scope

Bridge-free review of the running claim-grade det-shift Ramsey/T2star/13C job `nv23_ramsey_20260514_230820_auto_ramsey`. No bridge queue mutation was performed.

## Running state

- Bridge state: `running` / `run_experiment_scan_point`
- Message: (7/16) averages completed for 1 scans Autosave is enabled. Once the first average is saved, the in-progress savedexperiment MAT file can be raw-exported with claw_export_savedexperiment_mat_raw to inspect raw readouts before execute completes.
- Final count text: `Final = 44.147 kcps`
- Monitor last_error: ``
- stop_requested: `False`
- Autosave MAT: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-231101.mat`

## Data reviewed

- Stored averages reviewed: 6 (largest even subset) from 7 currently stored averages; planned terminal averages: 16
- Repetitions per average: 50000
- Current shots per point: 300000; planned terminal shots per point: 800000
- Tau grid: 0 to 1e-05 s, 51 points, step 2e-07 s
- Scan order: snake; drift source: Scan.ScanOrderEachAvg; flagged averages: []

## Provisional FFT target bins (readout2 / signal self-baseline)

- Direct 13C Larmor (0.384587 MHz target): 0.46%
- det - 13C (0.615413 MHz target): 0.28%
- det carrier (1.000000 MHz target): 0.41%
- det + 13C (1.384587 MHz target): 1.09%
- Previous det=1.5 MHz ambiguity (1.923000 MHz target): 0.51%

## Interpretation

6 averages (largest even subset) were reviewed from 7 stored averages in the running det=1.0 MHz Ramsey job. This is a provisional even snake-order subset; the bridge remains running with message '(7/16) averages completed for 1 scans Autosave is enabled. Once the first average is saved, the in-progress savedexperiment MAT file can be raw-exported with claw_export_savedexperiment_mat_raw to inspect raw readouts before execute completes.', final count text 'Final = 44.147 kcps', monitor last_error '', and stop_requested=False. Combined readout2/self-baseline FFT target-bin amplitudes are direct 13C 0.46%, det-13C 0.28%, carrier 0.41%, det+13C 1.09%, and previous 1.9 MHz ambiguity 0.51%. At only 300000 shots/point versus the planned 800000, this is not claim-grade; use it as progress/provenance and wait for terminal 16-average data unless a hard anomaly appears.

No T2star or 13C claim is made from this running autosave. Continue waiting for terminal/anomaly evidence.

## Artifacts

- Raw export: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_ramsey_det1_autosave_raw_even_subset_20260515_0048.json`
- Summary JSON: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_ramsey_det1_autosave_summary_even_subset_20260515_0048.json`
- Drift JSON: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_ramsey_det1_autosave_drift_even_subset_20260515_0048.json`
- Figure: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/figures/reimage1804_c02_ramsey_det1_autosave_even_subset_20260515_0048.png`
- Status before/after: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/bridge_results/reimage1804_c02_ramsey_det1_running_status_before_autosave_review_20260515_0048.json`, `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/bridge_results/reimage1804_c02_ramsey_det1_running_status_after_autosave_review_20260515_0048.json`
