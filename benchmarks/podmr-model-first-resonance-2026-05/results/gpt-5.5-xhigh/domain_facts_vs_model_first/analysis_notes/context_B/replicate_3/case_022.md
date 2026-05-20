Case: podmr_007_2026-05-16-013306

Sequence identification:

- Sequence file/name: Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" branch is inactive. do_adiabatic_inversion is set, but it is inside the inactive branch and does not affect the active sequence.
- Active readout order:
  1. adj_polarize, then detection: this is the true m_S = 0 reference, corresponding to raw readout 1.
  2. rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then detection: this is the microwave-pulse signal, corresponding to raw readout 2.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounding step is 4 ns and 52 ns is unchanged.

Quantitative expected signal model:

Use the supplied setup facts: contrast C = 0.22 between m_S = 0 and m_S = +1, and Rabi frequency f_R = 10 MHz at mod_depth = 1. For a rectangular microwave pulse of duration tau = 52 ns, the two-level transition probability versus detuning delta_f is

P1(delta_f) = f_R^2 / (f_R^2 + delta_f^2) * sin^2(pi * tau * sqrt(f_R^2 + delta_f^2)).

At zero detuning:

- pi * tau * f_R = pi * 0.52.
- P1(0) = 0.9961.
- Expected fractional optical drop = C * P1(0) = 0.2191, i.e. essentially the full 22% setup contrast.
- The mean readout 1 level is 35.986, so the expected on-resonance readout 2 level is 35.986 * (1 - 0.2191) = 28.10.

Comparison with data:

- Minimum combined readout 2 occurs at 3.880 GHz: readout 2 = 28.212, paired readout 1 = 36.904, ratio = 0.764.
- This observed value is very close to the model expectation of about 28.10 for a near-pi pulse and 22% contrast.
- Neighboring readout 2 values form the expected broad pulsed-ODMR dip: 31.231 at 3.870 GHz, 28.962 at 3.875 GHz, 28.212 at 3.880 GHz, and 31.769 at 3.885 GHz.
- Readout 1 remains comparatively flat over the same region, so the feature is in the microwave-pulse signal rather than in the 0-state reference.

I also fit the fixed-physics lineshape using readout 1 as the local baseline:

R2_i = a * R1_i * (1 - C * P1(f_i - f0)).

With C = 0.22, f_R = 10 MHz, tau = 52 ns fixed, the best center is f0 = 3.87843 GHz and a = 0.9906. The squared residual for this resonance model is 55.7, compared with 155.7 for the no-resonance scale-only model R2_i = a * R1_i, a 64% residual reduction.

The two stored averages are not treated as a strong independent repeatability test because they can reflect tracking cadence, but both averages show the central readout-2 suppression near 3.875-3.880 GHz.

Decision: resonance_present.
