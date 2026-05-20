Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. The XML has full_expt = 0, so the optional m_S = +1 reference block is skipped.

Readout roles:
- Readout 1 follows adj_polarize and detection only, so it is the polarized m_S = 0 bright/reference readout.
- Readout 2 follows rabi_pulse_mod_wait_time and then detection, so it is the microwave-pulse signal readout.

Pulse settings before deciding:
- mod_depth = 1
- length_rabi_pulse = 52 ns
- With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, this is approximately a pi pulse.

Decision reasoning:
For a near-pi pulse on resonance, the post-pulse readout should show a frequency-localized drop relative to the m_S = 0 reference, with a scale approaching the stated 22% m_S = 0 to m_S = +1 contrast. The combined readout differences are much smaller, mostly scattered at the few-percent level, and the larger positive points occur at several separated scan values rather than forming one coherent resonance feature. The stored averages differ substantially and are not strong independent repeatability evidence because they can reflect tracking cadence. I therefore do not see a clear pODMR resonance in this case.
