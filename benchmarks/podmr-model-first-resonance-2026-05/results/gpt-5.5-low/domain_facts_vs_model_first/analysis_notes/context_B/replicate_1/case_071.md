Case podmr_057_2026-05-17-051839.

Sequence identification:
- The provided sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is not active.
- The first detection occurs immediately after optical polarization and is the m_S = 0 / bright reference readout.
- The second active detection occurs after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay) and is the signal readout for the MW pulse.
- length_rabi_pulse = 52 ns after sample-rate rounding at 250 MS/s.
- mod_depth = 1 in the provided sequence variables and exported active variable values.

Quantitative model:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1 and linear scaling with mod_depth, use f_R = 10 MHz.
- For a square resonant Rabi pulse, transferred population is P = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fractional signal in the post-pulse readout relative to the bright reference is about -0.22 * 0.996 = -0.219.
- The mean bright reference readout is 45.46, giving an expected resonant change of about -9.96 raw-readout units if the scan hits resonance.

Data comparison:
- I used signal minus reference, i.e. readout 2 - readout 1, because readout 1 is the bright reference and readout 2 is after the MW pulse.
- The observed differences across the scan have mean -0.035 and standard deviation 0.985 raw-readout units.
- The most negative point is -2.08 raw-readout units at 3.925 GHz, far smaller than the expected approximately -10 unit resonant drop and not a coherent line shape.
- A simple affine-baseline versus negative Gaussian dip grid fit improves SSE only from 18.06 to 14.26 and prefers a narrow edge/noise-like feature with amplitude on the order of a few units, not the expected physical contrast.
- Stored averages are only two and can reflect tracking cadence, so I do not treat the per-average traces as a strong repeatability confirmation.

Decision:
The active pulse should produce a large ODMR-like decrease if a resonance is present in the scanned band, but the measured signal channel does not show a quantitatively compatible dip. I therefore classify this case as resonance_absent.
