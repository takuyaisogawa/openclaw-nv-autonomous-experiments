Case podmr_012_2026-05-16-121601

I used the provided sequence XML and raw export only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive.
- The active instructions first polarize and detect the true m_S = 0 level. This is readout 1.
- The active signal path then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This is readout 2.
- The relevant pulse is therefore the final Rabi-modulated microwave pulse before readout 2, not an adiabatic inversion or a separate m_S = +1 reference.

Sequence parameters:
- length_rabi_pulse = 52 ns.
- mod_depth = 1 from inputs/sequence.xml and the exported variable values.
- sample_rate = 250 MHz, so 52 ns rounds to 13 samples, still 52 ns.

Expected signal model:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, this pulse has f_R = 10 MHz.
- For a resonant square pulse, the transfer probability from m_S = 0 to m_S = +1 is P = sin^2(pi * f_R * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance readout-2 fluorescence loss relative to readout 1 is 0.22 * 0.996 = 0.219, about 21.9%.
- With a readout-1 baseline near 42.1 counts, the expected resonant drop is about 9.2 counts. Imperfect contrast, detuning grid placement, linewidth, and normalization can reduce the measured point depth, but the expected feature should be a sizable negative dip in readout 2 relative to readout 1.

Observed data:
- The readout-1 mean is 42.08 counts and stays comparatively flat over the scan.
- Readout 2 has a localized depression from 3.870 to 3.885 GHz: 36.87, 35.54, 33.92, and 36.73 counts.
- The largest readout1-readout2 difference is 7.31 counts at 3.880 GHz, which is 17.7% of the local readout-1 value.
- Excluding points within +/-10 MHz of that dip center, the readout1-readout2 difference has mean 0.54 counts and sample standard deviation 1.06 counts. The peak difference is therefore about 6.37 standard deviations above the off-feature difference level.
- The dip is present in both stored averages, but those averages mainly reflect tracking cadence and are not treated as a strong independent repeatability test.

Decision:
The active pulse sequence predicts a large readout-2 dip on resonance, and the data show a localized 17.7% drop at 3.880 GHz with neighboring depressed points, close to the 21.9% model expectation. I classify this as resonance_present.
