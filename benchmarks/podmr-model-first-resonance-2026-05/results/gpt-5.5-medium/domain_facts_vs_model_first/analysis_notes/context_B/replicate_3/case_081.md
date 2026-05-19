<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_081

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence identification:
- Sequence: Rabimodulated.xml.
- The active path first polarizes the NV and detects immediately. This is the true m_S = 0 reference readout.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The active signal block then applies rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.
- Therefore readout 1 is the polarized m_S = 0 reference, and readout 2 is the post-Rabi-pulse pODMR signal.
- mod_depth = 1 from the provided sequence XML variable values.
- length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz, round(length_rabi_pulse * sample_rate) = round(13 samples), so the active duration remains 52 ns.

Physical model calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the on-resonance transition probability for a square pulse is:
  P_exc(0) = sin^2(pi * f_R * t)
           = sin^2(pi * 10e6 * 52e-9)
           = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, an on-resonance pulse should reduce the signal readout by:
  contrast_drop_fraction = 0.22 * 0.996 = 0.219.
- The mean measured m_S = 0 reference readout is 48.920 counts, so the expected on-resonance readout-2 drop is:
  48.920 * 0.219 = 10.72 counts.
- Expected on-resonance readout 2 is therefore about 38.20 counts if a resonance is driven near the scan.
- For finite detuning, I used the square-pulse response:
  P_exc(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).
  Around a candidate center this still predicts multi-count depressions over nearby 5 MHz samples, for example about 8.1 counts at +/-5 MHz and about 2.9 counts at +/-10 MHz from line center.

Measured data comparison:
- Scan: 3.825 GHz to 3.925 GHz in 5 MHz steps, 21 points.
- Combined readout means:
  mean(readout 1) = 48.920
  mean(readout 2) = 48.757
  mean(readout 2 - readout 1) = -0.163 counts.
- The standard deviation of readout 2 - readout 1 over the scan is 1.568 counts.
- The largest negative combined difference is -2.346 counts at 3.885 GHz.
- No point approaches the expected roughly -10.7 count on-resonance signal. The observed small negative excursions are comparable to the scan scatter, and stored averages are not treated as a strong independent repeatability test because they may reflect tracking cadence.

Decision:
The active pulse should produce a large negative pODMR feature if a resonance is present in this scan, but the measured readout-2 signal remains near the m_S = 0 reference with only small, noisy excursions. I therefore decide that a pODMR resonance is absent.
