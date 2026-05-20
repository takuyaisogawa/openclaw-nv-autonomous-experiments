Sequence inspection:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S=+1 reference block is skipped.
- Readout 1 role: true m_S=0 reference after optical polarization and detection.
- Readout 2 role: signal after a microwave rabi_pulse_mod_wait_time pulse and detection.
- mod_depth = 1 from the provided sequence XML / variable values.
- Rabi pulse duration = 52 ns after sample-rate rounding at 250 MS/s.

Physics expectation:
At mod_depth = 1 the setup Rabi frequency is about 10 MHz, so a 52 ns pulse is close to a pi pulse. If the microwave frequency hits a real pODMR resonance, the post-pulse signal readout should be substantially lower than the m_S=0 reference readout, with contrast on the order of the stated 22% scale.

Observed data:
The combined readout means are nearly equal (readout 1 about 45.46, readout 2 about 45.42). Pointwise signal/reference differences fluctuate in both signs, with the largest negative ratio only about -4.5% at the high-frequency edge. Other negative excursions of similar size appear without a stable resonance shape, and positive excursions are also present. The per-average traces are noisy and should not be treated as a strong independent repeatability check because stored averages can reflect tracking cadence.

Decision:
The data do not show the expected large, coherent post-pulse fluorescence reduction for a near-pi pulse. I classify this case as resonance_absent.
