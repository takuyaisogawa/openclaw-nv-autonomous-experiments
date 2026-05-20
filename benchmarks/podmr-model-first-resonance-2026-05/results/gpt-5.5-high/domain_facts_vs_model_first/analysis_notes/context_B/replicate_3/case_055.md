Case: podmr_041_2026-05-16-224136

I used only the provided inputs in this workspace. The active sequence is Rabimodulated.xml. In the provided sequence XML, full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. The actual acquisition therefore has two active readout roles: first a true ms=0 reference after optical polarization and detection, then a driven readout after a rabi_pulse_mod_wait_time pulse followed by detection. The relevant pulse has length_rabi_pulse = 52 ns after sample-rate rounding, with mod_depth = 1. The scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Physical signal model:
For this setup the ms=0 to ms=+1 contrast scale is about 22%. The Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so here f_R = 10 MHz. For a rectangular pulse, the driven population transfer at detuning Delta is

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

At resonance, with t = 52 ns, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996. The expected pODMR readout drop at resonance is therefore 0.22 * 0.996 = 0.219, about 21.9% of the ms=0 reference. The measured reference readout is about 46.35 counts, so the expected resonant dip is about 10.16 counts in the driven readout.

Observed data:
The combined readout differences r2 - r1 have mean -0.21 counts and RMS 1.42 counts. The largest observed normalized drop, (r1 - r2) / r1, is 0.056, only about 5.6%, and there are also positive excursions where the driven readout is brighter than the reference. The low and high stored averages differ strongly in absolute level, consistent with tracking or collection changes between averages rather than a stable independent repeatability test.

Model comparison:
Using the fixed physical model above and constraining a resonance center to the scanned 3.825-3.925 GHz band, the best fixed-contrast model has an RMS residual of about 2.95 counts because it necessarily predicts a roughly 10-count dip. The no-resonance model has RMS about 1.42 counts. If the resonance amplitude is allowed to float freely, the best fitted contrast amplitude is only about 0.045, far below the expected 0.219 for the active pulse. This fitted amplitude is comparable to the point-to-point scatter and does not form a convincing pODMR line under the relevant physical model.

Decision:
The expected resonance for the active 52 ns, mod_depth 1 pulse should be large and obvious, but the measured driven readout only shows small, irregular fluctuations. I therefore decide that a pODMR resonance is absent in this scan.
