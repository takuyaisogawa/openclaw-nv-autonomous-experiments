<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_028

Sequence/readout identification:
- Active sequence: Rabimodulated.xml / Rabi-modulated pODMR scan varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize and detect the bright m_S = 0 reference, then run the modulated Rabi pulse and detect the signal. The conditional +1 reference block is inactive because full_expt = 0.
- Readout 1 role: bright m_S = 0 reference.
- Readout 2 role: post-microwave Rabi-pulse signal.
- mod_depth = 1 from the provided XML and exported variable values.
- Active pulse duration: length_rabi_pulse = 52 ns, rounded at 250 MS/s and unchanged.

Quantitative physical model:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant pi-pulse time is 1/(2 f_R) = 50 ns.
- With t = 52 ns, the resonant transition probability is sin^2(pi f_R t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With setup contrast C = 0.22, the expected fractional PL drop at resonance is C * P = 0.219, about 22%.
- Using the rectangular-pulse off-resonant model
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * sqrt(f_R^2 + delta^2) * t),
  the observed readout 2 can be modeled as readout2 = readout1 * (1 - C * P(freq - f0)).

Observed signal:
- Near 3.875 GHz: readout1 = 44.404, readout2 = 34.673, fractional drop = 9.731 / 44.404 = 0.219.
- Near 3.880 GHz: readout1 = 43.058, readout2 = 34.077, fractional drop = 8.981 / 43.058 = 0.209.
- Adjacent points show a broadened dip consistent with the finite 52 ns pulse: drops of 12.6% at 3.870 GHz and 14.0% at 3.885 GHz.

Explicit fit:
- Fitting the fixed-contrast physical model gives best center f0 = 3.8779 GHz with RMSE = 1.46 counts.
- Allowing contrast to fit gives f0 = 3.8779 GHz, contrast = 0.239, RMSE = 1.43 counts.
- A simple nonresonant linear readout2-vs-readout1 null model gives RMSE = 2.92 counts, about 4.14 times larger SSE than the fitted physical resonance model.

Decision:
The dip magnitude, center, and width are quantitatively consistent with the expected near-pi-pulse pODMR response for the active sequence. A pODMR resonance is present.
