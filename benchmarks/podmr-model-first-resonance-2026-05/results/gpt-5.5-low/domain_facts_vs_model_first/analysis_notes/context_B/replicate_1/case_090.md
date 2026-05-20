Active sequence and readout roles

The active sequence is Rabimodulated.xml from the saved scan metadata. The run varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The relevant saved variable values are length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, and do_adiabatic_inversion = 1. Because full_expt is zero, the conditional m_S=+1 reference block is not active. Each shot first polarizes and detects a true m_S=0 reference, then applies a modulated square Rabi pulse, then performs the signal detection. Therefore readout 1 is the bright m_S=0 reference and readout 2 is the post-microwave signal readout.

Quantitative expected-signal model

Given the supplied calibration, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square resonant pulse of duration t = 52 ns, the transition probability is

P_flip = sin^2(pi * f_Rabi * t)
       = sin^2(pi * 10e6 * 52e-9)
       = 0.996.

With an m_S=0 to m_S=+1 contrast scale of about 22%, an on-resonance point should reduce the post-pulse signal by about 0.22 * 0.996 = 0.219, or 21.9% relative to the bright reference. The combined raw baseline is about 50.9 counts, so the expected on-resonance drop is roughly 11.2 counts. In readout terms, readout 2 should be near 39.8 counts at resonance if readout 1 stays near 51 counts, aside from noise and tracking drift.

Observed data check

The two combined readouts have means readout 1 = 51.03 and readout 2 = 50.82. Their pointwise difference, readout 2 minus readout 1, has standard deviation about 1.42 counts and ranges only from about -2.73 to +2.14 counts. No point has the order-11-count post-pulse suppression expected from a resonant pi pulse. The largest apparent combined-readout trough is around 3.91 GHz, but it appears in both readouts and has an amplitude around 1 to 3 counts, consistent with baseline/tracking variation rather than a spin-dependent microwave response. Stored averages are only two and are not treated as a strong repeatability test.

Decision

The physical model predicts a large post-pulse readout drop for a real pODMR resonance under these pulse settings. The observed signal is far smaller and does not show the required readout-role-specific contrast. I therefore classify this case as resonance_absent.
