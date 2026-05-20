Active sequence: Rabimodulated.xml / 1DExp-seq-Rabimodulated-vary-mw_freq, scanning mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence XML has full_expt = 0, so the optional 1-level reference block is disabled. The active readouts are:
- readout 1: the true m_S = 0 reference after optical polarization and before the microwave pulse.
- readout 2: the signal readout after the modulated Rabi pulse.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s. At the 250 MHz sample rate this is exactly 13 samples, so the rounded pulse duration remains 52 ns. The active mod_depth is 1. With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is close to a pi pulse. On resonance, the second readout should therefore be substantially reduced relative to the m_S = 0 reference; with a 22% m_S = 0 to m_S = +1 contrast scale and raw levels near 50, an ideal strong resonance would be a much larger drop than the observed few-count scatter.

The combined readout2 - readout1 differences have mean about -0.05 counts, minimum about -2.85 counts at 3.890 GHz, and maximum about +3.13 counts at 3.915 GHz. The largest negative excursion is only about -5.4% of the reference level and is comparable to positive excursions and point-to-point scatter. The stored per-average traces also show tracking-like shifts rather than a consistent frequency-localized dark feature. Given the strong active pulse expected from mod_depth = 1 and 52 ns duration, the data do not show a convincing pODMR resonance.

Decision: resonance_absent.
