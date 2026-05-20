Case podmr_060_2026-05-17-060259

Inputs used:
- sequence XML: inputs/sequence.xml
- raw numeric export: inputs/raw_export.json
- no labels, prior outputs, sibling cases, or external context

Active sequence and readout roles:
- The active sequence is Rabimodulated.xml.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped even though do_adiabatic_inversion is true.
- The two detections that remain are:
  1. readout 1: polarized m_S = 0 reference after adj_polarize.
  2. readout 2: signal after the Rabi-modulated microwave pulse.
- The relevant contrast observable is therefore readout 2 relative to readout 1, not two independent ODMR traces.

Pulse parameters from the provided XML:
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- mod_depth = 1.
- Given the domain fact that the Rabi frequency is about 10 MHz at mod_depth = 1, I used f_R = 10 MHz.
- The setup contrast scale between m_S = 0 and m_S = +1 is about C = 0.22.

Quantitative physical model:
- I modeled a square Rabi pulse versus detuning using
  P_flip(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)),
  where f_R and delta are in cycles/s and tau = 52 ns.
- The expected signal/reference ratio is
  ratio(delta) = 1 - C * P_flip(delta).
- On resonance:
  P_flip(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961,
  so the expected ratio is 1 - 0.22 * 0.9961 = 0.7809.
- At detuning 5 MHz, the expected ratio is 0.8353.
- At detuning 10 MHz, the expected ratio is 0.9400.
- Because the scan step is 5 MHz, any resonance center inside the scanned interval should put at least one sampled point within 2.5 MHz of resonance, giving an expected minimum ratio no higher than about 0.7956.

Observed data summary:
- Scan range: 3.825 GHz to 3.925 GHz in 5 MHz steps, 21 points.
- Mean readout 1 = 50.9432.
- Mean readout 2 = 50.1969.
- Mean readout 2/readout 1 ratio = 0.9858.
- Minimum readout 2/readout 1 ratio = 0.9308 at 3.875 GHz.
- Maximum apparent contrast (readout1 - readout2) / readout1 = 0.0692.
- Per-average scatter is about 1.16 to 1.20 raw readout units, so the stored averages indicate noticeable tracking/noise fluctuations and are not a strong independent repeatability test.

Model comparison:
- A flat multiplicative baseline readout2 = s * readout1 gives s = 0.9849 with SSE = 44.73.
- Searching resonance center over the scan using the fixed physical contrast C = 0.22 gives best SSE = 193.64, worse than the flat baseline.
- Allowing the apparent contrast to vary from 0 to 0.22 gives best apparent contrast C = 0.037, far below the expected 0.22 for this setup.

Decision:
- The expected pODMR signal for the active 52 ns, mod_depth 1 pulse is a large, localized roughly 20% dip in readout 2 relative to the m_S = 0 reference.
- The observed data show only a small, noisy ratio depression, with no point close to the expected on-resonance ratio and no improvement from the fixed-contrast resonance model.
- I therefore decide resonance_absent.
