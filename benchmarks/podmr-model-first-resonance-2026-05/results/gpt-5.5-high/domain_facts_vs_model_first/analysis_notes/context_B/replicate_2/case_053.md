Case: podmr_039_2026-05-16-221215

Sequence interpretation from inputs/sequence.xml:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Readout 1 role: after adj_polarize and before any microwave pulse, so it is the m_S = 0 fluorescence reference.
- full_expt = 0, so the conditional m_S = +1 reference block is disabled.
- Readout 2 role: after a rabi_pulse_mod_wait_time pulse, so it is the microwave-driven pODMR signal readout.
- Microwave pulse: length_rabi_pulse = 52 ns, mod_depth = 1.

Quantitative model:
The setup contrast between m_S = 0 and m_S = +1 is about 22%. The Rabi frequency is about 10 MHz at mod_depth = 1, so the 52 ns square pulse has on-resonance transition probability

P(0) = sin^2(pi * f_R * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.

Thus a resonance sampled on center should reduce readout 2 relative to readout 1 by 0.22 * 0.996 = 0.219, about 21.9%. With mean readout 1 = 49.35 counts, that is an expected drop of about 10.81 counts, giving a signal near 38.53 counts.

For finite detuning I used the square-pulse two-level response

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

Because the scan step is 5 MHz, a resonance inside the scan should have at least one point within 2.5 MHz. At 2.5 MHz detuning, P = 0.929, so the expected normalized fluorescence drop is 0.22 * 0.929 = 0.204, still about 20.4% or 10.09 counts.

Observed readout comparison:
- readout 1 mean = 49.35 counts; readout 2 mean = 49.19 counts.
- The normalized drop 1 - readout2/readout1 has mean 0.0026 and standard deviation 0.0323.
- The largest observed normalized drop is 0.0491 at 3.850 GHz, corresponding to only 2.54 counts.
- The minimum signal/reference ratio is 0.9509, far above the roughly 0.78 to 0.80 ratio expected for an in-scan resonance under the active mod_depth = 1, 52 ns pulse model.
- Other apparent deviations are comparable in size and include opposite-sign excursions, such as readout 2 exceeding readout 1 at 3.855 GHz by 8.7%.

Decision:
Under the active pulse settings, a real pODMR resonance in this scan should be a large, directly visible readout 2 drop relative to the m_S = 0 reference. The measured trace does not contain a dip of the required amplitude or coherent shape. Stored per-average traces are not treated as a strong independent repeatability test because they can reflect tracking cadence. I therefore decide that a pODMR resonance is absent.
