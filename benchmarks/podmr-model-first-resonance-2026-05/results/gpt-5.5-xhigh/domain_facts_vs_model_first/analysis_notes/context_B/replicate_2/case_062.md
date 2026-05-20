Case podmr_048_2026-05-17-002650

I used the standalone provided inputs/sequence.xml to identify the active pulse sequence. It is Rabimodulated.xml. The active instructions first polarize and detect, giving readout 1 as the true mS=0 fluorescence reference. Because full_expt = 0, the mS=+1 reference block is not executed. The second active detection occurs after rabi_pulse_mod_wait_time, so readout 2 is the post-Rabi pODMR signal. The active pulse parameters from the provided XML are mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the pulse is already on a 4 ns sample grid, so rounding leaves it at 52 ns.

Quantitative expected-signal model:

Use the given setup facts: the mS=0 to mS=+1 contrast scale is about 22%, and the Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular pulse, with angular Rabi rate Omega = 2*pi*10 MHz and detuning Delta, the transition probability is

P1(Delta) = Omega^2 / (Omega^2 + Delta^2) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

where t = 52 ns. On resonance this gives

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.

The expected fluorescence reduction at resonance is therefore 0.22 * 0.9961 = 0.2191, or about 21.9% relative to the mS=0 reference. Since the scan step is 5 MHz, any resonance lying inside the scan range has a sampled point within 2.5 MHz. At 2.5 MHz detuning the same model gives P1 = 0.9292, so the expected reduction at the nearest sampled point is still about 0.22 * 0.9292 = 0.2044, or 20.4%.

Observed normalized signal:

I used c = 1 - readout2/readout1, with readout1 as the active mS=0 reference. Across the 21 scan points the mean c is 0.0134 and the maximum observed drop is 0.0735 at 3.850 GHz, where readout1 = 52.5769 and readout2 = 48.7115. The largest observed drop is therefore only about one third of the minimum modeled response expected at the nearest sampled point for an in-range resonance, and it is far below the 21.9% on-resonance response. At the mean readout1 level, an on-resonance response would put readout2 near 39.42 counts, while the measured readout2 values remain near 48-52 counts.

The two stored averages do not provide a strong independent repeatability test because they can reflect tracking cadence. They also do not rescue the result: the strongest combined point remains a small 7.4% drop, not the approximately 20-22% dip predicted by the active pulse model.

Decision: resonance_absent.
