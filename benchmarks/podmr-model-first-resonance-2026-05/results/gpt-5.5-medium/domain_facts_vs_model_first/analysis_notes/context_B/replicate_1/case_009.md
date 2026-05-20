Case: podmr_016_2026-05-12-120649

Inputs used:
- sequence XML: inputs/sequence.xml
- raw data: inputs/raw_export.json

Active sequence and readout roles:
- SequenceName in the export is Rabimodulated.xml.
- The sequence has full_expt = 0, so the optional +1 reference branch is inactive.
- The active detections are:
  1. adj_polarize followed by detection: this is the true m_S = 0 reference readout.
  2. a modulated Rabi pulse followed by detection: this is the pulsed pODMR signal readout.
- The active pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- From inputs/sequence.xml and exported Variable_values, length_rabi_pulse = 52 ns and mod_depth = 1. The embedded Sequence text in raw_export.json contains an older-looking default line with mod_depth = 0.3, but the requested provided sequence XML and Variable_values both specify mod_depth = 1, so I used mod_depth = 1 for the physical model.

Physical model calculation:
- Given setup Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Rabi frequency scales linearly with mod_depth, so here f_R = 10 MHz.
- Pulse duration t = 52 ns.
- For a resonant square Rabi pulse, the transferred population is P_1 = sin^2(pi * f_R * t).
- pi * f_R * t = pi * 10e6 * 52e-9 = 1.6336 rad.
- P_1 = sin^2(1.6336) = 0.9961.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance fluorescence drop in the pulsed signal readout relative to the m_S = 0 reference is 0.22 * 0.9961 = 0.2191, or about 21.9%.
- Therefore a resonance should produce signal/reference near 1 - 0.2191 = 0.7809 at the resonance point, aside from noise and tracking drift.

Observed quantitative comparison:
- The combined reference readout is readout 1 and the pulsed signal readout is readout 2.
- The measured signal/reference ratios across the scan are:
  1.0117, 1.0652, 1.0340, 1.0333, 1.0143, 1.0000, 1.0924, 1.0613, 1.0205, 1.0110, 0.9918, 1.0286, 1.0326, 1.0295, 0.9468, 0.9881, 1.0963, 0.9781, 0.9467, 0.9719, 1.0048.
- Minimum observed ratio = 0.9467, corresponding to only a 5.3% drop.
- Mean ratio = 1.0171 with population standard deviation = 0.0395.
- The largest negative signal-reference differences are -1.365 counts at 3.895 GHz and 3.915 GHz. At the local reference level near 25 counts, the expected 21.9% resonance dip would be about 5.5 counts, much larger than observed.

Decision:
The active pulse should be nearly a pi pulse at mod_depth = 1, so a real pODMR resonance should cause an approximately 22% signal reduction relative to the m_S = 0 reference. The data never approaches that contrast-scale response and instead shows only small, scattered signal/reference deviations comparable to drift/noise. I therefore decide resonance_absent.
