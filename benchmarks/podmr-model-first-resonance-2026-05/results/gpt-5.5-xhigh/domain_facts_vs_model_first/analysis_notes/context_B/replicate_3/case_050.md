# pODMR analysis note

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- Active sequence: Rabimodulated.xml.
- The XML has full_expt = 0, so the "Acquire 1 level reference" branch is inactive.
- Readout 1 is the true 0-level reference: adj_polarize, then detection.
- Readout 2 is the signal readout after rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then detection.
- sample_rate = 250 MHz, length_rabi_pulse = 52 ns. The pulse is already on the 4 ns sample grid.
- mod_depth = 1.

Quantitative model calculation:
- Setup Rabi frequency: f_R = 10 MHz * mod_depth = 10 MHz.
- Rectangular-pulse transition probability versus detuning df:
  P1(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * T * sqrt(f_R^2 + df^2)).
- With T = 52 ns, P1(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.
- With the stated 22% contrast scale, the expected normalized signal is S2/S1 = 1 - 0.22 * P1(df).
- On resonance, expected S2/S1 = 0.781, a 21.9% drop. With mean readout 1 = 50.985, that is an expected drop of about 11.17 raw-count units.
- The scan step is 5 MHz. For any resonance center inside the scan range, the nearest sampled point is within 2.5 MHz. A dense grid over possible in-range centers gives minimum sampled max(P1) = 0.929, so an in-range resonance should produce at least 0.22 * 0.929 = 20.4% contrast at some sampled point, about 10.4 raw-count units at the observed reference level.

Data comparison:
- Observed mean readout 1 = 50.985 and mean readout 2 = 50.476.
- Observed normalized contrast y = 1 - readout2/readout1 ranges from -6.99% to +5.39%, with maximum positive contrast at 3.920 GHz.
- That maximum observed drop is 2.79 raw-count units, far below the approximately 10 to 11 raw-count-unit drop expected for an in-range resonance.
- Fitting the same Rabi lineshape with free baseline and free amplitude gives best amplitude 0.0426, with maximum fitted contrast about 4.7%, far below the physical 22% contrast scale. The constant-only SSE is 0.0143, and the free-amplitude lineshape SSE is 0.0118, a small improvement consistent with noise/tracking variation rather than a resonance-scale feature.
- Forcing the physical 22% amplitude gives best center at the scan edge but still predicts a greater than 20% dip; its SSE is 0.0603, much worse than the constant-only model.
- The stored averages show different strongest contrast locations, and stored averages can reflect tracking cadence rather than independent repeatability. They do not rescue a resonance-scale feature.

Decision: resonance_absent.
