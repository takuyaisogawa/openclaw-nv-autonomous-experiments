<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_095

Sequence identification:
- SequenceName: Rabimodulated.xml.
- Active pulse sequence: polarize, detect bright reference, wait, apply rabi_pulse_mod_wait_time, detect post-pulse signal, final wait.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive despite do_adiabatic_inversion being true. There is no independent dark-state reference in the active sequence.
- Readout roles: readout 1 is the true m_S = 0 bright reference acquired immediately after optical polarization; readout 2 is the measurement after the Rabi-modulated microwave pulse.
- Active pulse settings from the provided sequence XML/export values: length_rabi_pulse = 52 ns, mod_depth = 1, mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative model:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1, the resonant transition probability for a rectangular pulse is
  P = sin^2(pi * f_Rabi * tau).
- With f_Rabi = 10 MHz and tau = 52 ns:
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, an on-resonance post-pulse readout should be approximately
  R_signal / R_bright = 1 - 0.22 * 0.996 = 0.7809.
- At the observed mean bright-reference readout of 47.34 counts, the expected resonant drop is about
  47.34 * (1 - 0.7809) = 10.37 counts.

Observed data check:
- Mean readout 1 = 47.34 counts.
- Mean readout 2 = 47.10 counts.
- Mean difference readout2 - readout1 = -0.24 counts, with standard deviation 1.30 counts across scan points.
- The minimum observed readout2/readout1 ratio is 0.9548 at 3.905 GHz, corresponding to only a 4.5% drop.
- No scan point approaches the expected on-resonance ratio near 0.781 or the expected roughly 10-count drop. The observed point-to-point structure is consistent with small drift/noise and the stored averages should not be treated as a strong repeatability test because they can reflect tracking cadence.

Decision:
The active sequence would produce a large post-pulse PL decrease at resonance for these pulse settings. The measured post-pulse readout remains close to the bright reference throughout the scan and is far from the quantitative resonant expectation. I therefore decide that a pODMR resonance is absent.
