Case podmr_007_2026-05-11-064944

The saved scan reports SequenceName = Rabimodulated.xml and varies mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps. The executed variable table gives
length_rabi_pulse = 52 ns and mod_depth = 1. With the supplied setup facts, this
corresponds to roughly a 10 MHz Rabi frequency and therefore a near-pi pulse on
resonance.

The active instructions acquire a true m_S = 0 reference first:
adj_polarize -> detection -> wait. The optional m_S = +1 reference block is not
active because full_expt = 0, even though do_adiabatic_inversion is true. The
sequence then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) and
performs the second detection. Thus readout 1 is the bright 0-reference and
readout 2 is the post-microwave-pulse readout.

For this setup, a resonant near-pi pulse should create a localized reduction of
the post-pulse readout relative to the 0-reference, with possible contrast on
the order of the stated 22 percent scale if the pulse is effective. The observed
combined readouts fluctuate around about 30 to 34 counts, and readout 2 is not
consistently depressed at any frequency. The point-to-point differences change
sign several times, and the two stored averages show substantial tracking-scale
offsets and inconsistent structure rather than a reproducible resonance-shaped
dip. The largest excursions appear as isolated noise or drift, including a high
readout 2 endpoint, not as a coherent ODMR feature.

Decision: resonance_absent.
