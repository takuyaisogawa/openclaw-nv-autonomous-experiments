Sequence and readout identification:
- The provided sequence is Rabimodulated.xml / Rabimodulated.
- full_expt is 0, so the optional mS=+1 reference block is inactive.
- The active detections are therefore:
  1. readout 1: after adj_polarize, before microwave pulse, the bright mS=0 reference.
  2. readout 2: after the modulated Rabi pulse, the signal readout.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns.
- mod_depth = 1. The setup Rabi frequency is therefore approximately 10 MHz.

Physical model calculation:
- Use a driven two-level square-pulse model:
  P_transition(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
- With f_R = 10 MHz and t = 52 ns, the on-resonance transition probability is:
  sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated mS=0 to mS=+1 contrast scale of 22%, an on-resonance pi-pulse-like response should make readout 2 about:
  1 - 0.22 * 0.996 = 0.781 of readout 1.
- On a roughly 54-count baseline, this is an expected readout 2 dip of about 11.8 counts relative to readout 1.

Observed quantitative comparison:
- Combined readout 1 mean: 53.855 counts.
- Combined readout 2 mean: 54.175 counts.
- readout2 - readout1 mean: +0.320 counts.
- readout2/readout1 mean: 1.006.
- Minimum observed readout2/readout1 ratio across the scan: 0.969.
- The largest observed negative readout2 - readout1 value is -1.654 counts, far smaller than the approximately -11.8-count resonant expectation.
- A fixed 22% contrast square-pulse model expects a minimum ratio of 0.781 at resonance. No scan point approaches that scale.
- A free-amplitude fit to the square-pulse lineshape gives a best contrast amplitude of about -0.030, i.e. the best fit prefers the opposite sign and only a few percent magnitude, not the expected 22% dip.
- The two stored averages have different absolute count levels, consistent with tracking cadence/brightness changes, and are not a strong independent repeatability test. Their normalized ratios also remain near unity.

Decision:
The active pulse should produce a large readout-2 suppression at resonance, but the measured signal readout is not suppressed relative to the mS=0 reference at the required scale. I therefore decide resonance_absent.
