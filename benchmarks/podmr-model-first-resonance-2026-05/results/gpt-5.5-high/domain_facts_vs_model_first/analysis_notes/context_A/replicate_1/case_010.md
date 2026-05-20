Active sequence: Rabimodulated.xml pODMR, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The sequence first polarizes and detects a true m_S = 0 reference, then applies rabi_pulse_mod_wait_time using length_rabi_pulse and detects the post-pulse signal. Because full_expt = 0, the conditional "1 level reference" block is skipped; the two stored readouts should therefore be interpreted as the pre-microwave bright reference and the post-Rabi signal, not independent 0 and 1 references. The active pulse duration is 52 ns. The provided sequence XML and exported variable values give mod_depth = 1.

At mod_depth = 1, the supplied setup facts imply a Rabi frequency of about 10 MHz, so a 52 ns pulse is close to a pi pulse. If the swept microwave frequency crossed a real driven resonance, the post-pulse signal should show a coherent dip relative to the m_S = 0 reference, with a possible contrast scale approaching the stated 22% setup contrast.

The combined raw readouts do not show that behavior. The signal/reference ratio fluctuates from roughly 0.91 to 1.10, with the largest apparent drop near 3.855 GHz being only about 9% and isolated. Other negative differences occur at scattered frequencies without a consistent resonance line shape, and the per-average traces mainly show strong drift/tracking structure rather than repeatable spectral contrast. Since stored averages can reflect tracking cadence, I do not treat the two averages as an independent confirmation.

Decision: resonance absent.
