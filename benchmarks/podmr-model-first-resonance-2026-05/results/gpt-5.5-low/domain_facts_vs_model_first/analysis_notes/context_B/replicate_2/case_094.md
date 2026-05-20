Case: podmr_080_2026-05-17-105113

Sequence and readout roles:
- Active sequence: Rabimodulated.xml / Rabi-modulated pODMR frequency scan, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional m_S=+1 reference block is inactive despite do_adiabatic_inversion being true.
- The executed detections are therefore:
  1. After laser polarization, before the microwave pulse: m_S=0 / bright reference readout.
  2. After the Rabi-modulated microwave pulse: pODMR signal readout.
- Active pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns.
- mod_depth from the provided sequence XML / active variable table is 1.

Physical model calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant transition probability for a square pulse of duration t = 52 ns is
  P_1(Delta=0) = sin^2(pi * f_R * t).
- Numerically, P_1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S=0 to m_S=+1 contrast scale of 22%, an on-resonance pODMR signal should cause an approximate normalized signal reduction of
  0.22 * 0.996 = 0.219, i.e. about 22%.
- More generally, using the driven two-level model
  P_1(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * sqrt(f_R^2 + Delta^2) * t),
  the resonance should be a broad, strong feature on the scale of the 10 MHz Rabi frequency and 5 MHz scan spacing, not a sub-percent isolated fluctuation.

Observed quantitative comparison:
- I normalized the post-pulse signal readout by the pre-pulse reference readout at each scan point.
- The measured normalized contrast 1 - signal/reference has:
  mean = -0.00066, standard deviation = 0.0171, minimum = -0.0298, maximum = 0.0346.
- The largest observed signal reduction is 3.46%, far below the approximately 21.9% expected resonant reduction for the active 52 ns, mod_depth 1 pulse.
- The two stored averages differ strongly in baseline and appear consistent with tracking cadence effects rather than an independent confirmation of a stable resonance.

Decision:
No pODMR resonance is present. The data do not show the amplitude or line-shape expected from the active pulse sequence and setup contrast scale.
