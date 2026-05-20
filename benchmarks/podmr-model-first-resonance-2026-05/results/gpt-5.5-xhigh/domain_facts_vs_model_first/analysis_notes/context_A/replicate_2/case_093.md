The active sequence is Rabimodulated.xml. The XML sets full_expt = 0, so the optional m_s = +1 reference block is skipped. The acquired readouts are therefore:

1. readout 1: after optical polarization and detection, a bright m_s = 0 reference.
2. readout 2: after a modulated microwave Rabi pulse and detection, the pODMR signal readout.

The relevant pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns. The provided sequence XML sets mod_depth = 1. With the stated setup calibration, this corresponds to about a 10 MHz Rabi frequency, so a 52 ns pulse is near a pi pulse. On resonance, a single NV should show a clear transfer out of m_s = 0 in readout 2 relative to the bright readout 1 reference, with contrast on the order of the stated 22% scale if the resonance is well driven.

The combined readouts do not show that behavior. The mean readouts are almost identical, about 50.72 for readout 1 and 50.78 for readout 2. The signal-minus-reference excursions run only from about -2.10 to +2.31 counts, and the normalized signal/reference range is about 0.961 to 1.048. These fluctuations are much smaller than the expected full contrast scale and are not organized as a coherent frequency-localized dip. The per-average overlay mainly shows a tracking-like offset between stored averages rather than an independently repeated resonance feature.

Decision: resonance absent.
