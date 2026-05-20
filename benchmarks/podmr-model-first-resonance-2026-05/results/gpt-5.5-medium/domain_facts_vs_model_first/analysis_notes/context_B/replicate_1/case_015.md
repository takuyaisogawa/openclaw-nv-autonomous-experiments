Case podmr_034_2026-05-15-235221

Inputs used: inputs/sequence.xml and inputs/raw_export.json only. I did not use labels, sibling cases, previous outputs, or external context.

Sequence and readout roles:
- Active sequence file: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first run adj_polarize, then detection. This is readout 1 and is the true m_S = 0 bright reference.
- full_expt = 0, so the optional +1 reference block is inactive. The do_adiabatic_inversion flag is therefore not used for the acquired data.
- The active manipulation is rabi_pulse_mod_wait_time followed by detection. This is readout 2, the signal after the microwave pulse.
- mod_depth = 1 from the provided sequence XML.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded pulse duration remains 13 samples = 52 ns.

Physical model calculation:
- Given setup Rabi frequency approximately 10 MHz at mod_depth = 1 and linear scaling with mod_depth, the expected Rabi frequency here is 10 MHz.
- For a resonant square Rabi pulse, transferred population P = sin^2(pi * f_Rabi * tau).
- With f_Rabi = 10 MHz and tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup m_S = 0 to m_S = +1 contrast scale is about 22%, so the expected resonant fractional fluorescence reduction in readout 2 relative to the bright reference is 0.22 * 0.996 = 0.219.
- The measured readout 1 mean is 36.012 raw units, so the expected resonant readout 2 value is 36.012 * (1 - 0.219) = 28.121 raw units, an expected drop of 7.891 raw units.

Data check:
- The combined readout 2 minimum is 26.288 at 3.880 GHz.
- At 3.875 GHz, readout 1/readout 2 are 34.231/26.808, a fractional drop of 21.7%.
- At 3.880 GHz, readout 1/readout 2 are 34.885/26.288, a fractional drop of 24.6%.
- Excluding the dip region from 3.865 to 3.885 GHz, readout 2 has mean 35.373 and standard deviation 1.167, so the minimum is 7.79 standard deviations below the off-region readout 2 mean.
- A simple square-pulse detuning model P(d) = (f_Rabi^2/(f_Rabi^2+d^2)) * sin^2(pi * tau * sqrt(f_Rabi^2+d^2)), with the 22% contrast scale, gives its best center near 3.8765 GHz and predicts a dip with the correct magnitude and width around the observed feature.

Decision:
The observed narrow readout 2 fluorescence dip around 3.875-3.880 GHz has the expected sign, magnitude, and approximate width for a near-pi pODMR pulse at mod_depth = 1. A pODMR resonance is present.
