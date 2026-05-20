Case podmr_014_2026-05-12-081841

Sequence and readout roles:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first polarizes and detects, giving the true m_S = 0 bright reference. This is readout 1.
- full_expt = 0, so the optional "1 level reference" block is inactive.
- The active microwave operation is one rabi_pulse_mod_wait_time call followed by detection. This post-pulse channel is readout 2.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is already aligned to 13 samples.

Physical model calculation:
- Given the setup Rabi frequency is approximately 10 MHz at mod_depth = 1, use Omega_R = 10 MHz.
- For a square Rabi pulse, the resonant transfer probability is P = sin^2(pi * Omega_R * t).
- With t = 52 ns, P_res = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a resonance should reduce the post-pulse readout by about 0.22 * 0.996 = 0.219, i.e. about 21.9% of the bright readout.
- The observed readout 1 mean is 46.62 counts, so the expected resonant drop is about 10.2 counts if the swept frequency reaches the transition. Even if the resonance is midway between 5 MHz scan points, the detuned Rabi model still gives a large transfer probability near the nearest point, not a sub-count effect.

Observed data:
- readout 1 mean = 46.62, sample standard deviation = 1.14.
- readout 2 mean = 46.32, sample standard deviation = 1.08.
- The post-minus-reference differences have mean -0.31 counts and sample standard deviation 1.33 counts.
- The largest observed drop is -3.13 counts at 3.865 GHz, about -6.3% of the local readout 1 value. Other negative excursions are similarly small and not a coherent resonance-shaped feature.
- A simple scan over possible resonance centers using y2 = y1 * (1 - c * P_detuned) gives a best-fit contrast c = 0.038, much smaller than the expected c about 0.22.

Decision:
The active pulse should produce an approximately full pi-pulse response on resonance, corresponding to a roughly 10-count fluorescence drop. The measured readout difference contains only small, noisy point-to-point fluctuations and no feature with the expected amplitude. I therefore decide that a pODMR resonance is absent.
