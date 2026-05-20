Active sequence identification:

The active scan is Rabimodulated.xml with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes the NV and immediately performs a detection, so readout 1 is the m_S = 0 fluorescence reference. Because full_expt = 0, the optional "Acquire 1 level reference" block is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by a second detection, so readout 2 is the post-microwave pODMR signal.

Physical model calculation:

For a square resonant pulse, the transferred population is

P = sin^2(pi * f_R * t)

using f_R in cycles/s. The setup fact gives f_R ~= 10 MHz at mod_depth = 1. With t = 52 ns,

P_on = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the setup contrast scale C ~= 0.22 between m_S = 0 and m_S = +1, the expected normalized post-pulse fluorescence on resonance is

F2/F1 = 1 - C * P_on = 1 - 0.22 * 0.996 = 0.781.

The mean readout 1 level is 45.68, so an on-resonance pi pulse should reduce readout 2 by about

45.68 * 0.22 * 0.996 = 10.0 counts,

putting readout 2 near 35.7 counts at resonance if the transition is in the scanned range.

Data comparison:

The measured readout-2/readout-1 ratio has mean 0.998, standard deviation 0.039, minimum 0.931, and maximum 1.069. The largest observed negative differences are about -3.2 counts near 3.885 to 3.890 GHz, much smaller than the expected roughly -10 count on-resonance change. Other similarly sized negative excursions occur at 3.910 GHz and 3.925 GHz, so these are not a clean single resonance feature.

I also evaluated the square-pulse detuning model

P(detuning) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

with Omega = 2*pi*10 MHz, t = 52 ns, and C = 0.22. Fitting only an overall baseline multiplier, the best model centered near 3.886 GHz gives a worse squared residual than a constant-ratio null model. Allowing the contrast amplitude to float gives an apparent amplitude of only about 0.063, far below the expected 0.22 for a real pi-pulse pODMR resonance in this setup.

Decision:

No pODMR resonance is present. The active pulse should create a large, broad, easily visible dip if it hits the NV transition, but the observed variations are small compared with the expected physical signal and are consistent with tracking/noise scatter.
