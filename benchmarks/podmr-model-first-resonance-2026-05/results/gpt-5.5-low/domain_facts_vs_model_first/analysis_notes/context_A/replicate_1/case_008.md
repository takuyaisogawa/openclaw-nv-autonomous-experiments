Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the optional +1 reference block is skipped even though do_adiabatic_inversion is true. The actual acquisition is:
1. polarize and detect the bright m_S = 0 reference readout,
2. apply rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1,
3. detect the post-pulse readout.

Thus readout 1 is the polarized m_S = 0 reference, and readout 2 is the microwave-pulse readout. With the stated setup, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. If a pODMR resonance were present, the post-pulse readout should show a sizable, frequency-localized reduction relative to the bright reference, on the order of the 22% contrast scale.

The combined data do not show that behavior. Readout 1 and readout 2 mostly overlap around 44-50 counts with irregular crossings. The largest apparent differences are only a few counts and are not coherent across the two stored averages; the per-average traces look dominated by tracking/drift and shot-to-shot scatter rather than a stable resonance feature. Stored averages are only two and may reflect tracking cadence, so they do not provide strong independent repeatability evidence.

Decision: resonance absent.
