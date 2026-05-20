Case podmr_010_2026-05-16-114624

Sequence/readout interpretation

The provided sequence is Rabimodulated.xml. The variable values set length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps, and full_expt = 0. Because full_expt is zero, the "Acquire 1 level reference" block is inactive. The active sequence is:

1. adj_polarize, then detection: readout 1, the bright mS = 0 reference.
2. wait.
3. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), then detection: readout 2, the signal after the microwave pulse.

Thus readout 2 should dip relative to readout 1 when the swept microwave frequency is resonant with the NV transition.

Quantitative physical model

The setup contrast between mS = 0 and mS = +1 is about C = 0.22. The Rabi frequency is about 10 MHz at mod_depth = 1, and this sequence uses mod_depth = 1. The 52 ns pulse is rounded by the 250 MHz sample clock to 13 samples, still 52 ns.

For a square pulse, using frequency units in cycles/s,

P(+1) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * sqrt(f_R^2 + Delta^2) * tau)

and the expected normalized fluorescence is approximately

readout2/readout1 = 1 - C * P(+1).

At resonance, f_R = 10 MHz and tau = 52 ns:

P_res = sin^2(pi * 10e6 * 52e-9) = 0.996.

The expected resonant fractional PL dip is therefore 0.22 * 0.996 = 0.219, so the expected resonant ratio readout2/readout1 is about 0.781.

Data comparison

The combined readouts give readout2/readout1 ratios:

- 3.865 GHz: 39.019 / 40.250 = 0.969, dip 3.1%.
- 3.870 GHz: 33.212 / 40.327 = 0.824, dip 17.6%.
- 3.875 GHz: 31.192 / 40.904 = 0.763, dip 23.7%.
- 3.880 GHz: 33.038 / 39.192 = 0.843, dip 15.7%.
- 3.885 GHz: 34.327 / 36.885 = 0.931, dip 6.9%.

The off-resonant first eight scan points average readout2/readout1 = 0.988, close to no contrast after allowing for drift and photon noise. The minimum observed ratio is 0.763 at 3.875 GHz, very close to the model expectation of 0.781 for a resonant near-pi pulse. The neighboring points also follow the expected detuned square-pulse response: the 5 MHz detuned points should retain a large dip, while the 10 MHz detuned points should be much smaller.

Decision

A pODMR resonance is present. The depth, center, and width are quantitatively consistent with the active 52 ns, mod_depth 1 Rabi pulse and the expected 22% contrast scale.
