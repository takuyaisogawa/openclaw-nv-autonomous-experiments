Case podmr_028_2026-05-13-100213

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:

- SequenceName is Rabimodulated.xml, with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize and detect: this first detection is the true m_S = 0 fluorescence reference, corresponding to readout 1.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, ...) and detects again: this post-pulse detection is the pODMR signal readout, corresponding to readout 2.
- The provided sequence variables give length_rabi_pulse = 52 ns and mod_depth = 1. The pulse is already sample-grid aligned at 250 MHz: 52 ns is 13 samples.

Physical expectation:

The setup facts give a Rabi frequency of about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. For the active mod_depth = 1, f_R = 10 MHz. For a rectangular resonant pulse, the transfer probability is

P_1 = sin^2(pi f_R t).

With t = 52 ns, P_1 = sin^2(pi * 10e6 * 52e-9) = 0.996. Thus a resonance sampled near its center should nearly invert the spin. With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the post-pulse readout should show a fractional fluorescence drop of about 0.22 * 0.996 = 0.219, i.e. about a 22% dip relative to the bright reference. At the observed readout 1 mean of 27.69 counts, the expected on-resonance readout 2 level is about 21.62 counts, a drop of about 6.07 counts.

I also evaluated the standard detuned rectangular-pulse response

P_1(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi t sqrt(f_R^2 + Delta^2))

on the scan grid and fitted readout2/readout1 = baseline - amplitude * P_1(f - f0), with f0 allowed anywhere in the scan and amplitude clipped to the physical 0 to 0.22 range. The best fit was centered near 3.90415 GHz with amplitude 0.066, baseline 0.996, and RMSE 0.0566 versus null RMSE 0.0596. This is only a small improvement over no resonance and the fitted amplitude is far below the approximately 0.219 expected from the active pulse.

Observed data:

- Mean readout1 = 27.69 counts.
- Mean readout2 = 27.25 counts.
- The largest readout2/readout1 drop is at 3.905 GHz: 24.12 / 27.62 = 0.873, a 12.7% drop.
- The adjacent points do not match the expected near-pi rectangular-pulse spectral response cleanly: at 3.900 GHz the ratio is 0.936, but at 3.910 GHz it recovers to 1.018.
- A real resonance under the active mod_depth = 1, 52 ns pulse should produce an approximately 22% dip near the resonance center, not a weak and asymmetric feature whose best physical-model amplitude is about 6.6%.

Decision:

The active sequence should produce a strong pODMR dip if a resonance is present in this scan. The measured post-pulse readout has only a modest local depression and the quantitative pulse-response fit is weak and much smaller than the expected contrast. I therefore decide that a pODMR resonance is absent.
