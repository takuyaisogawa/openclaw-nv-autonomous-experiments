Sequence inspection:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional +1 reference block is skipped.
- Readout 1 is the first detection after adj_polarize, serving as the true m_S = 0 reference.
- Readout 2 is the detection after rabi_pulse_mod_wait_time, serving as the post-microwave pulse signal.
- length_rabi_pulse is 52 ns after rounding at 250 MHz sample rate.
- mod_depth is 1 from the provided sequence/variable values.

Decision reasoning:

At mod_depth = 1, the setup Rabi frequency is about 10 MHz, so a 52 ns pulse is close to a pi pulse. If a pODMR resonance were present in this scan, readout 2 should drop substantially relative to the m_S = 0 reference readout, with an expected contrast scale approaching the setup's approximately 22% m_S = 0 to m_S = +1 difference.

The combined data do not show that behavior. The largest negative readout-2 minus readout-1 excursions are only about 5-6%, while other nearby features are positive, including roughly 8-9% positive excursions. The per-average overlay is dominated by baseline/tracking offsets rather than a stable resonance-shaped post-pulse PL dip. Stored averages are therefore not strong independent confirmation here.

Conclusion: resonance_absent.
