The active sequence is Rabimodulated.xml / Rabimodulated, scanning mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. In the provided sequence, full_expt = 0, so the optional m_S = +1 reference block is inactive. The two recorded readouts are therefore:

- readout 1: after adj_polarize and detection, the polarized m_S = 0 fluorescence reference.
- readout 2: after a Rabi-modulated microwave pulse and detection, the signal readout.

The relevant pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns. The provided sequence file has mod_depth = 1; the exported variable values also list mod_depth = 1, although the embedded saved sequence text contains an older-looking default of 0.3. Using the provided sequence and variable values gives mod_depth = 1.

Physical model calculation:

The setup contrast between m_S = 0 and m_S = +1 is about C = 0.22. The Rabi frequency is about f_R = 10 MHz at mod_depth = 1. For a square pulse at detuning Delta, the transferred population is modeled as

P1(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

With t = 52 ns:

- On resonance, P1 = sin^2(pi * 10 MHz * 52 ns) = 0.996, so the expected readout-2 fluorescence drop relative to the m_S = 0 readout is C * P1 = 0.219, about 22%.
- At 5 MHz detuning, expected drop is about 16.5%.
- At 10 MHz detuning, expected drop is about 6.0%.
- At 20 MHz detuning, expected drop is about 1.1%.
- At 50 MHz detuning, expected drop is about 0.7%.

Measured combined ratios readout2/readout1 show a localized dip:

- Edge median ratio from the outer four points on each side is 0.974.
- Minimum ratio is 24.2885 / 31.4231 = 0.773 at 3.875 GHz, a drop of 0.201 relative to the edge median.
- Adjacent points at 3.870, 3.880, and 3.885 GHz also show depressed ratios of 0.882, 0.804, and 0.813, respectively.
- Away from this band the ratios mostly return near the edge level, modulo tracking and readout noise.

The observed maximum normalized dip of about 20% is close to the 21.9% drop expected for a near-pi pulse on resonance. Its width over the neighboring 5 MHz-spaced scan points is compatible with the finite 52 ns pulse response and experimental drift/noise. Stored averages show large tracking-related trends, so I do not treat the two averages as a strong independent repeatability test, but the combined normalized readout contrast matches the quantitative pODMR resonance model.

Decision: resonance_present.
