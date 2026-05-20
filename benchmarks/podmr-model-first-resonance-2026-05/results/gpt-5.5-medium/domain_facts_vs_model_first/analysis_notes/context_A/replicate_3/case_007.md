Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML instructions first polarize and detect a true m_S = 0 reference, then because full_expt = 0 the optional m_S = 1 reference block is skipped, then a modulated Rabi microwave pulse is applied before the second detection. Therefore readout 1 is the bright m_S = 0 reference and readout 2 is the post-pulse pODMR signal.

The relevant pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the provided setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse, so a real resonance should produce a strong reduction in readout 2 relative to readout 1 with a contrast scale up to roughly the stated 22%.

The combined data show readout 2 dropping from about 22 near the off-resonant points to a minimum near 16.98 around 3.88 GHz, while readout 1 stays near 20-21 in the same region. The readout-2 dip relative to the local bright reference is on the order of 20%, matching the expected contrast for a near-pi pulse. The per-average traces are influenced by tracking cadence, but both averages are consistent with a frequency-dependent depression of the signal channel around the same central region after accounting for their slow drifts.

Decision: a pODMR resonance is present.
