Sequence and readout interpretation:

The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes the NV and immediately performs a detection, giving the true m_S = 0 bright-state reference. Because full_expt = 0, the optional m_S = +1 reference acquisition block is skipped. The only microwave manipulation in the active experiment is then rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Thus readout 1 is the pre-pulse bright reference and readout 2 is the post-Rabi-pulse readout.

Pulse expectation:

Using the supplied domain facts, mod_depth = 1 gives an approximately 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse on resonance. With a setup m_S = 0 to m_S = +1 contrast scale of about 22%, a real on-resonance response should produce a clear local drop of the post-pulse readout relative to the bright reference, on the order of many raw readout units for counts near 50 if the pulse is effective.

Observed data:

Both readouts mainly show a slow upward drift across the frequency sweep, consistent with tracking or brightness drift. The post-pulse readout is usually only slightly below the bright reference, with differences typically around 0 to 3 raw units and several points where it is equal to or above the reference. The deepest deficits are small relative to the expected near-pi-pulse contrast and do not form a clean, reproducible resonance feature across the two stored averages. The per-average traces show substantial point-to-point variation, and the stored averages likely reflect tracking cadence rather than a robust independent repeatability check.

Decision:

Given the near-pi pulse condition, the expected resonance contrast should be much larger and more structured than the observed weak, inconsistent readout separation. I therefore classify this case as resonance absent.
