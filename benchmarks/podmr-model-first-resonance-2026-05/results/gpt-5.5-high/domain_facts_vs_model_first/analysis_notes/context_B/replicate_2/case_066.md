Case: podmr_052_2026-05-17-015447

Input sequence decision:
- Active sequence: Rabimodulated.xml / Rabimodulated pulse sequence.
- The executed instruction block first performs polarization and detection, then skips the optional 1-state reference because full_expt = 0, then applies one rabi_pulse_mod_wait_time pulse and detects again.
- Readout 1 role: bright m_S = 0 reference acquired immediately after optical polarization.
- Readout 2 role: signal readout after the microwave Rabi pulse.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns.
- mod_depth = 1 from the provided sequence XML and scan variable values.

Quantitative physical model:
The setup contrast scale between m_S = 0 and m_S = +1 is 22%. The stated Rabi frequency is about 10 MHz at mod_depth = 1, so the square-pulse transition probability versus detuning is modeled as

P(detuning) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * sqrt(f_R^2 + detuning^2) * tau)

where f_R = 10 MHz and tau = 52 ns. The expected signal ratio for readout 2 relative to the bright reference is then

S2/S1 = 1 - 0.22 * P(detuning).

For the active pulse:
- On resonance: P = sin^2(pi * 10 MHz * 52 ns) = 0.996, so S2/S1 should be about 0.781, a 21.9% dip.
- At 5 MHz detuning: P = 0.749, so S2/S1 should be about 0.835, a 16.5% dip.
- At 10 MHz detuning: P = 0.273, so S2/S1 should be about 0.940, a 6.0% dip.
- At 15 MHz detuning: P = 0.0117, so the dip is only 0.26%.

Thus a true resonance sampled on the 5 MHz grid should appear as a broad dip with at least one point near 0.78 and adjacent points around 0.84 when centered on a grid point. If centered between grid points, the two nearest sampled points would still be strongly suppressed, roughly at the 0.84 level.

Observed combined readouts:
- readout 1 ranges roughly 25.58 to 28.96 counts.
- readout 2 ranges roughly 25.71 to 28.27 counts.
- The readout2/readout1 ratios have mean 0.985 and standard deviation 0.039.
- The minimum ratio is 0.900 at 3.925 GHz, but the neighboring 3.920 GHz point is 1.020, which is inconsistent with the modeled broad detuning response.
- Other low ratios are isolated or shallow; none show the expected 0.78 on-resonance ratio or paired neighboring suppression near 0.84.

The per-average traces show large opposing baseline drift between stored averages, which is consistent with tracking cadence rather than independent repeatability. The combined trace partly cancels this drift, so the decision should be based on the explicit readout role and the normalized detuning model rather than treating each stored average as a separate resonance confirmation.

Decision: resonance_absent. The active pulse should produce a large, broad contrast feature if a pODMR resonance were present, but the measured normalized signal only shows small, irregular fluctuations and no physically consistent detuning-shaped dip.
