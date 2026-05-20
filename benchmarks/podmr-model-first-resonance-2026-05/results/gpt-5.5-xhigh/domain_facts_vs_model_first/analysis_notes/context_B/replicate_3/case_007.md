Case: podmr_011_2026-05-11-181506

Sequence interpretation:
- The active sequence is Rabimodulated.xml.
- full_expt = 0, so the "Acquire 1 level reference" branch is inactive.
- Readout 1 is the true ms=0 reference: polarize, then detection before the microwave pulse.
- Readout 2 is the signal readout after a single rabi_pulse_mod_wait_time call.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so rounding leaves it at 52 ns.

Quantitative model:
- Use the stated setup Rabi frequency f_R = 10 MHz * mod_depth = 10 MHz.
- For a square resonant pulse, the transfer probability is P = sin^2(pi f_R t).
- With t = 52 ns, P_res = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated ms=0 to ms=+1 contrast scale C = 0.22, the expected resonant fractional drop in the post-pulse readout relative to the ms=0 reference is C * P_res = 0.219.
- Around the observed dip, readout 1 at 3.880 GHz is 21.346 and readout 2 is 16.981. The measured fractional drop is 1 - 16.981/21.346 = 0.205, corresponding to a 4.37 count decrease. The model expectation at full transfer is about 0.219 * 21.346 = 4.68 counts.
- A finite-pulse detuning model P(delta) = (f_R^2/(f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)) fit to the normalized contrast gives a best center near 3.877 GHz, fitted amplitude about 0.199, and near-zero offset. The model-shaped fit reduces SSE from about 0.082 for a constant/linear null to about 0.017, with correlation about 0.89 between observed normalized contrast and the expected pulse response.

Decision:
The post-pulse readout has a localized suppression near 3.875-3.880 GHz with the amplitude expected for a near-pi pulse at mod_depth = 1. Stored per-average trends appear dominated by tracking cadence, but both averages show the largest normalized suppression near the same region. I therefore decide that a pODMR resonance is present.
