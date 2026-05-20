Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executed sequence has full_expt = 0, so the optional m_S = +1 reference block is skipped. The first detection after optical polarization is therefore the bright m_S = 0 reference/readout 1. The second detection follows a modulated microwave Rabi pulse and is the signal/readout 2.

Pulse settings from the provided sequence XML/raw export values: length_rabi_pulse = 52 ns, mod_depth = 1, mw_ampl = -5 dBm, IQ frequency = 50 MHz. With the stated setup calibration, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. On resonance, a strong transfer from m_S = 0 toward m_S = +1 should reduce fluorescence by roughly the setup contrast scale, about 22%.

The data show readout 1 staying near 43-46 counts without a matching sharp loss, while readout 2 drops from the low 40s to about 34 counts around 3.875-3.880 GHz. That is roughly a 20-22% reduction relative to the local bright level and is localized in microwave frequency. The same feature appears in the per-average traces, though the two stored averages should not be over-weighted because they may reflect tracking cadence.

Decision: a pODMR resonance is present.
