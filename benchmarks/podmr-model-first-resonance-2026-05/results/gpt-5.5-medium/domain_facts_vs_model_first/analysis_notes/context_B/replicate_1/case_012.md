Case: podmr_030_2026-05-13-160024

Used only the provided sequence XML and raw export in this workspace.

Sequence interpretation:
- Active sequence: Rabimodulated.xml / Rabimodulated pulse ODMR, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- Readout 1 role: post-polarization bright m_S = 0 reference acquired before the microwave pulse.
- Readout 2 role: signal readout after the modulated Rabi microwave pulse.
- mod_depth = 1 from inputs/sequence.xml and exported Variable_values.
- Active pulse duration: length_rabi_pulse = 5.2e-08 s = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples after rounding.

Quantitative physical model:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1, use f_R = 10 MHz.
- Starting in m_S = 0, resonant transfer probability after a square Rabi pulse is P_1 = sin^2(pi f_R t).
- For t = 52 ns, P_1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so an on-resonance pulse should reduce the second readout relative to the first by about 0.22 * P_1 of the bright readout.
- The measured mean readout 1 is 27.367 counts, giving an expected resonant drop of 0.22 * 0.996 * 27.367 = 5.997 counts. Thus a true resonance near a sampled frequency should have readout2 - readout1 near -6 counts, before allowing for noise.

Measured comparison:
- Mean readout2 - readout1 is +0.362 counts, not negative.
- The deepest observed point is readout2 - readout1 = -2.260 counts at 3.860 GHz, far smaller than the expected approximately -6 count resonant dip.
- The point-to-point standard deviation of readout2 - readout1 is 1.571 counts, so the expected resonant dip is about 3.8 standard deviations in the difference trace and should be visible.
- A detuned-Rabi model using P(delta) = Omega^2/(Omega^2 + delta^2) * sin^2(pi t sqrt(Omega^2 + delta^2)), with Omega = 10 MHz, t = 52 ns, and fixed 22% contrast, was scanned over resonance centers across the measurement range. Even allowing a free vertical offset, the best model SSE was 91.15, worse than the flat null SSE of 49.36.

Decision:
The relevant pulse should produce a large negative signal in readout 2 relative to readout 1 at resonance, but the measured trace shows only small unstructured fluctuations and the quantitative resonance model fits worse than a flat null. I therefore decide that a pODMR resonance is absent.
