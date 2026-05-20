Sequence and readout interpretation:

The active sequence is Rabimodulated.xml. In the XML, full_expt is 0, so the optional mS=+1 reference block is skipped. The first detection after adj_polarize is therefore the true mS=0 reference readout. The second recorded detection occurs after rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth, so readout 2 is the microwave-pulse-dependent signal.

Relevant pulse settings:

- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns
- mw_freq is scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps
- averages = 2, repetitions = 100000

Decision reasoning:

With the stated setup scale, the Rabi frequency is about 10 MHz at mod_depth = 1, so a 52 ns pulse is near a pi pulse. If the scan crossed a real pODMR resonance, the post-pulse signal readout should drop strongly relative to the mS=0 reference, on the order of the stated 22% contrast scale for a good transfer.

The combined data do not show that. Readout 1 averages about 53.79 and readout 2 averages about 52.95, only about 1.6% lower overall. The largest pointwise normalized drop is only about 6%, and the low points are scattered across the scan rather than forming a clear frequency-localized resonance feature. The per-average overlay shows substantial point-to-point and average-to-average variation, consistent with tracking/noise cadence rather than a strong independent repeatability check.

Conclusion: resonance_absent.
