Case: podmr_061_2026-05-17-061719

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The provided sequence has one active microwave pulse before the final detection:
  rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- The earlier readout after adj_polarize is the m_S = 0 fluorescence reference.
- full_expt = 0, so the optional +1 reference block is skipped; the second readout is the post-drive signal readout, not an independent +1 reference.
- length_rabi_pulse = 52 ns after sample-rate rounding at 250 MHz.
- mod_depth = 1 in the provided sequence and in Variable_values.

Physical model calculation:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1 and linear scaling, f_R = 10 MHz.
- For a resonant square Rabi pulse, the population transferred to m_S = +1 is
  P(+1) = sin^2(pi * f_R * t).
- With t = 52 ns:
  P(+1) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected signal/reference ratio at resonance is
  1 - 0.22 * 0.996 = 0.781.
- With a reference readout near 50 raw counts, this predicts a resonant driven readout near 39 counts, a drop of about 11 counts.

Observed quantitative comparison:
- The combined reference readout mean is 49.62 counts.
- The combined driven readout mean is 49.09 counts.
- The driven/reference ratios over the scan have mean 0.990 and standard deviation 0.035.
- The minimum combined ratio is 0.925 at 3.880 GHz, corresponding to a drop of about 3.73 counts, not the roughly 11-count drop expected for a resonant near-pi pulse.
- The point at 3.880 GHz is lower in both averages, but its magnitude is much smaller than the mod_depth = 1 model prediction and comparable to scan noise/tracking variation; another average has its deepest ratio at 3.830 GHz.
- Stored averages are only two and may reflect tracking cadence, so they are not a strong repeatability test.

Decision:
The relevant sequence model predicts a large, near-full-contrast resonance feature for a 52 ns, mod_depth = 1 pulse. The measured data show only small, noisy readout-ratio fluctuations without the expected approximately 22% contrast loss. I therefore classify this case as resonance_absent.
