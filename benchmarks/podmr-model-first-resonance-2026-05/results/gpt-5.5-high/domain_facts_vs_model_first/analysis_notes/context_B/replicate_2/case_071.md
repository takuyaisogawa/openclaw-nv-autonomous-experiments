Case podmr_057_2026-05-17-051839

I used only the isolated inputs for this case. The provided sequence XML and raw export identify the active sequence as Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions have full_expt = 0, so the optional +1 reference block is skipped. The active readout roles are therefore:

- readout 1: detection immediately after optical polarization, the m_S = 0 fluorescence reference.
- readout 2: detection after the microwave Rabi pulse, the pODMR signal readout.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. The sample-rate rounding at 250 MHz leaves 52 ns unchanged.

Quantitative expected-signal model:

For the setup, the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. A square Rabi pulse gives excited spin population P = sin^2(pi f_R t). With f_R = 10 MHz and t = 52 ns,

P = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52 pi) = 0.996.

Using the stated m_S = 0 to m_S = +1 contrast scale of 22%, an on-resonance point should reduce the post-microwave readout by about

0.22 * 0.996 = 0.219, or 21.9% of the local fluorescence.

The observed fluorescence level is about 45.4 counts, so the expected on-resonance drop is about 9.9 to 10.0 counts if a resonance is present under these active settings.

Observed data check:

The combined readout difference readout2 - readout1 has mean -0.035 counts and standard deviation 0.985 counts. Its largest negative excursion is -2.077 counts at the final sweep point, only about -4.6% of the local fluorescence, and it is at the edge of the scan rather than a resolved line. The largest positive excursion is +1.788 counts. A simple negative Lorentzian fit to readout2 - readout1 improves the constant-model SSE only from 19.41 to 15.68 and chooses a 5 MHz-wide feature at the scan endpoint with amplitude 1.97 counts, about 4.3% of the fluorescence. This is far below the 21.9% / 10-count expected response for the active 52 ns, mod_depth 1 pulse.

The two stored averages do not provide strong independent repeatability because stored averages can reflect tracking cadence, but they also do not show a stable resonance-scale feature. At the endpoint where the combined trace is most negative, the per-average differences are -4.96 counts and +0.81 counts, not a consistent 10-count resonant dip.

Decision:

The active physical model predicts a large near-pi-pulse pODMR contrast feature. The measured signal only shows small noisy readout differences at the few-percent level with no resolved resonance-scale dip. I therefore decide that a pODMR resonance is absent.
