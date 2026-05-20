Case podmr_045_2026-05-16-234216.

I used the provided sequence XML and raw export only. The active sequence is Rabimodulated.xml / Rabi-modulated pODMR with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML has full_expt = 0, so the "Acquire 1 level reference" block is inactive. The executed readouts are:

- readout 1: bright m_S = 0 reference after adj_polarize and detection, before the microwave pulse.
- readout 2: signal readout after rabi_pulse_mod_wait_time and detection.

Relevant pulse parameters from the provided XML are length_rabi_pulse = 52 ns and mod_depth = 1. The microwave pulse is therefore the active pODMR perturbation. The adiabatic inversion variables are not active because the block containing them is gated off by full_expt = 0.

Quantitative expected-signal model:

Use the two-level resonant Rabi transition probability P = sin^2(pi f_R t). The stated setup gives f_R = 10 MHz at mod_depth = 1, and here t = 52 ns. Thus:

P = sin^2(pi * 10e6 * 52e-9) = 0.996.

The stated optical contrast between m_S = 0 and m_S = +1 is about 22%. The measured bright reference mean is 48.85 counts, so an on-resonance pi-like pulse should lower the post-microwave readout by approximately:

48.85 * 0.22 * 0.996 = 10.70 counts.

Thus the expected resonance signature is readout2 - readout1 near -10.7 counts at resonance, modulo experimental noise and linewidth broadening.

Measured comparison:

Across the 21 frequency points, readout2 - readout1 has mean -0.084 counts, standard deviation 1.039 counts, and minimum -1.827 counts at 3.845 GHz. This is only about 17% of the expected resonant drop and is within ordinary point-to-point scatter. There is no broad or localized negative feature close to the expected approximately -10.7 count response. Stored averages do not provide a strong independent repeatability test, and their minima occur at different scan points with amplitudes of only a few counts.

Decision: resonance_absent. The active pulse should have produced a large, obvious pODMR dip if a resonance were present in the scanned range, but the measured post-microwave readout remains statistically consistent with the bright reference within approximately count-level noise.
