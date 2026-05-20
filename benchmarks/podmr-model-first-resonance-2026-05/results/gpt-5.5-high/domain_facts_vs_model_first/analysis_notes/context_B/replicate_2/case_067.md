Case: podmr_053_2026-05-17-042031

I used the provided sequence XML and the raw export data only. The active sequence is Rabimodulated.xml, scanned in mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions contain two detection windows because full_expt = 0 skips the optional m_S = +1 reference block. Therefore readout 1 is the post-polarization m_S = 0 reference, and readout 2 is the signal readout after the Rabi-modulated microwave pulse. The pulse used for the pODMR test is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. The first optional +1 reference pulse block is inactive.

Physical model calculation:

The setup contrast scale between m_S = 0 and m_S = +1 is 22%. The Rabi frequency is about 10 MHz at mod_depth = 1, and the driven population transfer for a rectangular pulse is

P_flip(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau)

with f_R = 10 MHz and tau = 52 ns. On resonance this gives

P_flip(0) = sin^2(pi * 10e6 * 52e-9) = 0.996

so the expected resonant fluorescence loss in readout 2 relative to the m_S = 0 reference is about

0.22 * 0.996 = 0.219, or 21.9%.

With the observed readout scale near 45 counts, a true on-resonance response under these pulse settings should be roughly 9.9 counts darker than the m_S = 0 reference, with a detuned Rabi line shape spread over neighboring scan points.

Observed quantitative comparison:

The combined readout means are readout 1 = 45.197 and readout 2 = 45.018, so the mean fractional reference-minus-signal difference is only 0.35%. The largest single positive fractional difference is at 3.880 GHz: (45.8846 - 42.5962) / 45.8846 = 7.17%. Another positive point occurs at 3.890 GHz, but the intervening 3.885 GHz point is near zero/negative, so the feature is not shaped like the expected detuned Rabi response. The standard deviation of the pointwise fractional differences is 3.39%, much larger than the mean offset.

I also fit the explicit detuned Rabi response above to the fractional reference-minus-signal data with a linear baseline and a free center frequency. The best fitted contrast amplitude is 0.0436, about 20% of the expected 0.22 contrast, with an amplitude z of about 1.73. Forcing the physically expected 0.22 amplitude makes the fit much worse than a baseline-only model. The stored two averages differ strongly in baseline/trend, consistent with tracking cadence, so I did not treat them as an independent repeatability test.

Decision:

The expected resonant signal for the active 52 ns, mod_depth = 1 pulse is a near-full contrast drop of about 22%, but the measured readout-2 suppression is at most about 7%, is not line-shape consistent, and is not statistically strong in the explicit model fit. I therefore decide that a pODMR resonance is absent.
