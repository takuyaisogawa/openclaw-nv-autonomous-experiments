Active sequence and readout roles:

The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes with the laser and detects, so readout 1 is the bright m_S = 0 reference. full_expt is 0, so the optional independent m_S = +1 reference block is skipped. The sequence then applies rabi_pulse_mod_wait_time and detects again, so readout 2 is the microwave-pulse-affected signal.

Pulse parameters:

The exported variable values give length_rabi_pulse = 52 ns and mod_depth = 1. With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is about 0.52 Rabi cycles, close to a pi pulse. Therefore, an on-resonance transition should reduce the post-pulse readout relative to the polarized reference by a sizable fraction of the setup's roughly 22 percent contrast scale.

Data assessment:

The combined readouts show readout 2 dropping clearly below readout 1 near 3.900-3.905 GHz, reaching about 24.8 and 24.1 counts while readout 1 is about 26.5 and 27.6 counts. This gives the largest negative contrast feature in the sweep, roughly consistent in location and sign with a driven pODMR resonance for this sequence. The per-average traces should not be overinterpreted as independent repeatability tests because the stored averages can reflect tracking cadence, but the combined trace still shows a localized microwave-frequency-dependent dip in the signal readout.

Decision:

A pODMR resonance is present.
