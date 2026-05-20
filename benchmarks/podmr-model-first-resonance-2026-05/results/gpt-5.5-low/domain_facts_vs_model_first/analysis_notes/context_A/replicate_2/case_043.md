Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The instructions first polarize and detect a true m_S = 0 reference, then skip the optional m_S = +1 reference because full_expt = 0, then apply a rabi_pulse_mod_wait_time pulse and detect the signal readout. Thus readout 1 is the polarized reference and readout 2 is the post-microwave signal readout, not two independent resonance traces or a full 0/1 calibration pair.

The relevant pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. With the given setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse on resonance. Since the setup contrast between m_S = 0 and m_S = +1 is about 22%, a resonance should produce a clear signal-readout drop relative to the reference, on the order of many raw-readout units for a baseline near 45.

The observed readout differences are small and irregular. Around the middle of the scan there are local negative differences, but they are only a few raw units at most, change sign across the scan, and are comparable to average-to-average/tracking variation. The stored averages should not be treated as strong independent repeatability, and the expected near-pi-pulse contrast is not present.

Decision: resonance absent.
