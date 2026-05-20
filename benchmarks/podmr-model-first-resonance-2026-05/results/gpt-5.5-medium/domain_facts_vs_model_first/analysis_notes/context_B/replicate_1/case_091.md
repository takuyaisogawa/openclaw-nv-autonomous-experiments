Case: podmr_077_2026-05-17-100811

Sequence interpretation

The active sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. full_expt = 0, so the "Acquire 1 level reference" block is inactive. The active readouts are therefore:

1. readout 1: after adj_polarize and before the microwave pulse, a bright m_S = 0 reference.
2. readout 2: after one rabi_pulse_mod_wait_time pulse, the pODMR-sensitive readout.

The pulse used for the pODMR test is length_rabi_pulse = 52 ns. The provided sequence XML and exported active variable values give mod_depth = 1. The stored Sequence text in raw_export contains a stale-looking default of 0.3, but the explicit Variable_values and sequence.xml both give mod_depth = 1, so I use mod_depth = 1 as the active setting.

Quantitative expected signal

For a square microwave pulse, the excited population on detuning delta is modeled as

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

where f_R is the on-resonance Rabi frequency in cycles/s and delta is the frequency detuning in Hz. The setup fact gives f_R = 10 MHz * mod_depth, so at mod_depth = 1, f_R = 10 MHz. With t = 52 ns:

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected resonant readout-2 fractional drop relative to readout 1 is

0.22 * 0.996 = 0.219, or 21.9%.

At the measured reference level of about 50.94 counts, this predicts an on-resonance drop of about

50.94 * 0.219 = 11.2 counts.

Data comparison

The combined readouts have:

- mean readout 1 = 50.936
- mean readout 2 = 50.769
- mean(readout 2 - readout 1) = -0.167 counts
- standard deviation of pointwise differences = 1.192 counts
- most negative observed difference = -2.192 counts at 3.825 GHz
- most negative observed fractional difference = -4.22%

Thus the largest observed drop is only about 20% of the predicted resonant drop for the active mod_depth = 1 pulse, and the pointwise differences fluctuate in both signs with no resonance-like feature. The expected resonant signal would be about 9 times the observed pointwise-difference scatter and should be visually dominant in this sweep. Stored averages are not treated as an independent repeatability test because they can reflect tracking cadence.

Decision

The quantitative Rabi-response model predicts a large approximately 22% readout-2 dip at resonance for the active pulse, but the measured readout difference is near zero with only small mixed-sign fluctuations. A pODMR resonance is absent.
