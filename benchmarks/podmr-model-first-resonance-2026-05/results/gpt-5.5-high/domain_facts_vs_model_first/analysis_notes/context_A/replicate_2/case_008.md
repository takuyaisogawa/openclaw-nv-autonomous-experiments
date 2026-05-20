Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The active path has full_expt = 0. The sequence first polarizes and detects without a microwave pulse, giving a bright m_S = 0 reference readout. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by a second detection readout, so readout 2 is the post-microwave signal. The skipped full_expt block means no active m_S = +1 reference is acquired.

Using the provided setup facts, mod_depth = 1 gives about a 10 MHz Rabi frequency, so the 52 ns pulse is close to a pi pulse. If the swept microwave frequency hits the NV transition, the post-pulse readout should show a clear localized drop relative to the bright reference, with a scale approaching the stated 22% m_S = 0 to m_S = +1 contrast.

The combined data do not show that behavior. Readout 2 differs from readout 1 by only a few percent at the largest apparent deficits, with isolated dips around several different frequencies rather than a single convincing resonance feature. The per-average traces also show substantial tracking-like drift and point-to-point variation; the repeated dips are far below the expected near-pi-pulse contrast scale. Stored averages are not a strong independent repeatability test here, but the magnitude and localization are still not persuasive.

Decision: resonance absent.
