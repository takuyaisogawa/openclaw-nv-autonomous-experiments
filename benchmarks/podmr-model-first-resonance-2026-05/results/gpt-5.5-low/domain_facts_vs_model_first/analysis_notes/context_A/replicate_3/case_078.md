Sequence and roles:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional m_S=+1 reference block is skipped.
- Readout 1 is the true m_S=0 bright reference immediately after optical polarization.
- Readout 2 is the measurement after the microwave rabi_pulse_mod_wait_time block.

Pulse settings:
- mod_depth is 1.
- length_rabi_pulse is 52 ns, rounded on a 250 MHz sample clock.
- With the provided setup fact of about 10 MHz Rabi frequency at mod_depth=1, a 52 ns pulse is approximately a pi pulse. If the microwave frequency were resonant, readout 2 should show a substantial fluorescence decrease relative to the readout 1 bright reference, on the order of the available contrast scale.

Data assessment:
The two combined raw readouts are noisy and track each other only weakly. Readout 2 does not show a clear localized dip relative to readout 1 over the scanned microwave frequency range. Instead, the largest feature is a positive readout 2 excursion near 3.915 GHz, opposite the expected sign for transfer from m_S=0 to m_S=+1. The per-average overlay indicates that point-to-point variation and tracking/cadence effects are comparable to the apparent features, and the stored two averages are not a strong independent repeatability test.

Decision:
Given the pulse should be strong enough to produce an obvious contrast feature if resonant, but the measured post-pulse readout lacks a consistent negative contrast feature relative to the m_S=0 reference, I classify this case as resonance_absent.
