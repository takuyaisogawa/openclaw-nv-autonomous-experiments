# reimage1804_c02 terminal pODMR review: accept aligned branch with caveat

Created: 2026-05-14T19:59:15-04:00

Bridge job: `nv23_pulsed_odmr_rabimodulated_v1_20260514_191847_reimage1804_c02_strong_podmr`
Savedexperiment: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-Rabimodulated-vary-mw_freq-2026-05-14-192106.mat`

## Terminal status

- Bridge execute completed successfully at 2026-05-14T19:55:57.
- Raw export contains 4 averages x 50000 repetitions.
- In-run alignment was healthy (`align_final_counts_kcps = 44.294` in the bridge result).

## Readout roles

`Rabimodulated.xml` with `full_expt=0`: readout 1 is the mS=0 reference; readout 2 is the signal after `length_rabi_pulse`.

## Terminal observation

The 4-average mean shows a clear signal-only depression near the expected ms=+1 resonance:

- raw signal minimum: 3.875000 GHz, 41.462 kcps
- linear off-resonant signal baseline at that point: 48.119 kcps
- raw signal depression: 13.8%
- fitted-reference ratio depression: 14.0%
- pointwise signal/reference depression: 13.4%
- reference depression at the signal minimum: ~0.0% (reference is not depressed)
- empirical Gaussian-dip fit center: 3.876461 GHz, covariance uncertainty ~0.69 MHz
- Gaussian fit FWHM: ~11.2 MHz
- dip-to-off-resonant residual RMS: ~5.6

The depth is lower than the expected ~22% strong-pi contrast, but it is much stronger and more coherent than the rejected c01 terminal pODMR (~4-5%). Average-level checks are mixed but not single-point-only: avg 1 is strong at 3.875 GHz, avg 2 is weak/noisy, avg 3 has a nearby dip at 3.878 GHz, and avg 4 is clear near 3.875-3.878 GHz.

## Decision

Accept `reimage1804_c02` as the magnetic-field-aligned NV for this project branch, with a lower-than-expected-contrast caveat. This is a usable resonance for targeted T2star/Ramsey follow-up. Use the fit center or a weak-pi-refined center if a later advisory/planning check says the strong-pi center uncertainty is too broad for the next measurement.

Do not claim T2star or 13C yet.

## Artifacts

- Raw export: `work/artifacts/analysis/reimage1804_c02_podmr_terminal_raw_4avg_20260514_1957.json`
- Summary: `work/artifacts/analysis/reimage1804_c02_podmr_terminal_summary_4avg_20260514_1957.json`
- Figure: `work/artifacts/figures/reimage1804_c02_podmr_terminal_4avg_20260514_1957.png`
- Bridge result: `work/artifacts/bridge_results/reimage1804_c02_strong_podmr_done_result_20260514_1956.json`
