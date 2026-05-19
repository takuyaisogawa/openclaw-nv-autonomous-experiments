<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_039

Sequence and readout roles:
- The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the provided sequence XML, full_expt = 0, so the optional m_S = +1 reference block is inactive despite do_adiabatic_inversion = 1.
- The two active detections are therefore:
  1. readout 1: true m_S = 0 level reference, taken immediately after laser polarization.
  2. readout 2: signal readout after the rabi_pulse_mod_wait_time pulse.
- The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. The sample-rate rounding at 250 MHz leaves 52 ns exactly.

Expected quantitative signal model:
- Given setup contrast C = 0.22 between m_S = 0 and m_S = +1.
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, with linear scaling in mod_depth.
- For a resonant square Rabi pulse of duration t, the transferred population is modeled as P1 = sin^2(pi f_R t).
- With f_R = 10 MHz and t = 52 ns, f_R t = 0.52 cycles and P1 = sin^2(pi * 0.52) = 0.996.
- Expected resonant fluorescence ratio is signal/reference = 1 - C * P1 = 1 - 0.22 * 0.996 = 0.781.
- With the observed reference mean near 53.86 raw units, the expected on-resonance drop is about 11.8 raw units.

Observed quantitative comparison:
- Mean readout 1 = 53.855 raw units.
- Mean readout 2 = 54.175 raw units.
- Mean readout2 - readout1 = +0.320 raw units, so the post-pulse readout is slightly higher on average, not lower.
- The pointwise readout2/readout1 ratio has mean 1.006, standard deviation 0.0206, minimum 0.969, and maximum 1.050.
- The deepest observed ratio, 0.969 at 3.895 GHz, corresponds to only a 3.1% drop, far smaller than the 21.9% drop expected from the active pulse parameters.
- A brute-force Lorentzian dip fit over plausible centers and widths did not find a physical positive dip amplitude; the best least-squares solution preferred a negative dip amplitude, i.e. a peak rather than a resonance dip.

Decision:
The expected resonant pODMR signature for the active pulse sequence is large and should be unmistakable in these raw readouts. The observed readout ratio remains close to unity and lacks a consistent resonance-shaped drop. I therefore decide that a pODMR resonance is absent.
