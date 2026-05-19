<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_023 analysis note

I used only inputs/raw_export.json, inputs/raw_readouts.png, and inputs/sequence.xml.

Sequence identification:
- SequenceName: Rabimodulated.xml.
- Active sequence path: full_expt = 0, so the optional mS=+1 reference block is skipped.
- Readout 1 role: after adj_polarize and detection, a polarized mS=0 / bright reference.
- Readout 2 role: after one rabi_pulse_mod_wait_time pulse, then detection.
- Relevant microwave pulse: length_rabi_pulse = 52 ns after sample-rate rounding.
- Relevant modulation depth: Variable_values gives mod_depth = 1 for this saved scan.

Quantitative expected signal:
- Given setup contrast between mS=0 and mS=+1 is about 22%.
- Given Rabi frequency is about 10 MHz at mod_depth = 1.
- For a resonant square pulse, population transfer P1 = sin^2(pi * f_R * t).
- With f_R = 10 MHz and t = 52 ns, P1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Using the mean readout-1 bright level 41.44, expected resonant readout-2 is
  41.44 * (1 - 0.22 * 0.996) = 32.36.
- Detuned square-pulse model used:
  P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
  This gives approximate expected readout values of 34.61 at +/-5 MHz,
  38.95 at +/-10 MHz, and 41.34 at +/-15 MHz from the same baseline.

Observed signal:
- Readout 2 off-resonance baseline, excluding 3.865 to 3.885 GHz, is 41.07.
- Readout 2 minimum is 31.31 at 3.875 GHz.
- Observed dip is 9.76 counts, or 23.8% of the off-resonance readout-2 baseline.
- This is consistent with the expected 22% full-contrast dip for a nearly pi pulse.
- Stored average 1 has readout 2 at the minimum point = 32.42, with outside baseline 41.82.
- Stored average 2 has readout 2 at the minimum point = 30.19, with outside baseline 40.32.
  The averages are not treated as a strong independent repeatability test, but both contain the central dip.
- A fixed-contrast square-pulse line-shape fit improved SSE from 199.61 for a flat model to 29.32, with best center near 3.8774 GHz.

Decision:
The measured readout-2 dip amplitude, frequency-localized shape, and magnitude agree with the quantitative resonant Rabi-pulse expectation. I therefore decide that a pODMR resonance is present.
