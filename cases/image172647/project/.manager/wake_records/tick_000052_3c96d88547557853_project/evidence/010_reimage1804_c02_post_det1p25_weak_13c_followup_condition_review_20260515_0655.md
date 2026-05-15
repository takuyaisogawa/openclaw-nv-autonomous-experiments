# Post-det=1.25 weak-13C follow-up condition review (2026-05-15 06:55 EDT)

## Candidate physical signature

Terminal det=1.25 MHz Ramsey keeps a weak det-shift-consistent candidate alive: the high-sideband target amplitudes across det=1.5, det=1.0, and det=1.25 MHz are about 1.95%, 0.84%, and 1.01%. In the terminal det=1.25 run, fixed old-high/static alternatives are weak (old det=1 high/static 0.39%, previous 1.9 MHz 0.23%). This argues against a simple fixed 1.4/1.9 MHz artifact.

## Why Ramsey remains ambiguous

The terminal det=1.25 target amplitudes are still only about 0.5-1.0% and are far below the 11-14% pODMR resonance contrast. Low-sideband, direct-Larmor, and carrier support are incomplete across the three Ramsey detunings, and the time-domain T2star fits remain sensitive to early tau and fit window. So the current conclusion is a weak candidate, not a claim-grade nearby 13C observation.

## Explicit model calculation for a non-blind follow-up

Using the weak-pi pODMR center, the expected 13C Larmor frequency is 384.6 kHz.

`CPMG.xml` timing review: the XML waits `tau`, applies a pi pulse, then waits `tau` inside each CPMG loop. Adjacent pi pulses are therefore separated by about `2*tau`. The common toggling-function estimate for a nuclear/AC resonance is then `f ~= 1/(4*tau)`, giving target `tau = 0.650 us`. Because lab conventions sometimes quote the interpulse version `tau = 1/(2*f) = 1.300 us`, the first scout should cover both regions rather than assuming one convention.

Bounded follow-up candidate (not submitted here):

- Route: `auto__cpmg` / `CPMG.xml` after fresh verifier/advisory gates.
- Purpose: magnitude-style nuclear-spectroscopy discriminator for the weak Ramsey 13C candidate.
- Suggested scan: `tau = 0.45..1.60 us`, 59 points, step 19.8 ns.
- Suggested pulse count: `N = 8`, so the total free-evolution span is roughly 7.2..25.6 us.
- MW/IQ: use weak-pi center `mw_freq = 3.876501337 GHz`, `length_pi = 52 ns`, `mod_depth = 1`, `mw_ampl=-5`, `ampIQ=5`, `freqIQ=50 MHz` unless a fresh calibration/advisory says otherwise.
- Readout caution: `CPMG.xml` has a true-0 reference, a pi-pulse reference, and a final echo readout; verify saved readout roles from terminal metadata before interpreting. The final echo should be treated as the candidate signal, not readout2 by default.

## Decision

Do not enqueue directly from this review. The next safe bridge-touching step would be to author a fresh CPMG experiment intent and run the deterministic verifier plus MATLAB advisory, including current drift/window checks and an expected-signal/distinguishability note. This is an agent-side next work item, not a human/external blocker.

Artifacts: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c02_post_det1p25_weak_13c_followup_condition_review_20260515_0655.json`
