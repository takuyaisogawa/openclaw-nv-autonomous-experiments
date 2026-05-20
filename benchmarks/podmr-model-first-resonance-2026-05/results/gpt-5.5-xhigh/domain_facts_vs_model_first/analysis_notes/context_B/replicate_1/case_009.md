Case: podmr_016_2026-05-12-120649

Sequence interpretation

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence has full_expt = 0, so the optional m_S = +1 reference block is inactive. The active measurements are:

- readout 1: after optical polarization and before the microwave pulse, serving as the bright m_S = 0 reference.
- readout 2: after the modulated Rabi microwave pulse, serving as the pODMR signal readout.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. The sample-rate rounding is exact here: 52 ns * 250 MHz = 13 samples.

Quantitative model

Using the provided setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular pulse, I used the standard driven two-level transition probability:

P(f) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

where f_R = 10 MHz, t = 52 ns, and delta is the detuning in Hz from resonance. On resonance,

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the setup contrast scale of 22% between m_S = 0 and m_S = +1, the expected signal/readout-reference ratio at resonance is approximately

1 - 0.22 * 0.996 = 0.781.

At the mean bright-reference level of 25.73 raw counts, this corresponds to an expected resonant drop of about 5.64 counts in readout 2 relative to readout 1. Even if the resonance center fell halfway between 5 MHz-spaced scan points, the nearest sampled detuning would be 2.5 MHz and the expected ratio would still be about 0.796. At 5 MHz detuning the expected ratio is about 0.835.

Data comparison

From the combined raw readouts, the normalized signal ratio readout2/readout1 ranges from 0.9467 to 1.0963, with mean 1.0171. The largest apparent contrast, 1 - readout2/readout1, is only 0.0533, or about 1.37 counts at that point. This is far smaller than the expected near-pi-pulse pODMR contrast for mod_depth = 1, and no point approaches the expected 0.78 to 0.84 ratio range for a resonance sampled within a few MHz.

I also checked a simple Rabi-lineshape fit over possible resonance centers using the same 10 MHz, 52 ns model. A fixed 22% contrast resonance inside the scan would require a much deeper localized dip than the data show. The best small improvement with fixed contrast places the resonance center outside the scanned range, near 3.942 GHz, where the scan only sees a weak tail; this is not evidence for a resonance present in the measured scan window. The per-average traces show large cadence-like changes, so I did not treat them as independent repeatability evidence.

Decision

The active pulse should produce a large, localized signal drop if a pODMR resonance is present in the sweep. The observed normalized readout deviations are much smaller and not consistent with the expected driven-transition response. I therefore decide that a pODMR resonance is absent in this case.
