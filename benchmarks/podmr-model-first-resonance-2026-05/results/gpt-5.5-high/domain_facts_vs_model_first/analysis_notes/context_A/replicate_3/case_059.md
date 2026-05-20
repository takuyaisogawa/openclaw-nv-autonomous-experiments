Sequence interpretation:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects a true m_S = 0 fluorescence reference. Because full_expt = 0, the optional m_S = +1 reference branch is not active. It then applies one modulated Rabi microwave pulse and detects the post-pulse signal readout.

Relevant pulse settings from the provided sequence are mod_depth = 1 and length_rabi_pulse = 52 ns. With the given setup estimate of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is approximately a pi pulse on resonance, so a real pODMR resonance should produce a sizable fluorescence reduction in the post-pulse readout relative to the m_S = 0 reference, on a scale tied to the stated 22% contrast.

Data assessment:

The two combined raw readouts remain close together across the sweep, with point-to-point changes of only a few raw units around a mean near 48-50. There is no consistent, frequency-localized contrast feature where the post-pulse readout drops strongly relative to the reference. The apparent fluctuations are comparable to the per-average spread, and the stored two averages mainly reflect tracking cadence rather than independent repeatability. The expected near-pi-pulse contrast signature is absent.

Decision: resonance_absent.
