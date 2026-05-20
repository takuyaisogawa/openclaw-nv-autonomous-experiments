Case: podmr_076_2026-05-17-095337

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first run adj_polarize followed by detection, so readout 1 is the optically polarized m_S = 0 reference.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time followed by detection, so readout 2 is the microwave-pulsed signal readout.
- The provided XML and exported variable values give mod_depth = 1 and length_rabi_pulse = 52 ns. At a 250 MHz sample rate, 52 ns rounds to 13 samples and remains 52 ns.

Expected physical signal model:
- Given f_Rabi = 10 MHz at mod_depth = 1, the on-resonance rotation angle is 2*pi*f_Rabi*t = 2*pi*10e6*52e-9 = 3.27 rad, essentially a pi pulse.
- Starting from m_S = 0, the driven population in m_S = +1 versus detuning delta is
  P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi*t*sqrt(f_R^2 + delta^2)).
- With t = 52 ns and f_R = 10 MHz, P1(0) = 0.996. With the stated 22% m_S = 0 to m_S = +1 contrast scale, a resonance should reduce readout 2 relative to readout 1 by 0.22*0.996 = 0.219, about 22%.
- For a baseline readout near 51 counts, that expected on-resonance drop is about 11.2 counts. Even if the resonance sits between 5 MHz scan grid points, the nearest sampled detuning is at most 2.5 MHz, giving P1 = 0.929 and an expected drop of about 10.4 counts. At 5 MHz detuning the expected drop is still about 8.4 counts.

Observed quantitative comparison:
- Combined readout 1 mean = 51.03 counts; readout 2 mean = 50.82 counts.
- The pointwise contrast estimate (readout1 - readout2) / readout1 has mean 0.0039, standard deviation 0.0270, minimum -0.0415, and maximum 0.0519.
- The largest observed pulsed-readout decrease is therefore about 5.2%, or 2.6 counts, far below the 16% to 22% contrast expected for a sampled resonance with the active pulse parameters.
- A least-squares fit of the Rabi spectral-response shape with free baseline and amplitude over possible resonance centers gives best amplitude -0.025, opposite the expected positive 0.22 contrast. Forcing the physical amplitude 0.22 gives a much poorer residual than a flat baseline.
- The stored two averages differ substantially in baseline and are consistent with tracking cadence effects; they do not provide a strong independent repeatability test for a small isolated feature.

Decision:
The active mod_depth = 1, 52 ns pulse should create a large pODMR dip if a resonance is in the scanned range. The observed readout differences are small, inconsistent with the required amplitude, and not well matched by the Rabi response model. I therefore decide that a pODMR resonance is absent.
