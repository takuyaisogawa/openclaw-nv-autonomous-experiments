Case: podmr_061_2026-05-17-061719

Sequence interpretation

The provided sequence XML is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active sequence has full_expt = 0, so the optional "1 level reference" block is skipped even though do_adiabatic_inversion is true. The acquired readout roles are therefore:

- readout 1: after adj_polarize and detection, a bright m_S = 0 reference with no microwave pulse.
- readout 2: after a single rabi_pulse_mod_wait_time pulse and detection, the pODMR signal readout.

The pulse used for the pODMR readout has length_rabi_pulse = 52 ns and mod_depth = 1. The setup facts give a Rabi frequency of about 10 MHz at mod_depth = 1.

Quantitative expected signal model

For a square resonant pulse, using the usual Rabi transfer probability

P(+1) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * sqrt(Omega^2 + Delta^2) * t),

with Omega = 10 MHz and t = 52 ns. On resonance, Omega*t = 0.52 cycles, so

P(+1, Delta=0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The stated contrast between m_S = 0 and m_S = +1 is about 22%. The measured bright reference mean is 49.62 counts. Therefore an on-resonance pODMR response should be approximately

expected drop = 49.62 * 0.22 * 0.996 = 10.87 counts
expected pulsed readout = 49.62 - 10.87 = 38.74 counts
expected normalized readout2/readout1 near resonance = 1 - 0.22 * 0.996 = 0.781.

Data comparison

The measured combined readout2/readout1 ratios are mostly near 1. The minimum ratio is 0.9247 at 3.880 GHz, corresponding to a drop of only about 3.73 counts relative to that point's readout 1. Other low points occur at 3.830 and 3.845 GHz, not as a single Rabi/ODMR line shape. The raw readout2 minimum is 45.79 counts, far above the approximately 38.74 counts expected for the near-pi pulse at true resonance.

A least-squares fit of ratio = baseline - A * P(+1, Delta) over possible center frequencies gives a best amplitude A = 0.054, whereas the physical expectation from the contrast is A = 0.22. The flat-ratio SSE is 0.02396 and the best resonance-model SSE is 0.01917, only a small improvement for an amplitude about four times too small. Given the 2 stored averages and the fact that stored averages can reflect tracking cadence, the scattered shallow dips are not strong independent repeatability evidence.

Decision

The active pulse would produce a large, near-22% pulsed-readout depression if it hit a pODMR resonance. The observed data do not show that expected magnitude or a convincing resonance-shaped feature. I therefore decide that a pODMR resonance is absent.
