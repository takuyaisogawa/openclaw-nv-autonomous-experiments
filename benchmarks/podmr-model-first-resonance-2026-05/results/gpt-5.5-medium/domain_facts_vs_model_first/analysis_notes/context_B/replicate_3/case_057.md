<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_057

Sequence and readout interpretation:

The active sequence is Rabimodulated.xml. The saved scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The relevant XML variables are length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, pumping_time = 1 us, delay_wrt_1mus = 0.2 us, and length_last_wait = 1 us.

Because full_expt = 0, the optional "Acquire 1 level reference" block is skipped. The acquired readouts are therefore:

1. readout 1: after optical polarization, the true m_S = 0 reference.
2. readout 2: after the modulated Rabi pulse, the pODMR signal readout.

Physical model calculation:

Use a two-level driven transition model for the pulse. The setup facts give Rabi frequency f_R = 10 MHz at mod_depth = 1. For pulse duration t = 52 ns, the on-resonance transfer probability is

P(0) = sin^2(pi f_R t)
     = sin^2(pi * 10e6 * 52e-9)
     = 0.996.

With a 22% m_S = 0 to m_S = +1 contrast scale, an on-resonance pi-like pulse should reduce the post-pulse readout relative to the zero reference by about

0.22 * 0.996 = 0.219, or 21.9%.

At the observed reference level of about 47 raw units, the expected on-resonance drop is approximately

47 * 0.219 = 10.3 raw units.

The finite-detuning response used for the scan check was

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi t sqrt(f_R^2 + delta^2)).

This gives a broad, easily visible dip over the 5 MHz scan spacing if the resonance lies in the scanned window.

Data check:

The measured combined readout means are readout 1 = 47.11 and readout 2 = 47.55. The pointwise post-pulse/reference ratio has mean 1.009, standard deviation 0.0196, minimum 0.976, and maximum 1.041. The measured minimum ratio is therefore only a 2.4% reduction from the reference, whereas the expected resonant ratio is about 0.781. In raw units, the largest observed negative difference readout2 - readout1 is -1.19, far smaller than the approximately -10.3 raw-unit resonance expected from the pulse model.

A fit of the expected negative pODMR response shape to the normalized data does not find a physical in-window dip. Allowing the amplitude to float gives the best in-window center near 3.865 GHz only with a negative dip amplitude, meaning the data prefer a peak rather than the expected fluorescence loss. With the physical 22% amplitude fixed, the best fit pushes the resonance outside the scan window where the modeled response is weak.

Stored averages do not provide a strong independent repeatability test here, and I did not use them as decisive evidence. The decisive comparison is the explicit pulse model versus the combined normalized readout: the expected pODMR signal is much larger and opposite in character to the observed fluctuations.

Decision: resonance_absent.
