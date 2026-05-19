<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_038

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- The active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first run adj_polarize followed by detection. This is readout 1, the bright m_S = 0 reference.
- full_expt is 0, so the optional m_S = +1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This is readout 2, the pODMR signal after the microwave pulse.
- From the provided XML and exported variable values, mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, 52 ns is exactly 13 samples, so rounding does not change the duration.

Expected signal model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant pulse area for tau = 52 ns is f_R * tau = 0.52 cycles.
- For a rectangular driven two-level pulse, the transition probability is
  P(delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau),
  with Omega = 2*pi*10 MHz and Delta = 2*pi*detuning.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The contrast scale between m_S = 0 and m_S = +1 is about 22%, so an on-resonance point should reduce the post-pulse readout by about 0.996 * 22% = 21.9% relative to the bright reference.
- With readout 1 averaging 47.55 raw counts, the expected resonant dip is about 10.42 counts, giving an expected readout 2 near 37.13 counts at resonance.
- Even if the resonance were halfway between 5 MHz-spaced scan points, detuning 2.5 MHz gives P = 0.929 and an expected dip of about 9.72 counts. At 5 MHz detuning, P = 0.749 and the expected dip is still about 7.83 counts.

Observed comparison:
- readout 1 mean = 47.55, population standard deviation across scan = 1.02 counts, min/max = 45.90/49.92.
- readout 2 mean = 47.69, population standard deviation across scan = 0.98 counts, min/max = 45.38/49.65.
- The pointwise difference readout2 - readout1 has mean +0.14 counts, standard deviation 1.42 counts, and minimum -2.48 counts.
- The largest observed fractional readout2 drop relative to readout1 is 5.1% at 3.835 GHz, far below the roughly 22% dip expected for a resonant 52 ns pulse at mod_depth = 1.
- Stored averages show broad drift between averages and should mainly be treated as tracking cadence evidence, not as a strong independent repeatability test.

Decision:
The physical model predicts a large, scan-step-robust pODMR dip if the resonance is in the scanned range. The combined readouts show no dip of the required magnitude and no stable resonance-shaped feature. I therefore decide that a pODMR resonance is absent.
