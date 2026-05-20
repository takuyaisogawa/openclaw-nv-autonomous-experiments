Case: podmr_052_2026-05-17-015447

Inputs used:
- Sequence XML: inputs/sequence.xml
- Raw readouts: inputs/raw_export.json

Active pulse sequence and roles:
- SequenceName in the export is Rabimodulated.xml, and the provided sequence XML contains the active Rabimodulated sequence.
- The instructions first polarize the NV, then perform detection before the microwave pulse. This is the true m_S = 0 reference, corresponding to readout 1.
- full_expt = 0, so the optional separate m_S = +1 reference block is inactive.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This is the signal readout after the microwave pulse, corresponding to readout 2.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence parameters from provided XML:
- length_rabi_pulse = 5.2e-08 s = 52 ns
- mod_depth = 1
- sample_rate = 250 MHz, so the pulse duration is already an integer 13 samples after rounding.

Physical model calculation:
- Given setup Rabi frequency: f_Rabi approximately 10 MHz at mod_depth = 1.
- On resonance, a resonant rectangular pulse transfers population from m_S = 0 to m_S = +1 with probability
  P = sin^2(pi * f_Rabi * tau).
- For tau = 52 ns and f_Rabi = 10 MHz:
  f_Rabi * tau = 0.52 cycles
  P = sin^2(pi * 0.52) = 0.996
- With a setup contrast scale of 22%, the expected fractional PL drop in the post-pulse signal on resonance is:
  0.22 * 0.996 = 0.219, or about 21.9%.
- At the observed readout level of about 27 counts, this implies an expected on-resonance absolute drop of about:
  27 * 0.219 = 5.9 counts.

Observed quantitative comparison:
- Combined readout 1 mean = 27.413 counts.
- Combined readout 2 mean = 26.974 counts.
- Mean difference readout2 - readout1 = -0.439 counts, only about a 1.5% mean reduction.
- Pointwise fractional drops 1 - readout2/readout1 range from about -10.1% to +10.0%; none approach the expected 21.9% drop.
- The largest observed drop is at the final scan point, not a clean isolated resonance feature, and is still only about 10%.
- Stored per-average traces show strong monotonic drifts with opposite directions between averages, so they mainly reflect tracking cadence and drift rather than independent repeatability of a resonance.

Decision:
- The relevant resonant-pulse model predicts a large, easily visible post-pulse PL dip if a pODMR resonance lies in this scan.
- The observed readout 2 is nearly the same as readout 1 across the sweep, with drift/noise-scale deviations and no feature close to the expected 22% contrast.
- Therefore a pODMR resonance is absent in this measurement.
