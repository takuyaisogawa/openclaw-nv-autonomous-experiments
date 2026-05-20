Case: podmr_074_2026-05-17-092418

Sequence interpretation:
- Active sequence: Rabimodulated.xml / Rabimodulated pODMR scan, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- Readout 1 role: after optical polarization, a bright m_S = 0 reference.
- Readout 2 role: after the Rabi-modulated microwave pulse, the pODMR signal readout.
- mod_depth = 1 from the provided sequence XML variables.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, this is already an integer 13 samples and remains 52 ns after rounding.

Quantitative model:
The setup Rabi frequency is about 10 MHz at mod_depth = 1. For a square resonant pulse, the spin-transfer probability is

P = sin^2(pi * f_R * t)

Using f_R = 10 MHz and t = 52 ns:

P = sin^2(pi * 10e6 * 52e-9) = 0.996.

The optical contrast between m_S = 0 and m_S = +1 is about 22%, so a resonant point should produce an expected fractional drop in readout 2 relative to the readout 1 reference of

0.22 * 0.996 = 0.219, or about 22%.

For the measured data I used the contrast-like observable C = 1 - readout2/readout1. The observed C values span about -4.7% to +7.7%, with mean about +0.56% and point-to-point standard deviation about 3.47%. The largest positive value is at 3.900 GHz, not at the final modeled on-resonance point for the nominal mw_freq = 3.925 GHz, where C = -1.71% (readout 2 is brighter than readout 1). A square-pulse detuned Rabi model with f_R = 10 MHz predicts the largest drop at the resonant point and increasing response toward it over the last few scan points; the observed contrast instead has negative correlation with that expected model shape.

The stored two averages are not a strong independent repeatability test, and they are also inconsistent at the final point: one average gives a negative contrast there, while the other gives only about +0.8%. Because the expected on-resonance signal is large, about 22%, and no point shows a compatible drop or modeled lineshape, I decide that a pODMR resonance is absent in this scan.
