Case podmr_004_2026-05-16-005019

Sequence and readout roles:
- The provided sequence is Rabimodulated.xml / Rabimodulated.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- Readout 1 is the initial polarized m_S = 0 fluorescence reference after adj_polarize.
- Readout 2 is the signal readout after the active rabi_pulse_mod_wait_time pulse.
- mod_depth = 1 from the provided sequence variables.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz this is 13 samples, so the rounded duration remains 52 ns.

Physical model calculation:
- Setup Rabi frequency at mod_depth = 1 is approximately 10 MHz.
- For a resonant square pulse, the transferred population is P = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With an m_S = 0 to m_S = +1 contrast scale of 22%, the expected on-resonance fluorescence reduction is 0.22 * 0.996 = 0.219, about 21.9%.

Data comparison:
- The strongest dip in readout 2 relative to readout 1 occurs at scan point 3.875 GHz.
- At that point readout 1 = 41.288 and readout 2 = 32.423, giving readout2/readout1 = 0.785.
- The off-dip median ratio, excluding points within two scan steps of the dip, is about 0.971.
- The observed relative dip is 1 - 0.785/0.971 = 0.191, about 19.1%.
- This observed dip is close to the 21.9% model expectation for an on-resonance 52 ns pi-like pulse at mod_depth = 1.
- Stored averages show the same central depression, but I do not treat the two averages as a strong independent repeatability test because they can reflect tracking cadence.

Decision:
The active post-Rabi signal readout shows a quantitatively expected ODMR/Rabi-transfer dip near 3.875 GHz, so a pODMR resonance is present.
