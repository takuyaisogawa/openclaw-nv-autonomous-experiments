Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The XML has full_expt = 0, so the optional +1 reference block is skipped. The active readouts are:
- readout 1: the detection immediately after optical polarization, a bright m_S = 0 reference.
- readout 2: the detection after a rabi_pulse_mod_wait_time call, the microwave-driven signal readout.

The pulse uses length_rabi_pulse = 52 ns and mod_depth = 1. With the provided setup scale of about 10 MHz Rabi frequency at mod_depth = 1, 52 ns is close to a pi pulse, so a resonant transition should produce near-maximal contrast in readout 2 while leaving readout 1 relatively unaffected.

The combined data show readout 1 staying comparatively flat around the high-30 raw-count range, while readout 2 has a pronounced localized dip near 3.875-3.880 GHz, reaching about 28-29 counts from an off-resonance level near 37-39 counts. This is roughly the expected contrast scale for the stated setup and appears in the microwave-driven readout role, not in the reference readout. The two stored averages differ in offset as expected for tracking cadence, but both are compatible with a signal-channel dip around the same frequency region.

Decision: a pODMR resonance is present.
