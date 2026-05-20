Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The sequence first polarizes and detects the bright m_S = 0 reference. Because full_expt = 0, the optional m_S = +1 reference block is skipped. The active pODMR readout is the later detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, ...). Thus readout 1 is the bright reference and readout 2 is the microwave-pulse signal.

From the provided sequence XML, mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, this is approximately a pi pulse. If a resonance were present, the post-pulse signal should show a substantial reduction relative to the bright reference, on the order of the setup contrast scale of about 22%.

The combined readouts instead track each other closely around 50 counts. The largest negative readout2-minus-readout1 excursions are about -2.5 counts and -2.4 counts, roughly 5% of the signal level, and they appear as isolated points rather than a coherent resonance feature. Stored averages are only two and mainly reflect tracking cadence, so they do not provide a strong independent repeatability test. Overall the observed contrast is far below the expected near-pi-pulse resonance response and is not shaped like a reliable pODMR dip.

Decision: resonance_absent.
