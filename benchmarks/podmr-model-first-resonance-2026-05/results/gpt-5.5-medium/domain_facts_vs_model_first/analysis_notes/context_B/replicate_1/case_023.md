<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_023 analysis

Active sequence and readout roles:
- The sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence has full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 is the "true 0 level reference": laser polarization followed by detection, so it is the bright m_S = 0 reference.
- Readout 2 is the pODMR measurement: laser polarization, a Rabi-modulated microwave pulse, then detection.
- The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. The sample-rate rounding at 250 MHz leaves 52 ns unchanged.

Quantitative model:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1 and linear scaling with mod_depth, the expected on-resonance Rabi frequency is 10 MHz.
- For a resonant square pulse, the population transfer probability is P = sin^2(pi * f_Rabi * tau).
- With f_Rabi = 10 MHz and tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance readout-2 reduction relative to the bright reference is 0.22 * 0.996 = 0.219, or about 22%.

Data comparison:
- Using readout2/readout1 to reduce common drift, the off-resonant baseline ratio excluding +/-15 MHz around 3.875 GHz is 0.9859 with standard deviation 0.0370.
- The minimum ratio is at 3.875 GHz: readout 1 = 42.4615, readout 2 = 31.3077, ratio = 0.7373.
- The observed relative dip from the off-resonant baseline is (0.9859 - 0.7373) / 0.9859 = 0.252, about 25%.
- This is close to the 22% model expectation for a resonant near-pi pulse, and the ratio excursion is 6.7 baseline standard deviations.
- The adjacent points at 3.870 GHz and 3.880 GHz are also suppressed, giving a frequency-localized dip rather than an isolated one-point fluctuation.

Decision:
The active sequence and quantitative Rabi/contrast model predict a large resonant dip, and the observed readout-2 suppression around 3.875 GHz matches that expectation. A pODMR resonance is present.
