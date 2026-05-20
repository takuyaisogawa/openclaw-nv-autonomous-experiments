Case: podmr_041_2026-05-16-224136

I used inputs/sequence.xml as the sequence source. The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz. The instructions first polarize and detect, then because full_expt = 0 they skip the optional m_S = +1 reference block, then apply one rabi_pulse_mod_wait_time pulse and detect again. Therefore readout 1 is the polarized m_S = 0 reference and readout 2 is the pODMR signal after the microwave pulse.

Relevant active pulse settings from the XML:
- length_rabi_pulse = 52 ns, rounded at 250 MS/s and unchanged because 52 ns is 13 samples.
- mod_depth = 1.
- do_adiabatic_inversion is true as a variable, but the adiabatic-inversion block is inside the skipped full_expt block, so it is not active for the pODMR signal.

Quantitative expected-signal model:
- Given Rabi frequency approximately 10 MHz at mod_depth = 1, use Omega = 10 MHz.
- For a square resonant Rabi pulse, population transfer probability is P = sin^2(pi * Omega * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance scan point should show a fractional fluorescence drop of about 0.22 * 0.996 = 0.219, or about 21.9%.
- With the observed reference readout near 46 counts, the expected resonant readout 2 value is about 46 * (1 - 0.219) = 35.9 counts, a drop of about 10.1 counts relative to readout 1.

Measured data summary from raw_export.json:
- readout 1 mean = 46.354, standard deviation = 0.459, range = 45.538 to 47.077.
- readout 2 mean = 46.142, standard deviation = 1.363, range = 43.500 to 48.327.
- readout2 - readout1 mean = -0.212, standard deviation = 1.435, range = -2.596 to +2.212.
- The largest apparent negative point is at 3.895 GHz, where readout 1 = 46.096 and readout 2 = 43.500, a 5.6% drop from readout 1. This is much smaller than the approximately 21.9% drop expected for a resonant 52 ns pulse at mod_depth = 1.

Decision:
The expected resonant response is a near-pi-pulse scale dip of about 10 counts, but the observed scan contains only small, non-systematic fluctuations of a few counts and no feature with the predicted magnitude. Stored averages here should not be treated as a strong independent repeatability test. I therefore decide that no pODMR resonance is present.
