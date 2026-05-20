Sequence and readout interpretation

The provided XML is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active microwave pulse is:

- rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)
- length_rabi_pulse = 52 ns after sample-rate rounding at 250 MHz
- mod_depth = 1
- full_expt = 0, so the optional m_S = +1 reference block is not active

Therefore the two raw readouts are not independent 0 and 1 references. Readout 1 is the true m_S = 0 level reference acquired immediately after optical polarization and detection. Readout 2 is the signal readout after the 52 ns modulated microwave pulse.

Quantitative physical expectation

Given the stated setup calibration, the Rabi frequency is about 10 MHz at mod_depth = 1. For a resonant rectangular Rabi pulse, the transition probability from m_S = 0 to m_S = +1 is

P = sin^2(pi * f_Rabi * t)

With f_Rabi = 10 MHz and t = 52 ns:

P = sin^2(pi * 10e6 * 52e-9) = 0.996

The stated optical contrast scale between m_S = 0 and m_S = +1 is about 22%, so an on-resonance point should reduce the post-pulse signal relative to the true-0 reference by approximately:

0.22 * 0.996 = 0.219

Equivalently, the signal/reference ratio expected on resonance is about:

1 - 0.219 = 0.781

The mean true-0 reference level is 52.72 counts, so the expected on-resonance signal level would be roughly 41.2 counts, a drop of about 11.6 counts from the reference, if the swept microwave frequency hits resonance and the 52 ns pulse is effective.

Observed data comparison

The observed signal/reference ratios across the scan have mean 1.0006. The minimum ratio is 0.929 at 3.920 GHz, corresponding to a drop of only 3.94 counts from the same-point reference. Most points are within a few percent of unity, and the second readout often exceeds the first readout. The single deepest point is far smaller than the expected near-pi-pulse resonance contrast and is not supported by a broad or reproducible dip structure in the two stored averages, which mainly reflect tracking cadence.

Decision

Under the active sequence and the calibrated Rabi/contrast model, a real pODMR resonance should produce a large localized depression of readout 2 relative to readout 1, near a ratio of about 0.78. The observed data do not show such a feature. I classify this case as resonance_absent.
