Case: podmr_054_2026-05-17-043636

Sequence identification:
- Provided sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active readouts:
  - Readout 1 is the true m_S = 0 reference: adj_polarize, then detection.
  - The m_S = +1 reference block is skipped because full_expt = 0.
  - Readout 2 is after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), then detection.
- do_adiabatic_inversion is not active in the measured readout path because the full_expt block is skipped.
- sample_rate = 250 MHz, length_rabi_pulse = 52 ns. The sequence rounds this to 13 samples, still 52 ns.
- mod_depth = 1 from the provided sequence XML and the exported active Variable_values.

Quantitative physical model:
- Setup contrast between m_S = 0 and m_S = +1 is about C = 0.22.
- Rabi frequency is about fR = 10 MHz at mod_depth = 1.
- For a square pulse of duration t = 52 ns, the transition probability versus detuning df is:

  P1(df) = (fR^2 / (fR^2 + df^2)) * sin^2(pi * t * sqrt(fR^2 + df^2))

- The expected normalized readout-2/readout-1 signal is:

  S(df) = 1 - C * P1(df)

Model values:
- On resonance, P1(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996, so S(0) = 0.781.
- At df = 2.5 MHz, S = 0.796.
- At df = 5 MHz, S = 0.835.
- At df = 10 MHz, S = 0.940.
- Therefore, if a resonance is inside the scanned range, the 5 MHz sampled scan should contain at least one point with readout-2/readout-1 near 0.78 to 0.80, or at minimum a strong local dip below about 0.84 if sampled one step from center.

Observed data calculation:
- Combined readout 1 mean = 42.517.
- Combined readout 2 mean = 42.266.
- Combined ratio readout2/readout1 mean = 0.9945.
- Minimum combined ratio = 0.9468 at 3.840 GHz.
- Maximum combined ratio = 1.0559.
- No combined point has ratio below 0.90.
- The largest negative raw difference readout2 - readout1 is -2.327 counts, while an on-resonance 22% contrast dip near this baseline would be about -9.3 counts.

Simple model fit check:
- A flat ratio model has SSE = 0.01522.
- A fixed-contrast Rabi model scanned over possible resonance centers, with only a multiplicative baseline fitted, chooses a center outside the scan at about 3.7955 GHz and gives SSE = 0.01423.
- This is only a small improvement over flat and the best model keeps the in-window minimum ratio at 0.978, not an in-scan pODMR-like dip.
- If the resonance center is constrained to lie inside the measured scan, the model requires a sampled minimum ratio between 0.781 and 0.796, which is far below the observed minimum 0.947.

Per-average note:
- The two stored averages differ in absolute level, consistent with tracking cadence/drift.
- Their ratio minima are 0.938 and 0.918, still far above the expected near-0.78 resonance response and not a strong independent repeatability test.

Decision:
The observed normalized data remain near unity and lack the contrast-scale dip required by the active 52 ns, mod_depth 1 Rabi pulse model, so a pODMR resonance is absent.
