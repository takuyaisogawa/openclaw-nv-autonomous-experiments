Case podmr_032_2026-05-14-161051

The active sequence is Rabimodulated with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction flow first polarizes and detects the true mS=0 reference, then skips the mS=+1 reference block because full_expt = 0, then applies the modulated Rabi pulse and detects the signal. Thus readout 1 is the polarized mS=0 reference and readout 2 is the microwave-pulse signal.

The provided sequence XML and exported variable values give mod_depth = 1 and length_rabi_pulse = 52 ns. At the stated setup scale, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. On resonance, the signal readout should therefore be substantially lower than the mS=0 reference, with a possible contrast approaching but not necessarily reaching the about 22 percent setup contrast.

The combined signal/reference contrast has its strongest local dip at 3.880 GHz: readout 1 is 35.65 and readout 2 is 29.31, about -17.8 percent. The neighboring point at 3.875 GHz is also negative at about -7.7 percent, while points immediately outside this region recover toward zero or positive contrast. Both stored averages show negative contrast around 3.875 to 3.880 GHz, although the per-average raw levels drift strongly in opposite directions, so I treat the per-average overlay mainly as tracking context rather than a strong independent repeatability test.

Decision: resonance_present. The localized readout-2 suppression near 3.880 GHz has the expected sign and approximate magnitude for a near-pi pODMR response under the active pulse settings.
