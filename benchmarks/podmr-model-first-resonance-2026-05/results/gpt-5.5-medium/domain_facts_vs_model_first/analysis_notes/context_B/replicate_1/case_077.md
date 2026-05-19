<!-- Model-generated analysis note. Not a ground-truth label. -->

Active sequence and readout roles

The provided XML is Rabimodulated.xml. The executed scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the sequence, full_expt = 0, so the "Acquire 1 level reference" block is skipped. Therefore the two combined readouts are:

- readout 1: initial bright m_S = 0 reference after optical polarization and detection
- readout 2: detection after the active Rabi-modulated microwave pulse

The active microwave pulse is:

- function: rabi_pulse_mod_wait_time
- length_rabi_pulse: 52 ns
- mod_depth: 1
- switch_delay: 100 ns

Quantitative expected-signal model

Given the supplied setup facts, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a resonant square pulse, the transferred population is modeled as

P_1 = sin^2(pi * f_Rabi * t)

with f_Rabi = 10 MHz and t = 52 ns. This gives:

pi * f_Rabi * t = pi * 0.52 = 1.6336 rad
P_1 = sin^2(1.6336) = 0.996

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance pulse should reduce the post-pulse fluorescence by:

0.22 * 0.996 = 0.219

Thus the expected resonant ratio is:

readout2 / readout1 = 1 - 0.219 = 0.781

This is a large expected effect. Even allowing detuning within the 5 MHz frequency grid, the nearest sampled point to a resonance should still show a strong dip because the Rabi frequency is about 10 MHz and the pulse is near a pi pulse. A point 5 MHz detuned would still be expected to show roughly 16% contrast in this simple driven two-level model.

Observed data check

The observed combined readout2/readout1 ratios across the scan are:

min = 0.950
max = 1.033
mean = 0.992
standard deviation = 0.026

The deepest observed relative reduction is only about 5.0%, at 3.840 GHz, and it is not close to the expected resonant ratio of about 0.781. The observed post-pulse readout is about 9 to 13 counts higher than the resonant model prediction at every sampled frequency. The per-average traces show similar small fluctuations and common drift, but the stored averages are only two averages and should mainly be treated as tracking cadence, not a robust repeatability test.

Decision

The active pulse should have produced an approximately 22% fluorescence reduction if a pODMR resonance were present in the scanned range. The measured readout2/reference ratios remain near unity with only few-percent fluctuations and no near-pi-pulse contrast feature. Therefore this case is classified as resonance_absent.
