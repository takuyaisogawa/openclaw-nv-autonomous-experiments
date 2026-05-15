# Shifted-sideband reanalysis and revised closeout - 2026-05-14 13:20 EDT

## Question
Process the new advice inbox request: reanalyze the final refreshed-center Ramsey with a carrier shift from residual resonance-frequency calibration error and possible 13C sidebands around that shifted carrier. Do not run additional measurements and do not reject solely from stored-average disagreement.

## Inputs read
- `NV_RESEARCH_MEMORY.md` startup rules and relevant `NV_RESEARCH_KNOWLEDGE.md` sections: Experiment Defaults, Shot Budget And Data Quality, and Research Practice And Closeout.
- Project `brief.md`, `human_advice.md`, `work/state.md`, and current project status.
- Advice inbox message `advice/inbox/2026-05-14_resume_bridge_free_shifted_sideband_report.md`.
- Terminal refreshed-center Ramsey review/model-comparison JSON, raw export, drift result, and figures.
- Shared bridge queue status from cron/status and direct directory check: no queued/running bridge job; no bridge mutation was needed or performed.

## Action taken
- Ran bridge-free shifted-sideband reanalysis on the final refreshed-center Ramsey raw export.
- Tested the hypothesis that residual resonance-frequency calibration shifts the effective Ramsey carrier from the programmed det=1.5 MHz to about det + f13C = 1.884807 MHz, giving a 13C triplet at 1.500000, 1.884807, and 2.269613 MHz.
- Compared shifted triplet models against the previous fixed-carrier/fixed-sideband and single-frequency alternatives in ratio, fitted-reference-line normalization, raw-signal, and skip-first-4-tau views.
- Ran a targeted stored-average bootstrap for the shifted triplet. Stored-average disagreement was used as uncertainty/provenance, not as a sole rejection criterion.
- Rewrote the closeout report to reflect the changed 13C interpretation.
- Updated `NV_RESEARCH_KNOWLEDGE.md` with the reusable shifted-sideband Ramsey lesson.

## Result
- Companion reanalysis JSON: `work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_shifted_sideband_reanalysis_20260514_1308.json`.
- Companion reanalysis figure: `work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_shifted_sideband_reanalysis_20260514_1308.png`.
- Targeted bootstrap JSON: `work/artifacts/analysis/image145844_reimage_r03_shifted_triplet_targeted_bootstrap_20260514_1312.json`.
- Targeted bootstrap figure: `work/artifacts/figures/image145844_reimage_r03_shifted_triplet_targeted_bootstrap_20260514_1312.png`.
- Revised closeout report PDF: `work/artifacts/reports/20260514_1320_r03_shifted_sideband_recloseout/image145844_reimage_r03_shifted_sideband_recloseout_report_20260514_1320.pdf`.
- Revised TeX source: `work/artifacts/reports/20260514_1320_r03_shifted_sideband_recloseout/image145844_reimage_r03_shifted_sideband_recloseout_report_20260514_1320.tex`.

The shifted-sideband check changes the scoped 13C interpretation. The previous negative/unsupported nearby-13C wording is too strong. The final Ramsey supports plausible nearby-13C candidate evidence conditional on a residual carrier shift of about +0.39 MHz: the expected triplet at 1.500000/1.884807/2.269613 MHz is favored over single-frequency alternatives across robust views.

T2star remains conditional rather than an unconditional claim-grade numeric result. The shifted-triplet common-envelope fits imply an order-3-us decay scale: full ratio about 4.59 us, full signal/reference-line about 3.01 us, skip-first-4-tau about 3.51 us and 2.69 us, with bootstrap medians about 4.60 us and 2.95 us for ratio and signal/reference-line views.

## Checks actually performed
- Axis contract verified: averaging `ExperimentDataEachAvg` over stored averages reproduces `ExperimentData` for both readouts.
- Bridge-free only: no bridge job was enqueued, stopped, or mutated.
- LaTeX build wrapper completed with returncode 0, no log warnings, PDF exists, and `%PDF-1.5` header verified.
- Targeted bootstrap: 140 stored-average resamples; a shifted triplet beat a single-frequency model in 97.9% of ratio resamples and 100% of fitted-reference-line resamples.

## Remaining uncertainty
- The shifted-sideband interpretation is a model revision of one Ramsey branch, not an independently confirmed coupling experiment.
- The numeric T2star value should not be quoted unconditionally; it is conditional on the shifted-triplet model and its common-envelope assumption.
- Confirmation would require a new explicit protocol-development/confirmation branch if operator wants it. The current advice explicitly said not to run additional measurements.

## Next pointer
Record the revised report/evidence, dispose the advice inbox as processed, update project state to line-complete/completed with the revised conclusion, and do not submit further bridge work unless operator explicitly requests a new confirmation branch.
