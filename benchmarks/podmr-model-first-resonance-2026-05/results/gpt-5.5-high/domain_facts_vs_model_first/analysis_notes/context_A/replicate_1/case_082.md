Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The sequence first polarizes and detects the bright m_S = 0 reference. Because full_expt = 0, the optional +1 reference block is skipped even though it is present in the XML. The active experimental pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection readout. Thus readout 1 is the 0-level reference/tracking readout and readout 2 is the post-Rabi-pulse signal readout.

At mod_depth = 1 the stated setup Rabi frequency is about 10 MHz, so a 52 ns pulse is effectively a pi pulse on resonance. With an m_S = 0 to m_S = +1 contrast scale of about 22%, a true resonance should give a clear reduction of the post-pulse signal readout relative to the 0-reference readout at the resonant frequency.

The measured readouts do not show such a contrast-scale feature. Readout 2 minus readout 1 fluctuates around zero with excursions of roughly a few percent, and both readouts share the same broad downward drift at the high-frequency end. The per-average traces are only two averages and are consistent with tracking cadence/common-mode variation rather than a reproducible resonance dip. The largest normalized suppressions are far smaller than the expected near-pi-pulse contrast, and the high-frequency rolloff appears in both readout channels.

Decision: resonance_absent.
