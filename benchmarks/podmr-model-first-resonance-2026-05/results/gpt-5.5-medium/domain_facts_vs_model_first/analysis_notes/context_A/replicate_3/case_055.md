Active sequence: Rabimodulated.xml / Rabimodulated pODMR style scan with mw_freq varied from 3.825 to 3.925 GHz in 5 MHz steps.

The active XML has full_expt = 0, so the "Acquire 1 level reference" block is disabled. The two active detections are therefore:
- readout 1: after adj_polarize, a bright m_S = 0 reference for each scan point
- readout 2: after the modulated Rabi microwave pulse, the signal readout used to look for microwave-induced population transfer

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the provided setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is close to a pi pulse, so a real resonance should be capable of producing a large fluorescence reduction approaching the stated 22 percent contrast scale between m_S = 0 and m_S = +1, allowing for experimental imperfections.

The combined readout ratio shows only small excursions. The deepest combined readout2-vs-readout1 deficit is about -5.6 percent near 3.895 GHz, with other negative points around 3.88 to 3.90 GHz and 3.915 GHz, but there are also positive excursions of similar size elsewhere. The per-average traces are strongly offset by tracking cadence and do not provide a robust independent repeatability check; the apparent dip is not consistently reproduced as a clean, centered ODMR line across the stored averages.

Decision: resonance_absent. The observed changes are too small and irregular relative to the expected near-pi-pulse contrast for mod_depth = 1 and 52 ns.
