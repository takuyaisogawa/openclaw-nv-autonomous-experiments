Case: podmr_033_2026-05-15-233800

Sequence interpretation:
- The active sequence is Rabimodulated.xml while varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first polarizes the NV and records a detection before the microwave pulse; this is the m_S = 0 fluorescence/reference readout.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The second active detection occurs after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay), so readout 2 is the microwave-pulse signal readout.
- The provided sequence XML and exported variable values give length_rabi_pulse = 52 ns and mod_depth = 1. The raw export also contains an embedded Sequence string showing mod_depth = 0.3, but the XML file supplied for this case and Variable_values list mod_depth = 1, so I use mod_depth = 1 for the active model. I also checked mod_depth = 0.3 as a consistency test.

Physical model calculation:
- Given Rabi frequency f_R = 10 MHz * mod_depth, the resonant transition probability after pulse time t is P = sin^2(pi f_R t).
- With mod_depth = 1 and t = 52 ns, f_R t = 0.52 cycles and P = sin^2(pi * 0.52) = 0.996.
- With setup contrast C = 0.22, the expected resonant signal/reference ratio is 1 - C P = 1 - 0.22 * 0.996 = 0.781, i.e. an expected dip of about 21.9%.
- A detuned two-level check using P(Delta) = (f_R^2/(f_R^2+Delta^2)) sin^2(pi t sqrt(f_R^2+Delta^2)) predicts sampled ratios around resonance of approximately [0.940, 0.835, 0.781, 0.835, 0.940] for detunings -10, -5, 0, +5, +10 MHz.
- If mod_depth were 0.3 instead, f_R = 3 MHz and the resonant contrast would be only 4.9%, with predicted central ratio 0.951; this is much too small for the observed central feature.

Data comparison:
- The minimum readout 2 point is at 3.875 GHz: readout 1 = 38.5, readout 2 = 28.8269.
- The observed signal/reference ratio there is 28.8269 / 38.5 = 0.7488, a dip of 25.1%.
- Excluding the three central points, the off-feature readout-2/reference ratio has mean 0.9745 and standard deviation 0.0386; the central ratio is 5.84 standard deviations below that off-feature level.
- The two stored averages both show a central dip at 3.875 GHz: ratios 0.8008 and 0.6926. These averages are not treated as a strong independent repeatability test, but they do not contradict the model-based feature.

Decision:
The observed central dip magnitude and width match the 52 ns, mod_depth 1 Rabi-pulse pODMR expectation, and the feature is much larger than off-feature fluctuations. A pODMR resonance is present.
