Active sequence and readout roles

The active scan is the Rabimodulated.xml pulse sequence, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions are:

1. adj_polarize, then detection: this is the true m_S = 0 reference readout, corresponding to readout 1.
2. full_expt = 0, so the optional m_S = 1 reference branch is skipped.
3. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), then detection: this is the pODMR signal readout after the microwave pulse, corresponding to readout 2.

The provided sequence variables and exported Variable_values give length_rabi_pulse = 52 ns and mod_depth = 1. The raw_export also contains an embedded sequence text with mod_depth = 0.3, but the explicit provided sequence.xml and exported Variable_values both identify mod_depth = 1, so I used mod_depth = 1 for the decision. I also checked the mod_depth = 0.3 case as a sensitivity check.

Physical expectation

For a square Rabi pulse, using Rabi frequency f_R in cycles/s and detuning Delta in Hz, the transition probability is

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

The setup facts give f_R approximately 10 MHz * mod_depth. With mod_depth = 1 and t = 52 ns:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With a 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance normalized drop in readout 2 relative to readout 1 is approximately 0.22 * 0.996 = 0.219, or about 10.3 counts for a 47 count baseline. The expected model line is also not a single isolated point: at +/-5 MHz detuning from resonance, P is about 0.749, giving an expected drop of about 16.5%, or 7.7 counts.

Measured data

The combined readouts have mean readout 1 = 47.188 and mean readout 2 = 46.660. The pointwise normalized contrast y = 1 - readout2/readout1 has mean 0.0108, standard deviation 0.0276, and maximum 0.0763 at 3.885 GHz. The largest raw drop is 3.69 counts at 3.885 GHz. Neighboring points do not show the expected broad, symmetric high-contrast Rabi response; for example, around 3.885 GHz the drops are 1.08, 3.69, 1.17 counts at 3.880, 3.885, and 3.890 GHz, and the 3.895 GHz point is an increase rather than a drop.

Explicit model comparison

Using the square-pulse line shape across all possible resonance centers in the scan range:

- For mod_depth = 1 with the physical 22% contrast scale fixed, the best fixed-amplitude model has RSS about 0.084 in normalized contrast units. This is much worse than the null/near-flat RSS about 0.018.
- If the amplitude is allowed to float freely, the best mod_depth = 1 fit uses amplitude about 0.045, far below the known 0.22 contrast scale expected for a full pi-like pulse.
- As a sensitivity check, mod_depth = 0.3 gives an on-resonance expected contrast of about 4.87%. A freely fit model can match a weak feature near 3.883 GHz, but that relies on the conflicting embedded sequence text rather than the provided active variable values, and the evidence is not robust because only two stored averages are present and these averages mainly reflect tracking cadence.

Decision

Given the active mod_depth = 1 and 52 ns pulse, a real pODMR resonance should produce a large, multi-point, roughly 22% on-resonance dip. The observed trace has only small, noisy readout differences and no physically consistent line shape at the expected signal scale. I decide that a pODMR resonance is absent.
