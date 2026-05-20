Case: podmr_041_2026-05-16-224136

Sequence interpretation

The active sequence is Rabimodulated.xml. The instruction order is:

1. adj_polarize, then detection: this is the true m_S = 0 reference readout.
2. The optional m_S = 1 reference block is guarded by full_expt, and full_expt = 0, so that block is inactive.
3. A rabi_pulse_mod_wait_time pulse is applied with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection: this is the pODMR signal readout.

Thus readout 1 is the polarized m_S = 0 reference and readout 2 is the post-microwave-pulse signal. The scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative expected signal model

Use the given setup model: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. With mod_depth = 1, f_R = 10 MHz. For a square resonant pulse of duration t = 52 ns, the transferred population is

P_1 = sin^2(pi f_R t)
    = sin^2(pi * 10e6 * 52e-9)
    = 0.996.

The m_S = 0 to m_S = +1 contrast scale is about 22%, so the expected resonant fractional readout drop for readout 2 relative to readout 1 is

0.22 * 0.996 = 0.219, or about 21.9%.

The measured readout 1 mean is 46.35 raw counts. Therefore an on-resonance pi-pulse response should reduce the signal by about

46.35 * 0.219 = 10.15 counts,

placing readout 2 near 36.2 counts at the resonance center, apart from linewidth and sampling effects. Even if the resonance center falls between sampled points, a nearby point in a 5 MHz grid should show a large depletion unless the resonance is much narrower than the scan step; the observed traces do not show such a feature.

Observed data comparison

The combined readout ratio readout2/readout1 has mean 0.9955 and standard deviation 0.0303. The minimum ratio is 0.9437 at 3.895 GHz, corresponding to a 5.6% drop, or a 2.60 count deficit. Other negative excursions of similar scale occur at 3.880, 3.915, and 3.925 GHz, while neighboring points recover or fluctuate upward. The largest observed deficit is only about one quarter of the 10-count resonant pi-pulse expectation.

Stored averages show tracking offsets between averages, so they should not be treated as a strong independent repeatability test. Still, the per-average behavior is consistent with noisy few-count fluctuations rather than a robust 22% pODMR dip.

Decision

Under the active Rabimodulated pulse model with mod_depth = 1 and 52 ns pulse duration, a true resonance should produce a large post-pulse readout depletion. The measured data show only small, irregular excursions and no quantitatively consistent resonance feature. I therefore decide that a pODMR resonance is absent.
