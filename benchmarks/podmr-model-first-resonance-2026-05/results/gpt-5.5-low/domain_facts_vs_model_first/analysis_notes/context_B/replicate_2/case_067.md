Case podmr_053_2026-05-17-042031

Sequence and roles:
- The saved scan reports SequenceName = Rabimodulated.xml and varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active sequence first performs optical polarization and detection, giving the true m_S = 0 reference readout.
- full_expt = 0, so the optional m_S = 1 reference block is skipped even though do_adiabatic_inversion is true.
- The only microwave manipulation before the scanned signal readout is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
- Therefore readout 1 is the m_S = 0 reference and readout 2 is the post-Rabi-pulse pODMR signal.

Quantitative expected signal model:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, the expected Rabi frequency here is 10 MHz.
- For a square pulse, the transferred population on resonance is sin^2(pi * f_Rabi * t).
- With f_Rabi = 10 MHz and t = 52 ns, the transfer is sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so a resonant scan point should produce an expected normalized fluorescence drop of 0.22 * 0.996 = 0.219, approximately a 21.9% dip of readout 2 relative to readout 1.
- Around a reference level near 45 raw units, this corresponds to an expected signal readout near 35 raw units at resonance, or a readout2/readout1 ratio near 0.781.

Measured comparison:
- The measured combined readout2/readout1 ratios across the scan are:
  0.992, 1.084, 0.997, 0.977, 1.007, 1.014, 1.030, 0.967, 0.998, 0.997, 1.041, 0.928, 1.005, 0.930, 1.004, 0.985, 0.974, 1.019, 0.998, 0.994, 0.983.
- The minimum ratio is 0.928 at 3.880 GHz, a 7.2% drop, far smaller than the 21.9% expected contrast-scale dip for this pulse.
- A simple linear detrend of the ratio gives a most negative residual of about -0.0666, still only about one third of the expected resonant contrast.
- The per-average traces mainly show tracking-scale drift between the two stored averages, so they do not provide a strong independent repeatability check.

Decision:
The physically expected pODMR signal for this pulse would be a large, near-full-contrast dip in the post-pulse readout relative to the m_S = 0 reference. The observed scan only has small ratio fluctuations and no feature close to the expected 22% contrast scale, so I decide resonance_absent.
