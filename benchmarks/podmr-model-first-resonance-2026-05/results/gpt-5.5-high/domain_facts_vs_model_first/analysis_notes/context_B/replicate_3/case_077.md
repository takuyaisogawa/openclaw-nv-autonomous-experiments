Case: podmr_063_2026-05-17-064555

I used the provided sequence XML to identify the active experiment. The sequence is Rabimodulated with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active readouts are:

- readout 1: detection immediately after optical polarization, before the microwave pulse; this is the true m_S = 0 reference.
- readout 2: detection after the active rabi_pulse_mod_wait_time pulse.

The "Acquire 1 level reference" branch is inactive because full_expt = 0, so there is no separately acquired m_S = +1 reference in these data. The active microwave pulse has length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, and the 52 ns pulse is exactly 13 samples after rounding.

Quantitative expected signal model:

Given the stated calibration, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a square pulse, the transition probability at detuning Delta is

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

With f_R = 10 MHz and t = 52 ns, the on-resonance transition probability is

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

Using the setup contrast scale of 22% between m_S = 0 and m_S = +1, a resonance should reduce the post-pulse readout to about

1 - 0.22 * 0.996 = 0.781

of the m_S = 0 reference, equivalent to an expected drop of about 11.4 raw-count units for a reference level near 51.8. The expected normalized ratios remain strongly depressed near resonance: about 0.796 at 2.5 MHz detuning, 0.835 at 5 MHz detuning, and 0.940 at 10 MHz detuning.

Observed data:

The combined readout2/readout1 ratios over the sweep have mean 0.992, standard deviation 0.026, minimum 0.950, and maximum 1.033. The largest raw difference readout2 - readout1 is only -2.73 counts at 3.840 GHz, far smaller than the approximately -11.4 count resonant response expected from the active pulse. A least-squares fit of the Rabi lineshape on top of a linear baseline prefers an effective contrast amplitude of only about 0.052, versus the physically expected 0.22, and only weakly improves the baseline-only residual. The small dips are comparable to scan noise and drift, and the stored two averages should not be treated as a strong independent repeatability test because they may reflect tracking cadence.

Decision:

No pODMR resonance is present. The physically expected resonant response for the active 52 ns, mod_depth = 1 pulse would be much larger and more structured than the measured readout2/reference changes.
