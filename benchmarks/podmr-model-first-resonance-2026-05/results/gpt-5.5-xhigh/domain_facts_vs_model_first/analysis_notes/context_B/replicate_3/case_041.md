Case: podmr_027_2026-05-16-184117

I used the provided sequence XML and the exported scan data only.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 is acquired immediately after optical polarization and is the true m_S = 0 fluorescence reference.
- Readout 2 is acquired after the active microwave Rabi pulse and is the pODMR signal readout.
- Active pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Physical signal model:
The setup contrast between m_S = 0 and m_S = +1 is about 22%. The stated Rabi frequency is about 10 MHz at mod_depth = 1, so the 52 ns pulse has 10 MHz * 52 ns = 0.52 Rabi cycles. For a square pulse, the transition probability versus detuning is

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).

With f_R = 10 MHz and tau = 52 ns:
- On resonance, P = sin^2(pi * 0.52) = 0.996.
- Expected on-resonance fluorescence depression in readout 2 relative to readout 1 is 0.22 * 0.996 = 0.219, or about 21.9%.
- Expected readout-2/readout-1 ratio at resonance is about 0.781.
- Even if the resonance is halfway between 5 MHz-spaced samples, the nearest sampled point should still show about 20.4% depression.

Measured normalized contrast:
I computed contrast_i = 1 - readout2_i / readout1_i from the combined readouts.
- Mean contrast = 1.54%.
- Largest single-point contrast = 6.32%.
- Smallest contrast = -3.18%.
- The largest measured point is less than one third of the expected near-pi-pulse resonance contrast and is not accompanied by the detuning envelope expected from the Rabi model.

Model comparison:
I grid-fit the Rabi detuning model across possible resonance centers using a constant baseline plus a fitted model amplitude. The best fit placed the center near 3.87975 GHz, with fitted model amplitude 3.80% and baseline 0.87%. The expected amplitude scale from the sequence and setup is 22%, so the fitted feature is far too small. A fixed 22% resonance model gives much worse residuals than the small-amplitude fit and would require a large dip that is not present in the readouts.

Decision:
The data do not show the expected model-scale pODMR dip for the active 52 ns, mod_depth = 1 pulse. The visible differences between readout 1 and readout 2 are small, scattered, and consistent with readout/order noise or tracking-related fluctuations rather than a pODMR resonance.
