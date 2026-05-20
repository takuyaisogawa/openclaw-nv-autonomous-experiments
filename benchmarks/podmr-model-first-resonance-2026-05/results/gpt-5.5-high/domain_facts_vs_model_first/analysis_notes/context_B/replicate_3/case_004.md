Case: podmr_007_2026-05-11-064944

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName in the raw export is Rabimodulated.xml.
- The instructions first call adj_polarize, then detection, then wait_for_awg. This first detection is the polarized m_S = 0 fluorescence reference.
- full_expt = 0, so the optional second reference block ("Acquire 1 level reference") is inactive.
- The active measurement block then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This second detection is the signal readout after the microwave pulse.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Pulse parameters:
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- mod_depth = 1 in inputs/sequence.xml and in the raw export Variable_values table. The embedded saved sequence text contains an older/default-looking "mod_depth = float(0.3,0,1)", but the active variable table resolves the value to 1.
- The pulse is rounded to the 250 MHz sample clock; 52 ns * 250 MHz = 13 samples exactly, so the active pulse remains 52 ns.

Quantitative physical model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant pulse area is f_R * t = 10e6 * 52e-9 = 0.52 Rabi cycles.
- For a driven two-level transition, the population transferred by a square pulse is
  P(detuning) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),
  where Omega = 2*pi*f_R and Delta = 2*pi*detuning.
- On resonance, P(0) = sin^2(pi * 0.52) = 0.996.
- The current setup contrast between m_S = 0 and m_S = +1 is about 22%, so a resonance should make the post-pulse signal readout lower than the m_S = 0 reference by about 0.22 * 0.996 = 0.219, i.e. a 21.9% normalized drop.
- At detunings of 2.5, 5, 10, 20, and 50 MHz, this same model predicts normalized drops of about 20.4%, 16.5%, 6.0%, 1.1%, and 0.7%, respectively. With 5 MHz scan spacing, a real resonance in the scan range should produce at least one pronounced negative point and likely a multi-point dip unless it lies between points with unusual cancellation.

Data comparison:
- Using contrast = (readout2 - readout1) / readout1, the 21 measured values have mean -0.0045 and standard deviation 0.0515.
- The most negative observed point is -0.1128 at 3.855 GHz. That is only about half the expected on-resonance contrast and appears as a single noisy fluctuation rather than the fixed Rabi-response line shape.
- Other nearby points do not form the expected dip: 3.850 GHz is -0.0454, 3.855 GHz is -0.1128, 3.860 GHz is +0.0203, and 3.865 GHz is -0.0466.
- A null model with constant contrast has RSS 0.0558. A fixed-amplitude physical model with the expected -22% contrast gives a worse best RSS of 0.0838 after optimizing the resonance center and a constant baseline.
- Allowing the amplitude to fit freely improves RSS only modestly to 0.0459, but the best fitted amplitude is positive (+0.0758), centered near 3.915 GHz, which is opposite in sign to the expected pODMR fluorescence dip.
- Stored averages are not treated as an independent repeatability proof because they can reflect tracking cadence. They also do not show a stable expected-scale resonance feature.

Decision:
The active sequence would strongly populate m_S = +1 on resonance and should create an approximately 22% reduction in the post-pulse readout relative to the m_S = 0 reference. The measured normalized signal fluctuates around zero and does not support the expected negative Rabi-response line shape. I therefore decide that a pODMR resonance is absent.
