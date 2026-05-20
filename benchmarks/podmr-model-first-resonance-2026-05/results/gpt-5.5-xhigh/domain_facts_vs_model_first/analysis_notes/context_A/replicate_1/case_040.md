The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. The XML has full_expt = 0, so the optional m_S = +1 reference block is skipped. The executed readouts are therefore:

1. Initial adj_polarize followed by detection: true m_S = 0 bright reference.
2. A rabi_pulse_mod_wait_time pulse followed by detection: signal after the microwave pulse.

The pulse used for the signal readout has length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns, and mod_depth = 1. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is close to a pi pulse on resonance. If the swept microwave frequency crosses a real transition, the second readout should approach the m_S = +1 level and show a large fluorescence decrease relative to the first readout, on the order of the setup contrast scale of about 22%.

The combined readouts stay near the same level: mean readout 1 is about 49.61 and mean readout 2 is about 49.58. The largest pointwise drop of readout 2 relative to readout 1 is about 5.9%, and the trace also contains positive excursions of similar size. The per-average traces show broad offset changes consistent with tracking cadence rather than a reproducible resonance feature. There is no narrow or physically large post-pulse fluorescence dip compatible with an on-resonance near-pi pulse.

Decision: resonance_absent.
