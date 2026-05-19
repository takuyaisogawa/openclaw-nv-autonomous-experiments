<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_073

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence identification:
- Sequence: Rabimodulated.xml.
- Scan variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps, 21 points.
- The active instructions acquire a true m_S = 0 reference first:
  adj_polarize -> detection -> wait_for_awg.
- full_expt = 0, so the commented/conditional m_S = 1 reference block is inactive.
- The active signal readout is then:
  rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) -> detection.
- Therefore readout 1 is the bright m_S = 0 reference and readout 2 is the post-microwave Rabi-pulse signal readout.
- From the provided sequence XML and exported variable values: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz. The pulse is already on a 4 ns sample grid.

Expected signal model:
- Setup contrast between m_S = 0 and m_S = +1 is about C = 0.22.
- Rabi frequency is about 10 MHz at mod_depth = 1, scaling linearly with mod_depth.
- For a resonant rectangular pulse, population transfer is
  P = sin^2(pi * f_R * tau).
- With f_R = 10 MHz and tau = 52 ns:
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected fractional fluorescence/readout drop at resonance:
  C * P = 0.22 * 0.996 = 0.219, about 21.9%.
- The mean readout-1 level is 42.670, so the expected resonant drop is
  42.670 * 0.219 = 9.35 raw-readout units. Thus a resonant point should have readout 2 near 33.3 if the readout-1 reference is near 42.7.

Observed quantitative comparison:
- Mean readout 1: 42.670.
- Mean readout 2: 42.108.
- Mean(readout2 - readout1): -0.562 raw-readout units.
- Observed fractional drop: 0.562 / 42.670 = 1.32%.
- Standard deviation of paired differences across the 21 scan points: 1.100 units.
- Standard error of the mean paired difference: 0.240 units.
- Paired t statistic for a nonzero average difference: -2.34, but the magnitude is only about 6% of the expected resonant drop.
- Pointwise readout2 - readout1 ranges from -2.865 to +1.519 units. Even the largest observed depression is only about 31% of the modeled resonant depression and is not a consistent spectral feature.

Decision:
The active pulse should produce a large, near-pi-pulse pODMR dip if the scanned transition is resonant. The observed data show only a small readout offset/noise-scale fluctuation, with no approximately 9-unit depression or coherent resonance-shaped feature. I therefore decide resonance_absent.
