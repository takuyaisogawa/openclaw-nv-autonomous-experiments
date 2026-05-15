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

- Read the shared NV startup memory at `<OPENCLAW_WORKSPACE>/NV_RESEARCH_MEMORY.md` before choosing NV project steps.
- Use its Memory Index to read relevant sections from `<OPENCLAW_WORKSPACE>/NV_RESEARCH_KNOWLEDGE.md` only when the current state, evidence, or human advice makes them useful.
- When an NV wake produces a durable reusable detailed lesson, update `<OPENCLAW_WORKSPACE>/NV_RESEARCH_KNOWLEDGE.md` in the relevant section with a concise dated note and provenance pointer.
- New NV projects use the `start-project` -> cron/force wake `nv-researcher` flow. `start-project` preserves the human request and durable state; `nv-researcher` owns the research agenda, backlog expansion, evidence synthesis, and experiment-design judgment.
- Treat backlog items as execution/audit pointers, not as a complete scientific plan. Keep any seed backlog item minimal unless operator explicitly asked for detailed gates.
- For usual-NV recovery, prefer recent tracking, explicit human seeds, or prompt-visible label-dataset evidence before standalone Imaging/TrackCenter. Do not use the legacy live landmark-map route for future execution or recovery.
- If NV tracking remains continuous and counts/alignment evidence stay healthy, absolute position motion by itself is not a reason to stop or block an experiment. Treat the motion as provenance and drift evidence to record, while continuing bounded work when the scientific intent and safety gates still hold.
- Do pause or re-check when tracking is lost, counts collapse, a discontinuous jump or branch switch lacks continuous tracking provenance, hardware safety is uncertain, or a project-specific human constraint explicitly requires a fixed landmark/position.

## Current Status

- Source image `3DXYZ-Image-2026-05-11-231924.mat` was exported with the explicit `ImageData_YXZ` axis contract. Candidate list is in `work/artifacts/analysis/image231924_candidate_list.json`; first candidate was `image231924_c01` at image seed `[113.000, 113.625, 115.000]` um.
- `image231924_c01` first standalone TrackCenter passed at 36.008 kcps, tracked position `[113.234866865, 113.897495018, 114.794647471]` um (evidence `bridge_result_20260511_233654_062241_c2446ad943`). This proved trackability only.
- First strong-pi pODMR attempt failed before acquisition: sequence auto-align counts were only 4.065 kcps, below the 12 kcps gate; no resonance data exists (evidence `bridge_result_20260511_234836_113723_6b27c2b941`). A standalone TrackCenter recheck then passed at 24.490 kcps (evidence `bridge_result_20260511_235944_332749_9c699573a9`).
- Bounded strong-pi pODMR retry completed successfully as job `nv23_image231924_c01_strong_podmr_retry1_20260512_000251_image231924_c01_strong_podmr_retry1_20260511_2359_execute`. Raw/readout-aware review shows a visible resonance near `3.879 GHz` with about `23-25%` normalized dip; alignment screen passed (evidence `analysis_20260512_003809_989333_77ec160705`).
- Weak-pi pODMR completed successfully as job `nv23_image231924_c01_weak_podmr_20260512_004207_image231924_c01_weak_podmr_20260512_0039_execute`. Review gives usable `mw_freq_hz = 3.8758666667 GHz` with about `+/-1 MHz` grid/noise-limited uncertainty; post-run final counts were 23.547 kcps (evidence `analysis_20260512_011623_997391_3236a174e0`).
- An FFT-aware Ramsey/T2star scout is now running as bridge job `nv23_image231924_c01_ramsey_t2star_scout_20260512_012010_image231924_c01_ramsey_t2star_scout_20260512_0118_execute`. Latest status check at 01:40 EDT found the job still running in `run_experiment_scan_point` with no monitor/control error, final counts text `24.290 kcps`, and first autosave MAT `1DExp-seq-ramsey-vary-tau-2026-05-12-012318.mat` materialized/reviewed.

## Candidate Findings

- `image231924_c01`: confirmed trackable and magnetic-field-aligned/resonant enough for targeted follow-up. Strong-pi pODMR established a visible ms=+1-band resonance; weak-pi pODMR refined the center to `3.8758666667 GHz` for Ramsey planning. Continue focusing on this NV per human advice unless Ramsey tracking/counts collapse or terminal data contradicts the line assignment.
- Other image231924 candidates remain untested and are on hold while c01 targeted follow-up is active.

## Final Claims

- Magnetic-field-aligned NV found: `image231924_c01`, supported by strong-pi pODMR visible resonance plus weak-pi pODMR refinement.
- Current usable microwave frequency for c01 Ramsey planning: `mw_freq_hz = 3.8758666667 GHz +/- ~1 MHz` (weak-pi pODMR, grid/noise-limited; not a sub-MHz calibration claim).
- No T2star conclusion exists yet. The first in-progress Ramsey autosave shows candidate oscillatory signal, but it is only one stored average and not claim-grade.
- No 13C conclusion exists yet. One-average FFT has power in the expected lower-sideband/carrier region, but 13C status remains unresolved until terminal/repeat evidence.

## Decisions

- Use strong-pi pulsed ODMR as the alignment/resonance screen because the piezo/field changed; weak-pi pODMR is required before using an `mw_freq_hz` for Ramsey/T2star.
- Treat the strong-pi retry as an alignment pass, not a precision center claim.
- Use the weak-pi center `3.8758666667 GHz` for the first Ramsey/T2star scout.
- Use `auto__ramsey` / `ramsey.xml` for the first T2star route: live manifest is validated and XML has a single active `tau` path.
- First Ramsey scout design: `tau = 0..8 us`, `51` points, `det = 2 MHz`, `4 x 100000` reps, even averaging. Advisory preview passed with no blockers; estimated runtime `2994 s`, per-average tracking window `742 s`, under the nighttime 900 s cap.
- Bridge-free Ramsey FFT expectation from the weak-pi center: `Bz ~359 G`, `13C Larmor ~384 kHz`; the programmed grid has `3.125 MHz` Nyquist and `125 kHz` bin spacing, so expected Ramsey features are near `2.000 MHz` carrier plus possible `1.616/2.384 MHz` 13C sidebands. This is an analysis-readiness expectation, not a data claim (evidence `analysis_20260512_012959_396850_844184fb18`).

## Next Step

- Wait for the running Ramsey/T2star scout terminal result.
- If completed with data: export raw savedexperiment data, inspect raw/readout-aware Ramsey signal, perform FFT with the actual tau grid, and assess T2star and 13C status separately. In the FFT, check the 2 MHz detuning carrier and the expected ~1.616/2.384 MHz 13C sideband windows, but keep any frequency claim grid-limited until follow-up data supports it.
- If the terminal Ramsey result remains non-claim-grade but tracking/counts were healthy: redesign a bounded Ramsey repeat using the observed one-average signal, final drift, SNR, and FFT resolution rather than abandoning c01.
- If Ramsey pre-align/acquisition fails or counts collapse: review current TrackCenter/count state before any retry.

## Evidence Pointers

- Candidate selection: `work/artifacts/analysis/image231924_candidate_list.json`, `work/notes/image231924_candidate_selection_20260511_2324.md`.
- First TrackCenter: `<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_track_20260511_2330/result.json`.
- First pODMR failure: `<NV_BRIDGE_ROOT>/failed/nv23_pulsed_odmr_rabimodulated_v1_20260511_234117_pulsed_odmr_rabimodulated_v1/result.json`.
- TrackCenter recheck: `<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_track_recheck_20260511_2350/result.json`.
- Strong-pi retry result/review: `<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_strong_podmr_retry1_20260512_000251_image231924_c01_strong_podmr_retry1_20260511_2359_execute/result.json`, `work/artifacts/analysis/image231924_c01_strong_podmr_retry1_review.json`, `work/notes/image231924_c01_strong_podmr_retry1_review_20260512_0038.md`.
- Weak-pi pODMR result/review: `<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_weak_podmr_20260512_004207_image231924_c01_weak_podmr_20260512_0039_execute/result.json`, `work/artifacts/analysis/image231924_c01_weak_podmr_20260512_004529_review.json`, `work/notes/image231924_c01_weak_podmr_review_20260512_0116.md`.
- Ramsey route review: `work/notes/ramsey_t2star_route_review_20260512_0046.md`.
- Running Ramsey scout batch/spec: `work/bridge_jobs/nv23_image231924_c01_ramsey_t2star_scout_20260512_0120.batch_spec.json`, `work/bridge_jobs/nv23_image231924_c01_ramsey_t2star_scout_20260512_0120.batch_state.json`.
- Ramsey FFT expectation/readiness: `work/artifacts/analysis/image231924_c01_ramsey_fft_expectation_20260512_0130.json`, `work/notes/image231924_c01_ramsey_fft_expectation_20260512_0130.md`.
- In-progress Ramsey autosave avg1 review: `work/artifacts/analysis/image231924_c01_ramsey_t2star_scout_autosave_avg1_raw_export.json`, `work/artifacts/analysis/image231924_c01_ramsey_t2star_scout_autosave_avg1_review.json`, `work/notes/image231924_c01_ramsey_t2star_scout_autosave_avg1_review_20260512_0139.md`.

## Note Convention

For each meaningful unit of work, write one short Markdown note under
`work/notes/` with: question, inputs read, action taken, result, checks
actually performed, remaining uncertainty, and next pointer.

Bridge-job JSON should contain execution contracts only: sequence/manifest, scan,
numeric variables, hard limits, queue/execute opt-in, target labels, and Markdown
note pointers. Scientific interpretation belongs in this file and `work/notes/`.
