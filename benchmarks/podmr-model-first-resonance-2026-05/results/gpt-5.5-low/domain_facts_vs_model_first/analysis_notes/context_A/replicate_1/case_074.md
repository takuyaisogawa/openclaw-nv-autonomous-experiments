Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The instruction flow first polarizes and detects the bright m_S = 0 reference. Because full_expt = 0, the optional m_S = +1 reference block is skipped. The active measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Thus readout 1 is the bright-state reference and readout 2 is the post-microwave-pulse signal.

With the given setup facts, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. If the scan crossed a real pODMR resonance for this single NV, readout 2 should show a substantial suppression relative to readout 1, on the order of the 22% contrast scale at resonance. Instead, both readouts fluctuate around roughly 50 counts, the readout-2/readout-1 differences are only a few percent and change sign/shape irregularly, and the two stored averages do not provide a stable reproducible dip. Stored averages are also likely tied to tracking cadence, so they should not be treated as strong independent confirmation.

Decision: no convincing pODMR resonance is present in this scan.
