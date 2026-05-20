Case podmr_048_2026-05-17-002650

I used the provided Rabimodulated.xml sequence and the raw export values. The active experiment varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects a true m_s = 0 reference. Because full_expt = 0, the optional m_s = +1 reference block is skipped. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Therefore readout 1 is the optical m_s = 0 reference and readout 2 is the signal after the microwave pulse.

Physical model:

The setup Rabi frequency is about 10 MHz at mod_depth = 1, so for a 52 ns pulse the resonant transition probability is

P_res = sin^2(pi * f_R * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_s = 0 to m_s = +1 contrast scale of 22%, a real on-resonance pODMR dip in readout 2 relative to readout 1 should have fractional depth

C * P_res = 0.22 * 0.996 = 0.219,

or about 21.9%. Since the mean readout 1 level is 50.48 raw units, the expected center dip is about

50.48 * 0.219 = 11.06 raw units.

I also evaluated the detuned square-pulse response

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

against the measured normalized contrast y = (readout1 - readout2) / readout1.

Data comparison:

Mean readout 1 = 50.48 raw units.
Mean readout 2 = 49.79 raw units.
Mean measured normalized contrast = 1.34%.
Largest measured normalized contrast = 7.35% at 3.850 GHz.
The expected active-sequence resonance contrast is 21.9%, about 11.06 raw units, much larger than any observed point.

A flat-offset null model for y has SSE = 0.01479. Forcing the active-sequence 22% square-pulse resonance model with a center inside the scanned range gives best SSE = 0.07196, about 4.86 times worse than the flat model. Letting the resonance amplitude float positive gives only 3.31% fitted amplitude, about 15% of the expected active-sequence contrast. The two stored averages do not provide strong repeatability evidence; their largest contrast points are at different frequencies, consistent with tracking or noise rather than a stable resonance.

Decision:

No pODMR resonance is present in this scan. The active 52 ns, mod_depth 1 pulse should produce a near-pi-pulse-scale, roughly 22% readout-2 dip if it hits a resonance, but the measured readout differences are small, irregular, and quantitatively incompatible with that model.
