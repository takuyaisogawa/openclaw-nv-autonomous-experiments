<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_019

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png for visual consistency only

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence has full_expt = 0, so the optional m_S = +1 reference block is inactive even though do_adiabatic_inversion is true.
- Readout 1 is acquired immediately after adj_polarize and is therefore the m_S = 0 / bright reference.
- Readout 2 is acquired after rabi_pulse_mod_wait_time and is the pODMR signal readout after the microwave pulse.
- The active pulse duration is length_rabi_pulse = 52 ns. At the listed sample rate of 250 MHz this remains 13 samples = 52 ns after rounding.
- mod_depth is 1 in inputs/sequence.xml and in Variable_values. The embedded saved Sequence text in raw_export contains an older/default-looking mod_depth = 0.3, but I used the provided sequence XML and exported Variable_values as the active settings.

Quantitative physical expectation:
- Given the stated setup, f_Rabi is about 10 MHz at mod_depth = 1.
- For a square resonant Rabi pulse, the transferred population is P = sin^2(pi f_Rabi t).
- With f_Rabi = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant fluorescence loss in readout 2 relative to readout 1 is 0.22 * 0.996 = 0.219, or about 21.9%.
- Including detuning in the square-pulse model, P(delta) = f_Rabi^2/(f_Rabi^2 + delta^2) * sin^2(pi t sqrt(f_Rabi^2 + delta^2)). This gives expected fluorescence losses of about 16.5% at +/-5 MHz, 6.0% at +/-10 MHz, and near zero by +/-15 MHz, aside from weak finite-pulse sidelobes.

Observed quantitative signal:
- The combined readouts show readout 1 staying near 40-42 counts across the sweep, while readout 2 has a localized trough near 3.875-3.880 GHz.
- At 3.875 GHz, readout 1 = 41.2885 and readout 2 = 32.4231. The ratio is 0.7853, so the normalized loss is 21.47%.
- At 3.880 GHz, readout 1 = 40.4231 and readout 2 = 31.8077. The normalized loss is 21.31%.
- Neighboring normalized losses are approximately 13.2% at 3.870 GHz and 11.9% at 3.885 GHz, with the off-feature mean normalized loss about 2.0% and standard deviation about 3.5%.
- The two stored averages both show the same localized readout-2 depression, but I treat that only as a tracking-cadence consistency check, not as a strong independent repeatability test.

Decision:
The expected resonant signal for this sequence is a roughly 22% drop in the post-pulse readout, with a width set by a 52 ns square pulse and 10 MHz Rabi rate. The observed readout-2 depression is localized in frequency, has the expected magnitude, and is absent from readout 1. Therefore this case contains a pODMR resonance.
