Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence roles from inputs/sequence.xml:
- readout 1 is acquired immediately after adj_polarize, so it is the bright m_S = 0 reference.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- readout 2 is acquired after rabi_pulse_mod_wait_time with the swept microwave frequency, so it is the pODMR signal readout.
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- mod_depth = 1.

Decision reasoning:
At mod_depth = 1 the stated setup Rabi frequency is about 10 MHz, so a 52 ns pulse is approximately a pi pulse. If the swept microwave frequency hit the single-NV resonance, the signal readout should show a clear dip relative to the bright reference, with a scale plausibly approaching the stated 22% m_S = 0 to m_S = +1 contrast.

The combined readouts do not show a resonance-sized normalized dip. The strongest signal/reference depression is only about 4.9% near 3.91 GHz, with similarly large nonresonant excursions elsewhere, including the signal being brighter than the reference around 3.855 GHz. The raw traces also show tracking-scale baseline motion in both readouts. The per-average traces are not a strong independent repeatability test, but they reinforce that the high-frequency depression is not a clean, stable pODMR line.

Conclusion: resonance_absent.
