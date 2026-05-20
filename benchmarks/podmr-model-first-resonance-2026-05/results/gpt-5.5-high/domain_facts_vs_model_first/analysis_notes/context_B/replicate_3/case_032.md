Case: podmr_017_2026-05-16-132945

Active sequence and readout roles:
- The provided sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional mS=+1 reference branch is inactive.
- The first detection happens immediately after optical polarization and is the mS=0/reference readout.
- The second detection happens after the Rabi-modulated microwave pulse and is the signal readout used for pODMR contrast.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MS/s, this is exactly 13 samples and is unchanged by rounding.
- mod_depth = 1 in the provided sequence variables and exported variable values.

Quantitative model:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly, the relevant Rabi frequency here is f_R = 10 MHz.
- For a square resonant pulse, the transition probability is P = sin^2(pi * f_R * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast scale between mS=0 and mS=+1 is about 22%, so the expected on-resonance signal drop is 0.22 * 0.996 = 0.219, or about 21.9%.
- Using the off-resonant readout-2 baseline excluding the +/-10 MHz region around the minimum gives 43.656 counts. The expected resonant drop is therefore about 43.656 * 0.219 = 9.57 counts.

Observed data:
- The minimum signal readout is at 3.875 GHz: readout 1 = 45.404, readout 2 = 34.173.
- The raw readout-2 drop from the off-resonant baseline is 43.656 - 34.173 = 9.483 counts, or 21.7%.
- Normalizing readout 2 by readout 1 gives an off-resonant ratio baseline of 0.986 and a minimum ratio of 0.753, a ratio-corrected dip of about 23.6%.
- The ratio minimum is 8.8 off-baseline standard deviations below the off-resonant ratio scatter.
- The two stored averages both show the same centered dip, although the stored averages are treated mainly as tracking-cadence snapshots rather than a strong independent repeatability test.

Decision:
The expected resonant response for the active pulse is a near-pi-pulse fluorescence reduction of about 22%, and the observed signal readout shows a centered dip of the same size while the reference readout does not. This is a pODMR resonance.
