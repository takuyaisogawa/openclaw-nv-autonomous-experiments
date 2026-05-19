<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_088

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- The provided XML is a Rabimodulated sequence scanning mw_freq.
- sample_rate = 250 MHz.
- length_rabi_pulse = 52 ns, rounded to 13 samples at 250 MHz, still 52 ns.
- mod_depth = 1.
- full_expt = 0, so the optional mS = +1 reference block is inactive.
- Readout 1 is the detection immediately after optical polarization, so it is the bright mS = 0 reference.
- Readout 2 is the detection after the active rabi_pulse_mod_wait_time pulse, so it is the microwave-response signal readout.

Physical model calculation:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, the expected resonant Rabi frequency here is f_R = 10 MHz.
- For a resonant square Rabi pulse, transfer probability P = sin^2(pi f_R tau).
- With tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- The stated bright/dark contrast scale is about 22%, so an on-resonance point should lower readout 2 relative to readout 1 by about 0.22 * 0.996 = 0.219, or 21.9%.
- The measured readout 1 mean is 49.08 counts, giving an expected on-resonance count drop of about 10.75 counts.

Measured response:
- The combined readout 2 minus readout 1 differences range from -3.92 to +2.31 counts, with mean -0.29 counts and standard deviation 1.72 counts.
- The largest normalized drop (readout1 - readout2) / readout1 is 0.07695 at 3.900 GHz, corresponding to only 3.92 counts.
- This is about 35% of the expected resonant contrast and is not accompanied by the expected model-sized dip.

Explicit lineshape check:
- I evaluated the standard detuned Rabi response
  P(detuning) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * tau * sqrt(f_R^2 + detuning^2))
  across possible resonance centers near the scanned 3.825 to 3.925 GHz interval.
- Fitting normalized contrast y = (readout1 - readout2) / readout1 to baseline + amplitude * P gave best-fit amplitude -0.056, not the expected positive approximately +0.22.
- Forcing the physical +0.22 amplitude improved the baseline-only residual only weakly and by placing the center outside the scanned range, which is not evidence for a present pODMR resonance in the scan.

Decision:
The active pulse should have produced a large darkening of readout 2 if a pODMR resonance were present. The observed fluctuations are much smaller than the expected 21.9% signal and the fitted Rabi response has the wrong sign, so I classify this case as resonance_absent.
