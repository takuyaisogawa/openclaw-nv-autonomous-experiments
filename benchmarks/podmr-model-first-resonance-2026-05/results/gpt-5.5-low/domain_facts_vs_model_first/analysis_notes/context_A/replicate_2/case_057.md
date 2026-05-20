Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. In the provided sequence XML, full_expt is 0, so the optional Acquire 1 level reference block is inactive despite do_adiabatic_inversion being true. The executed readout roles are therefore: first detection after optical polarization as the true m_S = 0 reference, then a modulated microwave pulse followed by the second detection as the signal readout.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, this is approximately a pi pulse on resonance. Since the expected m_S = 0 to m_S = +1 contrast scale is about 22%, a resonance should create a clear, frequency-localized drop of the post-pulse signal relative to the 0-level reference.

The raw combined readouts do not show such a contrast-scale feature. The post-pulse readout is often comparable to or higher than the reference, and the variations are only a few counts on a roughly 47 count baseline, with the two stored averages showing substantial tracking-like offsets rather than repeatable resonance structure. The largest local differences are not consistent with a robust dip of the signal readout relative to the reference at the expected scale.

Decision: resonance absent.
