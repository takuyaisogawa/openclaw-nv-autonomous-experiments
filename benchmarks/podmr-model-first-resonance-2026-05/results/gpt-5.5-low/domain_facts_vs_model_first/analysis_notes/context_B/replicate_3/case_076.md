Case podmr_062_2026-05-17-063134

Sequence and readout roles:
- Active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize and detect a bright m_S = 0 reference.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- The active experiment then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the second detection.
- Therefore readout 1 is the bright reference after optical pumping, and readout 2 is the post-Rabi signal.
- mod_depth = 1.
- length_rabi_pulse = 52 ns after rounding at sample_rate = 250 MHz; 52 ns is exactly 13 samples.

Physical model calculation:
- Given Rabi frequency about 10 MHz at mod_depth = 1 and linear scaling, Omega_R = 10 MHz here.
- For a resonant square pulse, transfer probability is P = sin^2(pi * f_R * tau).
- With f_R = 10 MHz and tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected on-resonance fractional fluorescence dip in the signal readout relative to the bright reference is about 0.22 * 0.996 = 0.219.
- At the observed bright level near 50 raw-count units, this predicts an on-resonance dip of about 10.96 raw-count units in readout 2 relative to readout 1, allowing for ordinary scaling details.

Data check:
- Mean readout2/readout1 ratio over the scan is 1.001 with standard deviation 0.025.
- The lowest ratio is at 3.920 GHz: readout1 = 50.404, readout2 = 47.250, ratio = 0.937, difference = -3.154 counts.
- This largest observed depression is only about 6.3%, far below the approximately 21.9% dip expected for a near-pi resonant pulse.
- Other low points are smaller and the per-average traces fluctuate at similar scale, so stored averages do not provide a strong independent repeatability test.

Decision:
The sequence should produce a large post-Rabi fluorescence dip if a pODMR resonance were present in this scan. The observed normalized readout data do not show a feature at the expected physical signal scale. I decide resonance_absent.
