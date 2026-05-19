<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_019

Inputs used:
- sequence XML: inputs/sequence.xml
- raw readout values: inputs/raw_export.json

Active sequence and readout roles:
- The active pulse sequence is Rabimodulated.xml / Rabimodulated.
- The instructions first run adj_polarize followed by detection, so readout 1 is the polarized m_S = 0 fluorescence reference.
- full_expt = 0, so the optional m_S = +1 reference block is disabled.
- The active signal readout is the detection after one rabi_pulse_mod_wait_time pulse, so readout 2 is the post-microwave-pulse fluorescence.
- Pulse settings from the provided XML: length_rabi_pulse = 52 ns, mod_depth = 1, mw_freq is swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Physical model calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1.
- With linear mod_depth scaling and mod_depth = 1, f_R = 10 MHz.
- For a resonant square pulse, the transferred population is P = sin^2(pi * f_R * t), where f_R is in cycles/s and the pi-pulse time is 1/(2 f_R).
- For t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected on-resonance fractional fluorescence dip is 0.22 * 0.996 = 0.219, or 21.9%.
- For a typical 40-count readout baseline this predicts an on-resonance readout near 40 * (1 - 0.219) = 31.2 counts.

Observed data:
- The minimum combined readout 2 value is 31.8077 at scan index 11, corresponding to 3.880 GHz.
- The paired readout 1 value there is 40.4231, giving readout2/readout1 = 0.7869 and an observed dip of 21.3%.
- The neighboring point at 3.875 GHz has readout 2 = 32.4231 and readout 1 = 41.2885, giving a similar ratio of 0.7853.
- The per-average traces both show the same strong readout-2 depression around 3.875-3.880 GHz, but I do not treat the two stored averages as a strong independent repeatability test because stored averages can reflect tracking cadence.

Decision:
The observed dip amplitude and location match the explicit resonant Rabi-pulse model for this pulse duration and modulation depth. A pODMR resonance is present.
