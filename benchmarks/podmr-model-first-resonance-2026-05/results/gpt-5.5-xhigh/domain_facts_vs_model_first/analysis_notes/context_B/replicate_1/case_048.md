Case: podmr_034_2026-05-16-204545

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:
- Active sequence file: Rabimodulated.xml.
- Sweep variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- Readout 1 role: detection immediately after optical polarization, the true m_S = 0 reference.
- Readout 2 role: detection after the active microwave Rabi pulse, the pODMR-sensitive driven readout.
- Active pulse: rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse = 5.2e-08 s = 52 ns. The sample-rate rounding at 250 MHz leaves 52 ns exactly.
- mod_depth = 1.

Quantitative physical model:
The provided setup facts give a Rabi frequency of about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. For this case f_R = 10 MHz. For a rectangular pulse starting in m_S = 0, I used the two-level detuned Rabi transfer probability

  P_1(delta) = f_R^2/(f_R^2 + delta^2) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau)

where delta is the microwave detuning in Hz and tau = 52 ns. On resonance,

  P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.

With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the driven readout should therefore be lower than the 0-reference readout by

  0.22 * 0.9961 = 0.2191

of the bright-state signal at resonance. Thus the expected readout-2/readout-1 ratio at resonance is about

  1 - 0.2191 = 0.7809.

At the observed readout level near 50 counts, this corresponds to an expected resonant dip of about 10.96 counts. Because the scan spacing is 5 MHz, a resonance between sampled points would still be sampled within about 2.5 MHz; the same Rabi model remains close to a large pi-pulse response there, so the expected signature would not disappear due to sampling.

Observed data calculation:
- mean readout 1 = 50.016 counts, standard deviation = 0.965 counts.
- mean readout 2 = 49.366 counts, standard deviation = 1.217 counts.
- mean readout-2/readout-1 ratio = 0.9872.
- minimum observed ratio = 0.9478.
- most negative observed readout2 - readout1 difference = -2.654 counts.

Model comparison:
Using the fixed physical model above and scanning possible resonance centers across the measured frequency range, the best fixed-contrast model still predicts a minimum ratio of about 0.789. Its sum of squared residuals in ratio space is 0.0628, substantially worse than a flat-ratio model with sum of squared residuals 0.0131. If the same Rabi line shape is allowed to fit an arbitrary amplitude, the best fitted ratio coefficient is -0.0308, while the physical contrast expectation is about -0.2172. The observed dip amplitude is therefore only about 14% of the expected physical pODMR response.

Decision:
The active sequence should produce a large, localized reduction in readout 2 relative to the 0-reference readout if a pODMR resonance were present in the swept band. The measured ratios fluctuate at the few-percent level, with no physically sized pi-pulse dip and no model-compatible resonance feature. I classify this case as resonance_absent.
