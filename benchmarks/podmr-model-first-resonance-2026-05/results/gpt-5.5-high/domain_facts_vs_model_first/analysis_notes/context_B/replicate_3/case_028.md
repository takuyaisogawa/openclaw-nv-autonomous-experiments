Case: podmr_013_2026-05-16-123121

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence interpretation:
- Active sequence: Rabimodulated.xml.
- The executed structure is polarize, detection, wait, one modulated Rabi pulse, detection, wait.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- readout 1 is the pre-microwave polarized mS = 0 optical reference.
- readout 2 is the signal after the scanned-frequency modulated Rabi pulse.
- From inputs/sequence.xml and the exported variable values, mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, round(52 ns * 250 MHz) = 13 samples, so the active pulse remains 52 ns.

Quantitative model:
- Given setup contrast C = 0.22 between mS = 0 and mS = +1.
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1.
- For a square driven two-level pulse, the transition probability versus detuning d is
  P1(d) = f_R^2 / (f_R^2 + d^2) * sin^2(pi * t * sqrt(f_R^2 + d^2)).
- With t = 52 ns and f_R = 10 MHz, the on-resonance transfer is
  sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- The expected on-resonance optical signal in readout 2 relative to the mS = 0 reference is therefore
  1 - C * P1(0) = 1 - 0.22 * 0.996 = 0.781.
- At detunings of about +/-5 MHz the same model gives P1 about 0.75 and an expected relative signal about 0.835; at +/-10 MHz it gives a much smaller response, about 0.94 relative signal.

Observed data check:
- The combined readout2/readout1 ratios near the dip are:
  - 3.870 GHz: 38.423 / 43.962 = 0.874
  - 3.875 GHz: 34.673 / 44.404 = 0.781
  - 3.880 GHz: 34.077 / 43.058 = 0.791
  - 3.885 GHz: 38.250 / 44.481 = 0.860
- The off-dip median readout2/readout1 ratio is about 0.983.
- A grid fit of the two-level response to the normalized ratio gives center about 3.8779 GHz and effective contrast about 0.221, matching the stated 0.22 contrast scale.
- The constant-ratio null residual is about 5.1 times larger than the fixed-contrast resonance model residual.
- The per-average traces both show their minimum normalized signal at 3.875 GHz. These averages are not treated as a strong independent repeatability test, but they are consistent with the combined trace.

Decision:
The readout 2 dip has the amplitude, width, and frequency-localized shape expected from a 52 ns, mod_depth 1 pODMR Rabi pulse with about 10 MHz Rabi frequency and 22% optical contrast, while readout 1 remains a reference. A pODMR resonance is present.
