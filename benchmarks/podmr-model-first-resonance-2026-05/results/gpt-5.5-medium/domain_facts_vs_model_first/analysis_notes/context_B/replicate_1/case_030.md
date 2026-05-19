<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_030

Inputs used:
- Provided sequence XML: Rabimodulated.xml / Rabimodulated sequence.
- Scan variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence has full_expt = 0, so the "Acquire 1 level reference" block is inactive.

Active readout roles:
- Readout 1 is acquired immediately after adj_polarize and is the bright mS = 0 reference.
- Readout 2 is acquired after a microwave rabi_pulse_mod_wait_time pulse and is the pODMR signal readout.

Pulse settings from the provided sequence:
- length_rabi_pulse = 52 ns, rounded at 250 MS/s. 52 ns is exactly 13 samples at this sample rate.
- mod_depth = 1.
- The active pODMR pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).

Quantitative physical model:
- Given setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Therefore f_R = 10 MHz for this case.
- For a square resonant pulse, transfer probability is P = sin^2(pi * f_R * t).
- With t = 52 ns, f_R * t = 0.52 cycles and P = sin^2(pi * 0.52) = 0.996.
- With a bright/dark contrast scale of 22%, the expected resonant fluorescence drop in readout 2 relative to readout 1 is 0.22 * 0.996 = 0.219, or about 21.9%.
- At a baseline near 45 counts, this corresponds to about 9.9 counts of drop.

Observed signal:
- The strongest feature is at 3.875 GHz.
- At 3.875 GHz, readout 1 = 46.2115 and readout 2 = 35.8654.
- The observed ratio is 0.7761, i.e. a fractional drop of 22.39%, or 10.35 counts.
- This closely matches the expected 21.9% resonant drop from the near-pi pulse model.
- Away from the feature, using points more than 25 MHz from 3.875 GHz, the readout-2/readout-1 ratio averages 0.970 with standard deviation 0.025. The central ratio at 3.875 GHz is about 7.7 standard deviations below that off-feature ratio.
- A square-pulse Rabi detuning model P(delta) = f_R^2/(f_R^2+delta^2) * sin^2(pi * t * sqrt(f_R^2+delta^2)), with contrast fixed at 22%, fits best near 3.878 GHz and reduces SSE from 283.9 for a no-effect readout-2-equals-readout-1 model to 34.1.
- Allowing the contrast scale to fit gives best contrast 22.6% at 3.878 GHz, consistent with the stated setup contrast.
- The two stored averages both show the central depression, but I do not treat that as a strong independent repeatability test because stored averages can reflect tracking cadence.

Decision:
The observed readout-2 dip has the correct readout role, center, width scale, and amplitude for a pODMR resonance under the active Rabimodulated near-pi pulse. A pODMR resonance is present.
