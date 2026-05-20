Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The relevant pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. The setup fact gives about 10 MHz Rabi frequency at mod_depth = 1, so this is approximately a pi pulse on resonance.

Readout roles:

full_expt = 0, so the conditional "Acquire 1 level reference" block is skipped. The first detection follows optical polarization and is the bright m_S = 0 reference. The second detection follows the microwave pulse and is the signal readout. Therefore a resonance should appear as a dip in readout 2 relative to readout 1, with a possible scale up to the setup contrast of about 22%.

Data assessment:

Readout 1 stays fairly flat around 46 counts. Readout 2 is noisy but shows a coherent depression relative to readout 1 over part of the sweep, especially around 3.880 to 3.895 GHz, where it falls to roughly 44.75, 44.46, and 43.5 while readout 1 remains around 46 to 47. This is a few to several percent contrast, below the full 22% scale but plausible for a detuned or imperfect pODMR response with only two stored averages. The high point near 3.905 GHz argues that the trace is noisy, but the multi-point dip in the microwave-pulsed readout is more consistent with a real resonance than with no resonance.

Decision: resonance_present.
