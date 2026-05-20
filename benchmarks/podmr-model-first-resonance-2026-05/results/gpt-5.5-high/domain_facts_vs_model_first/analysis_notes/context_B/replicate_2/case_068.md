Case: podmr_054_2026-05-17-043636

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles
- Sequence name in the export is Rabimodulated.xml.
- The executed instructions first polarize and detect, then wait. This is readout 1: the true m_S = 0 reference.
- The "Acquire 1 level reference" block is disabled because full_expt = 0, so no independent m_S = +1 reference is acquired.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This is readout 2: the post-pulse signal.
- The active pulse parameters from the provided sequence XML are length_rabi_pulse = 52 ns, mod_depth = 1, mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Physical model calculation
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1.
- Given contrast between m_S = 0 and m_S = +1 is approximately 22%.
- For a square pulse, the expected transition probability versus detuning is
  P1(delta) = f_R^2/(f_R^2 + delta^2) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau),
  with tau = 52 ns.
- On resonance, P1(0) = sin^2(pi * 10e6 * 52e-9) = about 0.996.
- The mean readout-1 level is 42.52 counts, so the expected on-resonance fluorescence reduction is
  0.22 * 42.52 * 0.996 = about 9.32 counts.
- Scanning the resonance center across the measured frequency range on the actual 5 MHz grid gives a maximum sampled P1 of about 0.978 for the best fixed-physics fit, corresponding to a deepest expected dip of about 9.14 counts.

Data comparison
- Mean readout 1: 42.517 counts.
- Mean readout 2: 42.266 counts.
- Mean paired difference readout2 - readout1: -0.252 counts.
- Standard deviation of paired differences across scan points: 1.177 counts.
- Most negative paired difference: -2.327 counts.
- Most positive paired difference: +2.308 counts.
- A flat null model for the paired differences has SSE = 27.70.
- A resonance model with the fixed physical 22% contrast and 10 MHz Rabi scale has best SSE = 118.88, much worse than the null model, because it predicts a large dip not present in the data.
- Allowing the resonance amplitude to float gives a best amplitude of only 1.79 counts, about 19% of the expected 9.35-count physical amplitude and only a small improvement over the null SSE.

Decision
The expected pODMR resonance for this sequence would be a large, grid-resolved dip in readout 2 relative to readout 1. The measured paired differences show only small fluctuations and no physically sized resonance feature. Stored averages show tracking drift, so they are not treated as independent confirmation. The resonance is absent.
