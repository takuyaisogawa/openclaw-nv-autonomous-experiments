Case podmr_076_2026-05-17-095337

I used only the provided inputs in this workspace. The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the provided sequence XML, full_expt = 0, so the intermediate m_S = +1 reference block is inactive. The readout roles are therefore:

- readout 1: detection immediately after optical polarization, the true m_S = 0 fluorescence reference.
- readout 2: detection after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

The relevant physical model is a square-pulse two-level Rabi response while scanning detuning:

P_transfer(detuning) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * t * sqrt(f_R^2 + detuning^2))

using f_R = 10 MHz at mod_depth = 1 and t = 52 ns. On resonance this gives:

P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

With the stated 22% contrast scale between m_S = 0 and m_S = +1, the expected resonant fractional fluorescence drop in readout 2 relative to readout 1 is:

0.22 * 0.996 = 0.219, about 21.9%.

The mean readout 1 level is 51.03 counts, so the expected resonant signal is a drop of about 11.18 counts, giving readout 2 near 39.85 counts at resonance. Because the scan endpoint is mw_freq = 3.925 GHz, and the active XML has mw_freq = 3.925 GHz with detuning = 0, the modeled resonance should appear at the final scan point.

Observed combined readouts at 3.925 GHz:

- readout 1 = 49.2885
- readout 2 = 50.3462
- readout 2 - readout 1 = +1.0577
- readout 2 / readout 1 = 1.0215

Thus the endpoint shows no fluorescence decrease; it is slightly brighter than the reference. Across all scan points, the largest fractional dip is at 3.905 GHz, where readout 2 / readout 1 = 0.9481, a 5.2% drop. That is far below the modeled 21.9% resonant drop and is not at the expected resonance frequency. The combined readout-difference standard deviation across scan points is about 1.42 counts, still much smaller than the expected 11.18 count resonant drop.

Stored averages are not treated as an independent repeatability test because they can reflect tracking cadence, but they also do not reveal the expected endpoint dip: at 3.925 GHz the two per-average differences are -1.27 and +3.38 counts, averaging to the observed positive endpoint difference.

Decision: resonance_absent. The physically expected pODMR signature for this pulse would be a large readout-2 suppression at the 3.925 GHz endpoint, and that signature is absent from the measured data.
