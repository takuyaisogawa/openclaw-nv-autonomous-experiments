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

- Source image `3DXYZ-Image-2026-05-11-231924.mat` was exported with the explicit `ImageData_YXZ` axis contract. Candidate list: `work/artifacts/analysis/image231924_candidate_list.json`; first candidate was `image231924_c01` at image seed `[113.000, 113.625, 115.000]` um.
- `image231924_c01` first standalone TrackCenter passed at 36.008 kcps, tracked position `[113.234866865, 113.897495018, 114.794647471]` um (evidence `bridge_result_20260511_233654_062241_c2446ad943`). This proved trackability only.
- First strong-pi pODMR attempt failed before acquisition because sequence auto-align counts were 4.065 kcps, below the 12 kcps gate; no resonance data exists (evidence `bridge_result_20260511_234836_113723_6b27c2b941`). A standalone TrackCenter recheck then passed at 24.490 kcps (evidence `bridge_result_20260511_235944_332749_9c699573a9`).
- Bounded strong-pi pODMR retry completed successfully as job `nv23_image231924_c01_strong_podmr_retry1_20260512_000251_image231924_c01_strong_podmr_retry1_20260511_2359_execute`. Raw/readout-aware review shows a visible resonance near `3.879 GHz` with about `23-25%` normalized dip; alignment screen passed (evidence `analysis_20260512_003809_989333_77ec160705`).
- First weak-pi pODMR completed successfully as job `nv23_image231924_c01_weak_podmr_20260512_004207_image231924_c01_weak_podmr_20260512_0039_execute`. Review gave usable `mw_freq_hz = 3.8758666667 GHz` with about `+/-1 MHz` grid/noise-limited uncertainty; post-run final counts were 23.547 kcps (evidence `analysis_20260512_011623_997391_3236a174e0`).
- First Ramsey/T2star scout completed successfully as job `nv23_image231924_c01_ramsey_t2star_scout_20260512_012010_image231924_c01_ramsey_t2star_scout_20260512_0118_execute`. Terminal review found a real Ramsey oscillation with dominant FFT bin near `1.593 MHz`; rough T2star scale about `3.6-4.4 us` remained candidate-fit-only, and the 13C interpretation was candidate-only because residual detuning could mimic the lower-sideband-like peak (evidence `analysis_20260512_024911_696911_41327c3aa3`).
- Narrow weak-pi pODMR center refresh after Ramsey completed successfully as job `nv23_image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025209_image231924_c01_narrow_weak_podmr_after_ramsey_20260512_0250_execute`. Raw signal and fitted-reference-normalized minima give updated center `3.8761166667 GHz` with grid-scale uncertainty about `+/-0.25 MHz`; pointwise ratio minimum is one grid point higher at `3.8763666667 GHz`. Drift diagnostic flagged no averages (evidence `analysis_20260512_031721_840657_19692bf40a`).
- A corrected-center Ramsey/T2star repeat is now running as bridge job `nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_032137_image231924_c01_corrected_center_ramsey_repeat_20260512_0320_execute`. Pre-enqueue advisory had no blockers, estimated runtime `4479 s`, per-average tracking window `742 s` under the 900 s night cap, and auto-align selected `23.416 kcps`. Latest check at 03:28 EDT found it running in average 1/6 with runtime final counts text `27.931 kcps` and no terminal/anomaly evidence (evidence `artifact_20260512_032618_651713_de6e78654b`).

## Candidate Findings

- `image231924_c01`: confirmed trackable and magnetic-field-aligned/resonant enough for targeted follow-up. Strong-pi pODMR established a visible ms=+1-band resonance; weak-pi/narrow weak-pi pODMR refined the center for Ramsey planning. Continue focusing on this NV per human advice unless corrected-center Ramsey tracking/counts collapse or terminal data contradicts the line assignment.
- Other image231924 candidates remain untested and are on hold while c01 targeted follow-up is active.

## Final Claims

- Magnetic-field-aligned NV found: `image231924_c01`, supported by strong-pi pODMR visible resonance plus weak-pi pODMR refinement.
- Current microwave frequency for c01 Ramsey planning: `mw_freq_hz = 3.8761166667 GHz +/- ~0.25 MHz` grid-scale calibration uncertainty from the narrow weak-pi pODMR. This is not a sub-grid precision claim.
- T2star: no final conclusion yet. The first Ramsey scout suggests a rough `3.6-4.4 us` scale, but that remains candidate-fit-only until corrected-center terminal Ramsey data is reviewed.
- 13C: no supported positive conclusion yet. The earlier lower-sideband-like `1.593 MHz` Ramsey peak is now plausibly explained by the +0.25 to +0.50 MHz resonance-center offset found by narrow weak-pi pODMR. Do not claim nearby 13C unless corrected-center Ramsey/repeat evidence supports it. A negative/no-13C conclusion also waits for the corrected-center Ramsey review.

## Decisions

- Use strong-pi pulsed ODMR as the alignment/resonance screen because the piezo/field changed; weak-pi pODMR is required before using an `mw_freq_hz` for Ramsey/T2star.
- Treat the strong-pi retry as an alignment pass, not a precision center claim.
- Treat the first weak-pi center `3.8758666667 GHz` as superseded for Ramsey planning by the narrow weak-pi center `3.8761166667 GHz`.
- The first Ramsey scout proved a real oscillatory signal but did not prove T2star or 13C. Its dominant `1.593 MHz` peak should now be treated as likely residual detuning until corrected-center data says otherwise.
- Use `auto__ramsey` / `ramsey.xml` for the corrected-center T2star route: live manifest is validated and XML has a single active `tau` path.
- Corrected-center Ramsey design: `mw_freq = 3.8761166667 GHz`, `det = 2 MHz`, `tau = 0..8 us`, `51` points, `6 x 100000` reps, even averaging. Grid has Nyquist `3.125 MHz` and bin spacing `125 kHz`; estimated `13C` sidebands are near `1.616/2.384 MHz` from the approximate field.

## Next Step

- Wait for the corrected-center Ramsey/T2star repeat terminal result.
- If completed with data: export raw savedexperiment data, inspect raw/readout-aware Ramsey signal, perform FFT with the actual tau grid, and assess Ramsey signal, T2star, and 13C status separately. Check whether the carrier moves near the intended `2 MHz` bin and whether sideband windows near `~1.616/2.384 MHz` remain after center correction.
- If corrected-center Ramsey is still non-claim-grade but tracking/counts were healthy: use terminal drift/SNR/FFT evidence to choose between a higher-shot repeat and a det-shift Ramsey diagnostic; do not make a blind repeat.
- If corrected-center Ramsey pre-align/acquisition fails or counts collapse: review current TrackCenter/count state before any retry.

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
- Corrected-center Ramsey running batch/spec: `work/bridge_jobs/nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_0320.batch_spec.json`, `work/bridge_jobs/nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_0320.batch_state.json`.

## Note Convention

For each meaningful unit of work, write one short Markdown note under
`work/notes/` with: question, inputs read, action taken, result, checks
actually performed, remaining uncertainty, and next pointer.

Bridge-job JSON should contain execution contracts only: sequence/manifest, scan,
numeric variables, hard limits, queue/execute opt-in, target labels, and Markdown
note pointers. Scientific interpretation belongs in this file and `work/notes/`.
