Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction block first performs adj_polarize followed by detection, which is the true mS = 0 reference readout. Because full_expt = 0, the optional mS = 1 reference block is skipped. The next active microwave operation is rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth, followed by the second detection. Thus readout 1 is the bright polarized reference and readout 2 is the post-Rabi-pulse signal.

The provided sequence values give length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration, the Rabi frequency is about 10 MHz at mod_depth = 1, so the pulse is approximately a pi pulse. If the swept microwave frequency passed through a real pODMR resonance, the post-pulse signal should be substantially darker than the reference, on the order of the setup contrast scale of about 22% for a well-driven transition.

The combined readouts instead show only small and inconsistent readout2-readout1 deviations. There are negative excursions near 3.845-3.850 GHz and again near the high-frequency edge around 3.910-3.925 GHz, but their combined size is only about 3-5%, and the trace also contains positive excursions of comparable or larger size, including a strong positive point near 3.855 GHz. The two stored averages do not provide a strong independent repeatability test and show tracking/noise-like variation rather than a stable resonance-shaped dark feature.

Decision: the data do not show a convincing pODMR resonance under the active near-pi pulse conditions.
