Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz. In the provided sequence XML, full_expt = 0, so the optional mS = +1 reference block is skipped. The first detection is the bright mS = 0 reference after optical polarization, and the second detection is the signal after the microwave Rabi-modulated pulse.

The active pulse uses length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is essentially a pi pulse on resonance. A true resonance should therefore cause a large post-pulse signal reduction approaching the setup contrast scale, about 22% between mS = 0 and mS = +1.

The combined data do not show that behavior. Both readouts share a slow downward drift across the scan, and the post-pulse/readout-reference differences are only a few percent with sign changes. The lowest normalized points are not a strong, isolated, repeatable contrast feature, and the two stored averages should not be treated as a strong independent repeatability test because they can reflect tracking cadence.

Decision: resonance_absent. The observed structure is consistent with drift/noise relative to the expected near-pi-pulse contrast, not a convincing pODMR resonance.
