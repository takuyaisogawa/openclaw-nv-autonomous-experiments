Case podmr_045_2026-05-16-234216

I used the provided sequence XML and the exported active variable values to identify the sequence and readout roles before deciding. The sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. Because full_expt = 0, the optional "1 level reference" block is skipped. The two active detections are therefore:

1. readout 1: after adj_polarize, the true m_S = 0 bright reference.
2. readout 2: after rabi_pulse_mod_wait_time, the pODMR/Rabi-modulated signal readout.

The relevant pulse parameters are length_rabi_pulse = 52 ns and mod_depth = 1. The current setup contrast scale between m_S = 0 and m_S = +1 is about 22%. The stated Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so here f_R = 10 MHz.

Explicit model calculation:

For a driven two-level transition, using f_R in cycles/s and detuning Delta in Hz,

P_1(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

The expected signal readout after the microwave pulse is approximately

S_2(Delta) = S_0 * (1 - 0.22 * P_1(Delta)),

with S_0 estimated from readout 1. The measured mean readout 1 is 48.8516 counts, so on resonance:

P_1(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The expected on-resonance drop is therefore

48.8516 * 0.22 * 0.996 = 10.70 counts,

so readout 2 should be near 38.15 counts at a sampled resonance. The frequency step is 5 MHz, so a resonance inside the scanned range should be within at most 2.5 MHz of one sampled point. At Delta = 2.5 MHz, the same model gives P_1 = 0.929 and an expected drop of 9.99 counts. Thus the expected resonance signature is a very large localized readout-2 dip relative to the bright reference.

Observed data check:

Mean(readout 1) = 48.8516, mean(readout 2) = 48.7674, mean(readout 2 - readout 1) = -0.0843 counts. The standard deviation of readout 2 - readout 1 across the scan is 1.039 counts. The largest negative point is only -1.8269 counts at 3.845 GHz, corresponding to -3.65% relative to readout 1. Several points have readout 2 above readout 1, including +2.4038 counts at 3.920 GHz. There is no localized, coherent, approximately 10-count dip in the signal readout.

Stored averages are only two averages and can reflect tracking cadence, so I do not treat their differences as independent repeatability proof. They also do not rescue a resonance interpretation: the expected physical signal for the active pulse would be far larger than the observed scatter.

Decision: resonance absent.
