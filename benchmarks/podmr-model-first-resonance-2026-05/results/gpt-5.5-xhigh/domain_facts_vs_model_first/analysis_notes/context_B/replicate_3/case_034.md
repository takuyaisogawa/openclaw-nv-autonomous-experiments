Case: podmr_019_2026-05-16-164247

I used the provided sequence XML and the raw export values, without using labels or outside case context.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional 1-level reference block is inactive.
- Readout 1 is taken immediately after adj_polarize and is the true m_S = 0 reference.
- Readout 2 is taken after the Rabi-modulated microwave pulse and is the pODMR signal readout.
- mod_depth = 1 in the standalone sequence XML and in the exported active variable values.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so rounding does not change it.

Quantitative model:
For a square microwave pulse, I used the two-level Rabi excitation probability

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

where f_R is the on-resonance Rabi frequency in cycles/s, delta is the detuning in Hz, and t is the pulse duration. The setup facts give f_R = 10 MHz at mod_depth = 1. With t = 52 ns,

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The current setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance point should reduce the signal readout by

0.22 * 0.996 = 0.219, or about 21.9% of the 0-reference readout.

The observed mean readout 1 level is 46.94 counts, so the expected on-resonance signal deficit is about 10.29 counts. The largest observed readout1 - readout2 deficit is only 3.42 counts, at 3.895 GHz, and some scan points have readout 2 above readout 1. In normalized form, the minimum readout2/readout1 ratio is 0.929, whereas the active-pulse model predicts an on-resonance ratio near 0.781 before allowing small baseline scaling.

I also compared model fits on the normalized ratio readout2/readout1. A constant-ratio null model has SSE = 0.01597. A fixed-contrast Rabi lineshape with contrast = 0.22, f_R = 10 MHz, and t = 52 ns gives its best center near 3.890 GHz but SSE = 0.07027, worse than the flat model, because it predicts a much deeper and broader dip than the data contain. If contrast is allowed to float freely, the best Rabi-shaped feature corresponds to only about 4.0% contrast, far below the expected 21.9% active-pulse effect.

Decision:
The physical model for the active pulse predicts a large near-pi-pulse pODMR dip if a resonance is in the scanned range. The measured readout difference is much smaller and does not match the fixed-contrast Rabi lineshape, so I decide that a pODMR resonance is absent.
