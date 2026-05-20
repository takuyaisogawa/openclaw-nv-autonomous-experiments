Case: podmr_075_2026-05-17-093901

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:

- Sequence name in the export is Rabimodulated.xml; the provided XML executes the Rabimodulated pulse sequence.
- The active instructions first run adj_polarize, then detection. This first detection is readout 1, the true m_s = 0 level reference.
- full_expt = 0, so the "Acquire 1 level reference" branch is inactive. The adiabatic inversion setting is therefore not part of the executed branch.
- The active microwave operation is one rabi_pulse_mod_wait_time call before the second detection. This second detection is readout 2, the post-microwave signal readout.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, round(52 ns * 250 MHz) = 13 samples, so the rounded pulse duration remains 13 / 250 MHz = 52 ns.
- mod_depth = 1 in the provided XML and recorded variable values.

Physical model calculation:

For this setup, the Rabi frequency is about 10 MHz at mod_depth = 1. I used the standard driven two-level transition probability

P(f) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau),

with Omega = 2*pi*10 MHz, tau = 52 ns, and Delta = 2*pi*(f - f0). The on-resonance pulse angle is Omega*tau = 3.267 rad = 1.04*pi, giving P(0) = sin^2(1.6336) = 0.996. With the stated 22% m_s = 0 to m_s = +1 contrast scale, an on-resonance point should have readout2/readout1 approximately 1 - 0.22*0.996 = 0.781. At a 50-count reference this is an expected post-pulse drop of about 10.96 counts.

The scan step is 5 MHz, so if a resonance lies within the scanned span, the nearest sampled point is at most 2.5 MHz detuned. The same model gives:

- 0 MHz detuning: P = 0.996, expected drop = 10.96 counts.
- 2.5 MHz detuning: P = 0.929, expected drop = 10.22 counts.
- 5 MHz detuning: P = 0.749, expected drop = 8.24 counts.
- 10 MHz detuning: P = 0.273, expected drop = 3.00 counts.

Observed data:

- readout1 mean = 50.523 counts; readout2 mean = 50.390 counts.
- readout2 - readout1 mean = -0.133 counts, standard deviation = 1.187 counts, min = -2.442 counts, max = +2.346 counts.
- Normalized contrast 1 - readout2/readout1 has mean = 0.00247, standard deviation = 0.02362, min = -0.0480, max = +0.0491.
- The largest apparent negative-going post-pulse feature is only about 4.9% normalized contrast, far below the expected about 22% resonance contrast, and it does not have the multi-point Rabi-broadened shape expected from a 52 ns pulse.

Model fit check:

I fit the normalized contrast to a linear baseline plus the Rabi line shape above while scanning f0 across the measured range. The best unconstrained line-shape amplitude was 0.038, much smaller than the physical 0.22 contrast scale. A fixed 0.22-amplitude resonance model made the residual sum of squares substantially worse than a simple linear baseline. This is inconsistent with a real pODMR resonance under the active pulse settings.

Decision:

The active pulse should produce a large, broad post-pulse readout drop if a resonance is present, but the measured readout2/reference contrast stays near zero with only small tracking-scale fluctuations. I therefore classify this case as resonance_absent.
