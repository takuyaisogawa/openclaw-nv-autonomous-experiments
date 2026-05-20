Sequence/readout context:

The provided sequence is Rabimodulated.xml. The active scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the active instructions, the first detection follows laser polarization and is the true m_S=0 reference. The full_expt variable is 0, so the optional m_S=1 reference block is skipped. The second active detection follows rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, so it is the pulsed ODMR signal readout after the microwave pulse.

Pulse-scale check:

With the supplied setup estimate of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is close to a pi pulse on resonance. The expected full m_S=0 to m_S=+1 readout scale is about 22%, so a clear resonance should appear as a lower post-pulse signal relative to the m_S=0 reference, though it need not reach the full contrast.

Data assessment:

Using readout 1 as the m_S=0 reference and readout 2 as the post-pulse signal, the combined signal/reference contrast has its strongest local depression near 3.875 GHz: readout 1 is 42.12 and readout 2 is 38.25, about 9.2% lower. The neighboring 3.870 GHz point is also lower by about 6.5%, and the signal mostly recovers by 3.880 GHz. There is another lower point near 3.830 GHz, but the most sequence-consistent feature is the 3.870-3.875 GHz dip. The stored averages differ in baseline and drift, consistent with tracking cadence, but both show positive reference-minus-signal contrast around 3.875 GHz.

Decision:

A pODMR resonance is present, with moderate confidence from a sub-full-contrast but sequence-consistent signal dip near 3.875 GHz.
