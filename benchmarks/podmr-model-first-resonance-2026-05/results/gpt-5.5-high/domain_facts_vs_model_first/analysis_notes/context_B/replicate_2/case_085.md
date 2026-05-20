Case: podmr_071_2026-05-17-084118

I used the provided sequence XML, whose active sequence is Rabimodulated.xml. The instructions first polarize and detect, then wait. Because full_expt = 0, the optional 1-level reference block is skipped. The sequence then applies one rabi_pulse_mod_wait_time pulse and detects again. Therefore readout 1 is the polarized m_S = 0 reference, and readout 2 is the post-Rabi-pulse signal. A pODMR resonance should appear as a reduction of readout 2 relative to readout 1 at the resonant scan value.

Relevant pulse parameters from the XML:
- mod_depth = 1
- length_rabi_pulse = 52 ns
- sample_rate = 250 MHz, so the pulse length remains 52 ns after rounding
- scanned variable = mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps

Quantitative model:
For a square pulse, I used

P(Delta) = (f_Rabi^2 / (f_Rabi^2 + Delta^2)) * sin^2(pi * T * sqrt(f_Rabi^2 + Delta^2))

with f_Rabi = 10 MHz * mod_depth = 10 MHz and T = 52 ns. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated contrast scale of 22%, the expected relative fluorescence drop in the post-pulse readout is about

-0.22 * 0.996 = -0.219,

or about -10.8 raw units for a baseline near 49.5. The model response is still large for detunings of a few MHz: about -20.4% at 2.5 MHz and -16.5% at 5 MHz.

Observed data:
- mean readout 1 = 49.459
- mean readout 2 = 49.448
- mean readout 2 - readout 1 = -0.011 raw units
- observed relative difference range = -5.43% to +5.72%
- largest negative point is at 3.860 GHz, only -2.79 raw units or -5.43%

I also compared the observed relative differences to the square-pulse spectral response. A free-amplitude fit over possible resonance centers found only about a 3.5% drop amplitude, far below the expected 21.9% on-resonance drop. A fixed 22% contrast model fits worse than a flat no-resonance model, because the data do not contain a deep post-pulse dip at any scan point.

Decision:
The expected physical signal for the active sequence is a large negative readout-2 dip relative to readout 1, but the measured differences are small, sign-changing, and consistent with scatter/tracking rather than a Rabi-driven pODMR line. I therefore classify this case as resonance absent.
