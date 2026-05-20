Case: podmr_005_2026-05-10-173726

I used the provided sequence.xml rather than labels or previous outputs. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active values are length_rabi_pulse = 52 ns and mod_depth = 1. The full_expt variable is 0, so the "Acquire 1 level reference" block is inactive despite do_adiabatic_inversion being true. The executed readouts are therefore:

1. readout 1: the true m_S = 0 bright reference after adj_polarize and detection.
2. readout 2: the signal readout after a 52 ns rabi_pulse_mod_wait_time pulse and detection.

Physical model calculation:

For the setup, the resonant Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular pulse with detuning Delta in Hz and resonant Rabi frequency f_R, the transition probability is

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

With f_R = 10 MHz and t = 52 ns, the on-resonance transition probability is

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

Using the stated 22% current contrast scale between m_S = 0 and m_S = +1, the expected on-resonance fractional drop of the signal readout relative to the bright reference is about

0.22 * 0.996 = 0.219, or 21.9%.

The observed normalized contrast 1 - readout2/readout1 has its main trough at 3.875-3.880 GHz:

- At 3.875 GHz: readout1 = 42.615, readout2 = 35.654, contrast = 16.3%.
- At 3.880 GHz: readout1 = 41.692, readout2 = 34.731, contrast = 16.7%.

The trough depth is below the ideal 21.9% model value but has the correct sign and a plausible magnitude for an imperfect experimental contrast/readout window. The readout2 off-trough mean outside the 3.865-3.890 GHz region is 41.66 counts, while the minimum is 34.73 counts, a drop of 6.93 counts. The fitted Rabi-lineshape amplitude is 7.33 counts, or about 17.5% of the fitted baseline, close to the directly normalized 16-17% trough depth.

I also fit the readout2 data to the detuned Rabi model above with a floating center, linear baseline, and amplitude. The best center is 3.8774 GHz. A linear-baseline-only null model gives SSE = 136.32, while the Rabi-lineshape model gives SSE = 47.85, reducing SSE by 88.47. This quantitative model comparison supports a resonance-like dip rather than only a monotonic drift. The stored two averages both place their lowest normalized points in the same 3.875-3.880 GHz region, but I do not treat the averages as a strong independent repeatability test because stored averages can reflect tracking cadence.

Decision: resonance_present.
