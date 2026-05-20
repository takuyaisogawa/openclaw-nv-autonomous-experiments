Case podmr_005_2026-05-10-173726

Sequence/readout interpretation:
The active sequence is Rabimodulated.xml, scanned in mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence has full_expt = 0, so the optional +1 reference block is inactive. The active readouts are therefore:
1. readout 1: true m_S = 0 reference after adj_polarize and detection.
2. readout 2: signal readout after a single rabi_pulse_mod_wait_time call and detection.

The active pulse is length_rabi_pulse = 52 ns. The provided XML and exported variable values give mod_depth = 1. With the supplied setup fact, the expected Rabi frequency is therefore approximately 10 MHz.

Quantitative model:
I used the standard driven two-level model for the population transferred out of m_S = 0 by the microwave pulse,

P1(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * tau * sqrt(Omega^2 + delta^2)),

with Omega = 10 MHz, tau = 52 ns, and delta in Hz. On resonance this gives
P1(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
With the stated 22% m_S = 0 to m_S = +1 contrast scale, the maximum expected signal-readout dip is about 0.22 * 0.996 = 21.9% relative to the m_S = 0 reference.

The measured normalized signal r = readout2/readout1 has its main minimum near 3.875-3.880 GHz:
- off-window mean ratio, excluding 3.865-3.885 GHz: 0.986
- ratio at 3.875 GHz: 35.654 / 42.615 = 0.837, a 14.9 percentage point dip from the off-window mean
- ratio at 3.880 GHz: 34.731 / 41.692 = 0.833, a 15.3 percentage point dip from the off-window mean

The observed dip amplitude is smaller than the nominal 21.9% maximum but is on the correct scale for an imperfect pi pulse/readout contrast measurement. Fitting the normalized data to a linear baseline plus the fixed 10 MHz, 52 ns Rabi line shape, with contrast constrained to <= 22%, gives a best center near 3.8774 GHz and an effective contrast of 17.6%. This reduces the normalized-ratio squared error from 0.0896 for a no-resonance linear baseline to 0.0384, a 57% reduction.

The two stored averages are not treated as a strong independent repeatability test, but they are consistent with the central dip: the mean ratio inside 3.865-3.885 GHz is lower than outside by 0.100 in average 1 and 0.118 in average 2. The low point at the high-frequency edge is not consistent with the expected 52 ns Rabi line shape and is not the basis for the decision.

Decision:
A pODMR resonance is present. The signal readout shows a localized, physically sized dip near 3.877 GHz relative to the m_S = 0 reference, and the quantitative 52 ns, mod_depth = 1 Rabi model explains the main feature substantially better than a no-resonance baseline.
