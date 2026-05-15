# c01 Ramsey/T2star terminal decision framework (2026-05-12 01:53 EDT)

## Question

While the c01 Ramsey/T2star scout is still running, what terminal review should separate: (1) Ramsey signal presence, (2) a usable T2star value, and (3) a supported 13C conclusion?

## Inputs read

- Project `brief.md`, `human_advice.md`, and `work/state.md`.
- Shared startup memory plus relevant detailed knowledge sections: Experiment Defaults, Shot Budget And Data Quality, OpenClaw Project Operation, and Shared Literature.
- Current bridge `status.json` for running job `nv23_image231924_c01_ramsey_t2star_scout_20260512_012010_image231924_c01_ramsey_t2star_scout_20260512_0118_execute`.
- First autosave avg1 review JSON: `work/artifacts/analysis/image231924_c01_ramsey_t2star_scout_autosave_avg1_review.json`.
- Prior lab comparison notes:
  - `nv23_usual_nearby_ramsey_t2star_20260425/work/notes/usual_ramsey_terminal_decision_framework_20260425_1648.md`.
  - `nv23_usual_nv_nearby_13c_hamiltonian_20260502/work/notes/2026-05-02_manual_cpmg_n16_n32_first_spectral_review.md`.
  - `nv23_usual_nv_nearby_13c_hamiltonian_20260502/work/notes/2026-05-02_minimal_hamiltonian_prior_from_manual_cpmg.md`.
- Local `literature/INDEX.md`; no new web source was needed before terminal interpretation because this note is a framework, not a final scientific decision.

## Current bridge check

At the status read used for this note, the bridge job was still running:

- state/phase: `running` / `run_experiment_scan_point`
- progress text: `(1/4) averages completed for 1 scans`
- elapsed: `1811 s`
- monitor: active, last error empty
- stop requested: false
- final-count text: `Final = 24.290 kcps`
- expected runtime in status: about `3294 s`, per-average window about `817 s`
- no queue mutation, stop request, or terminal marking was performed

Advice inbox was empty at this wake.

## Terminal analysis order

When the running job reaches terminal evidence, review it in this order before deciding any follow-up:

1. Confirm terminal state, `result.json`, savedexperiment path, final counts, sequence name, tau grid, averages/repetitions, scan-order metadata, and source weak-pi pODMR metadata.
2. Raw-export the terminal savedexperiment with the real 23-C object parser.
3. Inspect raw readouts before fit: readout 1 reference trend, readout 2 signal, point-wise normalization, fitted-reference normalization, and whether any feature is only normalization-produced.
4. Plot combined and per-average traces in tau order and, when possible, acquisition/snake order.
5. Run FFT on the actual terminal tau grid after transparent detrending/windowing; record bin spacing and Nyquist from the actual data rather than the intended grid alone.
6. Test Ramsey signal presence from raw/readout-aware visual and FFT evidence. Only then fit.
7. If signal presence is supported, fit bounded Ramsey models such as offset + contrast * envelope(t, T2star) * cos(2*pi*f*t + phase), checking exponential-like and Gaussian-like envelopes only if the shape warrants them. Compare against constant/no-feature and no-decay baselines, but do not let optimizer success override poor trace support.
8. Check stored-average support: per-average visual similarity, pairwise or leave-one-out correlations where meaningful, per-average FFT peak stability around the carrier/sideband windows, and sensitivity to excluding a visibly bad/drifted average.
9. Run the scan-order-aware drift diagnostic and record advisory drift flags as provenance, not automatic rejection.
10. Review final tracking/count and environment provenance over the run window.
11. Classify separately:
    - Ramsey signal: `present`, `candidate`, `not supported`, or `failed/no data`.
    - T2star: `usable_t2star_claim`, `candidate_fit_only`, `ambiguous_no_usable_t2star`, or `failed/no data`.
    - 13C: `supported_candidate`, `candidate_only`, `not supported`, or `unresolved`.

## Current expected frequency windows

Use the weak-pi pODMR center only as the planning basis, not a sub-MHz truth claim:

- weak-pi center: `3.8758666667 GHz +/- ~1 MHz`.
- derived field scale: about `359 G`.
- expected 13C Larmor scale: about `384 kHz`.
- programmed Ramsey carrier from `det`: `2.000 MHz`.
- candidate sideband windows: about `1.616 MHz` and `2.384 MHz`.
- planned grid: `0..8 us`, `51` points; first autosave review measured bin spacing about `122.55 kHz` and Nyquist about `3.064 MHz` from the actual exported grid.

The first autosave already showed one-average FFT power near the lower-sideband bin (`1.593 MHz`) and carrier bin (`1.961 MHz`), while the upper-sideband bin was weak. This is useful evidence to guide terminal review, but it is not a T2star or 13C conclusion.

## 13C interpretation boundary

A Ramsey FFT peak near `det +/- f13C` should be treated as a candidate sideband only if it survives terminal raw/readout-aware and average-level checks. The lab's recent manual CPMG evidence on the usual NV showed strong non-aliased structure near `2*f13C` on the CPMG tau axis, with weak/few-kHz coupling implications but no solved Hamiltonian. That CPMG result is a useful scale comparison, not direct proof that a Ramsey sideband on this c01 target is physical.

Do not claim a nearby 13C nucleus, hyperfine tensor, number of nuclei, coupling signs, or a final Hamiltonian from this Ramsey scout alone unless the terminal data are much stronger than expected and the physical model is explicitly justified. A sensible terminal outcome may be: `13C candidate/unresolved; follow-up needed`.

## Follow-up implications after terminal data

- If terminal data support a coherent Ramsey oscillation and a stable carrier/sideband pattern, prefer a targeted repeat or resolution-improving Ramsey follow-up over changing target. Choose tau span/points/det using the measured terminal peak locations, drift diagnostics, and current advisory cap.
- If T2star is fit-able but average support is weak, keep `candidate_fit_only` and redesign one bounded repeat to improve reproducibility rather than making a numeric claim.
- If the 13C sideband candidate persists but is grid-limited, use a follow-up with enough tau span/frequency resolution to resolve sideband separation while keeping Nyquist above `det + f13C`.
- If the run fails, has no saved data, or counts collapse, review TrackCenter/current counts before any retry.
- If terminal evidence clearly lacks Ramsey signal despite healthy tracking and good raw readouts, reconsider detuning/center choice before repeating blindly.

## Result

This wake produced a terminal-review framework and current bridge-free synthesis only. The running bridge job was left untouched.

## Remaining uncertainty

The project still has no terminal T2star or 13C conclusion. The current autosave is one stored average out of four, so all candidate spectral structure remains provisional.

## Next pointer

Wait for terminal result. Then raw-export the final savedexperiment, generate terminal figures, run raw/readout-aware FFT and fit checks, and update `work/state.md` with separate Ramsey/T2star/13C claim status before any next bridge-touching experiment.
