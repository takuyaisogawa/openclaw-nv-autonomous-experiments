Case: podmr_008_2026-05-11-131831

I used only the provided XML and raw export. The active sequence is Rabimodulated.xml with vary_prop mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first acquire a true mS=0 optical reference with adj_polarize followed by detection, then, because full_expt = 0, skip the separate mS=1 reference block. The active experimental readout is after one rabi_pulse_mod_wait_time followed by detection. Thus readout 1 is the mS=0 reference and readout 2 is the post-microwave-pulse readout. The pulse parameters from the provided sequence/Variable_values are length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative model:

Given the supplied setup calibration, the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For a resonant square pulse, the transferred population is

P = sin^2(pi * f_Rabi * t).

With f_Rabi = 10 MHz and t = 52 ns:

P = sin^2(pi * 10e6 * 52e-9) = 0.996.

The supplied contrast scale between mS = 0 and mS = +1 is about 22%, so an on-resonance point should reduce the post-pulse fluorescence relative to the mS=0 reference by approximately

0.22 * 0.996 = 0.219, or 21.9%.

For the observed readout 1 values, that would put a resonant readout 2 point around 14.6 to 16.8 counts over this scan. Instead, the measured readout 2 values are all 18.6 to 21.2 counts. The pointwise fractional drop 1 - readout2/readout1 has mean 0.012, standard deviation 0.055, and maximum 0.119. Only one point exceeds half of the expected 21.9% drop, and no point approaches the expected full resonant signal. Several points have readout 2 above readout 1, inconsistent with a robust pODMR dip from this pulse.

The stored per-average traces show strong slow drift/tracking cadence structure, so I did not treat the two averages as an independent reproducibility test. The combined readouts also lack a quantitatively plausible resonant fluorescence decrease. Decision: resonance_absent.
