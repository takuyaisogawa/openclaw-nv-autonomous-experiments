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
- Initial `image172647_c01` tracked once at 41.984 kcps, but its first pODMR execute failed before data with `NVBridge:AlignNVFailed` / low in-run counts, and immediate standalone retrack also failed low-count. This is count/freshness evidence, not no-resonance evidence. Late legacy recovery hooks for the old c01 batch are superseded and should be stopped, not retried.
- Fresh Imaging/re-image of the original image172647 region completed and was exported with explicit `ImageData_YXZ` / kcps axes.
- Fresh re-image candidate ranking selected `reimage1804_c01`, `reimage1804_c02`, then `reimage1804_c03` as fallback candidates.
- `reimage1804_c01` TrackCenter passed at 39.331 kcps, but its terminal 4-average strong-pi pODMR completed with healthy counts and no clear usable resonance. Raw/fitted-reference depressions were only about 4-5% versus expected ~22%; reject `reimage1804_c01` for this aligned-NV branch.
- `reimage1804_c02` TrackCenter completed successfully with final_counts_kcps = 39.690 at tracked position `[117.4211443249154,117.27496844942901,115.55260043233898]` um.
- Strong-pi pODMR for `reimage1804_c02` completed successfully as bridge job `nv23_pulsed_odmr_rabimodulated_v1_20260514_191847_reimage1804_c02_strong_podmr`.
- Terminal `reimage1804_c02` pODMR review (2026-05-14 19:59 EDT): 4 averages x 50000 reps completed with healthy in-run alignment counts. Raw/readout-aware review shows a clear signal-only resonance near 3.875 GHz: raw/fitted-reference depth about 13.8-14.0%, no matching reference dip, Gaussian center 3.876461 GHz with ~0.69 MHz covariance uncertainty, FWHM ~11.2 MHz. This is below the expected ~22% contrast but well above rejected c01; accept `reimage1804_c02` as the aligned-NV branch with a lower-contrast caveat.
- pODMR settings: `pulsed_odmr_rabimodulated_v1` / `Rabimodulated.xml`, `mw_freq = 3.825..3.925 GHz`, 31 points, 4 averages x 50000 reps, `mod_depth=1`, `length_rabi_pulse=52 ns`, `mw_ampl=-5`, `ampIQ=5`, `freqIQ=50 MHz`.
- The `reimage1804_c02` pODMR intent safety verifier passed, advisory/pre-enqueue response was OK with no blockers, and bridge queue was idle immediately before enqueue.
- The first c02 Ramsey/T2star scout design (`tau = 0..8 us`, 51 points, `det=2 MHz`, 4 x 100000 reps) was superseded before execute because MATLAB advisory estimated a 742.3 s per-average tracking window, above the 600 s daytime cap.
- Revised c02 Ramsey/T2star scout plan passed verifier/advisory gates with no blockers: `auto__ramsey` / `ramsey.xml`, `tau = 0..8 us`, 43 points, `det=1.5 MHz`, `mw_freq=3.876461010 GHz`, 8 averages x 50000 reps. Advisory estimated 581.8 s per-average tracking window under the active 600 s cap while preserving 400k total shots and the 8 us FFT span.
- Bridge state at this update: Ramsey/T2star scout bridge job `nv23_ramsey_20260514_201034_auto_ramsey` is running. Latest direct check at 2026-05-14 20:40 EDT showed running/`run_experiment_scan_point`, status message `(2/8) averages completed for 1 scans`, status updated 20:40:42, final count text 43.869 kcps, monitor active with no last_error, stop_requested=false, queued/staging empty, and no hard anomaly. Earlier running snapshots showed average 1/8 then average 2 progress with healthy counts, and pre-run alignment final_counts_kcps 43.710. Runtime status estimated ~656.8 s per average, slightly above the 600 s advisory cap; because the pre-enqueue advisory was under cap and the job is already running with healthy counts and no hard anomaly, treat this as provenance for monitor/terminal review, not a stop/mutation reason. Do not submit another bridge-touching job while it is queued/running. Wait for terminal result or a later autosave, then export/review the savedexperiment before fitting or making T2star/13C claims.
- First-average Ramsey autosave review (2026-05-14 20:28 EDT): one stored average is raw-exportable. Raw signal/reference views show structure, but low-frequency components are among the strongest FFT peaks and there is no average-to-average support yet. This snapshot is provisional only; no T2star or 13C claim is made.
- Bridge-free conditional Ramsey/T2star/13C model plans exist for use only after a candidate passes terminal pODMR with a clear usable resonance. The c02-specific plan re-inspected `auto__ramsey` / `ramsey.xml`, calculates expected 13C Larmor near 384 kHz at 3.875 GHz, and the revised running scout uses `det=1.5 MHz` so nominal sidebands near 1.115 and 1.885 MHz remain below the 2.625 MHz Nyquist of the 43-point / 8 us grid.

## Candidate Findings

- `image172647_c01`: initial candidate; tracked once but later was not trackable from its last seed. No pODMR data were acquired, so it has no resonance/alignment verdict. Do not rerun stale c01 pODMR without new evidence.
- `reimage1804_c01`: rejected for this branch. Terminal strong-pi pODMR had healthy counts but no clear usable resonance; weak normalization-only features were not promoted.
- `reimage1804_c02`: accepted aligned-NV branch. TrackCenter passed at 39.690 kcps; terminal strong-pi pODMR completed with a clear usable signal-only resonance near 3.875 GHz, Gaussian center 3.876461 GHz, and 13.8-14.0% raw/fitted-reference depth. Contrast is lower than expected ~22%, so carry a caveat into Ramsey/T2star planning.
- `reimage1804_c03`: fresh re-image fallback at `[114.500,116.375,115.000]` um if `reimage1804_c02` has no clear usable resonance or becomes non-trackable.

## Final Claims

- Magnetic-field-aligned NV branch established: `reimage1804_c02` has a terminal strong-pi pODMR signal-only resonance near 3.875 GHz and is accepted for targeted follow-up, with lower-than-expected contrast caveat.
- No T2star or 13C conclusion has been established yet.

## Decisions

- Do not repeat pODMR blindly on the stale initial c01 seed.
- Use the fresh re-image candidate list after low-count failures.
- Reject `reimage1804_c01` because terminal strong-pi pODMR did not show a clear usable resonance at expected contrast.
- Screened `reimage1804_c02` because it was the next fresh fallback and TrackCenter passed with healthy counts.
- Accept `reimage1804_c02` for the aligned-NV branch based on terminal strong-pi pODMR; proceed to targeted T2star/Ramsey follow-up after fresh queue, verifier, and advisory checks.
- The earlier `test_do_not_submit`/`--print-json` concern was checked: no bridge queued/running/staging/done/failed directory named `test_do_not_submit*` was found; knowledge notes that direct-helper `--print-json` is preview-only.
- Late recovery hook for stale old `image172647_c01` pODMR batch `nv23_pulsed_odmr_rabimodulated_v1_20260514_175129` was answered with `action=stop` plans for attempts 1 and 2, and a 20:43 recheck confirmed attempt 2 remains stopped, the old single-submit control has stop_requested=true, and no live old-batch process is present. This prevents obsolete c01 retry while the project has already recovered via fresh re-image candidates and current `reimage1804_c02` Ramsey/T2star follow-up. No bridge queue mutation was performed.

## Next Step

- Wait for the running Ramsey/T2star scout `nv23_ramsey_20260514_201034_auto_ramsey` to reach a terminal state or a real autosave. It was launched through the managed single-item path after verifier/advisory/queue gates passed.
- A bridge-free terminal-review protocol has been prepared for this scout. It freezes the expected det=1.5 MHz carrier, 13C sideband targets near 1.115/1.885 MHz, raw/readout-aware signal-before-fit gates, T2star fit-stability checks, and FFT/13C claim guardrails.
- If terminal success: export raw savedexperiment, plot raw readouts and fitted-reference/pointwise normalization views, decide signal presence before fitting, fit T2star only if a real Ramsey signal is visible, and FFT-check for 13C sidebands near `det +/- ~384 kHz` without claiming 13C from isolated low-SNR peaks.
- If terminal failure before data: distinguish route/hardware/code failure from tracking/count freshness evidence; do not interpret as T2star or 13C evidence.
- If the job remains running, bridge-touching work is blocked by bridge occupancy; only bridge-free analysis/planning is allowed.

## Evidence Pointers

- `image172647_export_yxz_kcps_20260514_1733`: initial explicit YXZ/kcps export JSON.
- `image172647_candidate_ranking_20260514_1734`: initial candidate ranking JSON.
- `track_image172647_c01_terminal_pass_20260514_1738`: initial c01 TrackCenter success.
- `podmr_execute_image172647_c01_failed_alignnv_20260514_1759`: initial c01 pODMR failed before data.
- `retrack_image172647_c01_after_podmr_alignfail_terminal_fail_20260514_1802`: immediate retrack failed low-count.
- `reimage_original_region_terminal_done_20260514_1809`: fresh re-image completed.
- `reimage1804_export_yxz_kcps_20260514_1811`: fresh re-image explicit YXZ/kcps export.
- `reimage1804_candidate_ranking_20260514_1812`: fresh candidate ranking.
- `track_reimage1804_c01_terminal_pass_20260514_1815`: `reimage1804_c01` TrackCenter success.
- `podmr_terminal_reimage1804_c01_no_clear_resonance_20260514_1900`: terminal c01 strong-pi pODMR rejection.
- `track_reimage1804_c02_queued_20260514_1902`: c02 TrackCenter queued.
- `track_reimage1804_c02_terminal_pass_20260514_1907`: c02 TrackCenter success.
- `podmr_plan_advisory_reimage1804_c02_31x4x50k_20260514_1916`: c02 pODMR model, submit spec, and advisory.
- `podmr_execute_reimage1804_c02_running_20260514_1921`: c02 pODMR running snapshot.
- `podmr_autosave_reimage1804_c02_1avg_promising_resonance_20260514_1930`: running autosave first-average raw/readout-aware review; promising ~23% signal-only dip near 3.875 GHz, nonterminal.
- `podmr_autosave_reimage1804_c02_2avg_provisional_review_20260514_1946`: running autosave two-average raw/readout-aware review; mean signal-only dip near 3.875 GHz is ~16%, still promising but weaker than expected and nonterminal.
- `podmr_autosave_reimage1804_c02_3avg_provisional_review_20260514_1950`: running autosave three-average raw/readout-aware review; odd intermediate snake-order mean signal-only dip near 3.875 GHz is ~13.5-13.9%, below expected ~22%, nonterminal.
- `podmr_terminal_reimage1804_c02_clear_usable_resonance_20260514_1959`: terminal 4-average strong-pi pODMR accepted c02 for aligned branch with lower-contrast caveat; center fit 3.876461 GHz.
- `conditional_ramsey_t2star_13c_model_plan_20260514_1843`: bridge-free conditional Ramsey/T2star/13C model plan after a valid pODMR resonance.
- `conditional_ramsey_t2star_13c_model_plan_reimage1804_c02_20260514_1948`: c02-specific conditional Ramsey/T2star/13C plan after terminal valid pODMR; includes current `auto__ramsey` route review and 2 MHz / 8 us / 51-point FFT guardrail.
- `ramsey_t2star_scout_rev1_plan_advisory_reimage1804_c02_20260514_2008`: first Ramsey plan superseded by drift-cap advisory; revised 43-point / det=1.5 MHz / 8x50000 plan passed advisory with 581.8 s per-average window.
- `ramsey_t2star_scout_reimage1804_c02_running_20260514_2011`: revised Ramsey/T2star scout materialized and running as bridge job `nv23_ramsey_20260514_201034_auto_ramsey`.
- `ramsey_t2star_scout_reimage1804_c02_avg_start_snapshot_20260514_2013`: running snapshot at Experiment average 1/8 with monitor active and healthy counts; post-launch runtime estimate ~656.8 s per average recorded as provenance.
- `ramsey_t2star_terminal_review_protocol_reimage1804_c02_20260514_2019`: bridge-free terminal-review protocol for the running c02 Ramsey/T2star scout; includes expected signal/FFT targets, raw/readout-aware fit gates, and branch logic.
- `ramsey_autosave_reimage1804_c02_1avg_provisional_review_20260514_2028`: first-average raw export/plot of the running c02 Ramsey/T2star scout; provisional only, no T2star/13C claim.
- Note: `work/notes/reimage1804_c01_podmr_terminal_review_reject_20260514_1900.md`.
- Note: `work/notes/reimage1804_c02_strong_podmr_plan_20260514_1915.md`.
- Note: `work/notes/reimage1804_c02_podmr_autosave_1avg_review_20260514_1930.md`.
- Note: `work/notes/reimage1804_c02_podmr_autosave_2avg_review_20260514_1946.md`.
- Note: `work/notes/reimage1804_c02_podmr_autosave_3avg_review_20260514_1950.md`.
- Note: `work/notes/reimage1804_c02_podmr_terminal_review_accept_20260514_1959.md`.
- Note: `work/notes/old_c01_recovery_hook_stopped_20260514_1939.md`.
- Artifact: `work/artifacts/recovery/old_c01_recovery_stop_summary_20260514_1939.json`.
- `old_c01_recovery_recheck_stop_20260514_2043`: rechecked stale c01 recovery attempt 2; wrote/confirmed `action=stop`, old single-submit stop_requested=true, no live old-batch process, queued/staging empty, and c02 Ramsey/T2star running healthy. Note: `work/notes/old_c01_recovery_recheck_stop_20260514_2043.md`; artifact: `work/artifacts/recovery/old_c01_recovery_recheck_stop_20260514_2043.json`.
- Note: `work/notes/conditional_ramsey_t2star_13c_after_valid_podmr_20260514_1843.md`.
- Note: `work/notes/conditional_ramsey_t2star_13c_for_reimage1804_c02_after_valid_podmr_20260514_1948.md`.
- Note: `work/notes/reimage1804_c02_ramsey_t2star_scout_rev1_plan_20260514_2006.md`.
