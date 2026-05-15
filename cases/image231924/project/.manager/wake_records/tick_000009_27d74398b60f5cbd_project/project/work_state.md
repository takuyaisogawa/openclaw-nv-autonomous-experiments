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
- `image231924_c01` first standalone TrackCenter passed at 36.008 kcps, tracked position `[113.234866865, 113.897495018, 114.794647471]` um (evidence `bridge_result_20260511_233654_062241_c2446ad943`). This proved trackability only, not magnetic-field alignment.
- First strong-pi pODMR attempt failed before acquisition: sequence auto-align counts were only 4.065 kcps, below the 12 kcps gate; no resonance data exists (evidence `bridge_result_20260511_234836_113723_6b27c2b941`).
- Standalone TrackCenter recheck passed after that failure at 24.490 kcps from refreshed position `[112.940103609, 114.231526340, 115.486967920]` um; drift/branch uncertainty remains but c01 is currently trackable (evidence `bridge_result_20260511_235944_332749_9c699573a9`).
- A bounded strong-pi pODMR retry from the refreshed c01 position is currently running as bridge job `nv23_image231924_c01_strong_podmr_retry1_20260512_000251_image231924_c01_strong_podmr_retry1_20260511_2359_execute` (submission evidence `artifact_20260512_000334_749153_6594bf748f`).

## Candidate Findings

- `image231924_c01`: trackable but not yet alignment-qualified. Counts were healthy in two standalone TrackCenter jobs (36.008 and 24.490 kcps) but failed inside one pODMR pre-align gate. Treat as a viable but drift/branch-sensitive candidate until the current pODMR retry resolves the alignment screen.
- Other image231924 candidates remain untested. If c01 pODMR retry fails the pre-align gate again or lacks a visible strong-pi pODMR resonance, do not blind-repeat c01; move to re-image/next-candidate review.

## Final Claims

- No magnetic-field-aligned NV has been confirmed yet.
- No T2star or 13C conclusion exists yet.

## Decisions

- Use strong-pi pulsed ODMR as the alignment/resonance screen because the piezo/field changed; weak-pi pODMR is still needed before precision `mw_freq_hz` claims.
- Keep initial strong-pi pODMR screen bounded to 21 points over 3.825-3.925 GHz, 4 averages x 50000 repetitions, even snake-order averaging, and no automatic bridge fit.
- After c01's first pODMR pre-align failure, perform exactly one bounded pODMR retry from the refreshed standalone TrackCenter position before abandoning or re-imaging c01.

## Next Step

- Wait for the current c01 strong-pi pODMR retry terminal result.
- If completed with data: export raw savedexperiment data, inspect raw/readout-aware pODMR line visibility, and decide whether to run weak-pi pODMR on c01.
- If pre-align fails again: stop c01 blind retries and choose re-image versus `image231924_c02`/next candidate from the saved-image candidate list.

## Evidence Pointers

- Candidate selection: `work/artifacts/analysis/image231924_candidate_list.json`, `work/notes/image231924_candidate_selection_20260511_2324.md`.
- First TrackCenter: `<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_track_20260511_2330/result.json`.
- First pODMR failure: `<NV_BRIDGE_ROOT>/failed/nv23_pulsed_odmr_rabimodulated_v1_20260511_234117_pulsed_odmr_rabimodulated_v1/result.json`.
- TrackCenter recheck: `<NV_BRIDGE_ROOT>/done/nv23_image231924_c01_track_recheck_20260511_2350/result.json`.
- Current pODMR retry submit spec: `work/artifacts/submit_specs/image231924_c01_strong_podmr_retry1_20260511_2359_execute_submit_spec.json`.

## Note Convention

For each meaningful unit of work, write one short Markdown note under
`work/notes/` with: question, inputs read, action taken, result, checks
actually performed, remaining uncertainty, and next pointer.

Bridge-job JSON should contain execution contracts only: sequence/manifest, scan,
numeric variables, hard limits, queue/execute opt-in, target labels, and Markdown
note pointers. Scientific interpretation belongs in this file and `work/notes/`.
