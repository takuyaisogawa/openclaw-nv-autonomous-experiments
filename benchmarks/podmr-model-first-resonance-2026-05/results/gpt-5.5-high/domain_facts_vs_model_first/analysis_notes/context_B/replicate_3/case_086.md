Case: podmr_072_2026-05-17-085551

Sequence identification:
- Provided XML sequence is Rabimodulated.xml.
- Active scan variable is mw_freq, swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- sample_rate = 250 MHz, so the 52 ns rabi pulse is already on the sample grid: 52 ns * 250 MHz = 13 samples.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- The active readouts are therefore:
  1. readout 1: true m_S = 0 optical reference immediately after adj_polarize.
  2. readout 2: signal readout after one rabi_pulse_mod_wait_time pulse.
- mod_depth = 1 in the provided sequence XML and in the exported active Variable_values.
- length_rabi_pulse = 52 ns.

Quantitative signal model:
For a rectangular microwave pulse, using frequency units rather than angular frequency,

P_1(detuning) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * sqrt(f_R^2 + detuning^2) * tau)

The given setup has f_R = 10 MHz at mod_depth = 1, approximately linear with mod_depth. With tau = 52 ns:

P_1(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance pulse should reduce the signal readout relative to the 0-reference by:

0.22 * 0.996 = 0.219, or about 21.9%.

The observed readout 1 mean is 50.17 counts, so the expected on-resonance dip is:

50.17 * 0.219 = 10.99 counts.

The same model gives the following expected dips versus detuning:
- 0 MHz: 10.99 counts
- 2.5 MHz: 10.26 counts
- 5 MHz: 8.27 counts
- 10 MHz: 3.01 counts
- 20 MHz: 0.53 counts

Data comparison:
- readout 1 mean = 50.17 counts, standard deviation across scan = 0.97.
- readout 2 mean = 49.54 counts, standard deviation across scan = 1.09.
- signal-minus-reference mean = -0.63 counts, standard deviation = 1.20.
- The largest observed reference-minus-signal dip is 2.44 counts, corresponding to a fractional dip of 4.8%.
- The observed signal/reference ratio ranges from 0.952 to 1.023.

I also fit the signal/reference ratio to the rectangular-pulse resonance model with the XML parameters, allowing only a global scale and an unknown resonance center. A resonance forced to any sampled in-window center predicts a minimum ratio near 0.79 at the center, much lower than the observed minimum ratio of 0.952. The best unconstrained fit moves the center outside the scan and only produces a shallow tail-like improvement over a flat model, which is not evidence for an in-scan pODMR resonance.

Decision:
With mod_depth = 1 and a 52 ns pulse, the physical model predicts a large, multi-point pODMR dip if a resonance is present in the swept range. The data show only small fluctuations at the few-count level and no dip with the expected amplitude or line shape. I therefore classify this case as resonance_absent.
