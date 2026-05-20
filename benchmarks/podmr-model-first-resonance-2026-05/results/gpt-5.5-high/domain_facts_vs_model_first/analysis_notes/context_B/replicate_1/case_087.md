Case: podmr_073_2026-05-17-090948

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- Sequence name: Rabimodulated.xml.
- The active experiment has full_expt = 0, so the commented/conditional mS = +1 reference block is not executed.
- The two active readouts are:
  1. readout 1: detection immediately after optical polarization, acting as the mS = 0 fluorescence reference.
  2. readout 2: detection after the Rabi-modulated microwave pulse, acting as the pODMR signal readout.
- mod_depth = 1 from the provided sequence XML and saved variable values.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the 4 ns sample period makes 52 ns exactly 13 samples after rounding.

Physical model calculation:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, the pulse is near a pi pulse.
- For a two-level driven transition, the transferred population versus detuning delta is:
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),
  using f_R and delta in cycles/s.
- At delta = 0 and t = 52 ns:
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup contrast scale of 22%, the expected resonant fluorescence reduction is:
  0.22 * 0.996 = 0.219, or about 21.9%.
- On the observed approximately 50-count reference baseline, a resonant point should therefore be lower by about 11 counts in readout 2 relative to readout 1.
- At the scan spacing of 5 MHz, the same model still predicts a strong nearby dip: about 16.5% at 5 MHz detuning and about 6.0% at 10 MHz detuning, so a real resonance within the scanned range should produce a conspicuous model-shaped depression over one or more scan points.

Data comparison:
- Mean readout 1 = 50.17 counts.
- Mean readout 2 = 50.04 counts.
- Mean readout2-readout1 = -0.12 counts.
- The most negative readout2-readout1 point is -2.52 counts, corresponding to a 5.0% fractional dip, far below the expected approximately 11-count / 21.9% resonant dip.
- Several points have readout 2 above readout 1, and the apparent dips do not form the expected detuning-dependent resonance profile.
- A fixed-amplitude resonance model with the expected 22% contrast gives a substantially worse residual than a null/no-resonance model; fitting the amplitude freely gives only about 2.1% contrast, far below the setup contrast expectation for this near-pi pulse.
- Stored averages are only two and can reflect tracking cadence, so I did not treat the per-average overlays as an independent repeatability test.

Decision:
The quantitative near-pi-pulse model predicts a large pODMR dip if a resonance is present in the scan window, but the observed signal readout relative to the mS = 0 reference shows only small, non-model-shaped fluctuations. I therefore decide resonance_absent.
