# 2026-05-14 04:45 EDT - det-shift terminal review and weak-pi pODMR refresh start

## Question

What does the terminal det=1.5 MHz short-tau Ramsey shift-check say about the r03 T2star/13C branch, and what is the next safe non-blind step?

## Inputs read

- Terminal bridge result/status for `nv23_ramsey_20260514_015423_auto_ramsey`.
- Savedexperiment `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-015440.mat`.
- Prior det=1.0 MHz short-tau terminal review and det-shift model plan.
- Prior fine weak-pi pODMR review at `3.8759 GHz`.
- Current bridge queue/project status and the `pulsed_odmr_rabimodulated_v1` manifest/XML basis.

## Action taken

- Copied terminal det-shift bridge artifacts and batch state into `work/bridge_jobs/`.
- Completed intent `image145844_reimage_r03_ramsey_det1p5_shiftcheck_shorttau_20260514_0142`.
- Raw-exported terminal det-shift data, ran scan-order-aware drift analysis, and wrote terminal review artifacts:
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_terminal_review_20260514_0424.json`
  - `work/artifacts/figures/image145844_reimage_r03_ramsey_det1p5_shiftcheck_terminal_review_20260514_0424.png`
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_terminal_raw_export_20260514_0424.json`
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p5_shiftcheck_terminal_drift_20260514_0424.json`
- Designed a fine weak-pi pODMR refresh because the previous weak-pi center is older than the default 5 h validity window:
  - `work/artifacts/analysis/image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_model_plan_20260514_0438.json`
  - `work/artifacts/analysis/image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_advisory_preview_20260514_0438.json`
  - `work/bridge_jobs/image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_submit_spec_20260514_0438.json`
- Queued and verified intent `image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_20260514_0438`; verifier verdict was `verified` with no hard errors/blockers and bridge idle.
- Started the refresh as running bridge job `nv23_pulsed_odmr_rabimodulated_v1_20260514_044105_pulsed_odmr_rabimodulated_v1` via batch `nv23_pulsed_odmr_rabimodulated_v1_20260514_043948`.

## Result

- Det-shift Ramsey completed safely: `12 x 90000` repetitions, final counts `44.796 kcps`, monitor `last_error=''`, `stop_requested=false`, and no scan-order-aware drift flags.
- Full-span ratio LS screen top shifted to about `1.623 MHz`. Programmed `1.5 MHz` ratio amplitude was `0.02399`; predicted det-tracking `1.692 MHz` amplitude was `0.02505`; the old fixed `1.192 MHz` artifact-control amplitude was only `0.00511`.
- After skipping the first 4 tau points, the top screen moved to about `0.746 MHz`; programmed/det-tracking amplitudes remained modest and per-average screens were mixed.
- Interpretation: the run argues against simply promoting a fixed `1.192 MHz` artifact, but it is still not clean enough to support a numeric T2star fit or nearby-13C conclusion.
- The pODMR refresh is healthy at initial status: running, average `1/4`, scan `3.8745..3.8775 GHz` in 31 points, `4 x 50000`, final-count text `44.796 kcps`, monitor error empty.

## Checks actually performed

- Bridge queue was idle before the new bridge-touching intent was verified/submitted.
- MATLAB advisory preview returned `ok=true`, blockers `[]`, estimated per-average tracking window about `414 s` in preview and `489 s` in live status, under the active nighttime cap.
- `verify-experiment-intent` returned `verdict=verified` with no hard errors or blockers.
- The actual running status was inspected and copied after enqueue.

## Remaining uncertainty

- No T2star or 13C claim is supported yet.
- The refreshed weak-pi pODMR must complete and receive terminal raw/readout-aware review before any extended Ramsey/T2star design uses a microwave center.
- The det-shift evidence is carrier-like but broad/coarse-window limited; it should guide a targeted next Ramsey design only after frequency refresh.

## Next pointer

Monitor `nv23_pulsed_odmr_rabimodulated_v1_20260514_044105_pulsed_odmr_rabimodulated_v1`. When terminal, copy job/result/status/control plus batch state, complete intent `image145844_reimage_r03_fine_weak_podmr_refresh_after_detshift_20260514_0438`, raw-export the savedexperiment, run scan-order-aware drift, and review raw signal plus fitted-reference-line normalization before selecting a refreshed `mw_freq_hz` for any longer Ramsey/T2star follow-up.
