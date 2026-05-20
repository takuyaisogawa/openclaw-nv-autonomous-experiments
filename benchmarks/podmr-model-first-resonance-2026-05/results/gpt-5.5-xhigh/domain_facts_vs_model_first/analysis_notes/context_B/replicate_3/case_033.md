Case: podmr_018_2026-05-16-134409

Sequence interpretation from inputs/sequence.xml:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" branch is skipped. do_adiabatic_inversion is therefore irrelevant here.
- Readout 1 is the first detection after adj_polarize, so it is the true m_S = 0 fluorescence reference for each scan point.
- Readout 2 is the detection after rabi_pulse_mod_wait_time, so it is the post-microwave-pulse readout used to test whether population was transferred out of m_S = 0.
- mod_depth = 1 and length_rabi_pulse = 52 ns. The 250 MHz sample rate gives exactly 13 samples, so rounding leaves the pulse at 52 ns.

Quantitative model:
- Given the setup fact that the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, use f_R = 10 MHz.
- For a square pulse with detuning df, the transfer probability is
  P(df) = f_R^2/(f_R^2 + df^2) * sin^2(pi * t * sqrt(f_R^2 + df^2)).
- On resonance with t = 52 ns:
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22 percent m_S = 0 to m_S = +1 contrast scale, the expected normalized readout drop on resonance is 0.22 * 0.996 = 0.219.

Measured normalized contrast:
- I used contrast = 1 - readout2/readout1 because readout1 is the local m_S = 0 reference and readout2 is the post-pulse signal.
- The main dip is:
  - 3.870 GHz: contrast 0.135
  - 3.875 GHz: contrast 0.193
  - 3.880 GHz: contrast 0.172
  - 3.885 GHz: contrast 0.082
- The maximum observed normalized drop is 0.193, close to the 0.219 expected from an almost pi pulse.

Model comparison:
- A grid search of the detuned Rabi model with fixed 22 percent contrast gives best center near 3.8771 GHz.
- At that center, the fixed-scale model predicts contrasts of about 0.121, 0.209, 0.200, and 0.103 at 3.870, 3.875, 3.880, and 3.885 GHz respectively, matching the observed dip shape and scale.
- Allowing a fitted contrast amplitude plus a small offset gives amplitude 0.186, offset 0.0108, and center 3.8771 GHz.
- The fitted Rabi-line model SSE is 0.0239 versus 0.0811 for a flat-contrast null model, so the structured resonance model explains substantially more variance.
- The two stored averages both have their largest local contrast near 3.875 GHz, but I do not treat the two averages as a strong independent repeatability test because stored averages can reflect tracking cadence.

Decision:
The post-pulse readout contains a frequency-localized dip with the expected near-pi-pulse contrast scale and detuned Rabi lineshape. A pODMR resonance is present.
