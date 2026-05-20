Case: podmr_055_2026-05-17-045046

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence interpretation:
- Sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "1 level reference" block is inactive despite do_adiabatic_inversion = 1.
- Readout 1 is the true m_S = 0 fluorescence reference: polarize, detect, then wait.
- Readout 2 is the signal after the modulated microwave Rabi pulse, then detection.
- Active Rabi pulse length = 52 ns. At the 250 MHz sample rate this is exactly 13 samples, so rounding leaves it at 52 ns.
- Active mod_depth = 1.

Quantitative expected signal model:
Using the supplied setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a resonant square pulse, the driven population transfer is

P_1(delta = 0) = sin^2(pi f_R t)

with f_R = 10 MHz and t = 52 ns. This gives

P_1 = sin^2(pi * 10e6 * 52e-9) = 0.996.

The expected resonant fluorescence reduction in the signal readout is therefore approximately

0.22 * 0.996 = 0.219

or about 21.9 percent of the m_S = 0 reference. The mean combined readout 1 level is 43.813 counts, so the expected on-resonance raw drop is about

43.813 * 0.219 = 9.60 counts.

Observed combined readouts:
- mean(readout 1) = 43.813, sd = 1.523
- mean(readout 2) = 43.448, sd = 1.527
- mean(readout 1 - readout 2) = 0.365 counts
- min/max(readout 1 - readout 2) = -3.192 to +2.615 counts
- min/max fractional difference (readout 1 - readout 2) / readout 1 = -7.63 percent to +5.89 percent

The largest observed positive signal drop is only 2.615 counts, about 5.9 percent, far below the approximately 9.60 count / 21.9 percent drop expected for a resonant near-pi pulse.

Template check:
I fit the expected two-level Rabi response

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi t sqrt(f_R^2 + delta^2))

against the combined differential trace as offset + A * P(delta), scanning possible resonance centers across the frequency range. The best raw differential fit found A = -1.63 counts at 3.8928 GHz, i.e. the opposite sign from a resonance because a resonance should make readout 2 lower than readout 1 and therefore A positive. In normalized units, the best fit gave C = -0.0387, also opposite in sign to the expected +0.219. Forcing the expected positive amplitude made the fit substantially worse than an offset-only null model, increasing RSS from 51.74 to 156.35.

The stored averages are not treated as strong independent repeatability evidence because they may reflect tracking cadence. They also do not rescue the resonance interpretation: average 1 and average 2 have different extrema and do not show a consistent, expected-size positive dip at a common frequency.

Decision:
The active pulse should produce a large near-pi-pulse pODMR contrast if a transition is in the swept range. The observed differential trace is small, changes sign, and is best matched by an opposite-sign template. I therefore decide resonance_absent.
