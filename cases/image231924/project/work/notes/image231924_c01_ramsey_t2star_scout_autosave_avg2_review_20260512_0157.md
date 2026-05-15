# c01 Ramsey/T2star scout autosave avg2 review (2026-05-12 01:57 EDT)

## Scope

Bridge-free in-progress review only. The bridge job was still running, so no terminal state, T2star, or 13C conclusion is claimed here.

## Inputs

- Running job: `nv23_image231924_c01_ramsey_t2star_scout_20260512_012010_image231924_c01_ramsey_t2star_scout_20260512_0118_execute`.
- Autosave MAT: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-12-012318.mat`.
- Raw export: `work/artifacts/analysis/image231924_c01_ramsey_t2star_scout_autosave_avg2_raw_export.json`.
- Review JSON: `work/artifacts/analysis/image231924_c01_ramsey_t2star_scout_autosave_avg2_review.json`.
- Review figures:
  - `work/artifacts/figures/image231924_c01_ramsey_t2star_scout_autosave_avg2_review.png`
  - `work/artifacts/figures/image231924_c01_ramsey_t2star_scout_autosave_avg2_raw_readouts.png`

## Bridge status during review

The savedexperiment raw export contained 2 stored averages out of the planned 4. The bridge status read around this review still showed `state=running`, phase `run_experiment_scan_point`, message `(2/4) averages completed for 1 scans`, and no monitor/control error. The job was not stopped, mutated, or marked terminal.

## Observations

- The combined raw reference readout remains usable for a fitted-reference normalization; readout 2 remains visibly structured.
- The combined FFT of linear-detrended fitted-reference-normalized signal still has its strongest non-DC bin at the expected lower-sideband neighborhood: nearest bin `1.593 MHz`.
- The carrier neighborhood nearest bin is `1.961 MHz`, but in this two-average autosave it is not a dominant FFT peak.
- The two stored averages have moderate detrended normalized trace agreement: Pearson correlation about `0.613`.
- The plot was visually checked and is readable; its labeled lower-sideband dominance and in-progress/no-claim annotation are consistent with the JSON review.

## Claim boundary

This strengthens the case that the running experiment contains a useful oscillatory Ramsey candidate and that waiting for terminal data is worthwhile. It still does not support a T2star value or 13C conclusion. Terminal four-average review must repeat raw/readout-aware FFT, per-average support checks, drift diagnostics, and bounded fits before any claim.

## Next step

Wait for terminal result. Then raw-export the final savedexperiment and apply `work/notes/image231924_c01_ramsey_terminal_decision_framework_20260512_0153.md` before any follow-up execute.
