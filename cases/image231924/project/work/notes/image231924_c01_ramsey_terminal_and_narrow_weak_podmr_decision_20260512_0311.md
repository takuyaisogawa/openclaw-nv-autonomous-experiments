# c01 Ramsey terminal review and narrow weak-pi follow-up (2026-05-12 03:11 EDT)

## Question

What does the terminal c01 Ramsey/T2star scout support, and what is the next safe targeted follow-up?

## Inputs read

- Project `brief.md`, `human_advice.md`, and `work/state.md`.
- Shared startup memory plus detailed knowledge sections: Experiment Defaults, Shot Budget And Data Quality, OpenClaw Project Operation, and Shared Literature.
- Terminal bridge result/status/job for `nv23_image231924_c01_ramsey_t2star_scout_20260512_012010_image231924_c01_ramsey_t2star_scout_20260512_0118_execute`.
- Terminal raw export, drift diagnostic, and review artifacts:
  - `work/artifacts/analysis/image231924_c01_ramsey_t2star_scout_terminal_raw_export.json`
  - `work/artifacts/analysis/image231924_c01_ramsey_t2star_scout_terminal_drift.json`
  - `work/artifacts/analysis/image231924_c01_ramsey_t2star_scout_terminal_review.json`
  - figures under `work/artifacts/figures/`.
- Previous weak-pi review: `work/artifacts/analysis/image231924_c01_weak_podmr_20260512_004529_review.json`.
- Local literature index and Crossref metadata fetch for Doherty et al., "The nitrogen-vacancy colour centre in diamond," Physics Reports 528, 1-45 (2013), DOI `10.1016/j.physrep.2013.02.001`; used only as general NV provenance, not as proof of this signal.

## Action taken

1. Raw-exported the terminal Ramsey savedexperiment with the real 23-C object parser.
2. Ran the scan-order-aware drift diagnostic.
3. Generated terminal combined/per-average figures and fit/FFT review JSON.
4. Completed the Ramsey experiment intent and the earlier weak-pi intent in the project manager.
5. Authored and verified a new experiment intent for a narrow weak-pi pODMR center refresh.
6. Submitted the narrow weak-pi pODMR via the managed batch path. The pre-enqueue advisory had no blockers.

## Result

### Terminal Ramsey scout

- Terminal bridge result completed with healthy final TrackCenter counts: `26.171 kcps`.
- Scan: `ramsey.xml`, `tau = 0..8 us`, `51` points, `4 x 100000` repetitions, snake order.
- Ramsey signal is present: raw readout2 and fitted-reference-normalized data both show a repeatable dominant oscillatory component near `1.593 MHz` across all four stored averages.
- FFT context from the weak-pi center and programmed `det=2 MHz` expected features near:
  - carrier: `2.000 MHz`
  - lower 13C sideband: `1.616 MHz`
  - upper 13C sideband: `2.384 MHz`
- Terminal combined FFT ranked the `1.593 MHz` bin first. The programmed carrier bin near `1.961 MHz` ranked 14th, and the upper-sideband bin near `2.328 MHz` ranked 7th.
- Envelope fits around the dominant component give only a rough T2star scale:
  - exponential envelope: about `3.6 us`
  - Gaussian envelope: about `4.4 us`
- Drift diagnostic used `Scan.ScanOrderEachAvg` snake metadata and flagged average 1 only. This is provenance, not a hard failure.

### Claim classification

- Ramsey signal: `present`.
- T2star: `candidate_fit_only`; not a well-supported final T2star value yet.
- 13C: `candidate_only_unresolved`; the lower-sideband-like peak is strong, but residual microwave detuning inside the previous weak-pi `+/- ~1 MHz` uncertainty can mimic a `det - f13C` feature.

## Follow-up submitted

A narrow weak-pi pODMR center refresh is now running as bridge job:

`nv23_image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025209_image231924_c01_narrow_weak_podmr_after_ramsey_20260512_0250_execute`

Design:

- sequence: `pulsed_odmr_rabimodulated_v1` / `Rabimodulated.xml`
- scan: `mw_freq = 3.8723666667..3.8793666667 GHz`, `29` points
- weak-pi settings: `length_rabi_pulse = 0.57 us`, `mod_depth = 0.1`
- acquisition: `2 x 100000` repetitions = `200000` shots, even snake-order average count
- pre-enqueue advisory: no blockers, estimated runtime `849 s`, per-average tracking window `412 s`
- auto-align at start passed: `26.780 kcps`

## Remaining uncertainty

The running narrow weak-pi result is needed to distinguish a real resonance-center offset from a 13C-sideband interpretation. Until that terminal data is reviewed, do not claim a nearby 13C or a final T2star.

## Next pointer

Wait for the narrow weak-pi pODMR terminal result. If it completes with data, raw-export and review the line center. Then choose between:

1. corrected-center Ramsey repeat for a stronger T2star value, if the narrow pODMR shows the prior center was shifted; or
2. det-shift Ramsey diagnostic / higher-quality repeat, if the pODMR center remains consistent and the 1.593 MHz Ramsey peak remains lower-sideband-like.
