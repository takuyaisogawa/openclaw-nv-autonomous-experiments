Case podmr_012_2026-05-16-121601.

Active sequence and readout roles:
- The provided sequence XML is Rabimodulated and scans mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- Readout 1 is the initial polarized m_S = 0 reference detection.
- Readout 2 is the detection after a modulated Rabi pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.

Physical model calculation:
- Given f_R = 10 MHz at mod_depth = 1 and linear mod_depth scaling, the relevant Rabi frequency is 10 MHz.
- For a rectangular driven two-level pulse, using f_R in cycles/s, the transition probability versus detuning df is:
  P(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * t * sqrt(f_R^2 + df^2)).
- At resonance with t = 52 ns, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup contrast scale of 22%, the expected resonant fluorescence dip is 0.22 * 0.996 = 0.219, i.e. about a 21.9% drop from the m_S = 0 reference. For a 42-count reference this predicts about 32.8 counts on resonance.

Observed data:
- The measured readout 2 has a structured dip centered around 3.875 to 3.880 GHz.
- The deepest point is at 3.880 GHz: readout 1 = 41.2308, readout 2 = 33.9231, normalized dip = (41.2308 - 33.9231) / 41.2308 = 0.177.
- Neighboring points also show large dips: 0.131 at 3.870 GHz, 0.128 at 3.875 GHz, and 0.133 at 3.885 GHz.
- A rectangular-pulse resonance model fit of readout 2 = scale * readout 1 * (1 - A * P(df, center)) gives best center = 3.8785 GHz, scale = 0.993, and A = 0.180. Its SSE is 22.3, compared with 113.3 for a no-resonance scaled-reference model.

Decision:
The observed dip amplitude, frequency-localized shape, and fitted center are consistent with the expected pODMR response for the active 52 ns mod_depth 1 pulse. A resonance is present.
