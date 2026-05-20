Case podmr_079_2026-05-17-103702

Sequence identification:
- The saved experiment sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The active detections are:
  - readout 1: after adj_polarize, before the microwave pulse; this is the true m_S = 0 reference.
  - readout 2: after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth); this is the pODMR signal readout.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this remains 52 ns because 52 ns * 250 MHz = 13 samples.

Physical model calculation:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1, the resonant transfer probability for a square pulse is
  P = sin^2(pi * f_Rabi * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant fractional fluorescence change in readout 2 is
  0.22 * 0.996 = 0.219.
- The measured readout-1 mean is 50.718 counts, so a resonant pulse should lower readout 2 by about
  50.718 * 0.219 = 11.114 counts, to roughly 39.60 counts near resonance.

Observed data:
- readout 1 mean = 50.718, standard deviation across scan points = 1.141.
- readout 2 mean = 50.782, standard deviation across scan points = 0.859.
- readout2 - readout1 mean = +0.064 counts, standard deviation = 1.288 counts, range = -2.096 to +2.308 counts.
- readout2/readout1 mean = 1.0017, standard deviation = 0.0253, minimum = 0.9607.
- The observed minimum readout 2 is 49.558 counts, nowhere near the approximately 39.60 counts expected for resonant transfer.

Explicit model comparison:
- I compared readout 2 against a square-pulse resonance model
  P(delta) = (Omega^2/(Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2))
  with Omega = 10 MHz and t = 52 ns, scanning the resonance center over the measured frequency range and fitting a nonnegative contrast amplitude.
- Best dip-model fit: center = 3.8969 GHz, fitted contrast amplitude = 0.0131, SSE = 32.24.
- A simple flat/linear no-resonance model using readout 1 as a baseline gave SSE = 14.22, substantially better than the constrained dip model.

Decision:
The active pulse should be essentially a pi pulse at resonance and should create a large readout-2 dip on the order of 22% of fluorescence. The data instead show readout 2 staying near the readout-1 level with only small scan-scale fluctuations and no quantitatively compatible resonant depression. Therefore the pODMR resonance is absent.
