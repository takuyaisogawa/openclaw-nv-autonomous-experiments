Active sequence and readout roles

The provided sequence is Rabimodulated.xml. The instructions first run adj_polarize followed by detection, so readout 1 is the true m_S = 0 fluorescence reference. full_expt = 0, so the optional one-level reference block is disabled; do_adiabatic_inversion is therefore not active in this run. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection, so readout 2 is the microwave-pulse signal channel. At sample_rate = 250 MS/s, 52 ns is exactly 13 samples and is unchanged by rounding.

Quantitative model

Using the stated setup calibration, the Rabi frequency at mod_depth = 1 is about 10 MHz. For a square pulse, I used

P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * tau * sqrt(Omega^2 + delta^2))

with Omega = 10 MHz and tau = 52 ns. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant readout drop is 0.22 * 0.9961 = 0.2191, or about 21.9% relative contrast between readout 1 and readout 2.

Data comparison

I normalized the combined raw readouts as y = 1 - readout2/readout1. The maximum observed drop is at 3.880 GHz:

readout1 = 21.3462
readout2 = 16.9808
y = 0.2045

This is close to the 0.219 expected contrast for a near-pi pulse on resonance. A fixed-contrast square-pulse model y = offset + 0.22 * P(f - f0) fit over the scan gives best f0 = 3.8772 GHz and offset = -0.0031, with SSE = 0.0181. A constant no-resonance model gives SSE = 0.0824, much worse. Allowing the contrast amplitude to fit gives amplitude = 0.1986 and offset = 0.0008 at the same f0, again consistent with the expected 22% scale.

Decision

Because the active pulse is a near-pi microwave pulse, the expected physical signature is a roughly 22% dip only in the microwave-driven readout. The observed readout 2 dip is about 20.5%, centered within the scan, and is quantitatively matched by the square-pulse Rabi model. Stored averages are not treated as a strong independent repeatability test, but the combined readout roles and model-scale agreement support a pODMR resonance being present.
