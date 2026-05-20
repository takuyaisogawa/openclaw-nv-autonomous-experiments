Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The saved export contains the operative sequence values. The relevant pulse is rabi_pulse_mod_wait_time after the initial polarized reference detection, with length_rabi_pulse = 52 ns and mod_depth = 1. full_expt = 0, so the optional intermediate m_S = 1 reference block is skipped. Therefore readout 1 is the post-polarization m_S = 0 reference, and readout 2 is the signal after the microwave pulse.

At mod_depth = 1 the stated setup Rabi frequency is about 10 MHz, so a 52 ns pulse is close to a pi pulse. On resonance, the signal readout should be reduced relative to the polarized reference, with a possible contrast scale up to roughly 22% but likely smaller in this raw count view.

The combined data show the clearest frequency-localized effect at 3.880 GHz: readout 2 falls to about 45.79 while readout 1 remains near 49.52, a difference of about 3.73 counts or roughly 7.5% of the reference level. This dip is also present in both stored averages for readout 2 at the same scan point, while the readout 1 values are not equivalently depressed. Other fluctuations exist, and the two stored averages mainly indicate tracking cadence rather than a strong repeatability test, but the 3.880 GHz readout-2-only dip matches the expected role and pulse behavior.

Decision: pODMR resonance present.
