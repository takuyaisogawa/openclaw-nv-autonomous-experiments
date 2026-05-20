Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The sequence first polarizes and detects the bright m_S = 0 reference. Because full_expt = 0, the optional m_S = +1 reference block is skipped. The second active readout is therefore the signal after rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1 from the provided sequence variables.

With the stated setup calibration, mod_depth = 1 gives an estimated Rabi frequency of about 10 MHz, so a 52 ns pulse is close to a pi pulse on resonance. A true resonance should therefore be capable of producing a fluorescence reduction on the order of the full setup contrast scale, about 22%, between the m_S = 0 reference readout and the post-microwave readout.

The combined data show a localized, frequency-dependent dip in readout 2 near 3.875-3.880 GHz: readout 2 falls to about 30.3-30.6 while readout 1 remains near 39-41. This is roughly a 22-26% reduction, matching the expected contrast scale for a near-pi pulse. Away from this region, readout 2 is much closer to the reference. The per-average overlay shows the same central depression in both stored averages, though stored averages should not be treated as a strong independent repeatability test because they may reflect tracking cadence.

Decision: a pODMR resonance is present.
