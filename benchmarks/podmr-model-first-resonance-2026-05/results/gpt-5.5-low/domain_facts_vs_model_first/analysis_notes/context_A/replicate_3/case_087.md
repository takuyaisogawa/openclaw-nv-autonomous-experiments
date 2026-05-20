Active sequence: Rabimodulated.xml / Rabimodulated, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the sequence:
- readout 1 follows adj_polarize and detection, so it is the bright m_S = 0 reference.
- full_expt = 0 disables the explicit m_S = +1 reference block.
- readout 2 follows rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, ...) and detection, so it is the post-microwave-pulse signal.

Pulse settings before deciding:
- length_rabi_pulse = 52 ns.
- mod_depth = 1 in the provided sequence file and exported variable values.
- With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is close to a pi pulse. A true resonance should therefore move population strongly toward m_S = +1 and produce a clear fluorescence reduction approaching the setup contrast scale, about 22%, in the signal readout relative to the 0 reference.

Data assessment:
- The combined readouts have means of about 50.17 for readout 1 and 50.04 for readout 2, a mean difference of only -0.12 counts.
- The largest local readout-2 deficit is around 5% relative to readout 1, and similar positive excursions are also present.
- The per-average traces do not show a stable, frequency-localized dip in the post-pulse readout; the variations look comparable to tracking/noise and average-to-average scatter.

Decision: resonance_absent. The pulse should be strongly contrast-sensitive if it were on resonance, but the data do not show a coherent pODMR dip at the expected contrast scale.
