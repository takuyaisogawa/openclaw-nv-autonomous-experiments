Case: podmr_005_2026-05-16-010352

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The active instructions polarize the NV, take a detection readout, wait, optionally acquire a 1-level reference only if full_expt is nonzero, then apply a modulated Rabi microwave pulse and take another detection readout.
- full_expt = 0, so the optional 1-level reference block is inactive.
- Readout 1 is therefore the optically polarized m_S = 0 fluorescence reference.
- Readout 2 is the post-Rabi-pulse fluorescence signal.
- mod_depth = 1 from the provided sequence XML / variable values.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz this is 13 samples, so the rounded pulse duration remains 52 ns.

Physical model calculation:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, the expected Rabi frequency here is f_R = 10 MHz.
- For a rectangular resonant pulse, the transfer probability is P = sin^2(pi f_R t).
- With t = 52 ns, P_on = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance normalized readout-2 drop relative to readout 1 is 0.22 * 0.996 = 0.219, i.e. readout2/readout1 should be about 0.781 at resonance.
- Off resonance I used the finite-pulse Rabi response:
  P(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * t * sqrt(f_R^2 + df^2)).
- This gives expected drops of about 21.9% at 0 MHz detuning, 16.5% at 5 MHz, 6.0% at 10 MHz, 0.26% at 15 MHz, with small side lobes at larger detuning.

Data comparison:
- The combined readouts have their strongest normalized drops at:
  - 3.875 GHz: readout1 = 40.962, readout2 = 30.635, ratio = 0.7479, drop = 25.2%.
  - 3.880 GHz: readout1 = 39.192, readout2 = 30.327, ratio = 0.7738, drop = 22.6%.
  - 3.885 GHz: ratio = 0.8616, drop = 13.8%.
- These central points match the expected on-resonance scale from the model. The drop width is also consistent with a near-pi 52 ns pulse with f_R about 10 MHz.
- A least-squares fit of readout2/readout1 to baseline - A * P(df), using the above Rabi response and scanning the center frequency, gives center about 3.8785 GHz, baseline ratio about 0.989, and fitted drop coefficient about 0.234. This is close to the expected 0.22 contrast scale. The flat-ratio SSE was 0.1109, while the Rabi-lineshape fit SSE was 0.0205.
- The two stored averages both show the same central dip near 3.875-3.880 GHz, but I treat that only as supportive because stored averages can reflect tracking cadence rather than independent repeatability.

Decision:
The measured readout-2 depression relative to the m_S = 0 reference has the expected magnitude and frequency-localized shape for the active 52 ns, mod_depth 1 Rabi-modulated pODMR pulse. A pODMR resonance is present.
