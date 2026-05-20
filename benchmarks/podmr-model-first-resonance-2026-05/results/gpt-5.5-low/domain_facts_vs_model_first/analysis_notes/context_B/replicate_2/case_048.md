Case: podmr_034_2026-05-16-204545

Sequence and readout roles

The provided XML/raw export identify the active sequence as Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active parameters are length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, sample_rate = 250 MHz, delay_wrt_1mus = 0.2 us, and pumping_time = 1 us.

Because full_expt = 0, the optional "1 level reference" block is skipped. The two active detections are therefore:

1. readout 1: after adj_polarize, before the microwave pulse; this is the true m_S = 0 fluorescence reference.
2. readout 2: after a rabi_pulse_mod_wait_time pulse of duration 52 ns and mod_depth 1; this is the pODMR signal readout.

Physical model calculation

Given the stated setup, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a square pulse, the driven transition probability versus detuning is

P(detuning) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * sqrt(f_R^2 + detuning^2) * tau)

with f_R = 10 MHz and tau = 52 ns. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52 pi) = 0.996.

The expected fluorescence loss from m_S = 0 to m_S = +1 is about contrast * P = 0.22 * 0.996 = 0.219, i.e. about 22%. The measured readout-1 baseline is about 50.02 counts, so the expected resonant drop in readout 2 relative to readout 1 is about 10.96 counts.

Even if the resonance lies halfway between adjacent 5 MHz scan points, the nearest detuning is 2.5 MHz. The same model gives P(2.5 MHz) = 0.929, corresponding to an expected drop of about 20.4%, or 10.22 counts. At 5 MHz detuning the expected drop is still about 8.24 counts. Thus a real resonance in the scanned window should produce a large negative feature in readout 2 relative to readout 1.

Observed data check

The combined readout means are:

- readout 1 mean = 50.016 counts, standard deviation across scan points = 0.965 counts.
- readout 2 mean = 49.366 counts, standard deviation across scan points = 1.217 counts.
- readout2 - readout1 mean = -0.649 counts, standard deviation = 1.286 counts.
- minimum readout2 - readout1 = -2.654 counts.
- maximum readout2 - readout1 = +1.808 counts.

The largest observed negative difference is only about 2.65 counts, far smaller than the expected 8-11 count resonant pODMR dip. Several candidate frequencies near the middle of the scan show readout 2 equal to or above readout 1 rather than a dip. A fixed-physics dip model using the known contrast and Rabi parameters also fits worse than a flat offset model, because the required resonance feature is absent from the data.

Decision

No pODMR resonance is present in this scan. The pulse duration and modulation depth should make an in-window resonance a high-contrast, broad, easily visible drop in the post-pulse readout relative to the m_S = 0 reference, but the measured differences remain small and inconsistent with that model.
