<!-- Model-generated analysis note. Not a ground-truth label. -->

# pODMR decision note

Case: case_091

Sequence identification from inputs/sequence.xml: the active sequence is Rabimodulated.xml. The instructions first polarize and detect, giving readout 1 as the true m_S=0 fluorescence reference. Because full_expt = 0, the optional m_S=1 reference branch is skipped. The sequence then applies one rabi_pulse_mod_wait_time pulse and detects again, so readout 2 is the pulsed pODMR signal readout. The active pulse uses length_rabi_pulse = 52 ns and mod_depth = 1. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative model: use the stated setup scale f_R = 10 MHz * mod_depth and contrast C = 0.22 between m_S=0 and m_S=+1. For a resonant square pulse, the transferred population is P = sin^2(pi f_R t). With mod_depth = 1 and t = 5.20e-08 s, f_R = 1e+07 Hz and P = 0.9961. The expected fluorescence drop in the signal readout at resonance is C*P = 0.2191, or 11.14 raw-count units around the measured baseline 50.85.

Observed data: readout 1 mean = 50.94, readout 2 mean = 50.77. The pointwise signal-reference difference readout2-readout1 has mean -0.17, standard deviation 1.19, minimum -2.19, and maximum 2.63. There is no frequency point or coherent feature approaching the predicted approximately 11.1-count resonant drop; the observed variations are small and irregular on the scale of the expected pODMR contrast.

Decision: resonance_absent.
