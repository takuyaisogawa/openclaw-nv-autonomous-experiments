# Project State: nv23_aligned_nv_t2star_13c_image231924_20260511_2319

This is the main readable project state. Keep it short, current, and useful.
Keep bridge-execution contracts in `work/bridge_jobs/` or the live bridge queue.
Put detailed derivations, checks, and failed ideas in `work/notes/` so future wakes
can look them up without carrying everything in context.

## Objective

Find a magnetic-field-aligned NV from image231924, then obtain a well-supported T2star and 13C conclusion.

## Vibe Physics Operating Pattern

- Work in small, separately summarized tasks.
- Record what was actually checked; do not write that something is verified unless it was checked.
- When a result matters, include the calculation, bridge artifact, code path, or evidence id that supports it.
- If an assertion is only taste, intuition, or a candidate interpretation, label it that way.
- Repeat verification after fixes; finding one issue is not proof that the rest is clean.

## Standing Operational Assumptions

- Read `<OPENCLAW_WORKSPACE>/NV_RESEARCH_MEMORY.md` before choosing NV project steps.
- Use its Memory Index to read relevant sections from `<OPENCLAW_WORKSPACE>/NV_RESEARCH_KNOWLEDGE.md` only when useful.
- If NV tracking remains continuous and counts/alignment evidence stay healthy, absolute position motion by itself is provenance, not a reason to stop.
- Pause or re-check when tracking is lost, counts collapse, a discontinuous jump or branch switch lacks continuous tracking provenance, hardware safety is uncertain, or a project-specific human constraint explicitly requires a fixed landmark/position.

## Current Status

- Project objective is satisfied for `image231924_c01`. No further bridge work is needed by default.
- Source image `3DXYZ-Image-2026-05-11-231924.mat` was exported with the explicit `ImageData_YXZ` axis contract. Candidate list: `work/artifacts/analysis/image231924_candidate_list.json`; first candidate was `image231924_c01` at image seed `[113.000, 113.625, 115.000]` um.
- `image231924_c01` first standalone TrackCenter passed at 36.008 kcps, tracked position `[113.234866865, 113.897495018, 114.794647471]` um (evidence `bridge_result_20260511_233654_062241_c2446ad943`). This proved trackability only.
- The first strong-pi pODMR attempt failed before acquisition because sequence auto-align counts were 4.065 kcps, below the 12 kcps gate; no resonance data exists (evidence `bridge_result_20260511_234836_113723_6b27c2b941`). A standalone TrackCenter recheck then passed at 24.490 kcps (evidence `bridge_result_20260511_235944_332749_9c699573a9`).
- Bounded strong-pi pODMR retry completed successfully as job `nv23_image231924_c01_strong_podmr_retry1_20260512_000251_image231924_c01_strong_podmr_retry1_20260511_2359_execute`. Raw/readout-aware review shows a visible resonance near `3.879 GHz` with about `23-25%` normalized dip; alignment screen passed (evidence `analysis_20260512_003809_989333_77ec160705`).
- First weak-pi pODMR completed successfully as job `nv23_image231924_c01_weak_podmr_20260512_004207_image231924_c01_weak_podmr_20260512_0039_execute`. Review gave usable `mw_freq_hz = 3.8758666667 GHz` with about `+/-1 MHz` grid/noise-limited uncertainty; post-run final counts were 23.547 kcps (evidence `analysis_20260512_011623_997391_3236a174e0`).
- First Ramsey/T2star scout completed successfully as job `nv23_image231924_c01_ramsey_t2star_scout_20260512_012010_image231924_c01_ramsey_t2star_scout_20260512_0118_execute`. Terminal review found a real Ramsey oscillation with dominant FFT bin near `1.593 MHz`; rough T2star scale about `3.6-4.4 us` remained candidate-fit-only, and the 13C interpretation was candidate-only because residual detuning could mimic the lower-sideband-like peak (evidence `analysis_20260512_024911_696911_41327c3aa3`).
- Narrow weak-pi pODMR center refresh after Ramsey completed successfully as job `nv23_image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025209_image231924_c01_narrow_weak_podmr_after_ramsey_20260512_0250_execute`. Raw signal and fitted-reference-normalized minima gave updated center `3.8761166667 GHz` with grid-scale uncertainty about `+/-0.25 MHz`; pointwise ratio minimum was one grid point higher at `3.8763666667 GHz`. Drift diagnostic flagged no averages (evidence `analysis_20260512_031721_840657_19692bf40a`).
- Corrected-center Ramsey/T2star repeat completed normally as bridge job `nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_032137_image231924_c01_corrected_center_ramsey_repeat_20260512_0320_execute`. Conditions: `ramsey.xml`, `mw_freq = 3.8761166667 GHz`, `det = 2 MHz`, tau `0..8 us`, 51 points, 6 averages x 100000 repetitions. Terminal savedexperiment: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-12-032449.mat`. Counts were healthy: auto-align 23.416 kcps and post-run final 26.645 kcps. Terminal review evidence `analysis_20260512_051832_635818_fe04d4f86f`.
- Terminal corrected-center Ramsey review: raw readout 2 and fitted-reference-normalized views show a repeatable oscillatory band near 1.76 MHz. The two largest FFT bins are 1.716 and 1.838 MHz, amplitude-weighted center about 1.774 MHz. Per-average detrended normalized trace correlations are moderate and positive (median 0.571, range 0.375..0.659). Scan-order-aware drift diagnostic used `Scan.ScanOrderEachAvg` / snake mode for all 6 averages and flagged no averages.
- Closeout report built and verified: `summaries/closeout_20260512_0525.pdf` and `.tex`; `latex_report_build.py` returned code 0, no log warnings, PDF header `%PDF-1.5` (evidence `report_20260512_054514_104058_aa78ec2042`; original bundle evidence `report_20260512_053512_487598_031bbfaa42`).

## Candidate Findings

- `image231924_c01`: confirmed trackable and magnetic-field-aligned/resonant enough for targeted follow-up. Strong-pi pODMR established a visible ms=+1-band resonance; weak-pi/narrow weak-pi pODMR refined the center; corrected-center Ramsey gives the final T2star/13C conclusion.
- Other image231924 candidates remain untested. They are not needed for this project because c01 satisfied the objective.

## Final Claims

- Magnetic-field-aligned NV found: `image231924_c01`, supported by strong-pi pODMR visible resonance plus weak-pi pODMR refinement.
- Current microwave frequency used for final Ramsey planning: `mw_freq_hz = 3.8761166667 GHz +/- ~0.25 MHz` grid-scale calibration uncertainty from the narrow weak-pi pODMR. This is not a sub-grid precision claim.
- Ramsey signal: present in terminal corrected-center data. Raw readout 2 and fitted-reference-normalized views show a repeatable oscillatory component near 1.76 MHz across 6 stored averages.
- T2star: supported scale about `4 us`. Gaussian-envelope fit to fitted-reference-normalized terminal Ramsey gives `T2* = 4.03 us` and `f = 1.759 MHz`; exponential/stretched/Gaussian fits give model dependence about `3.2..4.0 us`. Report as about `4 us`, not high precision.
- 13C: no resolved nearby `13C` coupling is supported by the corrected-center Ramsey data. Expected markers were carrier `2.000 MHz` and sidebands near `1.616/2.384 MHz`; terminal FFT carrier/lower/upper target-bin ranks were `5/3/19`, with the lower target bin embedded in a broad carrier/detuning-like band and the upper target bin weak. Do not claim a nearby 13C from this dataset.

## Decisions

- Use strong-pi pulsed ODMR as the alignment/resonance screen because the piezo/field changed; weak-pi pODMR is required before using an `mw_freq_hz` for Ramsey/T2star.
- Treat the strong-pi retry as an alignment pass, not a precision center claim.
- Treat the first weak-pi center `3.8758666667 GHz` as superseded for Ramsey planning by the narrow weak-pi center `3.8761166667 GHz`.
- Treat the first Ramsey scout as proving a real oscillatory signal but not T2star or 13C. Its dominant `1.593 MHz` peak is now treated as likely residual detuning / lower-sideband ambiguity, not 13C claim-grade evidence.
- Use the corrected-center terminal Ramsey result as the project closeout dataset for T2star and 13C. It supports a T2star scale and a no-resolved-13C conclusion.
- Do not submit more bridge work by default. Optional follow-up only on new human request: higher-shot/longer-span Ramsey for higher-precision T2star, or a targeted stronger-null / det-shift / decoupling diagnostic for a stronger weak-13C limit.

## Next Step

- Project is completed/inactive. No more autonomous bridge work is needed.
- If operator later asks for more precision: use the closeout report and terminal review as the starting point; do not blind-repeat. Choose measurement conditions that specifically target higher-precision T2star or a stronger 13C null.

## Evidence Pointers

- Candidate selection: `work/artifacts/analysis/image231924_candidate_list.json`, `work/notes/image231924_candidate_selection_20260511_2324.md`.
- First TrackCenter: `<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_track_20260511_2330/result.json`.
- First pODMR failure: `<NV_BRIDGE_ROOT>/failed/nv23_pulsed_odmr_rabimodulated_v1_20260511_234117_pulsed_odmr_rabimodulated_v1/result.json`.
- TrackCenter recheck: `<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_track_recheck_20260511_2350/result.json`.
- Strong-pi retry result/review: `<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_strong_podmr_retry1_20260512_000251_image231924_c01_strong_podmr_retry1_20260511_2359_execute/result.json`, `work/artifacts/analysis/image231924_c01_strong_podmr_retry1_review.json`, `work/notes/image231924_c01_strong_podmr_retry1_review_20260512_0038.md`.
- Weak-pi pODMR result/review: `<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_weak_podmr_20260512_004207_image231924_c01_weak_podmr_20260512_0039_execute/result.json`, `work/artifacts/analysis/image231924_c01_weak_podmr_20260512_004529_review.json`, `work/notes/image231924_c01_weak_podmr_review_20260512_0116.md`.
- Ramsey route review: `work/notes/ramsey_t2star_route_review_20260512_0046.md`.
- Ramsey FFT expectation/readiness: `work/artifacts/analysis/image231924_c01_ramsey_fft_expectation_20260512_0130.json`, `work/notes/image231924_c01_ramsey_fft_expectation_20260512_0130.md`.
- First Ramsey terminal review: `work/artifacts/analysis/image231924_c01_ramsey_t2star_scout_terminal_review.json`, `work/notes/image231924_c01_ramsey_terminal_and_narrow_weak_podmr_decision_20260512_0311.md`.
- Narrow weak-pi after Ramsey review: `work/artifacts/analysis/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_review.json`, `work/notes/image231924_c01_narrow_weak_podmr_after_ramsey_review_20260512_0318.md`.
- Corrected-center Ramsey terminal result: `<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_032137_image231924_c01_corrected_center_ramsey_repeat_20260512_0320_execute/result.json`.
- Corrected-center Ramsey terminal raw export/drift/review: `work/artifacts/analysis/image231924_c01_corrected_center_ramsey_repeat_terminal_raw_export.json`, `work/artifacts/analysis/image231924_c01_corrected_center_ramsey_repeat_terminal_drift.json`, `work/artifacts/analysis/image231924_c01_corrected_center_ramsey_repeat_terminal_review.json`, `work/artifacts/analysis/analyze_corrected_center_ramsey_terminal_20260512_0507.py`, evidence `analysis_20260512_051832_635818_fe04d4f86f`.
- Corrected-center terminal figures: `work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_terminal_review.png`, `work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_terminal_per_average.png`, `work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_terminal_raw_readouts.png`.
- Closeout note: `work/notes/image231924_c01_corrected_center_ramsey_terminal_closeout_20260512_0520.md`, evidence `note_20260512_053701_532922_3d11ca8a13`.
- Closeout report: top-level audit pair `summaries/closeout_20260512_0525.pdf`, `.tex`, evidence `report_20260512_054514_104058_aa78ec2042`; full bundle copy under `summaries/closeout_20260512_0525/`, evidence `report_20260512_053512_487598_031bbfaa42`.

## Note Convention

For each meaningful unit of work, write one short Markdown note under
`work/notes/` with: question, inputs read, action taken, result, checks
actually performed, remaining uncertainty, and next pointer.

Bridge-job JSON should contain execution contracts only: sequence/manifest, scan,
numeric variables, hard limits, queue/execute opt-in, target labels, and Markdown
note pointers. Scientific interpretation belongs in this file and `work/notes/`.
