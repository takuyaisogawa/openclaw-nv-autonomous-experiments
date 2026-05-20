Case: podmr_012_2026-05-16-121601

Sequence interpretation:
- The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the provided sequence XML, mod_depth = 1 and length_rabi_pulse = 52 ns. At sample_rate = 250 MHz, 52 ns rounds to 13 samples, so the executed pulse duration remains 52 ns.
- full_expt = 0, so the optional separate mS = +1 reference block is disabled.
- Therefore readout 1 is the true mS = 0 reference after optical polarization, and readout 2 is the readout after the modulated Rabi microwave pulse.

Quantitative physical model:
- The setup Rabi frequency is about 10 MHz at mod_depth = 1.
- For a square pulse of duration t = 52 ns, the two-level transition probability as a function of detuning df is:
  P1(df) = (fR^2 / (fR^2 + df^2)) * sin^2(pi * t * sqrt(fR^2 + df^2)),
  using fR and df in cycles/s.
- On resonance, P1(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.996.
- With a 22% fluorescence contrast between mS = 0 and mS = +1, the expected on-resonance normalized readout is 1 - 0.22 * 0.996 = 0.781, i.e. a 21.9% drop relative to the mS = 0 reference.
- The same model gives approximate drops of 16.5% at 5 MHz detuning, 6.0% at 10 MHz, 0.3% at 15 MHz, and only small off-resonant oscillatory structure farther away.

Observed data calculation:
- The mean readout 1 level is 42.08 counts, and the mean readout 2 level is 40.47 counts.
- Normalizing pointwise as readout2/readout1 gives an off-resonant mean of 0.9805 with standard deviation 0.0251 when points more than 20 MHz from the deepest dip are used.
- The minimum normalized value is 0.8228 at 3.880 GHz, with readout2 - readout1 = -7.31 counts.
- Relative to the off-resonant normalized mean, the dip is a 16.1% reduction. This is smaller than the ideal 21.9% expectation but close enough given finite sampling, readout noise, line broadening, and imperfect contrast realization.
- A grid fit of the Rabi response model to the normalized ratios gives a best center near 3.8785 GHz, baseline 0.993, and contrast amplitude about 0.178, consistent with a real driven transition.

Decision:
The sequence readout roles and quantitative Rabi model predict a strong dip in readout 2 relative to readout 1 at resonance. The data show a broad, centered reduction near 3.88 GHz of the expected sign and comparable magnitude, so a pODMR resonance is present.
