Case podmr_076_2026-05-17-095337.

I used the provided sequence.xml and the raw numeric export only.

Sequence interpretation:

- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "1 level reference" block is inactive even though do_adiabatic_inversion is true.
- Readout 1 is the detection immediately after adj_polarize, so it is the polarized m_S = 0 reference.
- Readout 2 is the detection after the active rabi_pulse_mod_wait_time pulse, so it is the signal readout after the microwave pulse.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-8 s. With sample_rate = 250 MHz, the quantized pulse duration is round(52 ns * 250 MHz) / 250 MHz = 52 ns.

Quantitative model calculation:

The supplied setup facts give a Rabi frequency of about 10 MHz at mod_depth = 1, with approximately linear scaling, so I used f_R = 10 MHz. For a square microwave pulse, the driven population transfer versus detuning is

P(det) = (f_R^2 / (f_R^2 + det^2)) * sin^2(pi * t * sqrt(f_R^2 + det^2)).

At t = 52 ns and det = 0:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

Using the setup contrast scale of 22% between m_S = 0 and m_S = +1, a resonant signal readout should drop by

0.22 * 0.996 = 0.219

relative to the m_S = 0 reference. For readouts near 50 counts, that is about 11 counts. Even one 5 MHz scan step away, the model gives P(5 MHz) = 0.749, or an expected drop of 0.165, about 8.2 counts. At 10 MHz detuning the expected drop is still about 0.060, about 3 counts.

Observed data comparison:

I computed the normalized signal drop y = 1 - readout2 / readout1 for the combined raw readouts. The mean drop is 0.0039, with point-to-point standard deviation 0.0277. The largest observed drop is 0.0519 at 3.905 GHz, corresponding to only about 2.6 counts. Several points have negative drop, where readout 2 is brighter than readout 1.

I also fit the square-pulse response shape across possible resonance centers on a 1 MHz grid using y = b + a * P(det). The best positive-amplitude fit gave a = 0.023, about one tenth of the expected physical amplitude a = 0.22. The physically fixed-amplitude model is much worse than a constant baseline model, because it predicts a large dip that is not present in the data.

Stored per-average overlays were not treated as strong independent repeatability evidence, since they may reflect tracking cadence. They also do not show a consistent large dip at a shared frequency.

Decision:

The active pulse should produce a large, easily visible resonant drop if an addressed pODMR resonance is in this scan. The observed readout2/readout1 variations are small, sign-changing, and far below the expected 22% contrast-scale response. I therefore decide that a pODMR resonance is absent.
