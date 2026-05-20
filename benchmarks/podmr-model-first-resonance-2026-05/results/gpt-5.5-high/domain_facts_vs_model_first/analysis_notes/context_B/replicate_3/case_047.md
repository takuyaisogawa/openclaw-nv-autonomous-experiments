Case: podmr_033_2026-05-16-203113

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles

The sequence is Rabimodulated.xml. With full_expt = 0, the optional "+1 level reference" block is skipped. The active measurement therefore has two readout roles:

1. readout 1: optical polarization followed by detection, the true m_S = 0 reference.
2. readout 2: a single rabi_pulse_mod_wait_time pulse followed by detection, the pODMR signal channel.

The active microwave pulse is:

- length_rabi_pulse = 5.2e-08 s = 52 ns.
- mod_depth = 1 from the provided sequence XML.
- Rabi frequency model from the supplied domain facts: f_R = 10 MHz * mod_depth = 10 MHz.

Quantitative expected-signal model

For a resonant square pulse starting from m_S = 0, I used

P_1(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2))

where Omega and delta are in cycles/s. The fluorescence contrast scale between m_S = 0 and m_S = +1 is C = 0.22, so the expected fractional readout drop in the post-pulse channel is C * P_1(delta).

With t = 52 ns and Omega = 10 MHz:

- delta = 0 MHz: P_1 = 0.996, expected drop = 0.219 of the m_S = 0 readout.
- delta = 2.5 MHz: P_1 = 0.929, expected drop = 0.204 of the m_S = 0 readout.
- delta = 5 MHz: P_1 = 0.749, expected drop = 0.165 of the m_S = 0 readout.
- delta = 10 MHz: P_1 = 0.273, expected drop = 0.060 of the m_S = 0 readout.

The measured readout 1 mean is 53.90 counts. Therefore an on-resonance point should show readout 2 below readout 1 by about 11.81 counts. Even if the resonance lay halfway between 5 MHz scan points, the expected drop would still be about 11.02 counts; at a 5 MHz offset it would be about 8.88 counts. This is much larger than the observed point-to-point variation.

Observed data check

Using the combined raw readouts:

- readout 1 mean = 53.899, standard deviation = 1.033.
- readout 2 mean = 54.309, standard deviation = 1.372.
- readout 2 - readout 1 mean = +0.409 counts.
- readout 2 - readout 1 standard deviation = 1.025 counts.
- minimum readout 2 - readout 1 = -1.442 counts.
- maximum readout 2 - readout 1 = +2.519 counts.

A pODMR resonance for this sequence should be a negative-going feature in readout 2 relative to the m_S = 0 reference. The observed differences are instead centered slightly positive and never approach the predicted negative drop. Stored averages differ substantially from each other, consistent with the note that averages can reflect tracking cadence, so they are not treated as an independent repeatability test.

Decision

The expected resonant signal for the active pulse is far larger than the observed negative excursions, and the sign of the combined readout change is not consistent with a resonance. I decide that a pODMR resonance is absent.
