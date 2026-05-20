Case podmr_045_2026-05-16-234216

Sequence interpretation:
- The active sequence is Rabimodulated.xml.
- The sequence first polarizes the NV, then performs detection before any microwave pulse. This readout is the true m_S = 0 reference.
- full_expt = 0, so the optional "1 level reference" block is inactive. There is no independent m_S = +1 reference readout in this scan.
- The only active microwave manipulation before the second detection is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- From the provided sequence XML and Variable_values, mod_depth = 1 and length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so rounding leaves it at 52 ns.
- Therefore readout 1 is the pumped m_S = 0 reference, and readout 2 is the resonance-sensitive post-Rabi-pulse readout.

Physical model calculation:
- Given the supplied setup facts, the on-resonance Rabi frequency at mod_depth = 1 is about 10 MHz.
- For a square resonant pulse, P(m_S=+1) = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10 MHz and t = 52 ns, P(m_S=+1) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22% m_S = 0 to m_S = +1 contrast scale, the expected post-pulse readout on resonance is 1 - 0.22 * 0.996 = 0.781 of the m_S = 0 reference.
- The mean readout 1 level is 48.85 counts, so an on-resonance point should put readout 2 near 38.15 counts, a dip of about 10.70 counts relative to readout 1.
- The same square-pulse model gives approximate expected dips of 8.05 counts at 5 MHz detuning, 2.93 counts at 10 MHz detuning, and negligible to small values by about 15 MHz detuning, so at least one or two adjacent 5 MHz-spaced scan points should show a large readout-2 suppression if the resonance lies inside the sweep.

Data comparison:
- The combined readouts over 3.825 to 3.925 GHz have mean(readout2 - readout1) = -0.084 counts with standard deviation 1.039 counts.
- The largest observed suppression of readout 2 relative to readout 1 is only -1.827 counts at 3.845 GHz, with readout2/readout1 = 0.964.
- This observed maximum suppression is about 17% of the expected on-resonance dip and is not arranged as the broad, high-contrast dip predicted by the 52 ns, mod_depth 1 pulse model.
- The per-average traces vary at the few-count level and are consistent with tracking/noise cadence rather than a repeatable high-contrast resonance.

Decision:
The relevant active pulse should produce an easily visible pODMR dip if a resonance were present in the scanned range. The observed post-pulse readout remains close to the m_S = 0 reference and lacks the expected 22%-scale depletion, so I decide resonance_absent.
