Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence has mod_depth = 1 and length_rabi_pulse = 52 ns. The instructions first polarize and detect the bright mS = 0 reference. The conditional mS = +1 reference block is disabled because full_expt = 0. The active microwave-dependent readout is therefore the later detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth). Readout 1 is the mS = 0 reference/tracking readout, and readout 2 is the post-pulse signal readout.

Given the stated setup, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. On resonance this should transfer a substantial fraction from mS = 0 to mS = +1 and produce a clear signal decrease on the scale of the available 22% contrast.

The raw readouts mostly share a slow upward drift. Signal/reference ratios have only small isolated deficits, with the deepest around 0.95 and no broad, repeatable ODMR-like dip across neighboring frequency points. Stored averages are only two and can reflect tracking cadence, so the apparent small dips are not a strong independent repeatability test. The observed contrast is far below the expected near-pi-pulse response and is not shaped like a convincing resonance.

Decision: resonance_absent.
