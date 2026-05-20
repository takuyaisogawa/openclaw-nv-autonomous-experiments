Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The active XML has full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. Readout 1 is the true 0-level reference acquired immediately after optical polarization and before the swept microwave pulse. Readout 2 is the signal readout acquired after rabi_pulse_mod_wait_time with the swept mw_freq.

Pulse settings used for the decision: mod_depth = 1 and length_rabi_pulse = 52 ns. With the provided setup fact of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is approximately a pi pulse, so a real resonance should create a large reduction in the post-pulse signal readout relative to the 0-level reference. The expected full contrast scale is about 22%.

The data show a pronounced dip only in readout 2 near 3.875-3.885 GHz, reaching about 33.9 counts while readout 1 remains near 41 counts. This is roughly a 17-18% drop relative to the local reference, close to the expected contrast scale for an on-resonance pi pulse. The per-average overlay shows the same readout-2 depression in both stored averages, though the stored averages should not be overinterpreted as independent repeatability because they may reflect tracking cadence.

Decision: pODMR resonance is present.
