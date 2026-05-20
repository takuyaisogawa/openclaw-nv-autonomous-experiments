Case: podmr_054_2026-05-17-043636

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The active instructions first polarize and detect the true m_s = 0 reference.
- full_expt = 0, so the optional "1 level reference" block is inactive even though do_adiabatic_inversion = 1 is defined.
- The active microwave-dependent part is one rabi_pulse_mod_wait_time call followed by detection.
- Therefore readout 1 is the polarized m_s = 0 reference and readout 2 is the post-MW pODMR signal.

Pulse parameters:
- sample_rate = 250000000 Hz.
- length_rabi_pulse = 5.2e-08 s. The sequence rounds this as round(t * sample_rate) / sample_rate = round(13) / 250000000 = 52 ns.
- mod_depth = 1.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative physical model:
- Given the setup fact, Rabi frequency at mod_depth = 1 is about 10 MHz.
- For a square pulse, the transition probability versus detuning is
  P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),
  with f_R = 10 MHz and t = 52 ns.
- On resonance this gives P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- With the stated 0-to-+1 contrast scale of about 22%, the expected on-resonance normalized fluorescence drop in readout 2 relative to readout 1 is 0.22 * 0.996 = 0.219.
- At the mean readout 1 level of 42.52, this is an expected drop of about 9.32 raw readout units.
- If the resonance center landed on a scan point, the expected normalized contrast pattern would have a central point near 0.219 and the adjacent +/-5 MHz points near 0.165; +/-10 MHz points remain around 0.060.

Observed normalized signal:
- I used c = (readout1 - readout2) / readout1 point by point.
- Observed mean c = 0.0055, standard deviation = 0.0276.
- Observed maximum c = 0.0532 at 3.840 GHz.
- Observed minimum c = -0.0559 at 3.880 GHz.
- The largest apparent drop is only about 24% of the expected on-resonance drop and is not accompanied by the expected neighboring-point line shape.
- The two stored averages show similar small contrast scale only; because stored averages can reflect tracking cadence, I did not treat them as a strong independent repeatability test.

Model comparison:
- Constant-baseline normalized contrast SSE: 0.01522.
- Forcing the physical 22% contrast model with a resonance center constrained inside the scan gives best SSE: 0.06632, worse than the no-resonance baseline.
- Allowing the model amplitude to float gives best amplitude 0.0413, only 18.8% of the expected physical contrast, consistent with small fluctuations rather than the expected pODMR response.

Decision:
The active pulse should be essentially a pi pulse on resonance and should create a large readout-2 drop. The data do not show the expected amplitude or detuning-dependent shape, so I decide resonance_absent.
