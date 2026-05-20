Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz. The active instructions first polarize and detect a true mS=0 bright reference, then wait, then apply rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then detect again. Because full_expt = 0, the optional mS=+1 reference block is inactive.

Readout role interpretation: readout 1 is the bright no-microwave reference after polarization. Readout 2 is the signal after the modulated microwave Rabi pulse.

Pulse settings used for the decision: length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, a 52 ns pulse is approximately a pi pulse, so an on-resonance microwave drive should produce a large drop in the post-pulse readout compared with the bright reference, up to the setup contrast scale of about 22%.

Observed data: readout 1 remains near 41-43 counts over the scan, while readout 2 shows a pronounced localized depression centered near 3.88 GHz, reaching about 33.9 counts. Relative to the simultaneous bright reference level near 41-42 counts, this is roughly a 18-20% reduction, close to the expected contrast scale for a single NV under a near-pi pulse. The dip also appears in both stored averages, although the averages should not be over-weighted because stored averages can reflect tracking cadence.

Decision: a pODMR resonance is present.
