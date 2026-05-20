Case: podmr_068_2026-05-17-075825

Sequence interpretation:
- Sequence name: Rabimodulated.xml.
- Active experiment: pODMR/Rabi-modulated microwave-frequency scan.
- Sweep: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 is the true m_S = 0 optical reference acquired immediately after polarization.
- Readout 2 is the signal readout after the active microwave pulse.
- Active pulse before readout 2: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative model:
The relevant square-pulse transition probability for detuning Delta is

P1(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

with t = 52 ns. The given setup has Rabi frequency about 10 MHz at mod_depth = 1, so on resonance

P1(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.

With an m_S = 0 to m_S = +1 contrast scale of about 22%, an on-resonance pulse should therefore reduce the post-pulse readout by

0.22 * 0.996 = 0.219, or about 21.9% of the bright reference.

For a 50-count bright readout this corresponds to an expected drop of about 10.96 counts. Thus a resonance sampled by this scan should appear as a large dip in readout 2 relative to readout 1, with a normalized ratio near 0.781 at the resonance point.

Observed data:
- Mean readout 1: 49.31 counts.
- Mean readout 2: 48.92 counts.
- Difference readout2 - readout1: mean -0.39 counts, RMS 1.04 counts, minimum -2.29 counts.
- Normalized readout2/readout1: mean 0.992, minimum 0.955.
- The largest observed normalized dip is 1 - 0.955 = 0.045, about 4.5%, far smaller than the expected 21.9%.

I also fit the square-pulse lineshape to the normalized ratio over possible resonance centers. A fixed 22% contrast model gives a poor match because it predicts a ratio minimum near 0.781, which is not present. Allowing the dip amplitude to float gives a best-fit amplitude of about 0.022, only about one tenth of the expected contrast, and the data are dominated by common-mode drift and small readout-to-readout scatter. The downward trend late in the scan is present in both readouts, so it is not a microwave-frequency-specific pODMR dip.

Decision: resonance_absent.
