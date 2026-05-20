Sequence and readout interpretation

The active sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the XML, full_expt = 0, so the conditional "Acquire 1 level reference" branch is skipped even though do_adiabatic_inversion is true. The actual readouts are therefore:

- readout 1: polarized m_S = 0 reference after adj_polarize followed by detection.
- readout 2: detection after a single rabi_pulse_mod_wait_time at the scanned microwave frequency.

The pulse parameters used for the active MW pulse are mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded pulse length remains round(52 ns * 250 MHz) / 250 MHz = 13 samples / 250 MHz = 52 ns.

Physical signal model

The setup facts give a Rabi frequency of about 10 MHz at mod_depth = 1 and an m_S = 0 to m_S = +1 contrast scale of about 22 percent. For a square Rabi pulse starting in m_S = 0, the transition probability versus detuning is

P(detuning) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * t * sqrt(f_R^2 + detuning^2)),

using f_R and detuning in cycles per second. On resonance, f_R = 10 MHz and t = 52 ns, so

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The expected on-resonance fluorescence drop of readout 2 relative to the readout 1 reference is therefore 0.22 * 0.996 = 0.219, meaning readout 2 should be about 0.781 times readout 1 at resonance. For detunings of 2.5, 5, 7.5, and 10 MHz, the same model gives expected drops of about 20.4%, 16.5%, 11.2%, and 6.0%, respectively.

Data comparison

Using the combined readouts, the normalized contrast (readout1 - readout2) / readout1 is:

- 3.870 GHz: 0.118
- 3.875 GHz: 0.227
- 3.880 GHz: 0.196
- 3.885 GHz: 0.187
- 3.890 GHz: 0.079

Outside this 3.870-3.890 GHz window, the mean normalized contrast is 0.0148 with standard deviation 0.0383. The largest central drops, 19.6% to 22.7%, are at the expected contrast scale for an on-resonance near-pi pulse. A least-squares fit of the square-pulse model to the normalized contrast, allowing only resonance center plus a linear contrast scale and offset, gives center frequency about 3.8787 GHz, fitted contrast scale 0.234, offset 0.008, and R2 = 0.760 relative to a constant-contrast null model. The fitted contrast scale is close to the independently expected 0.22.

The per-average traces show strong slow drift and should not be treated as a strong independent repeatability test. Still, normalizing each average by its own readout 1 reference gives central drops near the same frequency in both averages, for example 0.238 at 3.875 GHz in average 1 and 0.219 at 3.875 GHz plus 0.215 at 3.880 GHz in average 2.

Decision

A pODMR resonance is present. The central readout-2 dip has the correct sign, location-localized frequency dependence, and quantitative contrast scale expected from the active 52 ns, mod_depth 1 Rabi pulse model.
