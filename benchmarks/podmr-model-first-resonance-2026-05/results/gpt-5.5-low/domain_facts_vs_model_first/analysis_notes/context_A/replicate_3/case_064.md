Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence XML has mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi-pulse duration, so if the microwave frequency crosses a real NV resonance the post-pulse signal readout should show a clear ODMR/Rabi contrast feature on the order of the setup contrast scale, not just percent-level scatter.

Readout roles from the active instructions:
- First detection after optical polarization is the true m_S = 0 reference.
- The optional m_S = 1 reference block is inactive because full_expt = 0.
- The final detection after rabi_pulse_mod_wait_time is the frequency-dependent signal readout.

The combined readouts do not show a consistent resonance-shaped suppression of the signal readout relative to the m_S = 0 reference. The signal/reference difference changes sign and has isolated noisy excursions, including one deeper point near 3.91 GHz, but it is not a robust dip with neighboring support and is much smaller/less structured than expected for a near-pi pulse at full modulation depth. The per-average overlays mostly reflect tracking or baseline offsets rather than independent confirmation of a resonance.

Decision: resonance_absent.
