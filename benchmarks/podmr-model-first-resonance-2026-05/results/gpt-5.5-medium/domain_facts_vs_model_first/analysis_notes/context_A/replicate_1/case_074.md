<!-- Model-generated analysis note. Not a ground-truth label. -->

Active sequence: Rabimodulated pODMR scan varying mw_freq from 3.825 GHz to 3.925 GHz.

Readout roles: because full_expt = 0, the optional m_S = +1 reference block is skipped. Each point contains the initial post-polarization detection as the bright/0-level reference, followed by a rabi_pulse_mod_wait_time pulse and then the signal detection. Thus readout 1 is the 0/reference readout and readout 2 is the microwave-pulsed signal readout.

Pulse settings from the provided sequence XML: length_rabi_pulse = 52 ns and mod_depth = 1. With the supplied setup facts, mod_depth = 1 corresponds to about a 10 MHz Rabi frequency, so a 52 ns pulse is near a pi pulse on resonance. A real resonance should therefore make the pulsed readout substantially darker than the reference, on the order of the known 22% contrast scale for this setup.

Observed data: the two combined raw readouts fluctuate around about 50 counts and cross each other repeatedly. The pulsed readout is not consistently suppressed near any scan frequency; several apparent local differences are isolated and comparable to the scatter between the two stored averages. The stored averages are only two and may reflect tracking cadence, so they do not provide strong independent repeatability.

Decision: resonance_absent. The expected near-pi-pulse contrast at this pulse duration and modulation depth is not present in the raw readouts.
