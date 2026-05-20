Case: podmr_067_2026-05-17-074342

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence identification:
- Sequence file: Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- The actual repeated measurement has two readouts:
  1. readout 1: detection immediately after adj_polarize, a true m_S = 0 fluorescence reference.
  2. readout 2: detection after one rabi_pulse_mod_wait_time pulse, the signal readout.
- The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns.
- The provided XML variable list has mod_depth = 1. The raw export also reports Variable_values mod_depth = 1. The Sequence string embedded inside raw_export contains an older-looking default of 0.3, but the provided XML and exported variable value both indicate the active value is 1.

Physical model calculation:
- Given setup contrast between m_S = 0 and m_S = +1: C = 0.22.
- Given Rabi frequency at mod_depth = 1: f_R = 10 MHz, linear in mod_depth.
- For a resonant square pulse with duration t = 52 ns, the spin-transfer probability is modeled as
  P = sin^2(pi f_R t).
- With f_R = 10 MHz and t = 52 ns:
  f_R t = 0.52 cycles
  P = sin^2(pi * 0.52) = 0.996
  expected relative fluorescence dip = C * P = 0.219, about 22%.
- The mean m_S = 0 reference readout is 48.92 counts, so the expected resonant signal readout is
  48.92 * (1 - 0.219) = 38.20 counts, an expected paired difference readout2 - readout1 of about -10.72 counts.
- Even under the embedded stale/default mod_depth = 0.3 alternative, P = sin^2(pi * 3 MHz * 52 ns) = 0.222, giving an expected dip of 4.87%, or about -2.38 counts. That would still require a coherent frequency-localized dip rather than arbitrary tracking-like fluctuations.

Observed quantitative comparison:
- Combined readout 1 mean: 48.920 counts.
- Combined readout 2 mean: 48.757 counts.
- Mean paired difference readout2 - readout1: -0.163 counts.
- Standard deviation of paired differences across scan points: 1.568 counts.
- Largest negative paired difference: -2.346 counts at 3.885 GHz.
- Largest positive paired difference: +2.962 counts at 3.895 GHz.
- Mean readout2/readout1 ratio: 0.997.

Decision:
The measured post-pulse readout is essentially equal to the m_S = 0 reference on average, not lower by the roughly 22% expected from the active 52 ns, mod_depth 1 resonant pulse. The small local dips are at the scale of point-to-point scatter and are mixed with comparable positive excursions, including a positive excursion adjacent to the largest negative point. Stored averages are only two averages and can reflect tracking cadence, so they do not provide a strong independent repeatability test. The quantitative model therefore does not support a pODMR resonance in this scan.

Prediction: resonance_absent.
