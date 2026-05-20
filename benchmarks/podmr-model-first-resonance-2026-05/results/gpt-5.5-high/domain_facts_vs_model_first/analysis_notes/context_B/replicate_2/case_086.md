Case: podmr_072_2026-05-17-085551

Sequence interpretation:
- Active sequence: Rabimodulated.xml / Rabimodulated pODMR scan varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize and detect, then wait, then apply one modulated Rabi pulse, then detect again.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. The two stored readouts are therefore:
  - readout 1: true m_s = 0 fluorescence reference after laser polarization.
  - readout 2: signal fluorescence after the scanned microwave pulse.
- Active pulse duration: length_rabi_pulse = 52 ns. With sample_rate = 250 MHz this remains 13 samples = 52 ns after rounding.
- Active mod_depth: 1, from the provided sequence variable values.

Quantitative physical model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1 and approximately linear scaling, the active pulse has f_R = 10 MHz.
- For a square pulse starting in m_s = 0, the driven population transfer is
  P1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),
  using cycle-frequency units for f_R and detuning delta.
- At exact resonance with t = 52 ns:
  P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The scan step is 5 MHz, so even if the resonance lies halfway between sampled points, the nearest sampled detuning is at most 2.5 MHz:
  P1(2.5 MHz) = 0.929.
- With the stated m_s = 0 to m_s = +1 contrast scale of about 22% and the observed readout 1 reference mean of 50.17 counts, the expected signal readout dip is:
  exact resonance: 50.17 * 0.22 * 0.996 = 10.99 counts,
  worst sampled nearest point: 50.17 * 0.22 * 0.929 = 10.26 counts.
- Thus a real resonance under this pulse model should produce readout 2 values near 39-40 counts at at least one scan point, with readout 1 remaining near the m_s = 0 reference.

Data comparison:
- readout 1 mean/std/min/max: 50.17 / 0.97 / 48.54 / 52.06 counts.
- readout 2 mean/std/min/max: 49.54 / 1.09 / 47.17 / 51.58 counts.
- The minimum observed readout 2 value is 47.17 counts, about 7.3 counts above the conservative expected resonant value.
- The largest observed pointwise readout1 - readout2 drop is only 2.44 counts, much smaller than the expected approximately 10-11 count drop.
- A fixed 22% finite-pulse resonance model gives a much worse squared error than a constant trace because it necessarily predicts a deep dip that is absent.

Decision:
The expected pODMR signature for the active 52 ns, mod_depth 1 near-pi pulse is a large fluorescence dip in readout 2. The observed variations are small, irregular, and comparable to the baseline scatter, with no physically sized resonance feature. Therefore the pODMR resonance is absent.
