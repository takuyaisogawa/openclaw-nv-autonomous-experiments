Case podmr_004_2026-05-10-171142.

Sequence inspection:
- The provided sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active variables for the relevant pulse are mod_depth = 1 and length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so rounding does not change the duration.
- full_expt = 0 disables the optional "1 level reference" block. do_adiabatic_inversion is therefore not active in this run.
- Readout 1 is the detection immediately after adj_polarize, so it is the bright m_S = 0 reference.
- Readout 2 is the detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so it is the pulsed pODMR signal.

Quantitative physical model:
Use the two-level Rabi transition probability for a square pulse,

P1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * sqrt(f_R^2 + delta^2) * t),

where f_R is the on-resonance Rabi frequency in cycles/s, delta is detuning in cycles/s, and t is the pulse duration. The setup facts give f_R about 10 MHz at mod_depth = 1, and t = 52 ns.

On resonance:
- f_R * t = 10e6 * 52e-9 = 0.52 cycles.
- P1(0) = sin^2(pi * 0.52) = 0.996.
- With a 22% bright/dark contrast scale, the expected pulsed-readout drop is 0.22 * 0.996 = 0.219, so readout2/readout1 should be about 0.781 at resonance.
- For the observed bright reference near 44 counts, a full resonance should put the pulsed readout near 34 to 35 counts.

Finite-pulse line-shape checks:
- At 5 MHz detuning, P1 = 0.749, expected fractional drop = 16.5%.
- At 10 MHz detuning, P1 = 0.273, expected fractional drop = 6.0%.
- At 15 MHz detuning, P1 = 0.012, expected fractional drop = 0.26%.

Observed combined data:
- The minimum observed readout2/readout1 is 0.943 at 3.855 GHz, only a 5.7% drop.
- The mean fractional readout2-readout1 difference is positive, about +1.3%, rather than a negative resonance contrast.
- Adjacent points around the largest negative point do not show the expected broad finite-pulse pattern: at 3.850 GHz readout2 is above readout1 by 6.5%, at 3.855 GHz it is below by 5.7%, and at 3.860 GHz it is above by 1.2%.

Model comparison on y = (readout2 - readout1) / readout1:
- Flat offset model: best offset +0.0133, SSE = 0.0325.
- Fixed 22% physical Rabi model with free resonance center and free constant offset: best SSE = 0.0743, worse than the flat model.
- If the contrast amplitude is allowed to float between 0 and 22%, the best amplitude is only 4.2%, much smaller than the expected 22% and comparable to point-to-point scatter.
- An unconstrained fit prefers a negative amplitude, which would be a peak rather than the expected ODMR dip.

The stored averages show different largest dips at different scan points and mostly reflect tracking/drift cadence rather than a strong independent repeatability check. The active pulse should produce a large, structured pulsed-readout dip if a resonance were present in this scan. The measured data instead look like scatter and slow drift without the expected pODMR resonance signature.

Decision: resonance_absent.
