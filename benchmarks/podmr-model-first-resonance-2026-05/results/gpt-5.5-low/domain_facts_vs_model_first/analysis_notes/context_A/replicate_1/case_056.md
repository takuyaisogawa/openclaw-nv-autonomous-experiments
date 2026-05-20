Case podmr_042_2026-05-16-225623.

The provided XML is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize and detect a "true 0 level reference", then because full_expt = 0 the optional 1-level reference block is skipped. The final active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Thus readout 1 is the optical 0-state/reference readout and readout 2 is the post-Rabi-pulse signal readout.

With the stated setup scale, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is near a pi pulse on resonance. If a pODMR resonance were present, I would expect a sizable localized reduction in readout 2 relative to readout 1, potentially on the order of the 22% contrast scale for a good pi pulse. The raw traces both show a slow downward drift across the sweep. The readout2/readout1 ratio varies irregularly, with local negative excursions near 3.83, 3.84, 3.86, and 3.875 GHz, but none is large or isolated enough to look like the expected resonance response. The apparent dip near 3.875 GHz is only about 4% relative and occurs on top of a simultaneous reference drop, while the stored two averages differ substantially, consistent with tracking/noise rather than a robust spectral feature.

Decision: resonance_absent.
