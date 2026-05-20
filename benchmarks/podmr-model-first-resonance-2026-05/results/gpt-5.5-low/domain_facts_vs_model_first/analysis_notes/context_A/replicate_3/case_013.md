Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz.

The executed readout roles follow from full_expt = 0. The sequence first polarizes and detects the bright m_S = 0 reference, so readout 1 is the no-Rabi bright reference. The optional m_S = +1 reference block is skipped. The active measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection, so readout 2 is the post-microwave pulse signal.

Given the provided setup facts, mod_depth = 1 implies about 10 MHz Rabi frequency, with a Rabi period near 100 ns. A 52 ns pulse is therefore close to a pi pulse on resonance, so a real resonance should strongly transfer population out of m_S = 0 and reduce fluorescence by a fraction comparable to the stated 22% contrast scale.

The combined raw readouts show a pronounced readout 2 dip around 3.875 to 3.880 GHz, falling to about 29-30 counts while nearby off-resonant values are roughly 34-36 counts. Readout 1 does not show the same dip; it remains around the low-to-mid 30s and is actually high near 3.880 GHz. The dip magnitude is about 15-20%, consistent with a near-pi pulse and the expected contrast scale. The two stored averages have strong slow drift/tracking structure, so they are not a clean independent repeatability test, but the combined role-specific contrast is physically consistent with pODMR.

Decision: resonance_present.
