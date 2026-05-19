<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_020

I used the supplied sequence XML and raw export contents only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- full_expt = 0, so the conditional mS = 1 reference block is inactive.
- The active readouts are therefore:
  - readout 1: polarized true mS = 0 reference after adj_polarize and detection.
  - readout 2: signal after rabi_pulse_mod_wait_time followed by detection.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns.
- sample_rate = 250 MHz, so 52 ns rounds to 13 samples, still 52 ns.
- mod_depth = 1 from the provided variables/sequence values.

Quantitative expected-signal model:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, use f_R = 10 MHz.
- For a rectangular pulse, transition probability versus detuning delta is:
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
- With t = 52 ns, on resonance P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated mS=0 to mS=+1 contrast scale of 22%, the expected on-resonance post-pulse readout ratio is:
  S2/S1 = 1 - 0.22 * P(0) = 0.781.
- For a typical reference readout near 40 counts, this predicts an on-resonance signal near 31.2 counts.

Measured data comparison:
- The normalized ratio readout2/readout1 has its main minimum at 3.875 GHz: 30.635 / 40.962 = 0.748.
- The adjacent point at 3.880 GHz is 30.327 / 39.192 = 0.774.
- The fractional drops at these two points are 25.2% and 22.6%, matching the expected 22% contrast scale for an almost pi pulse.
- A rectangular-pulse model fit over center frequency with a single baseline scale gives best center near 3.8785 GHz, baseline scale 0.986, and reduces normalized-ratio SSE by about 81% compared with a constant-ratio null model.

Decision:
The dip in readout 2 relative to the simultaneously acquired mS=0 reference has the expected amplitude, frequency-localized shape, and width scale for a pODMR resonance under this 52 ns, mod_depth 1 pulse. Stored averages are consistent with the same feature but are not treated as an independent repeatability test.
