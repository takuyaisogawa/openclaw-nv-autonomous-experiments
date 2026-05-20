Sequence and readout interpretation:

The active sequence is Rabimodulated.xml with vary_prop = mw_freq. The instructions first run adj_polarize and detection, so readout 1 is the polarized m_S = 0 / true zero-level reference. Because full_expt = 0, the optional 1-level reference block is skipped. The sequence then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay) and performs detection, so readout 2 is the post-Rabi-pulse signal readout.

Relevant pulse parameters from the provided XML/export:

- length_rabi_pulse = 52 ns, rounded at 250 MS/s but unchanged because 52 ns is 13 samples.
- mod_depth = 1.
- mw_freq is swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- freqIQ = 50 MHz.
- full_expt = 0, so there is no independent m_S = +1 reference in the stored readouts.

Quantitative expected signal model:

Use the stated setup calibration: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For a resonant rectangular pulse, the spin-transfer probability is

P = sin^2(pi * f_R * tau).

Here f_R = 10 MHz and tau = 52 ns, so

P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

With the stated optical contrast scale of about 22% between m_S = 0 and m_S = +1, a true on-resonance point should reduce the post-pulse readout by approximately

0.22 * 0.996 = 0.219,

or about 21.9% relative to the zero-level reference. The mean readout-1 level is 52.72 counts, so the expected on-resonance drop is about 11.55 counts.

For finite detuning, the simple two-level rectangular-pulse model is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).

This predicts a Rabi-broadened feature over several 5 MHz scan points around resonance, not a single isolated one-point excursion.

Observed data:

- readout 1 mean = 52.72, standard deviation = 1.28 counts.
- readout 2 mean = 52.73, standard deviation = 0.94 counts.
- readout 2 - readout 1 mean = 0.007 counts, standard deviation = 1.36 counts.
- normalized post/reference signal mean = +0.0006, standard deviation = 0.0252.
- normalized post/reference minimum = -0.0710 at 3.920 GHz.

The deepest negative point is only about a 7.1% drop, roughly one third of the expected 21.9% resonant signal. It is also isolated: neighboring points do not show the expected detuned-pulse lineshape or a broad dip. Stored averages are not treated as a strong independent repeatability test because they can reflect tracking cadence.

Decision:

The active pulse should produce a large near-pi-pulse pODMR response if a resonance is present. The measured post-pulse/reference contrast is small, noisy, and lacks the expected Rabi-broadened structure. I therefore classify this case as resonance_absent.
