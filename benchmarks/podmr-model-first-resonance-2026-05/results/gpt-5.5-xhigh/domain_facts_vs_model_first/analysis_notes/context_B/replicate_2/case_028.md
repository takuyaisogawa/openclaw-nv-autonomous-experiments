Case podmr_013_2026-05-16-123121

I used the provided sequence XML and raw export only.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml.
- full_expt = 0, so the optional "1 level reference" branch is inactive.
- Readout 1 is acquired immediately after adj_polarize and is the bright m_S = 0 reference.
- Readout 2 is acquired after a modulated Rabi pulse and is the pODMR test readout.
- mod_depth = 1 from the provided XML and exported variable values.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz, round(52 ns * 250 MHz) = 13 samples, so the rounded pulse duration remains 52 ns.

Physical model calculation:
For a square pulse, using the stated setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the transition probability after a pulse of length t at detuning df is

P(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * t * sqrt(f_R^2 + df^2)).

On resonance, with t = 52 ns:
P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected readout reduction on resonance is
0.22 * 0.996 = 0.219, or 21.9% of the bright reference.

Observed data:
The normalized drop (readout1 - readout2) / readout1 is largest near the center of the sweep:
- 3.875 GHz: readout1 = 44.404, readout2 = 34.673, drop = 21.9%.
- 3.880 GHz: readout1 = 43.058, readout2 = 34.077, drop = 20.9%.

These drops match the expected 21.9% resonance contrast for the active 52 ns, mod_depth = 1 pulse. A least-squares fit of the fixed square-pulse line-shape model to the normalized drop gives a center near 3.8779 GHz, fitted amplitude 0.218, and offset 0.013. The model reduces squared error by about 5.1x relative to a flat normalized-drop model and about 4.7x relative to a linear baseline model.

Conclusion:
The raw readout 2 dip has the correct amplitude and width for the relevant pulse model, while readout 1 stays bright and does not show a comparable central dip. I decide that a pODMR resonance is present.
