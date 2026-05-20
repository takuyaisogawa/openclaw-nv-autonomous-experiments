Case: podmr_021_2026-05-16-171244

Sequence/readout identification from inputs/sequence.xml:

- Active sequence: Rabimodulated.xml style sequence with laser polarization, detection, wait, one modulated Rabi pulse, detection, and final wait.
- The `full_expt` variable is 0, so the "Acquire 1 level reference" block is inactive. The `do_adiabatic_inversion` boolean is therefore not part of the active pulse train.
- Readout 1 is the true m_s = 0 reference acquired immediately after polarization.
- Readout 2 is the signal readout after `rabi_pulse_mod_wait_time`.
- The active Rabi pulse duration is `length_rabi_pulse = 52 ns`. With sample_rate = 250 MHz, this is exactly 13 samples, so rounding leaves it at 52 ns.
- The provided XML gives `mod_depth = 1`.

Physical expected-signal calculation:

Using the stated setup calibration, the Rabi frequency at mod_depth = 1 is approximately 10 MHz. For a resonant square pulse, the transferred population is

P_1(delta=0) = sin^2(pi * f_R * t)

with f_R = 10 MHz and t = 52 ns:

f_R * t = 10e6 * 52e-9 = 0.52 cycles
P_1(0) = sin^2(pi * 0.52) = 0.996

The setup contrast between m_s = 0 and m_s = +1 is about 22%, so a real resonant response under this pulse should produce an optical readout-2 deficit of approximately

0.22 * 0.996 = 0.219, or 21.9% relative to the readout-1 reference.

I also evaluated the square-pulse detuning model

P_1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

over possible resonance centers in the 3.825-3.925 GHz scan. The measured normalized contrast was taken as `1 - readout2/readout1`.

Observed data summary:

- Mean normalized contrast across the scan: 0.00137.
- Standard deviation of normalized contrast across points: 0.0259.
- Largest observed positive normalized contrast: 0.0472 at 3.830 GHz.
- Around the visually lowest raw readout-2 region near 3.880-3.885 GHz, normalized contrasts are only 0.0239 and 0.0264.
- Several points have negative contrast, meaning readout 2 exceeds readout 1.

Model comparison:

- Offset-only null model SSE: 0.01403.
- Best fit using the mod_depth = 1 square-pulse shape with free center and free amplitude: center 3.839 GHz, fitted optical amplitude 0.0411, SSE 0.01113.
- Fixed physical expectation using mod_depth = 1 and optical amplitude 0.22: best-center SSE 0.06571, substantially worse than the null model.

Decision:

For the active pulse in the supplied XML, a resonance should be a broad, near-full-transfer response with roughly 22% readout-2 suppression. The measured pairwise normalized signal never approaches that scale and the physically expected model fits much worse than an offset-only model. The small few-percent fluctuations are consistent with drift/noise/tracking cadence rather than the expected pODMR resonance.

Prediction: resonance_absent
