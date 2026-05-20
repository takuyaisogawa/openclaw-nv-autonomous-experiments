Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. In the provided sequence XML, full_expt is 0, so the optional m_S=1 reference block is inactive. The two active detections are therefore: readout 1 immediately after optical polarization, serving as the bright m_S=0 reference; and readout 2 after the microwave rabi_pulse_mod_wait_time, serving as the pODMR signal readout.

Pulse settings before decision: mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup Rabi frequency of about 10 MHz at mod_depth 1, a 52 ns pulse is approximately a pi pulse, so a true resonance should be capable of producing close to the full m_S=0 to m_S=+1 contrast scale of about 22%.

The combined data show a localized signal drop in readout 2 around 3.875-3.880 GHz while readout 1 remains in its normal tracking range. The normalized readout2-vs-readout1 contrast reaches about -24% at 3.875 GHz and about -29% at 3.880 GHz, which is at or above the expected full-contrast scale for an on-resonant pi pulse. Neighboring points recover on both sides, so this is not just a monotonic scan drift. The two stored averages both contain a dip in the same frequency region, but I do not treat that as a strong independent repeatability test because stored averages often reflect tracking cadence.

Decision: a pODMR resonance is present.
