# reimage1804_c02 CPMG N=8 one-average autosave sanity review (2026-05-15 07:40 EDT)

This was bridge-free only. The bridge job `nv23_cpmg_20260515_072306_auto_cpmg` remained running during review; no queue mutation was performed.

## Data/source

- Autosave MAT: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-CPMG-vary-tau-2026-05-15-072537.mat`.
- Raw export verified `CPMG.xml`, tau 0.450..1.600 us, 37 points, one saved average x 50000 reps, snake scan order, and `do_adiabatic_inversion=0`.
- Status copy after review: state `running`, phase `run_experiment_scan_point`, `Final = 44.318 kcps`, monitor active with no last_error, stop_requested=false.
- Drift diagnostic is limited with one average; it reported no flagged averages and used a single-average common-mode method.

## Readout-role check

The raw export has three readouts. This matches the pre-launch `CPMG.xml` review: readout1 is the true-0 reference, readout2 is the pi/ms=1 reference, and readout3 is the final CPMG echo candidate signal. This should be re-verified from terminal metadata before final interpretation.

## Provisional target-tau view

Planned 13C target tau values are 0.650 us (`1/(4 f13)`) and 1.300 us (alternate interpulse convention). Nearest grid points are 0.642 us and 1.312 us.

For readout3 / linear self-baseline:

- near 0.650 us: relative 0.9995, local z 0.83;
- near 1.300 us: relative 0.9839, local z -0.82.

This one-average snapshot does **not** show an obvious target-tau dip in the final echo signal. It is only 50k shots/point and is not a rejection of the 13C branch.

Reference caveat: readout2 has a high point near the 1.300 us target (relative 1.1314, local z 4.02), so terminal review must compare raw readouts and fitted-reference/self-baseline views before using normalization.

## Next action

Continue the running job unless terminal or hard-anomaly evidence appears. Review a later even-average autosave or terminal result before any 13C conclusion.

Artifacts: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_summary_1avg_20260515_0740.json`, `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/figures/reimage1804_c02_cpmg_n8_autosave_1avg_20260515_0740.png`, `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_raw_1avg_20260515_0740.json`, `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_cpmg_n8_autosave_drift_1avg_20260515_0740.json`.
