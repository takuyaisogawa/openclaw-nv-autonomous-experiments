Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz.

The XML sequence first polarizes and detects the bright m_S = 0 reference, then because full_expt = 0 skips the optional m_S = +1 reference block. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Thus readout 1 is the bright reference and readout 2 is the microwave-pulse result.

Using the provided setup facts, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. On resonance this should transfer population from m_S = 0 toward m_S = +1 and reduce fluorescence by roughly the setup contrast scale, about 22%.

The raw data show readout 1 staying mostly around 44 to 48 counts without a matching dip, while readout 2 has a clear localized drop near 3.875 GHz from a baseline near 44 to 46 counts down to about 35.9 counts. That is an approximately 19% to 21% reduction relative to the local bright level, very close to the expected contrast for a near-pi pulse. The same feature is visible in the per-average data, though the two stored averages should not be over-weighted because they may reflect tracking cadence.

Decision: a pODMR resonance is present.
