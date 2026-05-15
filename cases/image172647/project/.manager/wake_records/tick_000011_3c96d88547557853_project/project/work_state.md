# Project State: nv23_aligned_nv_t2star_13c_image172647_20260514_1728

Keep this file short, current, and useful. Detailed checks belong in `work/notes/`.

## Objective

Find a magnetic-field-aligned NV from image172647, then obtain a well-supported T2star and 13C conclusion.

## Standing Operational Assumptions

- Use `<OPENCLAW_WORKSPACE>/NV_RESEARCH_MEMORY.md` as every-wake startup memory and read detailed NV knowledge sections only as needed.
- Use explicit SavedImages axis contracts before candidate coordinates drive TrackCenter. Do not infer X/Y/Z from array shape.
- Use explicit Imaging -> agent-visible candidate selection -> standalone TrackCenter -> sequence execution.
- Magnetic-field alignment must be judged by a strong-pi pulsed ODMR scan. If a candidate does not show a clear usable resonance, reject it and move on.
- Once one aligned NV is found, focus on that NV until T2star and 13C each have a well-supported conclusion.

## Current Status

- Initial saved image `3DXYZ-Image-2026-05-14-172647.mat` was exported with explicit `ImageData_YXZ` / kcps axes.
- Initial c01 tracked once at 41.984 kcps, but its first pODMR execute failed before data with `NVBridge:AlignNVFailed` (in-run TrackCenter 3.420 kcps < 8), and immediate standalone retrack also failed low-count (3.278 kcps < 8). This is not no-resonance evidence.
- Fresh Imaging/re-image of the original image172647 region completed and was exported with explicit `ImageData_YXZ` / kcps axes.
- Fresh re-image candidate ranking found top current candidate `reimage1804_c01` at `[116.000,117.375,116.000]` um, value 40.2 kcps, local contrast 19.5 kcps.
- Standalone TrackCenter for `reimage1804_c01` completed with `final_counts_kcps = 39.331` at tracked position `[116.01960123089442,117.39137641463844,116.35177881539126]` um.
- Strong-pi pODMR alignment screen for `reimage1804_c01` is running as bridge job `nv23_pulsed_odmr_rabimodulated_v1_20260514_182054_pulsed_odmr_rabimodulated_v1`.
- pODMR settings: `pulsed_odmr_rabimodulated_v1` / `Rabimodulated.xml`, `mw_freq = 3.825..3.925 GHz`, 31 points, 4 averages x 50000 reps, `mod_depth=1`, `length_rabi_pulse=52 ns`, `mw_ampl=-5`, `ampIQ=5`, `freqIQ=50 MHz`.
- Advisory for the running pODMR had no blockers. It reported high recent drift risk due the low-count failures; the live status estimator reports about 488 s per average / 1978 s total.
- A stale queued duplicate pODMR for old `image172647_c01` appeared from an interrupted old single-submit batch. It was superseded before execution, moved from `queued/` to `failed/`, the old batch control was stop-requested, and the stale old local `nv_batch_run.py` process was terminated after it remained alive. No hardware was touched by that stale queued job.
- Two autosaved averages from the running `reimage1804_c01` pODMR were raw-exported and plotted. This remains provisional only: readout 1 is `m_S=0` reference and readout 2 is signal; the 2-average view does not show an obvious 22% strong-pi dip. Terminal 4-average review is still required before alignment/rejection.
- While the bridge job continued running, a bridge-free conditional Ramsey/T2star/13C model plan was prepared for use only if terminal pODMR review finds a clear usable resonance. It calculates expected 13C Larmor near 384 kHz at 3.875 GHz and flags that an 8 us / 51-point Ramsey scout should use about 2 MHz detuning rather than the 5 MHz default to avoid FFT aliasing.
- Live bridge queue after cleanup: queued empty; running only the intended `reimage1804_c01` pODMR job.

## Candidate Findings

- `image172647_c01`: initial candidate; tracked once but then not trackable from its last seed. No pODMR data were acquired for it, so it has no resonance/alignment verdict. Do not rerun stale c01 pODMR without new evidence.
- `reimage1804_c01`: current active candidate from fresh re-image. TrackCenter passed at 39.331 kcps. Strong-pi pODMR is running; the 2-average autosave is not a terminal verdict and does not show an obvious 22% dip. Alignment verdict pending full terminal raw/readout-aware review.
- `reimage1804_c02`: fresh re-image fallback near the original c01 location at `[117.375,117.250,116.000]` um.
- `reimage1804_c03`: fresh re-image fallback at `[114.500,116.375,115.000]` um.

## Final Claims

- None yet. No magnetic-field-aligned NV, T2star, or 13C conclusion has been established.
- No candidate has yet been rejected for no resonance; the only complete pODMR-related failure so far was pre-data low-count alignment failure, and the only `reimage1804_c01` data so far are an in-progress first-average autosave.

## Decisions

- Do not repeat pODMR blindly on the stale initial c01 seed.
- Use the fresh re-image candidate list after the low-count failures.
- Screen `reimage1804_c01` first because it is the top current bright peak and has a successful fresh TrackCenter.
- Do not start any new bridge-touching work while the `reimage1804_c01` pODMR is running.

## Next Step

- First inspect bridge state for running job `nv23_pulsed_odmr_rabimodulated_v1_20260514_182054_pulsed_odmr_rabimodulated_v1`.
- If it completes with saved data: export the final savedexperiment, plot raw signal/reference plus safe normalizations, and decide whether there is a clear usable resonance for magnetic-field alignment before any Ramsey/T2star/13C work.
- If it fails before data from count/tracking gate: record as count/freshness evidence and decide between retrack/re-image/fallback candidate; do not call it no-resonance.
- If it completes with no clear usable resonance: reject `reimage1804_c01` and move to `reimage1804_c02`.
- If it is still running: do not mutate the bridge queue; at most inspect newer autosaves and update bridge-free notes.

## Evidence Pointers

- `image172647_export_yxz_kcps_20260514_1733`: initial explicit YXZ/kcps export JSON.
- `image172647_candidate_ranking_20260514_1734`: initial candidate ranking JSON.
- `track_image172647_c01_terminal_pass_20260514_1738`: initial c01 TrackCenter success.
- `podmr_execute_image172647_c01_failed_alignnv_20260514_1759`: initial c01 pODMR failed before data.
- `retrack_image172647_c01_after_podmr_alignfail_terminal_fail_20260514_1802`: immediate retrack failed low-count.
- `reimage_original_region_terminal_done_20260514_1809`: fresh re-image completed.
- `reimage1804_export_yxz_kcps_20260514_1811`: fresh re-image explicit YXZ/kcps export.
- `reimage1804_candidate_ranking_20260514_1812`: fresh candidate ranking.
- `reimage1804_candidate_figure_20260514_1812`: fresh candidate figure.
- `track_reimage1804_c01_terminal_pass_20260514_1815`: `reimage1804_c01` TrackCenter success.
- `podmr_advisory_reimage1804_c01_31x4x50k_20260514_1818`: advisory for running pODMR.
- `podmr_execute_reimage1804_c01_running_20260514_1821`: initial running pODMR job snapshot.
- `stale_image172647_c01_duplicate_queue_superseded_20260514_1830`: stale old-c01 queued duplicate superseded before execution.
- `podmr_execute_reimage1804_c01_running_snapshot_20260514_1830`: running pODMR status after queue cleanup.
- `podmr_autosave_reimage1804_c01_1avg_raw_review_20260514_1832`: first-average autosave raw review and figure.
- `podmr_execute_reimage1804_c01_running_snapshot_20260514_1843`: running snapshot while pODMR remained nonterminal.
- `podmr_autosave_reimage1804_c01_2avg_raw_review_20260514_1845`: two-average autosave raw review and figure; provisional, no terminal verdict.
- `conditional_ramsey_t2star_13c_model_plan_20260514_1843`: bridge-free conditional Ramsey/T2star/13C model plan after a valid pODMR resonance.
- Note: `work/notes/image172647_c01_podmr_alignfail_retrack_reimage_20260514_1809.md`.
- Note: `work/notes/reimage1804_c01_podmr_running_cleanup_autosave_20260514_1833.md`.
- Note: `work/notes/conditional_ramsey_t2star_13c_after_valid_podmr_20260514_1843.md`.
