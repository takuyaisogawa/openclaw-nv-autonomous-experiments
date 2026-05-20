Case: podmr_056_2026-05-17-050447

I used only the provided XML/exported raw readouts.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML has full_expt = 0, so the conditional "Acquire 1 level reference" block is skipped even though do_adiabatic_inversion is set.
- readout 1 is the detection immediately after adj_polarize, before the microwave pulse, i.e. the true mS=0 reference/readout baseline.
- readout 2 is the detection after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay), i.e. the microwave-pulse signal readout.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz this is exactly 13 samples, so the rounded active pulse duration remains 52 ns.

Physical model calculation:

Use the stated Rabi scale f_R = 10 MHz at mod_depth = 1. For a rectangular pulse of duration tau = 52 ns, the two-level transition probability versus detuning delta is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).

At delta = 0, P = sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated mS=0 to mS=+1 contrast scale of 22%, a resonance should reduce the post-pulse readout by about 0.22 * 0.996 = 21.9% relative to the 0-reference. Around the observed raw scale of 44 counts this is about 9.6 counts.

Because the scan step is 5 MHz, an in-band resonance should be sampled within 2.5 MHz of its center. The same model gives P(2.5 MHz) = 0.929, so the nearest sampled point should still show about a 20.4% drop, roughly 9 counts. Even at 5 MHz detuning the expected drop is about 16.5%, roughly 7.3 counts.

Observed quantitative comparison:

Using readout 1 as the mS=0 reference and readout 2 as the microwave-pulse signal, the normalized difference (readout2 - readout1) / readout1 has mean +0.0043 and sample standard deviation 0.0323. The largest observed negative excursion is only -0.0572 at 3.900 GHz, corresponding to about 2.6 counts, far smaller than the expected 9 to 10 count pi-pulse resonance signal and not accompanied by the required line shape.

A baseline-only linear fit to the normalized differential gave SSE = 0.01909. Fitting the physical Rabi line shape with a free positive contrast amplitude inside the scanned band gave best contrast amplitude 0.056 at f0 = 3.893 GHz, well below the required 0.22. Forcing the physically expected 22% contrast inside the scanned band gave best SSE = 0.05319, about 2.79 times worse than the baseline-only fit. Thus the measured data reject the expected in-band resonance-scale response.

The two stored averages are not treated as a strong independent repeatability test because stored averages can reflect tracking cadence. They also do not show a consistent resonance-scale dip at the same frequency.

Decision: resonance_absent.
