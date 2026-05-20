Case: podmr_055_2026-05-17-045046

Input files used: inputs/sequence.xml and inputs/raw_export.json only. I did not use labels, previous outputs, sibling cases, or outside context.

Sequence interpretation:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- From the provided sequence XML and exported variable values: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, full_expt = 0.
- The 1-level reference block is inactive because full_expt = 0.
- Readout 1 is the detection immediately after adj_polarize, so it is the true mS = 0 fluorescence reference.
- Readout 2 is the detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so it is the signal readout after the microwave pulse.

Physical model calculation:
- Given setup contrast C = 0.22 between mS = 0 and mS = +1.
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1.
- For a square pulse of duration t = 52 ns, the transition probability versus detuning delta is:
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected normalized signal readout on resonance is 1 - C * P(0) = 0.781, i.e. about a 21.9% drop of readout 2 relative to readout 1.
- With 5 MHz scan spacing, a resonance centered between samples is at most 2.5 MHz from a sampled point. At delta = 2.5 MHz, P = 0.929 and expected normalized signal is 0.796, still about a 20.4% drop.
- Even at delta = 5 MHz, expected normalized signal is 0.835, a 16.5% drop.

Observed quantitative comparison:
- Combined readout 1 mean = 43.813.
- Combined readout 2 mean = 43.448.
- Pointwise readout2/readout1 ratios have mean 0.992, standard deviation 0.0368, minimum 0.941, and maximum 1.076.
- The largest observed drop is only about 5.9%, at the scale of the scatter, not the expected 16-22% pODMR response from this pulse if a resonance were inside the scan window.
- A no-resonance constant ratio model has SSE = 0.0271.
- A fixed physical resonance model using C = 0.22 and the finite-pulse transition probability, with only center frequency and scale fit over the scanned range, has best SSE = 0.0863 and predicts a minimum normalized signal near 0.793. This is much worse than the flat model.
- Allowing the contrast amplitude to float gives an effective contrast of about -3.9%, i.e. the best small feature has the wrong sign for the expected pODMR dip.

Decision:
The expected signal from the active 52 ns, mod_depth 1 Rabi pulse would be a large post-pulse fluorescence dip relative to the mS = 0 reference. The data show only small, inconsistent readout-ratio fluctuations and do not support that physical model. I therefore decide that a pODMR resonance is absent.
