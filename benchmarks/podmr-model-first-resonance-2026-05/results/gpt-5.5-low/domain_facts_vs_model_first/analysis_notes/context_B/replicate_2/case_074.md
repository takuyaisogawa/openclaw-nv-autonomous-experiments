Case: podmr_060_2026-05-17-060259

Sequence identification:
- Active sequence: Rabimodulated.xml.
- The XML instruction path first polarizes and detects, then waits, then conditionally acquires an m_S=1 reference only if full_expt is nonzero. Here full_expt = 0, so the conditional 1-level reference block is inactive.
- Readout 1 role: true m_S=0 optical reference immediately after adj_polarize.
- Readout 2 role: signal readout after rabi_pulse_mod_wait_time.
- Active pulse parameters from the provided XML/variable values: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz. The 52 ns pulse is already on a 4 ns sample grid.

Quantitative physical model:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1 and approximately linear scaling, use f_R = 10 MHz.
- For a resonant rectangular Rabi pulse, transition probability P = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52 pi) = 0.996.
- Setup contrast scale between m_S=0 and m_S=+1 is about 22%, so an on-resonance post-pulse readout should be lower than the 0 reference by about 0.22 * 0.996 = 0.219, or 21.9%.
- The observed mean readout 1 baseline is 50.94 raw units, so the expected on-resonance drop is 50.94 * 0.219 = 11.16 raw units. Thus a real resonance sampled by this scan should produce readout 2 near 39.8 at resonance, not near 50.

Data check:
- Mean readout 1 = 50.94; mean readout 2 = 50.20.
- Mean paired difference readout2 - readout1 = -0.75 raw units, with point-to-point standard deviation 1.51 and SEM 0.33.
- The largest single paired depression is -3.63 raw units at 3.875 GHz, corresponding to only 6.9% contrast.
- Several points have readout 2 greater than readout 1, and the per-average traces fluctuate by comparable amounts. Stored averages are only two and likely reflect tracking cadence rather than a strong independent repeatability test.

Decision:
The active pulse should generate almost full spin transfer on resonance and therefore a large approximately 22% pODMR dip. The data show only small noisy readout differences, with no point approaching the expected roughly 11-count depression. I therefore decide that a pODMR resonance is absent.
