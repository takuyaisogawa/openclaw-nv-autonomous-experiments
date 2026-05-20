Case: podmr_045_2026-05-16-234216

I used the provided sequence XML to identify the active sequence as Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active variables in the provided XML are length_rabi_pulse = 52 ns and mod_depth = 1. The instruction block first polarizes the NV and immediately performs detection, then waits. Because full_expt = 0, the optional block that would acquire an explicit m_S = 1 reference is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by a second detection. Therefore readout 1 is the optically polarized m_S = 0 reference, and readout 2 is the post-Rabi measurement channel relevant for pODMR contrast.

Quantitative expected signal model:

For a rectangular resonant Rabi pulse, the transition probability is

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega^2 + Delta^2))

using frequency units in cycles/s. The setup facts give Omega = 10 MHz * mod_depth = 10 MHz, and t = 52 ns. On resonance,

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The stated m_S = 0 to m_S = +1 contrast scale is about 22%, so an on-resonance point should produce an approximately 0.22 * 0.996 = 21.9% PL drop in the post-Rabi readout relative to the m_S = 0 reference. At a typical raw level near 49 counts, this is about 10.7 counts. Even at 5 MHz detuning the same model gives P approximately 0.749, corresponding to an expected drop of about 8.1 counts. Thus a resonance within the scan should be a large, multi-point dip in readout 2 relative to readout 1.

Observed data comparison:

The measured readout-2/readout-1 ratios have mean 0.9986 and standard deviation 0.0215 around a constant baseline. The lowest ratio is 0.9635 at 3.845 GHz, corresponding to only a 3.65% drop, about 1.83 raw counts. This is far smaller than the expected 21.9% resonant drop and is isolated rather than having the expected rectangular-pulse spectral shape. Several high-frequency points instead have readout 2 above readout 1, including ratios 1.0295 and 1.0510 near 3.925 and 3.920 GHz. A single-dip fit using the expected pulse model does not find a physical positive-amplitude dip; the best unconstrained fit prefers the opposite sign near the high-frequency edge.

Stored averages are only two averages and can reflect tracking cadence, so I did not treat average-to-average repeatability as a strong independent test. The main decision is based on the active pulse sequence and the expected pODMR signal scale. Given the 52 ns, mod_depth = 1 pulse, a real resonance in this scan should be much larger than the observed readout differences. I therefore decide that no pODMR resonance is present.
