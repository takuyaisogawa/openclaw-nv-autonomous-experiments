Case podmr_017_2026-05-16-132945.

Sequence interpretation:
- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the provided sequence logic, full_expt = 0, so the "Acquire 1 level reference" block is disabled.
- The two active detections are therefore:
  1. readout 1: initial bright m_S = 0 reference after optical polarization.
  2. readout 2: signal readout after the modulated Rabi pulse.
- The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative physical model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1 and approximately linear scaling with mod_depth, the active pulse has f_R = 10 MHz.
- For a square resonant Rabi pulse, the transferred population is P = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected resonant signal decrease relative to the bright reference is 0.22 * P = 21.9% of the bright level.
- The off-dip readout 1 mean is about 44.42 counts, giving an expected resonant drop of 44.42 * 0.219 = 9.73 counts.

Observed data:
- The largest readout1-readout2 difference occurs at 3.875 GHz: readout 1 = 45.40, readout 2 = 34.17, drop = 11.23 counts.
- This is close to the expected 9.73 count resonant drop from the explicit Rabi/contrast model.
- Excluding the resonance window, the readout1-readout2 difference has mean 0.65 counts and standard deviation 1.15 counts; the peak drop is about 9.2 standard deviations above that off-resonant distribution.
- A detuned Rabi model centered at 3.875 GHz predicts a narrow dip with minimum readout2 near 34.7 counts and elevated neighboring contrast at +/-5 MHz; the measured readout2 values around 3.870, 3.875, and 3.880 GHz are 40.02, 34.17, and 36.94 counts, consistent with a resonance feature given the sparse 5 MHz sampling and only two stored averages.

Decision:
The active pulse should nearly invert the spin on resonance, producing an approximately 10 count fluorescence drop. The data show a localized drop of the expected size at 3.875 GHz, much larger than the off-resonant fluctuations. A pODMR resonance is present.
