Case podmr_030_2026-05-13-160024.

Sequence identification:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active instructions first polarize, then perform detection before any MW pulse. This is readout 1, the bright m_S = 0 reference.
- full_expt = 0, so the "Acquire 1 level reference" block is skipped; do_adiabatic_inversion is not active for the measured readouts.
- The active pODMR readout is after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), followed by detection. This is readout 2.
- From the provided sequence XML and variable values, length_rabi_pulse = 52 ns and mod_depth = 1. At sample_rate = 250 MHz this rounds to 13 samples, still 52 ns.

Quantitative model:
- Setup contrast scale between m_S = 0 and m_S = +1 is C = 0.22.
- Rabi frequency is about 10 MHz at mod_depth = 1, so fR = 10 MHz.
- For a square pulse at detuning Delta, the transition probability is:
  P1(Delta) = (fR^2/(fR^2 + Delta^2)) * sin^2(pi * tau * sqrt(fR^2 + Delta^2))
  with tau = 52 ns.
- On resonance, P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected on-resonance normalized fluorescence drop is C * P1(0) = 0.219, or about 5.99 counts using the observed readout 1 mean of 27.37 counts.
- The expected drop is still about 0.165 fraction at 5 MHz detuning and about 0.060 fraction at 10 MHz detuning, so a resonance in this scan should appear as a multi-point positive contrast feature where readout 2 is lower than readout 1.

Observed data:
- I used y = 1 - readout2/readout1 as the normalized pODMR contrast.
- Observed mean y = -0.0146, standard deviation = 0.0567, minimum = -0.1234, maximum = 0.0825.
- The largest positive contrast point is only 8.25%, well below the 21.9% on-resonance expectation for the active pulse, and the neighboring points do not form the expected square-pulse line shape.
- Readout 2 is on average slightly brighter than readout 1 rather than lower.

Fit check:
- A null constant-contrast model gives SSE = 0.06743.
- Fitting the expected mod_depth = 1 square-pulse profile within the scanned frequency range with a nonnegative free amplitude improves SSE only to 0.06513, with fitted coefficient 0.0367 versus the physical coefficient 0.22.
- Forcing the physical coefficient C = 0.22 makes the fit worse than the null model within the scan, SSE = 0.12272.

Decision:
The expected pODMR resonance signal for the active 52 ns, mod_depth = 1 pulse is large compared with the observed fluctuations and has a specific multi-point shape. The measured data show only unstructured readout-to-readout scatter with no physically scaled resonance feature, so I decide resonance_absent.
