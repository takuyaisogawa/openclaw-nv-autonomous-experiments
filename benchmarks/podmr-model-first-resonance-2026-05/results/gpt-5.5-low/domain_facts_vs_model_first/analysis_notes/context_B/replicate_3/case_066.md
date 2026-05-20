Case: podmr_052_2026-05-17-015447

I used the provided sequence XML and raw export without using labels or external cases.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The active acquisition path first performs adj_polarize, then detection. This is the bright m_S = 0 reference readout.
- full_expt is 0, so the optional m_S = 1 reference branch is skipped.
- The sequence then applies rabi_pulse_mod_wait_time followed by detection. This is the pODMR signal readout after the microwave pulse.
- Therefore readout 1 is the m_S = 0 reference and readout 2 is the post-pulse pODMR signal.

Pulse parameters used for the decision:
- mod_depth = 1 from the provided XML variable values.
- length_rabi_pulse = 52 ns. At the 250 MS/s sample rate this rounds to 13 samples, still 52 ns.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Explicit physical model calculation:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1, I used f_R = 10 MHz.
- For a square pulse, the driven transition probability versus detuning is
  P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau),
  with tau = 52 ns.
- On resonance, f_R * tau = 10e6 * 52e-9 = 0.52 cycles, so
  P(0) = sin^2(pi * 0.52) = 0.996. This is effectively a pi pulse.
- The current contrast scale between m_S = 0 and m_S = +1 is about 22%. The mean reference readout is 27.41 counts, so the expected on-resonance fluorescence drop is approximately
  0.22 * 27.41 * 0.996 = 6.0 counts.
- Thus a real resonance for this pulse should appear as a localized dip of roughly six counts in the post-pulse readout relative to the m_S = 0 reference, with a finite-pulse width on the order of 1/tau, not merely a sub-count fluctuation.

Data comparison:
- The measured readout2 - readout1 differences have mean -0.44 counts.
- The most negative point is -2.89 counts at 3.925 GHz, but this is at the scan edge and lacks the symmetric finite-pulse shape expected for a resonance.
- Around the nominal center region, examples are -0.67 counts at 3.875 GHz, -0.39 counts at 3.880 GHz, and -1.46 counts at 3.885 GHz, far below the about -6 count model expectation.
- A least-squares fit of readout2 - readout1 to the finite-pulse Rabi line shape over possible center frequencies did not recover the expected negative amplitude. The best unconstrained fit used a positive amplitude of about +1.32 counts and only weakly improved over a constant baseline, which is opposite in sign from the expected pODMR dip.
- The per-average traces show large slow drift/tracking structure, and stored averages are not a strong independent repeatability test here.

Decision:
The expected signal from the active pulse is large enough that a resonance should be obvious as a several-count negative contrast feature. The observed data do not match the sign, amplitude, or shape of the quantitative pODMR model, so I decide that a pODMR resonance is absent.
