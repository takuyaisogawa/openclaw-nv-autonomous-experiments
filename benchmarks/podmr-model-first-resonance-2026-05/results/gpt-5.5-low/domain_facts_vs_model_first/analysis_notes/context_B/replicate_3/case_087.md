Case podmr_073_2026-05-17-090948

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The active instructions polarize the NV, acquire the first detection readout as the true m_S = 0 reference, wait, apply one modulated Rabi pulse, then acquire the second detection readout as the post-pulse signal.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive. do_adiabatic_inversion is set but not used because that whole block is skipped.
- readout 1 is therefore the m_S = 0 reference readout. readout 2 is the signal after the scanned-frequency Rabi pulse.

Pulse parameters:
- varied parameter: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- length_rabi_pulse = 52 ns. At 250 MS/s this is exactly 13 samples, so the rounded pulse duration remains 52 ns.
- mod_depth = 1.
- setup Rabi frequency estimate at mod_depth = 1: 10 MHz.

Quantitative physical expectation:
For a driven two-level transition, the excited-state population after a square pulse is

P_1(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

with Omega = 2*pi*10 MHz at mod_depth = 1 and t = 52 ns. On resonance this reduces to

P_1(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.

The measured m_S = 0 reference level is about 50.17 raw counts. With the provided setup contrast scale of 22% between m_S = 0 and m_S = +1, a resonant pulse should reduce the post-pulse signal by

0.22 * 50.17 * 0.996 = 10.99 raw counts

relative to the m_S = 0 reference readout. Thus, if a pODMR resonance is present within the scan, the expected signature is an approximately 11 count dip in readout 2 relative to readout 1 near the resonance frequency, much larger than ordinary point-to-point scatter in this dataset.

Observed data check:
- Mean(readout 1) = 50.17 counts.
- Mean(readout 2 - readout 1) = -0.12 counts.
- Standard deviation of readout 2 - readout 1 across the scan = 1.09 counts.
- Most negative readout 2 - readout 1 value = -2.52 counts at 3.855 GHz.
- Maximum absolute readout difference = 2.52 counts.

The largest observed signal-reference depression is only about 23% of the expected resonant contrast and is not a coherent resonance-like feature. The per-average traces are only two stored averages and can reflect tracking cadence, so I do not treat them as an independent repeatability test. The combined readouts show no quantitatively plausible pODMR dip under the active pulse model.

Decision: resonance_absent.
