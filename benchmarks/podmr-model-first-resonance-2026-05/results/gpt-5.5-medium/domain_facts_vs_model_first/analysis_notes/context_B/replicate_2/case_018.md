Case: podmr_003_2026-05-16-003531

Sequence interpretation from inputs/sequence.xml:

- Active sequence: Rabimodulated.xml.
- Scan variable: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first runs adj_polarize followed by detection, then waits. This makes readout 1 the optically pumped m_S = 0 reference.
- full_expt = 0, so the optional "1 level reference" block is inactive. There is no independent m_S = +1 reference readout in this run.
- The active manipulation before the second detection is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. Therefore readout 2 is the post-Rabi-pulse readout.
- sample_rate = 250 MHz, so the 52 ns pulse is exactly 13 samples and is unchanged by the rounding instruction.

Quantitative physical expectation:

The setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. With the sequence's mod_depth = 1, f_R = 10 MHz. For a square resonant Rabi pulse with population transfer

P_transfer = sin^2(pi * f_R * tau),

using tau = 52 ns gives:

P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996.

The stated m_S = 0 to m_S = +1 contrast scale is about 22%, so the expected fractional readout-2 dip at resonance is approximately:

0.22 * 0.996 = 0.219, or about 22%.

Given raw readout levels around 37 counts, the expected on-resonance dip is about 8 counts relative to the pumped reference/baseline scale. If one instead used the stale embedded sequence text value mod_depth = 0.3, the model would give f_R = 3 MHz, P_transfer = 0.222, and an expected dip of only 4.9% or about 1.8 counts. The provided sequence XML and exported variable values identify mod_depth = 1, so the near-pi-pulse expectation is the relevant model.

Observed signal:

Combined readout 2 has a pronounced dip centered near 3.88 GHz:

- At 3.880 GHz, readout 1 = 39.98 and readout 2 = 28.06.
- The ratio readout2/readout1 is 0.702, a 29.8% suppression relative to readout 1.
- Excluding the dip region from 3.870 to 3.885 GHz, the readout2/readout1 ratio has mean 0.986 and standard deviation 0.049. The 3.880 GHz point is therefore about 0.284 below the off-region mean, far larger than the off-region scatter.
- The two stored averages both place their minimum readout2/readout1 ratio at 3.880 GHz, with ratios 0.744 and 0.667. These averages should not be overinterpreted as strong independent repeatability tests because stored averages may reflect tracking cadence, but they are consistent with the combined dip.

Decision:

The active sequence applies a 52 ns, mod_depth = 1 Rabi pulse, which is expected to act nearly as a pi pulse on resonance and produce a large ODMR dip of order 22%. The data show a localized readout-2 suppression of roughly 30% near 3.88 GHz, on the correct scale and shape for a resonance. I therefore decide that a pODMR resonance is present.
