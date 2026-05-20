Case podmr_064_2026-05-17-065956

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles

The active saved sequence name is Rabimodulated.xml. The executable instruction path polarizes the NV, takes a detection readout, waits, skips the optional "Acquire 1 level reference" block because full_expt = 0, applies one rabi_pulse_mod_wait_time pulse, then takes a second detection readout. Thus readout 1 is the true m_S = 0 fluorescence reference, and readout 2 is the post-microwave pODMR readout. There is no active m_S = +1 reference readout in this run.

Relevant pulse settings from the provided sequence XML are length_rabi_pulse = 52 ns and mod_depth = 1. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative physical model

Use the provided setup facts: contrast between m_S = 0 and m_S = +1 is about 22%, and Rabi frequency is about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. For a resonant square pulse, the transferred population is

P_transfer = sin^2(pi * f_Rabi * tau).

With f_Rabi = 10 MHz and tau = 52 ns:

P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996.

The expected resonant fluorescence reduction in readout 2 relative to readout 1 is therefore

0.22 * 0.996 = 0.219, or about 21.9%.

The mean readout level is about 51 counts, so the expected resonant dip size is about 11.2 counts if the microwave hits a real transition within the scan. Even if the embedded exported sequence text value mod_depth = 0.3 were used instead, the same model gives f_Rabi = 3 MHz, P_transfer = 0.222, expected contrast = 4.87%, or about 2.5 counts.

Observed data check

The combined readouts have mean readout 1 = 50.97 and mean readout 2 = 50.92. The pointwise difference readout2 - readout1 has mean -0.052 counts and standard deviation 1.38 counts. The most negative point is -2.85 counts at 3.890 GHz, and the largest positive point is +3.13 counts at 3.915 GHz. The minimum readout2/readout1 ratio is 0.946, but it is an isolated fluctuation, not a clear resonance-shaped dip, and it is far smaller than the approximately 0.781 ratio expected for the active XML pulse at mod_depth = 1.

Decision

A pODMR resonance is absent. The active pulse should produce a large, obvious dip if a resonance were present, while the observed trace shows only small noisy fluctuations around no contrast and no robust frequency-localized pODMR feature.
