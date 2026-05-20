Case: podmr_065_2026-05-17-071421

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first run adj_polarize followed by detection. This is readout 1, the polarized mS=0 reference.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. There is no active mS=+1 reference readout.
- The active microwave-dependent measurement is rabi_pulse_mod_wait_time followed by detection. This is readout 2, the pulsed pODMR readout.
- mod_depth = 1. The pulse duration is length_rabi_pulse = 5.2e-8 s. With sample_rate = 250 MHz, the rounding step gives round(52 ns * 250 MHz) = 13 samples, so the active pulse remains 52 ns.

Quantitative physical model:
- Given the setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant square-pulse transition probability for a 52 ns pulse is
  P_res = sin^2(pi * f_R * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a mS=0 to mS=+1 contrast scale of 22%, the expected on-resonance fractional fluorescence drop in readout 2 relative to readout 1 is
  0.22 * P_res = 0.219, or 21.9%.
- The mean readout 1 level is 47.48 raw units, so an on-resonance point should be about 47.48 * (1 - 0.219) = 37.07 raw units, a drop of about 10.4 raw units.
- Including detuning for a square pulse,
  P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).
  A resonance centered halfway between 5 MHz-spaced scan points would still have |Delta| <= 2.5 MHz at the nearest point, giving P = 0.929 and an expected drop of 20.4%. At 5 MHz detuning the expected drop is still 16.5%.

Observed data:
- Combined readout 1 mean/min/max: 47.48 / 45.46 / 49.90.
- Combined readout 2 mean/min/max: 47.21 / 44.33 / 50.08.
- Fractional drop 1 - readout2/readout1 has mean 0.55%, minimum -4.34%, maximum 4.77%, and standard deviation 2.53%.
- The largest observed positive drop is 4.77% at 3.830 GHz, far below the expected 20-22% resonance response. Several points have readout 2 above readout 1.
- Per-average normalized drops are not repeatable: average 1 has its largest drop at 3.835 GHz (7.76%), while average 2 at the same frequency is -0.47%; average 2 has a 7.29% drop at 3.905 GHz, while average 1 there is -3.75%. These stored averages are consistent with tracking cadence/drift and do not provide a strong independent reproducibility test.
- Fitting the normalized drop to the detuned Rabi model with a free amplitude gives a best amplitude of only 4.9% contrast, not the physically expected 22%. Forcing the physical 22% amplitude fits worse than a constant-offset null model.

Decision:
The active sequence should produce an approximately 22% readout-2 dip if a pODMR resonance is sampled in this scan. The observed readout contrast is small, sign-changing, and not reproducible across the two stored averages. I therefore decide that a pODMR resonance is absent.
