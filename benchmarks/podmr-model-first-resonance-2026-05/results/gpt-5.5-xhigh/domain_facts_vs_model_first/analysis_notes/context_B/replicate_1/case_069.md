I used inputs/sequence.xml for the sequence parameters. The active sequence is Rabimodulated.xml with full_expt = 0, so the "Acquire 1 level reference" block is not active. The two combined readouts are therefore:

- readout 1: true m_s = 0 reference after polarization and detection.
- readout 2: detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth).

The pulse parameters from the provided XML are sample_rate = 250 MHz, length_rabi_pulse = 52 ns, and mod_depth = 1. The pulse length is already exactly 13 samples at 250 MHz, so rounding does not change it.

Quantitative model:

Using the supplied setup calibration, the on-resonance Rabi frequency is 10 MHz at mod_depth = 1. For a square pulse, the driven population transfer versus detuning is

P1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2))

with f_R = 10 MHz and tau = 52 ns. On resonance,

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the given 22% m_s = 0 to m_s = +1 contrast scale, the expected readout2/readout1 ratio at resonance is

1 - 0.22 * 0.996 = 0.781,

or a 21.9% drop. For the observed reference scale near 43.8 raw units, that is about a 9.6 raw-unit dip. The scan step is 5 MHz, so any resonance inside the scanned range has a sampled point within 2.5 MHz; the same model gives P1(2.5 MHz) = 0.929, still implying about a 20.4% drop and a ratio near 0.796.

Data comparison:

The combined readout2/readout1 ratios over the 21 frequency points have mean 0.992, standard deviation 0.036, minimum 0.941, and maximum 1.076. The largest observed negative contrast is therefore only 5.9%, far below the roughly 20-22% dip expected for this pulse if a resonance were sampled. A fixed-contrast resonance model forced inside the scan requires a much deeper minimum than the data contain; allowing the dip amplitude to float gives only about 3.4% fitted contrast, not the expected physical scale. The stored averages show tracking-scale changes, so I did not treat them as a strong independent repeatability test.

Decision: resonance_absent.
