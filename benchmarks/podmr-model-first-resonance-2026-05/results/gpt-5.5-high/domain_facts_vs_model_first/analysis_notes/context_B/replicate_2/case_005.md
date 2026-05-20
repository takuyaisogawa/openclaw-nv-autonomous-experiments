Case: podmr_008_2026-05-11-131831

Sequence and readout roles:
- The active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence has full_expt = 0, so the optional "1 level reference" block is skipped.
- The two active detections are therefore:
  1. readout 1: after adj_polarize, before the microwave pulse; this is the m_S = 0 reference.
  2. readout 2: after the Rabi-modulated microwave pulse; this is the pODMR signal readout.
- The microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Physical signal model:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1, the relevant pulse is nearly a pi pulse.
- For a square resonant pulse, the transition probability is
  P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * sqrt(f_R^2 + Delta^2) * tau),
  with f_R = 10 MHz and tau = 52 ns.
- On resonance this gives P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated 22% contrast between m_S = 0 and m_S = +1, the expected on-resonance signal ratio is
  readout2/readout1 = 1 - 0.22 * 0.996 = 0.781.
- For a 20-count reference, this is an expected drop of about 4.38 counts.
- Even if the resonance center is halfway between scan points, the detuning is 2.5 MHz and the model gives P = 0.929, ratio = 0.796, and an expected drop of about 4.09 counts.
- At 5 MHz detuning the model still gives P = 0.749, ratio = 0.835, and an expected drop of about 3.29 counts. Thus a real resonance should produce a broad, multi-point dip at this 5 MHz scan spacing.

Observed readout comparison:
- Combined mean readout1 = 20.079 and mean readout2 = 19.791.
- Mean readout2 - readout1 = -0.288 counts, corresponding to a mean ratio of 0.988.
- The observed ratios readout2/readout1 range from 0.881 to 1.061.
- The largest fractional drop is 0.119 at 3.840 GHz, with other local drops near 3.865 GHz and 3.920 GHz, but these are isolated/noisy and do not show the expected neighboring-point structure.
- A least-squares scan of the explicit Rabi response model against fractional drop, allowing a constant offset and positive resonance amplitude, gives best-fit amplitude about 0.085 contrast-equivalent, far below the expected 0.22 for the stated setup and pulse. The fit is weak and is pulled to the scan edge rather than giving a clear resonance.
- The stored averages show large tracking/drift structure, so they are not treated as independent confirmations. Pairwise normalization by readout1 still does not reveal the expected near-0.78 ratio feature.

Decision:
The active pulse should make a pODMR resonance large and easy to see if present. The data show only small, inconsistent fluctuations relative to the expected model signal, so I classify this case as resonance_absent.
