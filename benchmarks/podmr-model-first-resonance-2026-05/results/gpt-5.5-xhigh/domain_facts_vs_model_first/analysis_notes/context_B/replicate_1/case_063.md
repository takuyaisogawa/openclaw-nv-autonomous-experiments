Case podmr_049_2026-05-17-004217.

I used the provided sequence XML as the pulse logic. The active sequence is Rabimodulated.xml. With full_expt = 0, the optional "Acquire 1 level reference" branch is skipped, so the two combined readouts have these roles:

- readout 1: true m_S = 0 reference after optical polarization and detection.
- readout 2: detection after one microwave rabi_pulse_mod_wait_time pulse.

The sequence variables and exported variable table give mod_depth = 1, sample_rate = 250 MHz, and length_rabi_pulse = 5.2e-8 s. The pulse is rounded to the sample grid:

round(52 ns * 250 MHz) / 250 MHz = 13 / 250 MHz = 52 ns.

Physical model calculation:

For this setup, the Rabi frequency at mod_depth = 1 is about 10 MHz. I modeled a square microwave pulse with

P_1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau),

where f_R = 10 MHz and tau = 52 ns. On resonance,

P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The current m_S = 0 to m_S = +1 readout contrast scale is about 22%, so the expected normalized post-pulse readout at resonance is

R2/R1 = 1 - 0.22 * 0.996 = 0.781.

With a typical reference readout near 50 counts, this predicts a resonance dip of about 10.96 counts. Even if the resonance were halfway between adjacent 5 MHz scan points, the nearest sampled point would still have P_1 about 0.93 and R2/R1 about 0.80, so the expected feature is not a subtle one.

Observed data calculation:

The combined readouts over 3.825 to 3.925 GHz give R2/R1 values with minimum 0.9487 at 3.850 GHz, maximum 1.0715 at 3.890 GHz, mean 0.9986, and standard deviation 0.0299. The deepest combined point is:

- frequency: 3.850 GHz
- readout 1: 50.9423
- readout 2: 48.3269
- observed ratio: 0.9487
- expected resonant readout for mod_depth = 1: 39.7792

Thus the deepest observed trough is about 8.55 counts above the resonance model expectation. A constrained dip-template fit to the normalized data with the mod_depth = 1 pulse model gives an apparent contrast amplitude of only about 0.054, far below the expected 0.22. Allowing the template sign to float prefers a peak-like feature near 3.891 GHz, not the ODMR dip sign.

The two stored average blocks show shallow, inconsistent minima and are treated as tracking-cadence readouts rather than independent repeatability evidence. The combined data do not show the contrast-scale dip required by the active pulse sequence and physical model.

Decision: resonance_absent.
