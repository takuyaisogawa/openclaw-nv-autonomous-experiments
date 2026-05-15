# reimage1804_c02 det=1.25 MHz Ramsey autosave even-subset review (20260515_0513)

## Scope

Bridge-free review of the running third-det Ramsey/T2star/13C artifact-rejection job `nv23_ramsey_20260515_030822_auto_ramsey`. No bridge queue mutation was performed.

## Running state

- Bridge state: `running` / `run_experiment_scan_point`
- Message: (9/16) averages completed for 1 scans Autosave is enabled. Once the first average is saved, the in-progress savedexperiment MAT file can be raw-exported with claw_export_savedexperiment_mat_raw to inspect raw readouts before execute completes.
- Final count text: `Final = 43.869 kcps`
- Monitor last_error: ``
- stop_requested: `False`
- Autosave MAT: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-15-031116.mat`

## Data reviewed

- Stored averages in autosave: 9; averages used for balanced subset: 8 of planned 16
- Repetitions per average: 50000
- Current shots per point used: 400000; planned terminal shots per point: 800000
- Tau grid: 0 to 1e-05 s, 51 points, step 2e-07 s
- Scan order: snake; drift source: Scan.ScanOrderEachAvg; flagged averages: []

## Provisional FFT target bins (readout2 / signal self-baseline)

- Direct 13C Larmor (0.384587 MHz target): 0.27%
- det - 13C (0.865413 MHz target): 0.99%
- det carrier (1.250000 MHz target): 1.31%
- det + 13C (1.634587 MHz target): 1.22%
- Old det=1 high/static region (1.400000 MHz target): 0.14%
- Static low region (0.700000 MHz target): 0.71%
- Previous det=1.5 high region (1.900000 MHz target): 0.36%

## Interpretation

9 stored averages were raw-exportable from the running det=1.25 MHz Ramsey job; the analysis used a even snake-order subset (using first 8 of 9 stored averages for balance). The bridge remains running with final count text 'Final = 43.869 kcps', monitor last_error '', and stop_requested=False. Combined readout2/self-baseline FFT target-bin amplitudes are direct 13C 0.27%, det-13C 0.99%, carrier 1.31%, det+13C 1.22%, old det=1 high/static region 0.14%, static low region 0.71%, and previous 1.9 MHz region 0.36%. At only 400000 shots/point versus planned 800000, this is not claim-grade; use it as progress/provenance and wait for later even-subset or terminal data unless a hard anomaly appears.

No T2star or 13C claim is made from this running autosave. Continue waiting for terminal/anomaly evidence.

## Artifacts

- Raw export: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_ramsey_det1p25_autosave_raw_even_subset_20260515_0513.json`
- Summary JSON: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_ramsey_det1p25_autosave_summary_even_subset_20260515_0513.json`
- Drift JSON: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_ramsey_det1p25_autosave_drift_even_subset_20260515_0513.json`
- Figure: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/figures/reimage1804_c02_ramsey_det1p25_autosave_even_subset_20260515_0513.png`
- Status before/after: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/bridge_results/reimage1804_c02_ramsey_det1p25_status_before_autosave_review_20260515_0513.json`, `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/bridge_results/reimage1804_c02_ramsey_det1p25_status_after_autosave_review_20260515_0513.json`
