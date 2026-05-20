Case podmr_018_2026-05-16-134409

I used the provided Rabimodulated.xml sequence and the saved raw export values. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executable part first polarizes and detects the true m_S = 0 bright reference, then, because full_expt = 0, skips the separate m_S = 1 reference block. It then applies one rabi_pulse_mod_wait_time pulse and performs the second detection. Thus readout 1 is the direct polarized/bright reference, and readout 2 is the signal after the microwave pulse.

Relevant pulse settings from the run are length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration, the Rabi frequency at mod_depth = 1 is about 10 MHz. For a resonant square pulse, the population transfer model is

P_transfer = sin^2(pi * f_Rabi * t_pulse).

Using f_Rabi = 10 MHz and t_pulse = 52 ns gives P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated m_S = 0 to m_S = +1 optical contrast scale of about 22%, the expected resonant fluorescence reduction is therefore 0.22 * 0.996 = 0.219, or about a 22% drop from the bright level for an ideal resonant response.

Quantitative check on the data: excluding the obvious dip points at indices 9 through 12, the readout-2 off-resonance baseline is about 47.08 raw counts. The minimum readout-2 value is 38.96 at index 11, corresponding to 3.880 GHz. The observed fractional drop is (47.08 - 38.96) / 47.08 = 0.172, about 17%. Neighboring readout-2 points also form a smooth dip: 42.88 at 3.870 GHz, 39.77 at 3.875 GHz, 38.96 at 3.880 GHz, and 42.63 at 3.885 GHz.

Readout 1 is the bright reference and remains comparatively flat through the same region, so the feature is tied to the microwave pulse readout rather than a common-mode count fluctuation. The stored two averages show the same caution noted in the prompt: they mainly reflect tracking cadence, so I do not treat them as a strong independent repeatability test. Still, the observed dip magnitude and location are quantitatively consistent with the expected near-pi-pulse pODMR response.

Decision: resonance_present.
