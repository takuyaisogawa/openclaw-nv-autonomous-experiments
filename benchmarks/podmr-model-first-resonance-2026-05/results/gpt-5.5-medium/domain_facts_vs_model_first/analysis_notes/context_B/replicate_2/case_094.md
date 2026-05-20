Case: podmr_080_2026-05-17-105113

Inputs used:
- sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png only as a visual check of the exported arrays

Active sequence and readout roles:
- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first calls adj_polarize and detection, which is the true m_S = 0 fluorescence reference readout.
- full_expt is 0, so the optional m_S = +1 reference branch is inactive.
- The sequence then applies rabi_pulse_mod_wait_time and performs the second detection, which is the microwave-affected pODMR signal readout.
- The active microwave pulse is length_rabi_pulse = 52 ns with mod_depth = 1. The provided sequence.xml lists mod_depth = 1 and the exported variable values also list mod_depth = 1.

Physical model calculation:
- Given setup contrast C = 0.22 between m_S = 0 and m_S = +1.
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, scaling linearly with mod_depth.
- For a square resonant pulse with duration t = 52 ns, the transferred population is
  P = sin^2(pi * f_R * t).
- Numerically, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The expected fractional fluorescence drop on resonance is C * P = 0.219.
- The mean reference readout is 51.671 raw units, so the expected on-resonance signal readout drop is about 11.32 raw units.

Observed quantitative comparison:
- The combined readout means are reference readout 1 = 51.671 and signal readout 2 = 51.700.
- For signal minus reference, the mean is +0.028 raw units and the sample standard deviation over scan points is 0.884 raw units.
- The deepest observed signal-reference point is -1.808 raw units at 3.895 GHz, only -3.46% of the local reference.
- A real on-resonance response under the active 52 ns, mod_depth 1 pulse should be close to a 22% drop, about 11 raw units, and should be unmistakable relative to this noise scale.
- The stored two averages show a tracking-scale offset between averages, so they are not treated as a strong independent repeatability test.

Decision:
No pODMR resonance is present in this scan. The active pulse should produce a large near-pi-pulse contrast loss if a transition were resonant in the swept range, but the measured post-microwave readout remains essentially equal to the reference with only small fluctuations.
