Case: podmr_082_2026-05-17-111957

Sequence and roles:
- The active sequence in the saved export is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first runs adj_polarize followed by detection, which provides a true mS = 0 / bright reference readout.
- The optional mS = +1 reference block is gated by full_expt, but full_expt = 0, so that block is inactive. The second active detection follows the modulated Rabi pulse and is the pODMR signal readout, not an independent mS = +1 reference.
- mod_depth = 1 and length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is 13 samples, so the pulse duration remains 52 ns after rounding.

Quantitative model:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1 and approximately linear scaling, f_R = 10 MHz.
- For a resonant square pulse, the driven population transfer is P = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast scale between mS = 0 and mS = +1 is about 22%, so the expected resonant pODMR fluorescence drop is 0.22 * 0.996 = 0.219, or about 21.9% of the bright signal.
- The observed combined mean signal is about 50.2 raw-count units, so the expected on-resonance dip would be about 11.0 raw-count units if the swept mw_freq crosses the addressed transition.

Data check:
- Combined readout 1 has mean 50.38, standard deviation 1.02, min 48.50, max 52.44.
- Combined readout 2 has mean 50.03, standard deviation 1.48, min 47.90, max 52.98.
- The average of the two readouts has mean 50.20, standard deviation 1.02, min 48.47 at 3.835 GHz, and max 51.71 at 3.865 GHz.
- Around the central part of the sweep, including 3.875 GHz, the average readout is not suppressed: 3.865 GHz gives 51.71, 3.870 GHz gives 50.59, 3.875 GHz gives 51.65, and 3.880 GHz gives 50.15.

Decision:
The expected resonant signal from the active 52 ns, mod_depth 1 Rabi pulse is a large roughly 11-count fluorescence decrease. The measured data show only small count-level fluctuations and no consistent dip near the relevant frequencies. Stored averages are only two and may reflect tracking cadence, so they are not treated as a strong repeatability test. Based on the quantitative expected signal and the absence of a matching feature, this case is resonance_absent.
