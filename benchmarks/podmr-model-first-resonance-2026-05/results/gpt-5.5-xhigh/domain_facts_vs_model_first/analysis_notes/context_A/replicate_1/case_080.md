The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz. The sequence first acquires a true mS = 0 bright reference after optical polarization, then skips the optional mS = +1 reference because full_expt = 0, then applies a modulated Rabi microwave pulse and acquires the frequency-dependent readout. Thus readout 1 is the bright reference and readout 2 is the post-pulse pODMR signal.

Using the provided sequence XML and variable values, mod_depth is 1 and length_rabi_pulse is 52 ns. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is approximately a pi pulse. If a pODMR resonance were present, the post-pulse readout should be strongly suppressed relative to the bright reference, on the order of the 22% mS = 0 to mS = +1 contrast scale.

The combined data do not show that behavior. The lowest readout2/readout1 ratio is about 0.936, only a roughly 6% suppression, and the absolute post-pulse readout is mostly flat to drifting rather than showing a clear, isolated resonance dip. The apparent negative excursions are comparable to baseline/tracking variation between the two stored averages, and stored averages here are not a strong independent repeatability test.

Decision: resonance absent.
