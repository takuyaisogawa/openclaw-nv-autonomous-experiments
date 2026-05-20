Case: podmr_034_2026-05-15-235221

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize the NV and perform detection. This first acquired channel is the m_S=0 / bright reference readout.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive despite do_adiabatic_inversion being true.
- The active spectroscopy operation is one rabi_pulse_mod_wait_time call followed by detection. This second acquired channel is the post-microwave signal readout.
- The provided sequence XML gives length_rabi_pulse = 52 ns and mod_depth = 1. The raw export also reports Variable_values mod_depth = 1, although its embedded Sequence text contains an older-looking mod_depth default of 0.3; I use the provided XML and exported variable value for the actual setting.

Quantitative expected-signal model:
- Given the stated setup calibration, f_Rabi ~= 10 MHz * mod_depth.
- For mod_depth = 1 and pulse duration t = 52 ns, the resonant rotation model gives transition probability
  P = sin^2(pi * f_Rabi * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With setup contrast about 22% between m_S=0 and m_S=+1, the expected resonant PL reduction in the signal readout relative to the bright reference is
  0.22 * 0.996 = 0.219, or about 21.9%.
- For a typical bright readout of 35 counts, the expected on-resonance signal readout is 35 * (1 - 0.219) = 27.3 counts.
- If the conflicting embedded default mod_depth = 0.3 were used instead, P = sin^2(pi * 3e6 * 52e-9) = 0.222 and the expected drop would only be 4.9%, giving about 33.3 counts from a 35-count bright level. This does not match the observed central dip, further supporting that the active value is mod_depth = 1.

Measured comparison:
- Off-resonance, excluding points near the dip, mean readout 1 is 36.08 and mean readout 2 is 35.34, ratio 0.980, so the two readouts are normally close.
- Around the feature:
  - 3.870 GHz: readout 1 = 38.19, readout 2 = 30.83, contrast = 19.3%.
  - 3.875 GHz: readout 1 = 34.23, readout 2 = 26.81, contrast = 21.7%.
  - 3.880 GHz: readout 1 = 34.88, readout 2 = 26.29, contrast = 24.6%.
- The deepest point is close to the model-predicted value for a near-pi resonant pulse: about 26.3 counts observed versus about 27.3 counts expected for a 35-count bright level.
- The first readout remains near its normal bright level through the feature, while the second readout shows the physically expected dip. Stored average overlays show the dip in the same frequency region, but I do not treat those averages as a strong independent repeatability test because they may reflect tracking cadence.

Decision:
The observed frequency-localized drop in the post-microwave signal readout has the sign, width, and amplitude expected from the explicit resonant Rabi-pulse model. A pODMR resonance is present.
