Case: podmr_007_2026-05-11-064944

Used only the provided sequence XML and raw export data.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active path has full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- The first active detection follows adj_polarize and is the true m_S = 0 reference readout.
- The second active detection follows rabi_pulse_mod_wait_time and is the pODMR signal readout after the microwave pulse.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, the rounded pulse length is exactly 13 samples = 52 ns.

Quantitative physical model:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1, use f_R = 10 MHz.
- For a square pulse, the transition probability versus detuning is
  P1(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2)),
  with tau = 52 ns and frequencies in cycles/s.
- On resonance, P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated 22% m_S = 0 to m_S = +1 contrast scale, the expected normalized fluorescence drop at resonance is 0.22 * 0.996 = 0.219.
- The mean reference readout is 31.72 counts, so the expected resonant count drop is about 6.95 counts.
- If centered on a scan point, the same model predicts about 16.5% normalized contrast at +/-5 MHz and about 6.0% at +/-10 MHz, so a real resonance should form a clear multi-point feature at this scan spacing.

Observed data:
- Mean readout 1 = 31.72 and mean readout 2 = 31.55.
- Mean normalized contrast, computed as 1 - readout2/readout1, is 0.00446 with standard deviation 0.0528 across the 21 frequency points.
- The largest positive contrast is 0.1128 at 3.855 GHz, about half the expected resonant peak.
- If 3.855 GHz were the resonance center, the model predicts contrasts of about 0.1647 at both neighboring +/-5 MHz points. The observed neighboring contrasts are 0.0454 at 3.850 GHz and -0.0203 at 3.860 GHz, which do not match the expected Rabi line shape.

Model comparison:
- A flat-baseline model for normalized contrast has SSE = 0.05576.
- An unconstrained two-parameter fit y = baseline + A * P1(freq - f0), scanning f0 across the scan range, gives its best SSE = 0.04590 with A = -0.0758, i.e. the best shape has the opposite sign from a physical ODMR dip in readout 2 relative to the m_S = 0 reference.
- Constraining A >= 0 gives A = 0.0715, only 0.33 of the expected 0.22 contrast scale.
- Forcing the expected physical amplitude A = 0.22 gives best SSE = 0.08384, worse than the flat-baseline SSE.
- Stored averages are only 2 and can reflect tracking cadence; their median pointwise normalized-contrast scatter is 0.0397, so they do not provide a strong independent repeatability test. The expected 0.219 resonant contrast would still be a large effect relative to the plotted fluctuations.

Decision:
The observed readout differences do not show the expected amplitude or detuning-dependent line shape for the active 52 ns, mod_depth = 1 pODMR pulse. A pODMR resonance is absent.
