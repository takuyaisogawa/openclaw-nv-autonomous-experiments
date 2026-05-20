Analysis note for podmr_030_2026-05-13-160024

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

The provided sequence XML defines the active sequence as Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the active instructions, the sequence first performs adj_polarize followed by detection, giving a true m_S = 0 fluorescence reference. Because full_expt = 0, the optional m_S = 1 reference block is skipped. The second acquired readout is after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Therefore readout 1 is the m_S = 0 reference, and readout 2 is the post-Rabi-pulse signal readout. do_adiabatic_inversion is set true as a variable, but it is only inside the skipped full_expt block and is not active.

Quantitative expected signal model:

For this setup, the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. The active pulse has mod_depth = 1, so f_R = 10 MHz. For a resonant square Rabi pulse, the transferred population is P = sin^2(pi f_R t), where t is the pulse duration and f_R is the Rabi oscillation frequency. With t = 52 ns:

P = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so a resonance should reduce the post-pulse fluorescence by approximately 0.22 * 0.996 = 0.219, or 21.9%, relative to the m_S = 0 reference. The measured mean readout 1 is 27.37 counts, so the expected resonant drop is about 27.37 * 0.219 = 6.00 counts. Thus a resonant point should have readout2 - readout1 near -6 counts, modulo noise and lineshape broadening.

Observed data:

Mean readout 1 = 27.37 counts.
Mean readout 2 = 27.73 counts.
Mean(readout2 - readout1) = +0.36 counts.
Standard deviation of readout2 - readout1 across scan points = 1.57 counts.
Minimum observed readout2 - readout1 = -2.26 counts at 3.860 GHz.

The observed minimum deficit is only about 38% of the expected resonant drop and about 1.4 scan-point standard deviations from the mean difference. Other nearby points do not form a coherent dip; the strongest deviations include positive excursions where a resonance model predicts reduced fluorescence. The per-average traces mainly show tracking-scale drift and do not provide a strong independent repeatability test.

Decision: the expected resonant signal for the active pulse sequence is large, about a 6-count fluorescence drop, but the measured post-pulse readout does not show such a dip or a consistent resonance-shaped feature. I classify this case as resonance_absent.
