Case: podmr_019_2026-05-16-164247

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- The active sequence is Rabimodulated.xml / Rabimodulated.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "1 level reference" block is not executed.
- The executed readouts are therefore:
  - readout 1: detection immediately after adj_polarize, the true mS = 0 fluorescence reference.
  - readout 2: detection after one rabi_pulse_mod_wait_time pulse, the pODMR signal readout.
- The relevant pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns.
- mod_depth is 1 in the provided sequence XML and in Variable_values.

Quantitative model:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1, use f_R = 10 MHz.
- For a square pulse, the on-resonance transition probability is
  P = sin^2(pi * f_R * t), with t = 52 ns.
- P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated mS = 0 to mS = +1 contrast scale of 22%, the expected resonant fractional fluorescence drop in readout 2 relative to readout 1 is 0.22 * 0.996 = 0.219, or about 21.9%.
- The observed readout 1 mean is 46.94 counts, so a fully resonant point should be lower by about 10.29 counts, giving readout 2 near 36.65 counts at resonance.

Observed data:
- Mean readout 1 = 46.94.
- Mean readout 2 = 46.13.
- Mean fractional contrast 1 - readout2/readout1 = 0.0170.
- Largest observed fractional drop is 0.0707 at 3.895 GHz, corresponding to only 3.42 counts.
- The largest observed drop is about one third of the expected resonant contrast and is not shaped like the expected Rabi spectral response.

Explicit line-shape calculation:
- I modeled the detuning-dependent transition probability as
  P(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * t * sqrt(f_R^2 + df^2)).
- Fitting the measured fractional contrast to offset + A * P(df) over possible resonance centers gave the best unconstrained amplitude A = -0.198, i.e. the opposite sign of a pODMR dip.
- With the physically expected amplitude fixed at A = +0.22 and a free offset, the residual improvement over a flat baseline was negligible and the best center was outside the scan range.

Decision:
The physically expected pODMR resonance for this pulse should be a large readout-2 depletion of about 22% relative to the polarized reference. The measured trace only shows small fluctuations, and the quantitative Rabi model fit does not support a positive resonance feature. I therefore decide resonance_absent.
