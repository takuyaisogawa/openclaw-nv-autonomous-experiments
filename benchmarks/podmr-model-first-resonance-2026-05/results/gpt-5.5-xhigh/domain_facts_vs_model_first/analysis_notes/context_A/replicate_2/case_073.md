Active sequence: Rabimodulated.xml. The instruction block acquires a true bright m_S = 0 reference first, skips the m_S = +1 reference because full_expt = 0, then applies rabi_pulse_mod_wait_time and records the post-pulse signal. Thus readout 1 is the bright reference and readout 2 is the MW-pulse signal.

The provided sequence values give mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this is essentially a pi pulse on resonance. A real pODMR resonance in this sequence should therefore give a large drop of readout 2 relative to readout 1, on the order of the 22 percent m_S = 0 to m_S = +1 contrast scale if the resonance is sampled.

The combined data show the deepest normalized drop near 3.880 GHz, where readout2/readout1 is about 0.936, or roughly 6.4 percent contrast. There are also smaller apparent drops around neighboring and higher-frequency points, but the structure is not clean and the reference readout itself has comparable frequency-dependent excursions. The per-average overlays have large baseline shifts consistent with tracking cadence, so I do not treat them as a strong independent repeatability check.

Given the near-pi pulse condition, the observed weak and irregular readout-2 suppression is not strong enough to count as a pODMR resonance. I classify this case as resonance_absent.
