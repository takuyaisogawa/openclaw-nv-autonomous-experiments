<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_060

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The active instructions first run adj_polarize followed by detection, so readout 1 is the optically polarized m_S = 0 reference.
- full_expt = 0, so the separate m_S = +1 reference branch is disabled.
- The active signal operation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection, so readout 2 is the post-Rabi-pulse pODMR signal.
- From the provided XML and Variable_values, mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. At 250 MS/s this is exactly 13 samples, so the rounded pulse duration remains 52 ns.

Physical model calculation:
- Given setup contrast C = 0.22 between m_S = 0 and m_S = +1.
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1.
- For a rectangular resonant pulse, transition probability P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)), with t = 52 ns and delta in Hz.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.996.
- Expected fluorescence contrast on resonance is C * P(0) = 0.22 * 0.996 = 0.219, i.e. readout 2 should be about 21.9% lower than the m_S = 0 reference. Around a 52 count reference this is an expected drop of about 11.4 counts.

Observed normalized signal:
- The combined readout 1 mean is 52.16 counts and readout 2 mean is 51.12 counts.
- The normalized contrast 1 - readout2/readout1 has mean 0.019, standard deviation 0.029, minimum -0.018, and maximum 0.086.
- The largest observed drop is therefore only 8.6%, less than half the expected resonant 21.9% contrast, and it occurs as an isolated point rather than the expected pulse-broadened resonance feature.

Model fit check:
- I fit the measured readout2/readout1 ratio to base - A * P(f - f0), scanning f0 over and beyond the measured frequency window.
- The best unconstrained fit selected a negative amplitude A = -0.049, which is the wrong sign for pODMR contrast and indicates the data do not prefer the expected dip shape.
- Forcing the physical amplitude A = 0.22 gives a poor fit and places the best center outside the scan window, because an in-window resonance of this strength would create a much deeper dip than observed.

Decision:
The expected pODMR resonance for this sequence should be a near-pi-pulse contrast dip of roughly 22% in readout 2 relative to readout 1. The observed normalized readout differences are small, noisy, and not compatible with that quantitative model. I therefore decide that a pODMR resonance is absent.
