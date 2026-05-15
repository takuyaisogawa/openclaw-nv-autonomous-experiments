# 2026-05-14 05:40 - pODMR refresh review and refreshed-center Ramsey design

## Question
What did the terminal weak-pi pODMR refresh support, and what is the next safe non-blind Ramsey/T2star/13C step?

## Inputs read
- Terminal pODMR refresh review: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_terminal_review_20260514_0523.json`.
- Terminal det-shift Ramsey review: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_terminal_review_20260514_0424.json`.
- Prior 8 us Ramsey review: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p0_8us_terminal_review_20260513_2220.json`.
- Live `auto__ramsey` manifest/XML/function were inspected earlier in this wake/split turn; the plan records the active single-`tau` path and readout roles.
- Targeted literature/context lookup: local literature grep found no hits; Crossref metadata for Dutt et al. Science 2007 DOI 10.1126/science.1139831 and Zhao et al. Nature Nanotechnology 2012 DOI 10.1038/nnano.2012.152 was used only as a reminder that 13C claims require coherent nuclear-spin/sideband evidence, not isolated FFT peaks.

## Action taken
- Registered terminal pODMR refresh evidence and copied bridge/batch terminal artifacts into `work/bridge_jobs/`.
- Designed a refreshed-center long-span Ramsey follow-up and wrote model/advisory/submit-spec artifacts.
- Ran MATLAB advisory preview and project intent verification.

## Result
- pODMR refresh completed safely: final counts `40.396 kcps`, 4 x 50000 shots, no scan-order-aware drift flags.
- Raw signal and fitted-reference-line normalization both minimize at `3.8765 GHz`; point-wise ratio minimum is offset and treated as denominator-sensitive provenance.
- Use `mw_freq_hz=3876500000.0` for the next Ramsey with grid-supported precision only. This pODMR result is a frequency calibration only and does not establish T2star or 13C.
- Next Ramsey design: `auto__ramsey`, `mw_freq=3876500000.0`, `det=1.5 MHz`, `tau=48 ns..8.048 us`, 41 points, `20 x 50000` shots.
- Expected 13C Larmor from the refreshed working field model is `384.8 kHz`; target sidebands are `1.115` and `1.885 MHz` around the 1.5 MHz carrier.
- Advisory ok: `True`; blockers: `[]`. Project verifier response: `{"action": "verify_experiment_intent", "intent_id": "image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_20x50k_20260514_0540", "intent_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/experiment_intents/verified/image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_20x50k_20260514_0540.json", "lab_log_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/log.md", "ok": true, "project_id": "nv23_aligned_nv_t2star_13c_image145844_20260513_1507", "safety_verification": {"agent_role": "scientific_intent_author", "blockers": [], "bridge_activity": {"bridge_root": "<NV_BRIDGE_ROOT>", "busy": false, "exists": true, "queued": false, "queued_items": [], "running": false, "running_items": []}, "bridge_touching": true, "hard_errors": [], "project_id": "nv23_aligned_nv_t2star_13c_image145844_20260513_1507", "python_role": "safety_queue_and_har`.

## Checks actually performed
- Bridge queued/running/staging was empty before design/verification in the same wake.
- `verify-experiment-intent` JSON was parsed; do not rely on return code alone.
- Advisory preview was parsed from the helper JSON and checked for blockers.
- The plan uses an even average count under snake-order guidance and keeps repetitions per average at 50000 so the per-average tracking window stays comparable to the earlier 8 us run and under the stricter 600 s daytime cap if advisory confirms.

## Remaining uncertainty
- The pODMR center has 0.1 MHz grid spacing and several-100-kHz uncertainty; do not claim sub-grid precision.
- Previous Ramsey evidence remains non-claim-grade. The next run can support a T2star fit only if terminal raw/readout-aware carrier/decay signal presence is supported.
- A 13C conclusion still requires consistent sideband/coupling evidence near carrier +/- `384.8 kHz`; isolated FFT peaks are insufficient.

## Next pointer
If verifier and bridge gates remain clear, execute the verified refreshed-center Ramsey intent `image145844_reimage_r03_ramsey_refreshed_center_det1p5_8us_20x50k_20260514_0540`. Once running, queue occupancy blocks further bridge-touching submissions; terminal raw export/drift/review is required before any T2star or 13C claim.
