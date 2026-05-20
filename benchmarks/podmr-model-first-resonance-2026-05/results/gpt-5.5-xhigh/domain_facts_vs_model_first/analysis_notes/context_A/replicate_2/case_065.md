Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. With full_expt = 0, the optional m_S = +1 reference block is skipped, so the two active readouts are the polarized m_S = 0 reference after adj_polarize/detection and the signal readout after the microwave rabi_pulse_mod_wait_time followed by detection.

The provided sequence uses mod_depth = 1 and length_rabi_pulse = 52 ns, rounded at 250 MS/s to the same duration. Given the stated setup calibration, mod_depth = 1 gives about a 10 MHz Rabi frequency, so 52 ns is approximately a pi pulse. If the scanned microwave frequency hit a real pODMR resonance, the post-pulse readout should show a substantial drop relative to the m_S = 0 reference, on the order of the available contrast scale.

The normalized contrast (1 - readout2/readout1) is mostly small and sign-changing. The largest apparent dip is near 3.895 GHz at about 9%, while the overall points range from roughly -4% to +9% with a mean near 1%. That feature is well below the expected near-pi contrast and is not a clean, smooth resonance-scale depression across the scan. The stored averages show some alignment at the largest point, but those averages can reflect tracking cadence and do not provide a strong independent repeatability test.

Decision: resonance absent.
