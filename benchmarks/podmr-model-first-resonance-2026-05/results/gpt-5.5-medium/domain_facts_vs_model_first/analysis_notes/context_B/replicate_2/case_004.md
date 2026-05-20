Case: podmr_007_2026-05-11-064944

Sequence interpretation from the provided XML:
- Active sequence: Rabimodulated.xml / Rabimodulated style sequence, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- Readout roles: readout 1 is the direct post-polarization m_S = 0 fluorescence reference; readout 2 is the fluorescence after the active Rabi-modulated microwave pulse.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
- The stored averages are only 2, so they are useful mainly as a tracking/cadence check rather than as a strong repeatability test.

Quantitative physical model:
For a square microwave pulse, using the supplied setup calibration, the on-resonance Rabi frequency is approximately 10 MHz at mod_depth = 1. I used the two-level square-pulse transition probability

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega^2 + Delta^2))

with Omega = 10 MHz and t = 52 ns, with frequencies in cycles/s. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected signal/readout-reference ratio at resonance is

1 - 0.22 * 0.996 = 0.781.

The mean readout 1 level is 31.72 counts, so the expected line-center signal loss is about

31.72 * 0.22 * 0.996 = 6.95 counts.

The same pulse model also predicts a broad multi-point feature on the 5 MHz grid. If centered at 3.855 GHz, the expected ratios around resonance would be approximately:
- 3.845 GHz: 0.940
- 3.850 GHz: 0.835
- 3.855 GHz: 0.781
- 3.860 GHz: 0.835
- 3.865 GHz: 0.940

Data comparison:
- Mean readout 1 = 31.72, mean readout 2 = 31.55.
- Mean readout2/readout1 = 0.996, not near the expected resonant value of 0.781.
- The largest observed raw drop is at 3.855 GHz: readout 1 = 33.77, readout 2 = 29.96, ratio = 0.887. After allowing the overall readout2/readout1 baseline scale, this is about a 10.7% dip, roughly half the expected 21.9% dip.
- The neighboring point at 3.860 GHz has ratio 1.020, whereas the physical model would require a strong neighboring depletion near ratio 0.835 for a resonance centered at 3.855 GHz.
- A fixed-contrast resonance scan over possible center frequencies gives a worse sum of squared residuals than a flat no-resonance scaled-reference model (best resonance SSE about 87.18 versus null SSE about 57.47), because the expected resonance is too large and too broad for the observed trace.

Decision:
The active pulse should produce a large, visible, multi-point pODMR depletion if a resonance is present in this scan. The observed readout2 trace does not show the required amplitude or line shape, and the explicit model comparison favors no resonance. I therefore classify this case as resonance_absent.
