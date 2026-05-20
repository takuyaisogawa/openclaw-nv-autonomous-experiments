Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the optional 1-level reference block is skipped. The first detection is the polarized m_S = 0 reference after adj_polarize, and the second detection is the signal readout after the modulated Rabi pulse. The active Rabi pulse is length_rabi_pulse = 52 ns with mod_depth = 1 and switch_delay = 100 ns.

With the stated setup, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse on resonance. For a single NV with about 22% contrast between m_S = 0 and m_S = +1, a real resonance should appear as a localized, sizable negative contrast in the second readout relative to the first.

The combined raw traces mainly show common drift over the scan. The signal/reference ratio ranges only from about 0.955 to 1.037, with isolated dips near several frequencies and intervening positive excursions rather than a coherent ODMR line. The per-average traces have large offsets consistent with tracking cadence, so they do not provide strong independent confirmation. The observed differential structure is much smaller and less coherent than expected for the active near-pi pulse.

Decision: resonance_absent.
